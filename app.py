import streamlit as st
from utils import (
    generate_research_structure,
    parse_research_output,
    generate_pdf,
    analyze_research_gap,
    refine_abstract,
    expand_methodology,
    optimize_titles,
    recommend_conferences
)

# --------------------------------------------------
# PAGE CONFIG (ONLY ONCE)
# --------------------------------------------------
st.set_page_config(
    page_title="ResearchOS",
    page_icon="🧠",
    layout="wide"
)

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
st.sidebar.title("🧠 ResearchOS")

menu = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "📄 Blueprint Generator",
        "🧠 Research Gap Analyzer",
        "🚀 Research Copilot",
        "📅 Conference Recommendation"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("Built by Paras Mahajan")
# st.sidebar.markdown("Version 1.0")

# ==================================================
# HOME PAGE
# ==================================================
if menu == "🏠 Home":

    st.title("🧠 ResearchOS")
    st.subheader("AI-Powered Research Assistance Platform")

    st.markdown("""
    ### 🚀 What is ResearchOS?

    ResearchOS is an AI-powered research assistance system designed to help
    researchers from idea generation to publication planning.

    It combines:
    - Research Blueprint Generation
    - Deep Research Gap Analysis
    - Multi-Step AI Research Copilot
    - PDF Export Functionality
    - Conference Recommendation Engine

    Built using:
    - Streamlit
    - Gemini 2.5 AI
    # - Structured Prompt Engineering
    """)

    st.markdown("---")

    st.markdown("### 🔥 Core Features")

    st.markdown("""
    ✅ AI Research Paper Structuring  
    ✅ Deep Comparative Gap Analysis  
    ✅ Multi-Step Research Refinement Workflow  
    ✅ Publication-Oriented Title Optimization  
    ✅ PDF Blueprint Export 
    ✅ Conference Recommendation Based on Research Topic
    """)

# ==================================================
# BLUEPRINT GENERATOR
# ==================================================
elif menu == "📄 Blueprint Generator":

    st.header("📄 AI Research Blueprint Generator")

    topic = st.text_input("Research Topic")

    domain = st.selectbox(
        "Select Research Domain",
        [
            "Computer Science",
            "Artificial Intelligence",
            "Data Science",
            "Cybersecurity",
            "Electronics",
            "Mechanical Engineering",
            "Healthcare",
            "Social Sciences",
            "Other"
        ]
    )

    keywords = st.text_input("Keywords (Optional)")

    complexity = st.selectbox(
        "Select Complexity Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    generate_button = st.button("🚀 Generate Research Structure")

    if generate_button:
        if topic == "":
            st.warning("Please enter a research topic.")
        else:
            with st.spinner("Generating AI-powered research blueprint..."):
                result = generate_research_structure(topic, domain, keywords, complexity)

            parsed = parse_research_output(result)

            st.subheader("📄 Generated Research Blueprint")

            for section, content in parsed.items():
                with st.expander(section, expanded=(section == "Title")):
                    st.markdown(content)

            pdf_buffer = generate_pdf(parsed)

            st.download_button(
                label="📥 Download as PDF",
                data=pdf_buffer,
                file_name="Research_Blueprint.pdf",
                mime="application/pdf"
            )

# ==================================================
# RESEARCH GAP ANALYZER
# ==================================================
elif menu == "🧠 Research Gap Analyzer":

    st.header("🧠 Research Gap Deep Analyzer")

    topic_gap = st.text_input("Enter Your Research Topic")

    abstract_1 = st.text_area("Paste Abstract 1", height=150)
    abstract_2 = st.text_area("Paste Abstract 2 (Optional)", height=150)

    analyze_button = st.button("🔍 Analyze Research Gap")

    if analyze_button:
        if topic_gap and abstract_1:
            with st.spinner("Performing deep research gap analysis..."):
                gap_result = analyze_research_gap(topic_gap, abstract_1, abstract_2)

            st.subheader("📊 Gap Analysis Result")
            st.markdown(gap_result)
        else:
            st.warning("Please enter topic and at least one abstract.")

# ==================================================
# RESEARCH COPILOT
# ==================================================
elif menu == "🚀 Research Copilot":

    st.header("🚀 Multi-Step Research Copilot")

    copilot_topic = st.text_input("Enter Topic for Copilot Workflow")

    start_copilot = st.button("Start Copilot Process")

    if start_copilot and copilot_topic:

        with st.spinner("Generating initial blueprint..."):
            base_blueprint = generate_research_structure(
                copilot_topic, "Computer Science", "", "Advanced"
            )

        st.subheader("📄 Base Blueprint")
        st.markdown(base_blueprint)

        with st.spinner("Refining abstract..."):
            refined_abstract = refine_abstract(base_blueprint)

        st.subheader("✨ Refined Abstract")
        st.markdown(refined_abstract)

        with st.spinner("Optimizing titles..."):
            optimized_titles = optimize_titles(copilot_topic)

        st.subheader("🏆 Optimized Titles")
        st.markdown(optimized_titles)
elif menu == "📅 Conference Recommendation":

    st.header("📅 AI Conference Recommendation")

    conf_topic = st.text_input("Enter Your Research Topic")
    conf_domain = st.text_input("Research Domain")

    recommend_button = st.button("Suggest Conferences")

    if recommend_button and conf_topic:

        with st.spinner("Analyzing topic and recommending conferences..."):
            results = recommend_conferences(conf_topic, conf_domain)

        if results:
            for conf in results:
                st.subheader(conf["name"])
                st.write(f"Tier: {conf['tier']}")
                st.write(f"Website: {conf['website']}")
                st.markdown("---")
        else:
            st.warning("No direct match found in current database.")