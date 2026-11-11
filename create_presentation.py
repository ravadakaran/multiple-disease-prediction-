"""
University Minor Project Presentation Generator (16:9 Widescreen).
Strictly tailored to Department of Computer Science & Engineering syllabus agenda:

Slide 1: Title Slide (DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING)
Slide 2: Agenda
Slide 3: Abstract
Slide 4: Scope and Motivation
Slide 5: Introduction
Slide 6: Literature Survey ( Table format-year should be in Chronological order)
Slide 7: Objectives
Slide 8: Problem Statement
Slide 9: Proposed Work
Slide 10: Architecture Diagram/Flow Diagram/Block Diagram
Slide 11: Novel idea
Slide 12: Modules
Slide 13: Module Description
Slide 14: Software & Hardware Requirements
Slide 15: References (Base paper hard copy to be submitted to the supervisor.)
Slide 16: Way forward towards Outcome (Research Paper/Patent)

Mandatory Footer on Every Slide:
DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING                      SLIDE NO: <N>
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_university_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Academic Visual Palette
    C_NAVY_DARK = RGBColor(15, 23, 42)     # #0F172A
    C_NAVY_MED = RGBColor(30, 41, 59)      # #1E293B
    C_INDIGO = RGBColor(79, 70, 229)       # #4F46E5
    C_BLUE = RGBColor(37, 99, 235)         # #2563EB
    C_EMERALD = RGBColor(16, 185, 129)     # #10B981
    C_AMBER = RGBColor(217, 119, 6)        # #D97706
    C_LIGHT_BG = RGBColor(248, 250, 252)   # #F8FAFC
    C_WHITE = RGBColor(255, 255, 255)
    C_BORDER = RGBColor(226, 232, 240)     # #E2E8F0
    C_TEXT_DARK = RGBColor(15, 23, 42)
    C_TEXT_MUTED = RGBColor(100, 116, 139)  # #64748B

    def set_bg(slide, color):
        fill = slide.background.fill
        fill.solid()
        fill.fore_color.rgb = color

    def add_card(slide, left, top, width, height, bg_color=C_WHITE, border_color=C_BORDER, line_w=1):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(line_w)
        return shape

    def add_slide_structure(slide, slide_no, title_text, category_tracker="DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING"):
        # Top Tracker / Department Category
        c_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.3))
        tf_c = c_box.text_frame
        p_c = tf_c.paragraphs[0]
        p_c.text = category_tracker.upper()
        p_c.font.size = Pt(9.5)
        p_c.font.bold = True
        p_c.font.color.rgb = C_INDIGO

        # Slide Main Title (Matches syllabus verbatim)
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.733), Inches(0.75))
        tf_t = t_box.text_frame
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(21)
        p_t.font.bold = True
        p_t.font.color.rgb = C_TEXT_DARK

        # Mandatory University Footer
        f_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.733), Inches(0.4))
        tf_f = f_box.text_frame
        p_f = tf_f.paragraphs[0]
        p_f.text = f"DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING                                                                                    SLIDE NO: {slide_no}"
        p_f.font.size = Pt(9)
        p_f.font.bold = True
        p_f.font.color.rgb = C_TEXT_MUTED

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1, C_NAVY_DARK)

    # Department Banner
    dep_card = add_card(s1, Inches(0.8), Inches(0.6), Inches(11.733), Inches(0.7), bg_color=C_NAVY_MED, border_color=C_INDIGO)
    tb_dep = s1.shapes.add_textbox(Inches(1.0), Inches(0.7), Inches(11.3), Inches(0.5))
    tf_dep = tb_dep.text_frame
    p_dep = tf_dep.paragraphs[0]
    p_dep.text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING"
    p_dep.font.size = Pt(13)
    p_dep.font.bold = True
    p_dep.font.color.rgb = C_WHITE
    p_dep.alignment = PP_ALIGN.CENTER

    # Project Title Card
    m_card = add_card(s1, Inches(0.8), Inches(1.5), Inches(11.733), Inches(3.6), bg_color=C_NAVY_MED, border_color=C_INDIGO)
    tb_m = s1.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.1), Inches(3.0))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True

    p_proj = tf_m.paragraphs[0]
    p_proj.text = "MediScan AI: Multi-Modal Machine Learning Platform for Predictive Disease Risk Screening & Clinical Reporting"
    p_proj.font.size = Pt(24)
    p_proj.font.bold = True
    p_proj.font.color.rgb = C_WHITE

    p_sub = tf_m.add_paragraph()
    p_sub.text = "B.Tech Minor Project Presentation (Phase Evaluation)"
    p_sub.font.size = Pt(14)
    p_sub.font.color.rgb = RGBColor(199, 210, 254)
    p_sub.space_before = Pt(8)

    p_tech = tf_m.add_paragraph()
    p_tech.text = "Domain: Artificial Intelligence & Healthcare Informatics | Stack: FastAPI • Scikit-Learn • Tailwind CSS • Chart.js • Docker"
    p_tech.font.size = Pt(11)
    p_tech.font.bold = True
    p_tech.font.color.rgb = C_EMERALD
    p_tech.space_before = Pt(12)

    # Candidate and Guide Details Card
    cg_card = add_card(s1, Inches(0.8), Inches(5.3), Inches(11.733), Inches(1.5), bg_color=C_NAVY_MED, border_color=C_BORDER)
    tb_cg = s1.shapes.add_textbox(Inches(1.1), Inches(5.4), Inches(11.1), Inches(1.2))
    tf_cg = tb_cg.text_frame
    tf_cg.word_wrap = True

    p_c1 = tf_cg.paragraphs[0]
    p_c1.text = "Presented by: Student Candidate                                               Project Supervisor / Guide:"
    p_c1.font.size = Pt(11)
    p_c1.font.bold = True
    p_c1.font.color.rgb = C_WHITE

    p_c2 = tf_cg.add_paragraph()
    p_c2.text = "Reg. / Roll No: [University Roll Number]                                   Assistant Professor, Dept. of CSE"
    p_c2.font.size = Pt(10.5)
    p_c2.font.color.rgb = RGBColor(203, 213, 225)
    p_c2.space_before = Pt(4)

    # Slide 1 Footer
    f1_box = s1.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.733), Inches(0.4))
    tf_f1 = f1_box.text_frame
    p_f1 = tf_f1.paragraphs[0]
    p_f1.text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING                                                                                    SLIDE NO: 1"
    p_f1.font.size = Pt(9)
    p_f1.font.bold = True
    p_f1.font.color.rgb = C_TEXT_MUTED

    # =========================================================================
    # SLIDE 2: AGENDA
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2, C_LIGHT_BG)
    add_slide_structure(s2, 2, "Agenda")

    # Display the exact bulleted agenda specified in the syllabus
    card_left = add_card(s2, Inches(0.8), Inches(1.5), Inches(5.8), Inches(5.1))
    tb_al = s2.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.4), Inches(4.7))
    tf_al = tb_al.text_frame
    tf_al.word_wrap = True

    agenda_left = [
        ("Abstract", "Executive summary of clinical objectives, models, and empirical outcomes"),
        ("Scope and Motivation", "Healthcare burden, rural doctor shortages, and preventative screening"),
        ("Introduction", "Evolution of medical AI, clinical decision support systems (CDSS)"),
        ("Literature Survey", "Chronological table (1988–2024) evaluating prior state-of-the-art"),
        ("Objectives", "Quantifiable engineering, algorithmic, and deployment targets"),
        ("Problem Statement", "Mathematical risk formulation and shortcomings of legacy systems"),
        ("Proposed Work", "Six-phase end-to-end full-stack machine learning engineering methodology")
    ]

    for idx, (title, desc) in enumerate(agenda_left):
        p_t = tf_al.paragraphs[0] if idx == 0 else tf_al.add_paragraph()
        p_t.text = f"•  {title}"
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = C_INDIGO
        if idx > 0:
            p_t.space_before = Pt(8)

        p_d = tf_al.add_paragraph()
        p_d.text = f"    {desc}"
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = C_TEXT_MUTED
        p_d.space_before = Pt(1)

    card_right = add_card(s2, Inches(6.75), Inches(1.5), Inches(5.78), Inches(5.1))
    tb_ar = s2.shapes.add_textbox(Inches(6.95), Inches(1.7), Inches(5.4), Inches(4.7))
    tf_ar = tb_ar.text_frame
    tf_ar.word_wrap = True

    agenda_right = [
        ("Architecture Diagram / Flow Diagram / Block Diagram", "Four-tier decoupled client-server & model inference architecture"),
        ("Novel idea", "Acoustic phonation, multi-modal convergence, and dynamic PDF generation"),
        ("Modules", "Decomposition of Diabetes, Heart, Parkinson's, Breast Cancer, and Report engine"),
        ("Module Description", "Detailed algorithmic specifications, feature sets, and verified accuracies"),
        ("Software & Hardware Requirements", "Development libraries, frameworks, environment specs, and Docker specs"),
        ("References (Base paper submitted)", "Foundational academic literature (IEEE / Springer) and base paper submission"),
        ("Way forward towards Outcome", "Publication strategy (IEEE/Scopus), copyright/patent filing, and clinical trials")
    ]

    for idx, (title, desc) in enumerate(agenda_right):
        p_t = tf_ar.paragraphs[0] if idx == 0 else tf_ar.add_paragraph()
        p_t.text = f"•  {title}"
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = C_INDIGO
        if idx > 0:
            p_t.space_before = Pt(8)

        p_d = tf_ar.add_paragraph()
        p_d.text = f"    {desc}"
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = C_TEXT_MUTED
        p_d.space_before = Pt(1)

    # =========================================================================
    # SLIDE 3: ABSTRACT
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3, C_LIGHT_BG)
    add_slide_structure(s3, 3, "Abstract")

    add_card(s3, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.1))
    tb_abs = s3.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.1), Inches(4.5))
    tf_abs = tb_abs.text_frame
    tf_abs.word_wrap = True

    p_a1 = tf_abs.paragraphs[0]
    p_a1.text = "Executive Summary:"
    p_a1.font.size = Pt(14)
    p_a1.font.bold = True
    p_a1.font.color.rgb = C_INDIGO

    p_a2 = tf_abs.add_paragraph()
    p_a2.text = (
        "Early identification of chronic and life-threatening medical conditions is imperative for timely therapeutic "
        "intervention, mitigating morbidity rates, and reducing systemic burdens on hospital infrastructures. Conventional "
        "diagnostic workflows are frequently delayed by specialist deficits, laboratory turnaround times, and high financial costs. "
        "This project presents MediScan AI, an intelligent, multi-modal clinical decision-support system designed to perform "
        "instantaneous predictive disease risk screening across non-invasive clinical biomarkers.\n\n"
        "The proposed platform evaluates four distinct medical domains: Type 2 Diabetes Mellitus (Support Vector Classifier), "
        "Cardiovascular Disease (Logistic Regression with calibrated probability scoring), Parkinson's Disease via vocal acoustic "
        "dysphonia analysis (Linear SVM on 22 speech perturbations), and Breast Cancer fine needle aspirate biopsy cytopathology "
        "(Ensemble Random Forest Pipeline with StandardScaler).\n\n"
        "Addressing the severe latency and rigidity of prototype scripts (e.g., Streamlit), MediScan AI implements a high-performance "
        "asynchronous architecture leveraging FastAPI and Uvicorn. The client interface is built as a reactive Single Page Application (SPA) "
        "with Tailwind CSS and Chart.js, delivering real-time interactive risk meters in sub-20ms. Furthermore, an integrated automated "
        "reporting engine compiles downloadable, hospital-ready PDF diagnostic summaries with full patient telemetry. "
        "Empirical evaluation establishes test classification accuracies of 77.3% (Diabetes), 80.3% (Heart Disease), 87.2% (Parkinson's), "
        "and 97.4% (Breast Cancer), confirming the platform as an accurate, scalable preliminary clinical triage solution."
    )
    p_a2.font.size = Pt(11)
    p_a2.font.color.rgb = C_TEXT_DARK
    p_a2.space_before = Pt(8)

    # =========================================================================
    # SLIDE 4: SCOPE AND MOTIVATION
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4, C_LIGHT_BG)
    add_slide_structure(s4, 4, "Scope and Motivation")

    scope_cards = [
        ("Clinical Motivation", "• Non-Communicable Diseases (NCDs) cause 74% of all annual deaths worldwide (WHO).\n• Asymptomatic latency periods in cardiovascular illness, diabetes, and Parkinson's lead to delayed clinical diagnosis.\n• Global primary healthcare faces severe specialist deficits, demanding fast, low-cost pre-diagnostic screening tools.", C_INDIGO),
        ("Project Scope", "• Targets 4 major non-communicable disease categories: metabolic, cardiac, neurological, and oncological.\n• Ingests non-invasive clinical telemetry, laboratory vitals, acoustic voice recordings, and biopsy cytology.\n• Provides instant risk stratification, actionable lifestyle guidance, and official patient PDF summaries.", C_BLUE),
        ("Target Beneficiaries", "• Primary Healthcare Workers: Rapid triage prioritization of high-risk patients before specialist referral.\n• Telemedicine Centers: Remote screening in underserved rural clinics with zero-reload interface responsiveness.\n• Patients: Clear visual interpretation of personal risk indices and downloadable doctor-ready documentation.", C_EMERALD)
    ]

    for i, (title, content, color) in enumerate(scope_cards):
        left = Inches(0.8 + i * 3.95)
        add_card(s4, left, Inches(1.5), Inches(3.8), Inches(5.1))
        
        tb = s4.shapes.add_textbox(left + Inches(0.2), Inches(1.7), Inches(3.4), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = color

        p_c = tf.add_paragraph()
        p_c.text = content
        p_c.font.size = Pt(10.5)
        p_c.font.color.rgb = C_TEXT_DARK
        p_c.space_before = Pt(10)

    # =========================================================================
    # SLIDE 5: INTRODUCTION
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5, C_LIGHT_BG)
    add_slide_structure(s5, 5, "Introduction")

    intro_points = [
        ("Evolution of AI in Modern Healthcare", "Machine learning and artificial intelligence have evolved healthcare from reactive treatment to predictive, preventative triage. Machine learning algorithms uncover intricate, multi-dimensional correlations across physiological vitals that may escape standard clinical observation."),
        ("Clinical Decision Support Systems (CDSS)", "Modern CDSS applications empower physicians by functioning as intelligent preliminary decision aids. Rather than replacing certified medical practitioners, MediScan AI provides evidence-based risk scoring and flags anomalous biomarkers for immediate clinical review."),
        ("The Need for Multi-Modal Disease Convergence", "Current academic and clinical diagnostic tools are deeply fragmented—offering isolated single-disease scripts in silos. MediScan AI solves this by integrating metabolic, cardiovascular, neurological, and oncological risk screening into a single cohesive platform."),
        ("Transitioning from Prototypes to Production Software", "Conventional academic projects rely on script-based prototyping dashboards (e.g., Streamlit) that rerun the entire codebase on every user click, resulting in high latency. MediScan AI introduces a production-ready asynchronous FastAPI backend and a responsive Single Page Application.")
    ]

    for i, (head, text) in enumerate(intro_points):
        top = Inches(1.5 + i * 1.25)
        add_card(s5, Inches(0.8), top, Inches(11.733), Inches(1.12))
        
        tb = s5.shapes.add_textbox(Inches(1.0), top + Inches(0.12), Inches(11.3), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = head
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_INDIGO

        p_t = tf.add_paragraph()
        p_t.text = text
        p_t.font.size = Pt(10)
        p_t.font.color.rgb = C_TEXT_DARK
        p_t.space_before = Pt(3)

    # =========================================================================
    # SLIDE 6: LITERATURE SURVEY (Table format-year in Chronological order)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6, C_LIGHT_BG)
    add_slide_structure(s6, 6, "Literature Survey ( Table format-year should be in Chronological order)")

    # Table: 6 rows (1 header + 5 papers in chronological order), 5 columns
    t_shape = s6.shapes.add_table(6, 5, Inches(0.8), Inches(1.5), Inches(11.733), Inches(4.5))
    t = t_shape.table

    col_widths = [Inches(1.0), Inches(2.8), Inches(2.4), Inches(2.8), Inches(2.733)]
    for j, w in enumerate(col_widths):
        t.columns[j].width = w

    headers_lit = ["Year", "Author & Publication", "Domain & Dataset", "Methodology / Model", "Identified Limitations"]
    for j, h in enumerate(headers_lit):
        cell = t.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_NAVY_DARK
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

    lit_data = [
        ["1988", "Smith et al. (IEEE Computer Applications in Medicine)", "Diabetes (Pima Indians Dataset)", "ADAP Associative Learning Neural Network", "Small sample size (768 records); high false negative rate; no interactive web deployment."],
        ["1989", "Detrano et al. (Am. Journal of Cardiology)", "Cardiovascular (Cleveland Clinic)", "Logistic Regression & Probability Matrix", "Manual probability calculation; restricted to static features without real-time API integration."],
        ["1995", "Wolberg, Street, et al. (UCI / PNAS)", "Breast Cancer (Wisconsin FNA Biopsy)", "Linear Programming & Multisurface Method", "Evaluated single isolated image features; lacked ensemble learning and web diagnostic reporting."],
        ["2007", "Little et al. (IEEE Trans. Biomedical Eng.)", "Parkinson's Disease (Vocal Dysphonia)", "Non-linear dynamical speech analysis & SVM", "Acoustic-only study; lacked end-to-end client integration, visual risk gauges, and clinical summary export."],
        ["2021", "Mohan et al. (Springer Computer Methods)", "Heart Disease Prediction System", "Hybrid Machine Learning (Random Forest + Linear Model)", "Monolithic script architecture; high latency; no automated hospital-ready PDF generation."]
    ]

    for i, row in enumerate(lit_data):
        for j, val in enumerate(row):
            cell = t.cell(i + 1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_WHITE if i % 2 == 0 else C_LIGHT_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(9)
            p.font.color.rgb = C_TEXT_DARK
            p.alignment = PP_ALIGN.CENTER if j == 0 else PP_ALIGN.LEFT

    callout_lit = s6.shapes.add_textbox(Inches(0.8), Inches(6.1), Inches(11.733), Inches(0.6))
    tf_cl = callout_lit.text_frame
    p_cl = tf_cl.paragraphs[0]
    p_cl.text = "Research Gap Addressed: Existing literature focuses on siloed single-disease models without unified full-stack integration, instant zero-reload reactive user interfaces, or automated clinical report generation."
    p_cl.font.size = Pt(9.5)
    p_cl.font.italic = True
    p_cl.font.bold = True
    p_cl.font.color.rgb = C_INDIGO

    # =========================================================================
    # SLIDE 7: OBJECTIVES (Placed before Problem Statement per syllabus order)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7, C_LIGHT_BG)
    add_slide_structure(s7, 7, "Objectives")

    objs_data = [
        ("Objective 1: Multi-Class Biomedical Modeling", "Train, tune, and persist four specialized supervised classifiers: Support Vector Classifier for Diabetes (77.3%), Logistic Regression for Heart Disease (80.3%), Linear SVM for Parkinson's dysphonia (87.2%), and an Ensemble Random Forest Pipeline for Breast Cancer (97.4%)."),
        ("Objective 2: Robust Data Pipeline & Leakage Elimination", "Implement automated feature scaling pipelines using StandardScaler() encapsulated within Scikit-Learn Pipeline structures, preventing data leakage and guaranteeing feature schema alignment."),
        ("Objective 3: Decoupled Asynchronous API Development", "Architect high-performance RESTful API microservices utilizing FastAPI and Uvicorn with Pydantic request validation schemas and automatic OpenAPI / Swagger interactive documentation (/docs)."),
        ("Objective 4: Reactive Zero-Reload User Interface", "Construct a responsive Single Page Application (SPA) leveraging Tailwind CSS and Chart.js, rendering dynamic risk meters, visual gauges, and biomarker benchmark comparisons with sub-20ms AJAX latency."),
        ("Objective 5: Automated Clinical PDF Report Engine", "Develop an on-demand PDF report generation engine (fpdf2) that creates structured clinical screening summaries incorporating patient metadata, biomarker breakdown tables, and medical next-steps in 1 click."),
        ("Objective 6: Quality Assurance & Deployment Readiness", "Implement an automated test suite (test_app.py) validating 100% of prediction pathways and containerize the entire architecture with Docker for cross-platform cloud portability.")
    ]

    for i, (title, desc) in enumerate(objs_data):
        top = Inches(1.5 + i * 0.85)
        add_card(s7, Inches(0.8), top, Inches(11.733), Inches(0.75))
        
        tb = s7.shapes.add_textbox(Inches(1.0), top + Inches(0.08), Inches(11.3), Inches(0.6))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = C_INDIGO

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = C_TEXT_DARK
        p_d.space_before = Pt(2)

    # =========================================================================
    # SLIDE 8: PROBLEM STATEMENT
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8, C_LIGHT_BG)
    add_slide_structure(s8, 8, "Problem Statement")

    add_card(s8, Inches(0.8), Inches(1.5), Inches(11.733), Inches(1.5), bg_color=C_WHITE, border_color=C_INDIGO, line_w=1.5)
    tb_ps = s8.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.3), Inches(1.3))
    tf_ps = tb_ps.text_frame
    tf_ps.word_wrap = True

    p_p1 = tf_ps.paragraphs[0]
    p_p1.text = "Formal Problem Definition:"
    p_p1.font.size = Pt(13)
    p_p1.font.bold = True
    p_p1.font.color.rgb = C_INDIGO

    p_p2 = tf_ps.add_paragraph()
    p_p2.text = (
        "\"To design, develop, and validate an automated, asynchronous multi-disease clinical screening system that accurately "
        "predicts disease likelihood across metabolic, cardiovascular, neurological, and oncological vectors from non-invasive "
        "biomarkers, while delivering instantaneous visual risk indices and automated clinical PDF documentation with sub-20ms inference latency.\""
    )
    p_p2.font.size = Pt(11)
    p_p2.font.italic = True
    p_p2.font.color.rgb = C_TEXT_DARK
    p_p2.space_before = Pt(4)

    # 3 Root Challenges
    challenges = [
        ("Challenge 1: Isolated Diagnostic Silos", "Clinicians currently must rely on fragmented, standalone predictive scripts for different conditions, leading to inefficient clinical triage and inconsistent patient risk records."),
        ("Challenge 2: Inflexible Dashboard Performance", "Legacy Python dashboard prototypes (e.g. Streamlit) suffer from full-page re-execution on every parameter change, causing high latency, interface lag, and state loss."),
        ("Challenge 3: Absence of Actionable Output", "Existing academic models simply return binary values (0 or 1) without calculating continuous risk probabilities, comparative biomarker benchmarks, or generating hospital-ready reports.")
    ]

    for i, (h, b) in enumerate(challenges):
        left = Inches(0.8 + i * 3.95)
        add_card(s8, left, Inches(3.2), Inches(3.8), Inches(3.4))
        tb = s8.shapes.add_textbox(left + Inches(0.2), Inches(3.35), Inches(3.4), Inches(3.0))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = h
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_INDIGO

        p_b = tf.add_paragraph()
        p_b.text = b
        p_b.font.size = Pt(10)
        p_b.font.color.rgb = C_TEXT_DARK
        p_b.space_before = Pt(8)

    # =========================================================================
    # SLIDE 9: PROPOSED WORK
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_bg(s9, C_LIGHT_BG)
    add_slide_structure(s9, 9, "Proposed Work")

    phases = [
        ("Phase 1: Dataset Acquisition", "Collect and validate benchmark biomedical datasets (PIDD, Cleveland Heart, Oxford Voice, and Wisconsin Diagnostic Biopsy).", C_INDIGO),
        ("Phase 2: Preprocessing & Splitting", "Execute median/mean null imputation, stratified 80/20 train-test splitting, and unit standardization via StandardScaler.", C_BLUE),
        ("Phase 3: Model Engineering", "Train supervised models (Linear SVM, Logistic Regression, Random Forest); calibrate sigmoid probability scoring metrics.", C_INDIGO),
        ("Phase 4: API Backend Service", "Build asynchronous FastAPI endpoints (/api/predict/*, /api/report/pdf) with strict Pydantic payload validation.", C_BLUE),
        ("Phase 5: Reactive Web Interface", "Develop Tailwind CSS single-page interface with Chart.js visual gauges, presets, and asynchronous fetch() communication.", C_INDIGO),
        ("Phase 6: Clinical PDF Generation", "Integrate fpdf2 reporting module to compile formatted clinical reports with patient biomarkers and clinical next-steps.", C_EMERALD)
    ]

    for i, (title, desc, color) in enumerate(phases):
        col = i % 3
        row = i // 3
        left = Inches(0.8 + col * 3.95)
        top = Inches(1.5 + row * 2.5)
        
        add_card(s9, left, top, Inches(3.8), Inches(2.3))
        tb = s9.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), Inches(3.4), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = color

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = C_TEXT_DARK
        p_d.space_before = Pt(8)

    # =========================================================================
    # SLIDE 10: ARCHITECTURE DIAGRAM / FLOW DIAGRAM / BLOCK DIAGRAM
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_bg(s10, C_LIGHT_BG)
    add_slide_structure(s10, 10, "Architecture Diagram/Flow Diagram/Block Diagram")

    arch_blocks = [
        ("TIER 1: CLIENT PRESENTATION", "Tailwind CSS + Chart.js SPA", ["Single Page Interface", "Asynchronous AJAX fetch()", "Real-time Chart.js gauges", "Patient Presets & Demo data", "Zero page reloads"]),
        ("TIER 2: API GATEWAY", "FastAPI + Uvicorn Server", ["Asynchronous HTTP Router", "Pydantic Schema Validation", "Interactive Docs (/docs)", "Sub-20ms inference latency", "CORS & Request logging"]),
        ("TIER 3: INFERENCE PIPELINES", "Scikit-Learn ML Engines", ["StandardScaler Preprocessing", "SVM Linear Classifiers", "Logistic Regression Probabilities", "Random Forest Ensembles", "Serialized Model Binaries (.sav)"]),
        ("TIER 4: OUTPUT & REPORTING", "Clinical Document Generator", ["fpdf2 PDF Compilation Engine", "Itemized Biomarker Breakdown", "Categorized Risk Severity Badge", "Clinical Next-Steps Protocols", "1-Click Browser Download"])
    ]

    for i, (tier_title, subtitle, items) in enumerate(arch_blocks):
        left = Inches(0.8 + i * 2.95)
        add_card(s10, left, Inches(1.5), Inches(2.8), Inches(5.1))
        
        tb = s10.shapes.add_textbox(left + Inches(0.15), Inches(1.7), Inches(2.5), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = tier_title
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_INDIGO

        p_s = tf.add_paragraph()
        p_s.text = subtitle
        p_s.font.size = Pt(10)
        p_s.font.bold = True
        p_s.font.color.rgb = C_TEXT_DARK
        p_s.space_before = Pt(3)

        for item in items:
            pi = tf.add_paragraph()
            pi.text = f"• {item}"
            pi.font.size = Pt(9.5)
            pi.font.color.rgb = C_TEXT_MUTED
            pi.space_before = Pt(6)

    # =========================================================================
    # SLIDE 11: NOVEL IDEA
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_bg(s11, C_LIGHT_BG)
    add_slide_structure(s11, 11, "Novel idea")

    novelties = [
        ("1. Multi-Modal Clinical Convergence", "Unlike existing single-disease scripts, MediScan AI integrates four completely different clinical modalities into one unified decision-support engine—covering metabolic, cardiovascular, acoustic dysphonia, and biopsy cytopathology within a cohesive interface."),
        ("2. Asynchronous Decoupled Microservice Design", "Eliminates the performance bottleneck of legacy academic prototypes (such as Streamlit scripts that execute the entire codebase from line 1 on every click). Achieves sub-20ms inference latency with true async client-server decoupling."),
        ("3. Continuous Risk Index Calibration", "Transitions beyond naive binary 0/1 outputs by calculating calibrated continuous risk percentages (0-100%) through logistic sigmoid transformations and decision margins, providing clinicians with nuanced diagnostic confidence."),
        ("4. Automated Hospital-Grade Clinical PDF Generation", "Solves the clinical documentation gap by automatically compiling vector-rendered diagnostic summary reports complete with patient parameters, visual risk badges, and specialty-specific follow-up recommendations.")
    ]

    for i, (title, text) in enumerate(novelties):
        top = Inches(1.5 + i * 1.25)
        add_card(s11, Inches(0.8), top, Inches(11.733), Inches(1.15))
        
        tb = s11.shapes.add_textbox(Inches(1.0), top + Inches(0.12), Inches(11.3), Inches(0.95))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_INDIGO

        p_t = tf.add_paragraph()
        p_t.text = text
        p_t.font.size = Pt(10)
        p_t.font.color.rgb = C_TEXT_DARK
        p_t.space_before = Pt(3)

    # =========================================================================
    # SLIDE 12: MODULES
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_bg(s12, C_LIGHT_BG)
    add_slide_structure(s12, 12, "Modules")

    modules_list = [
        ("Module 1: Diabetes Mellitus Screening", "Evaluates metabolic vitals (Glucose, Insulin, BMI, Diastolic BP, Age, Skin Thickness, Pedigree) to screen for Type 2 Diabetes risk.", C_INDIGO),
        ("Module 2: Cardiovascular Disease Assessment", "Analyzes 13 cardiovascular variables (Chest Pain type, Resting BP, Cholesterol, ECG, Max HR, ST depression, Fluoroscopy) to detect coronary artery disease.", C_BLUE),
        ("Module 3: Parkinson's Acoustic Phonation Analysis", "Evaluates 22 vocal acoustic features (Fundamental frequencies, Jitter %, Shimmer dB, HNR, NHR, Fractal scaling, Pitch Period Entropy) for early neurodegenerative detection.", C_INDIGO),
        ("Module 4: Breast Cancer Biopsy Staging", "Classifies fine needle aspirate (FNA) cell nuclei morphology (Radius, Texture, Perimeter, Area, Smoothness, Concavity) into Benign or Malignant pathology.", C_BLUE),
        ("Module 5: Automated Clinical Reporting Engine", "Dynamic PDF compilation service generating official patient diagnostic summary documents with biomarker tables and medical protocols.", C_EMERALD)
    ]

    for i, (name, details, color) in enumerate(modules_list):
        top = Inches(1.5 + i * 0.98)
        add_card(s12, Inches(0.8), top, Inches(11.733), Inches(0.85))
        
        tb = s12.shapes.add_textbox(Inches(1.0), top + Inches(0.1), Inches(11.3), Inches(0.65))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = color

        p_d = tf.add_paragraph()
        p_d.text = details
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = C_TEXT_DARK
        p_d.space_before = Pt(2)

    # =========================================================================
    # SLIDE 13: MODULE DESCRIPTION
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_bg(s13, C_LIGHT_BG)
    add_slide_structure(s13, 13, "Module Description")

    mod_details = [
        ("Diabetes Screening", "Support Vector Classifier", "8 Vitals & Metabolic markers", "77.27%", "Calculates insulin resistance and glucose tolerance boundary margin; outputs diabetic risk stratification."),
        ("Cardiovascular Disease", "Logistic Regression (L2)", "13 Cardiac examination findings", "80.33%", "Estimates coronary disease odds ratio via Sigmoid transformation; provides calibrated percentage risk (0-100%)."),
        ("Parkinson's Vocal Analysis", "Linear Support Vector Machine", "22 Voice dysphonia measurements", "87.18%", "Evaluates acoustic micro-tremors, period fluctuations, and vocal noise ratios; identifies early Parkinsonian speech."),
        ("Breast Cancer Biopsy", "Random Forest Pipeline (100 Trees)", "30 FNA cell nuclei features", "97.37%", "Combines StandardScaler with 100 decision trees to detect non-linear atypia; delivers 97.6% clinical oncology recall.")
    ]

    for i, (m_name, algo, inputs, acc, desc) in enumerate(mod_details):
        col = i % 2
        row = i // 2
        left = Inches(0.8 + col * 5.95)
        top = Inches(1.5 + row * 2.5)
        
        add_card(s13, left, top, Inches(5.8), Inches(2.3))
        tb = s13.shapes.add_textbox(left + Inches(0.2), top + Inches(0.12), Inches(5.4), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = m_name
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = C_INDIGO

        p1 = tf.add_paragraph()
        p1.text = f"Algorithm: {algo}   |   Accuracy: {acc}"
        p1.font.size = Pt(10.5)
        p1.font.bold = True
        p1.font.color.rgb = C_EMERALD if "97" in acc or "87" in acc else C_BLUE
        p1.space_before = Pt(3)

        p2 = tf.add_paragraph()
        p2.text = f"Input Dimensions: {inputs}"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = C_TEXT_MUTED
        p2.space_before = Pt(3)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = C_TEXT_DARK
        p3.space_before = Pt(4)

    # =========================================================================
    # SLIDE 14: SOFTWARE & HARDWARE REQUIREMENTS
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_bg(s14, C_LIGHT_BG)
    add_slide_structure(s14, 14, "Software & Hardware Requirements")

    # Software Card
    add_card(s14, Inches(0.8), Inches(1.5), Inches(5.8), Inches(5.1))
    tb_sw = s14.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.4), Inches(4.7))
    tf_sw = tb_sw.text_frame
    tf_sw.word_wrap = True

    p = tf_sw.paragraphs[0]
    p.text = "Software Specifications"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_INDIGO

    sw_items = [
        ("Operating System", "Windows 10/11, Ubuntu Linux 20.04+, or macOS"),
        ("Programming Language", "Python 3.10 – 3.12 (64-bit)"),
        ("Backend Framework", "FastAPI (v0.110+) & Uvicorn ASGI Server"),
        ("Machine Learning", "Scikit-Learn (v1.3+), NumPy, Pandas"),
        ("Frontend Technologies", "HTML5, Tailwind CSS, Chart.js, Lucide Icons"),
        ("Reporting Engine", "fpdf2 (v2.7+) Vector PDF Generator"),
        ("Containerization", "Docker & Docker Compose (v20.10+)"),
        ("Development Tools", "Visual Studio Code, Git, PowerShell / Bash")
    ]

    for k, v in sw_items:
        p_item = tf_sw.add_paragraph()
        p_item.text = f"• {k}: {v}"
        p_item.font.size = Pt(9.5)
        p_item.font.color.rgb = C_TEXT_DARK
        p_item.space_before = Pt(5)

    # Hardware Card
    add_card(s14, Inches(6.75), Inches(1.5), Inches(5.78), Inches(5.1))
    tb_hw = s14.shapes.add_textbox(Inches(6.95), Inches(1.7), Inches(5.4), Inches(4.7))
    tf_hw = tb_hw.text_frame
    tf_hw.word_wrap = True

    p_h = tf_hw.paragraphs[0]
    p_h.text = "Hardware Specifications"
    p_h.font.size = Pt(14)
    p_h.font.bold = True
    p_h.font.color.rgb = C_BLUE

    hw_items = [
        ("Processor (CPU)", "Intel Core i3 / AMD Ryzen 3 or higher (Quad-core recommended)"),
        ("Memory (RAM)", "Minimum 4 GB (8 GB recommended for concurrent inference)"),
        ("Storage (Disk)", "Minimum 2 GB free disk space (for datasets, venv, and models)"),
        ("Display Resolution", "1366 × 768 minimum (1920 × 1080 Full HD recommended)"),
        ("Network Interface", "Standard Ethernet / Wi-Fi adapter (for local network hosting)"),
        ("Client Devices", "Compatible with desktop PC, laptop, iPad / Android clinical tablets")
    ]

    for k, v in hw_items:
        p_item = tf_hw.add_paragraph()
        p_item.text = f"• {k}: {v}"
        p_item.font.size = Pt(9.5)
        p_item.font.color.rgb = C_TEXT_DARK
        p_item.space_before = Pt(6)

    # =========================================================================
    # SLIDE 15: REFERENCES (Base paper hard copy to be submitted to supervisor)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_bg(s15, C_NAVY_DARK)

    # Header Box on Dark
    t_box = s15.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.733), Inches(0.8))
    tf_t = t_box.text_frame
    p_t = tf_t.paragraphs[0]
    p_t.text = "References (Base paper hard copy to be submitted to the supervisor.)"
    p_t.font.size = Pt(18)
    p_t.font.bold = True
    p_t.font.color.rgb = C_WHITE

    # Base Paper Notice Card
    notice_card = add_card(s15, Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.75), bg_color=C_NAVY_MED, border_color=C_EMERALD)
    tb_n = s15.shapes.add_textbox(Inches(1.0), Inches(1.38), Inches(11.3), Inches(0.6))
    tf_n = tb_n.text_frame
    p_n = tf_n.paragraphs[0]
    p_n.text = "★ Official Notice: Base paper hard copy to be submitted directly to the project supervisor."
    p_n.font.size = Pt(11)
    p_n.font.bold = True
    p_n.font.color.rgb = C_EMERALD

    # References Card
    ref_card = add_card(s15, Inches(0.8), Inches(2.2), Inches(11.733), Inches(4.4), bg_color=C_NAVY_MED, border_color=C_BORDER)
    tb_r = s15.shapes.add_textbox(Inches(1.0), Inches(2.35), Inches(11.3), Inches(4.1))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    p_rh = tf_r.paragraphs[0]
    p_rh.text = "Formal IEEE Format Citations:"
    p_rh.font.size = Pt(12)
    p_rh.font.bold = True
    p_rh.font.color.rgb = C_WHITE

    academic_refs = [
        "[1] W. H. Wolberg, W. N. Street, and O. L. Mangasarian, \"Breast Cancer Wisconsin (Diagnostic) Dataset,\" UCI Machine Learning Repository, 1995.",
        "[2] M. A. Little, P. E. McSharry, S. J. Roberts, D. A. Costello, and I. M. Moroz, \"Suitability of dysphonia measurements for telemonitoring of Parkinson's disease,\" IEEE Transactions on Biomedical Engineering, vol. 56, no. 4, pp. 1015-1022, 2009.",
        "[3] R. Detrano, A. Janosi, W. Steinbrunn, M. Pfisterer, J. Schmid, S. Sandhu, K. Guppy, S. Lee, and V. Froelicher, \"International application of a new probability algorithm for the diagnosis of coronary artery disease,\" The American Journal of Cardiology, vol. 64, no. 5, pp. 304-310, 1989.",
        "[4] J. W. Smith, J. E. Everhart, W. C. Dickson, W. C. Knowler, and R. S. Johannes, \"Using the ADAP learning algorithm to forecast the onset of diabetes mellitus,\" in Proc. Annu. Symp. Comput. Appl. Med. Care, 1988, pp. 261-265.",
        "[5] S. Mohan, C. Thirumalai, and G. Srivastava, \"Effective Heart Disease Prediction Using Hybrid Machine Learning Techniques,\" IEEE Access, vol. 7, pp. 81542-81554, 2019."
    ]

    for ref in academic_refs:
        p_ref = tf_r.add_paragraph()
        p_ref.text = ref
        p_ref.font.size = Pt(9.5)
        p_ref.font.color.rgb = RGBColor(203, 213, 225)
        p_ref.space_before = Pt(6)

    # Slide 15 Footer
    f15_box = s15.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.733), Inches(0.4))
    tf_f15 = f15_box.text_frame
    p_f15 = tf_f15.paragraphs[0]
    p_f15.text = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING                                                                                    SLIDE NO: 15"
    p_f15.font.size = Pt(9)
    p_f15.font.bold = True
    p_f15.font.color.rgb = C_TEXT_MUTED

    # =========================================================================
    # SLIDE 16: WAY FORWARD TOWARDS OUTCOME (Research Paper/Patent)
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    set_bg(s16, C_LIGHT_BG)
    add_slide_structure(s16, 16, "Way forward towards Outcome (Research Paper/Patent)")

    outcomes = [
        ("1. Research Paper Publication", "Target Venues: IEEE International Conference on Bioinformatics and Biomedicine (BIBM) / Springer Lecture Notes in Networks and Systems.\n\nManuscript Focus: 'A Decoupled Asynchronous Microservice Framework for Multi-Disease Clinical Triage and Automated Diagnostic Report Generation.'", C_INDIGO),
        ("2. Intellectual Property (IP / Copyright)", "Software Copyright Registration: Registering the MediScan AI source code, pipeline orchestration algorithms, and automated clinical PDF template compilation architecture under the National Copyright Office.\n\nPatent Potential: Method and system for multi-modal asynchronous clinical risk score calibration and automated document synthesis.", C_BLUE),
        ("3. Production Deployment & Telemedicine Pilot", "Container Deployment: Deploying the Dockerized container onto cloud infrastructure (Render / AWS ECS / HuggingFace Spaces) with SSL encryption.\n\nPilot Integration: Partnering with community clinics to evaluate usability, clinical decision support utility, and physician workflow efficiency.", C_EMERALD)
    ]

    for i, (head, body, color) in enumerate(outcomes):
        left = Inches(0.8 + i * 3.95)
        add_card(s16, left, Inches(1.5), Inches(3.8), Inches(5.1))
        
        tb = s16.shapes.add_textbox(left + Inches(0.2), Inches(1.7), Inches(3.4), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = head
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = color

        p_b = tf.add_paragraph()
        p_b.text = body
        p_b.font.size = Pt(10)
        p_b.font.color.rgb = C_TEXT_DARK
        p_b.space_before = Pt(10)

    output_path = "MediScan_AI_Department_Presentation.pptx"
    prs.save(output_path)
    print(f"University presentation successfully created: {output_path}")
    
    # Try also updating the original if not locked by PowerPoint
    try:
        prs.save("MediScan_AI_University_Presentation.pptx")
        print("Also updated: MediScan_AI_University_Presentation.pptx")
    except PermissionError:
        print("Note: MediScan_AI_University_Presentation.pptx is open in PowerPoint. Saved to MediScan_AI_Department_Presentation.pptx")

if __name__ == "__main__":
    create_university_deck()
