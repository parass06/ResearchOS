import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

from prompts import (
    build_research_prompt,
    build_gap_analysis_prompt,
    build_abstract_refinement_prompt,
    build_methodology_expansion_prompt,
    build_title_optimization_prompt,
    build_conference_recommendation_prompt
)

from conference_data import conferences

# --------------------------------------------------
# LOAD API KEY (works for both local and Streamlit Cloud)
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# If running on Streamlit Cloud, use secrets
if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    st.error("⚠️ Gemini API key not found. Please configure it in Streamlit Secrets.")
else:
    genai.configure(api_key=api_key)

def generate_research_structure(topic, domain, keywords, complexity):

    prompt = build_research_prompt(topic, domain, keywords, complexity)

    model = genai.GenerativeModel("models/gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text
def parse_research_output(text):

    section_titles = [
        "Title",
        "Abstract",
        "Problem Statement",
        "Research Gap",
        "Methodology",
        "Expected Contributions",
        "Outline"
    ]

    sections = {}
    current_section = None

    lines = text.split("\n")

    for line in lines:
        clean_line = line.strip().replace("**", "")

        # Check if line matches any known section title
        for title in section_titles:
            if clean_line.lower().startswith(title.lower()):
                current_section = title
                sections[current_section] = ""
                break
        else:
            if current_section:
                sections[current_section] += line + "\n"

    return sections

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.platypus import ListFlowable, ListItem
from reportlab.platypus import KeepTogether

import io

def generate_pdf(parsed_sections):

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)

    elements = []
    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    normal_style = styles["BodyText"]

    for section, content in parsed_sections.items():

        elements.append(Paragraph(section, title_style))
        elements.append(Spacer(1, 0.2 * inch))

        for line in content.split("\n"):
            if line.strip():
                elements.append(Paragraph(line, normal_style))
                elements.append(Spacer(1, 0.1 * inch))

        elements.append(Spacer(1, 0.3 * inch))

    doc.build(elements)

    buffer.seek(0)
    return buffer
def analyze_research_gap(topic, abstract_1, abstract_2):

    prompt = build_gap_analysis_prompt(topic, abstract_1, abstract_2)

    model = genai.GenerativeModel("models/gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text
def refine_abstract(text):
    prompt = build_abstract_refinement_prompt(text)
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text


def expand_methodology(text):
    prompt = build_methodology_expansion_prompt(text)
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text


def optimize_titles(topic):
    prompt = build_title_optimization_prompt(topic)
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

from conference_data import conferences
from prompts import build_conference_recommendation_prompt

def recommend_conferences(topic, domain):

    prompt = build_conference_recommendation_prompt(topic, domain)

    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(prompt)

    suggested_names = response.text

    matched = []

    for conf in conferences:
        if conf["name"].lower() in suggested_names.lower():
            matched.append(conf)

    return matched