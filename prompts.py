def build_research_prompt(topic, domain, keywords, complexity):
    return f"""
You are an expert academic research assistant.

Generate a structured research blueprint based on:

Topic: {topic}
Domain: {domain}
Keywords: {keywords if keywords else "Not specified"}
Complexity Level: {complexity}

Return the response strictly in this structured format:

Title:
Abstract:
Problem Statement:
Research Gap:
Methodology:
Expected Contributions:
Outline (numbered list):

Make it academically professional and realistic.
"""
def build_gap_analysis_prompt(topic, abstract_1, abstract_2):

    return f"""
You are an advanced academic research analyst.

Research Topic:
{topic}

Abstract 1:
{abstract_1}

Abstract 2:
{abstract_2 if abstract_2 else "Not provided"}

Perform deep comparative analysis and return:

1. Common Research Themes
2. Key Limitations Identified
3. Underexplored Areas
4. Refined Research Gap
5. Suggested Novel Research Direction

Be analytical and specific. Avoid generic statements.
"""
def build_abstract_refinement_prompt(blueprint_text):
    return f"""
You are an academic writing expert.

Refine and improve the following abstract to make it:
- More impactful
- Clearer
- Publication-ready
- Academically strong

Text:
{blueprint_text}
"""


def build_methodology_expansion_prompt(methodology_text):
    return f"""
Expand and strengthen this methodology section.
Add:
- Technical depth
- Tools/algorithms
- Evaluation metrics
- Experimental design clarity

Methodology:
{methodology_text}
"""


def build_title_optimization_prompt(topic):
    return f"""
Generate 5 high-impact, publication-optimized research titles for:

Topic:
{topic}

Make them suitable for Scopus/IEEE-level conferences.
"""
def build_conference_recommendation_prompt(topic, domain):
    return f"""
You are an academic conference advisor.

Based on this research topic:
{topic}

Domain:
{domain}

Suggest 5 well-known conferences where this work would be suitable.

Only return the conference names as a simple numbered list.
Do not add descriptions.
"""