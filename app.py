import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Research Profile | Nomsa Phoswa",
    page_icon="🧬",
    layout="centered"
)

# =========================
# HEADER
# =========================
st.title("Nomsa Phoswa")
st.write("### MSc Biochemistry Researcher")
st.write("Sefako Makgatho Health Sciences University")

st.divider()

# =========================
# ABOUT ME
# =========================
st.header("About Me")
st.write("""
I am a Master of Science (MSc) Biochemistry student with a strong research interest
in infectious diseases, particularly **nontuberculous mycobacteria (NTM)**.
My work focuses on understanding how anti-tuberculosis drugs affect the
metabolic pathways of NTM in order to improve treatment strategies and
address drug resistance.
""")

# =========================
# RESEARCH TITLE
# =========================
st.header("Research Title")
st.markdown("""
**Investigation of the effects of bedaquiline and clofazimine on the metabolic profile
of nontuberculous mycobacteria**
""")

# =========================
# PROBLEM STATEMENT
# =========================
st.header("Problem Statement")
st.write("""
Nontuberculous mycobacteria (NTM) infections pose a growing public health challenge
due to their resistance to conventional anti-tuberculosis treatments.
Although drugs such as bedaquiline and clofazimine have shown effectiveness
against drug-resistant tuberculosis, their metabolic effects on NTM are not
fully understood. Investigating these metabolic changes may reveal novel
drug targets and improve patient outcomes.
""")

# =========================
# AIM AND OBJECTIVES
# =========================
st.header("Aim and Objectives")

st.markdown("""
**Aim:**  
To investigate the effects of bedaquiline and clofazimine on the metabolic profile
of nontuberculous mycobacteria.

**Objectives:**  
- Identify metabolites associated with nontuberculous mycobacteria  
- Compare metabolic profiles before and after drug treatment  
- Differentiate drug-sensitive and drug-resistant NTM strains  
- Identify metabolic markers associated with drug resistance  
- Evaluate synergistic effects of combined drug treatment  
""")

# =========================
# RESEARCH INTERESTS
# =========================
st.header("Research Interests")
st.markdown("""
- Nontuberculous Mycobacteria (NTM)  
- Tuberculosis and Drug Resistance  
- Metabolomics  
- Antimicrobial Drug Mechanisms  
- GC-MS Analysis  
""")

# =========================
# METHODOLOGY OVERVIEW
# =========================
st.header("Methodology Overview")
st.markdown("""
- Culturing *Mycobacterium avium* and *Mycobacterium intracellulare*  
- Treatment with bedaquiline and clofazimine  
- Metabolite extraction and quenching  
- Gas Chromatography–Mass Spectrometry (GC-MS) analysis  
- Statistical analysis using ANOVA  
""")

# =========================
# SUPERVISION
# =========================
st.header("Supervision")
st.markdown("""
- **Supervisor:** Dr N. A. Makhado (Medical Microbiology, SMU)  
- **Co-supervisor:** Mr M. Nemukula (Biochemistry, SMU)  
- **Co-supervisor:** Dr V. S. Thibane (Biochemistry, SMU)  
""")

# =========================
# CONTACT
# =========================
st.header("Contact Information")
st.markdown("""
📞 **Phone:** 079 275 7954  
📧 **Email:** nomsaphoswa22@gmail.com  
🏫 **Institution:** Sefako Makgatho Health Sciences University  
""")
