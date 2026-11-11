"""
Visual Analytics & Plotly Chart Utilities for Multiple Disease Prediction System.
Provides interactive gauges, biomarker benchmark comparisons, and feature contribution plots.
"""

import plotly.graph_objects as go
import pandas as pd


def create_risk_gauge(risk_percent: float, title: str = "Disease Risk Index") -> go.Figure:
    """
    Creates an interactive radial risk meter gauge from 0% to 100%.
    """
    if risk_percent < 40:
        bar_color = "#22c55e"  # Green
    elif risk_percent < 70:
        bar_color = "#eab308"  # Amber
    else:
        bar_color = "#ef4444"  # Red

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=risk_percent,
            domain={"x": [0, 1], "y": [0, 1]},
            title={"text": title, "font": {"size": 18, "color": "#1e293b"}},
            number={"suffix": "%", "font": {"size": 28, "color": bar_color}},
            gauge={
                "axis": {"range": [0, 100], "tickwidth": 1, "tickcolor": "#94a3b8"},
                "bar": {"color": bar_color, "thickness": 0.28},
                "bgcolor": "white",
                "borderwidth": 1,
                "bordercolor": "#e2e8f0",
                "steps": [
                    {"range": [0, 40], "color": "#dcfce7"},   # Low risk light green
                    {"range": [40, 70], "color": "#fef9c3"},  # Moderate risk light yellow
                    {"range": [70, 100], "color": "#fee2e2"}, # High risk light red
                ],
                "threshold": {
                    "line": {"color": "#dc2626", "width": 3},
                    "thickness": 0.75,
                    "value": 70,
                },
            },
        )
    )

    fig.update_layout(
        height=260,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        font={"family": "sans-serif"},
    )
    return fig


def create_biomarker_bar_chart(patient_metrics: dict, benchmarks: dict) -> go.Figure:
    """
    Creates a grouped comparison bar chart comparing patient metrics against healthy reference norms.
    """
    categories = list(benchmarks.keys())
    patient_vals = [patient_metrics.get(cat, 0.0) for cat in categories]
    reference_vals = [benchmarks[cat]["normal_max"] for cat in categories]

    fig = go.Figure(
        data=[
            go.Bar(
                name="Patient Value",
                x=categories,
                y=patient_vals,
                marker_color="#3b82f6",
                text=[f"{v:.1f}" for v in patient_vals],
                textposition="auto",
            ),
            go.Bar(
                name="Normal Upper Limit",
                x=categories,
                y=reference_vals,
                marker_color="#94a3b8",
                text=[f"{v:.1f}" for v in reference_vals],
                textposition="auto",
            ),
        ]
    )

    fig.update_layout(
        barmode="group",
        title={"text": "Biomarker Levels vs. Standard Healthy Thresholds", "font": {"size": 15}},
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(241,245,249,0.5)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig


def create_feature_contribution_plot(features_dict: dict, top_n: int = 8) -> go.Figure:
    """
    Creates a horizontal bar chart displaying top contributing normalized features.
    """
    # Sort by absolute magnitude
    items = sorted(features_dict.items(), key=lambda x: abs(float(x[1])), reverse=True)[:top_n]
    keys = [item[0] for item in reversed(items)]
    vals = [float(item[1]) for item in reversed(items)]

    fig = go.Figure(
        go.Bar(
            x=vals,
            y=keys,
            orientation="h",
            marker=dict(
                color=vals,
                colorscale="Blues",
            ),
            text=[f"{v:.2f}" for v in vals],
            textposition="auto",
        )
    )

    fig.update_layout(
        title={"text": "Primary Input Parameters Breakdown", "font": {"size": 15}},
        height=280,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(241,245,249,0.5)",
        xaxis_title="Magnitude",
    )
    return fig

