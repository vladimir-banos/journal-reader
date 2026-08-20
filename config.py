# ============================================================
# config.py — Configuración central del pipeline
# ============================================================
# Aquí defines los parámetros del proyecto.
# Si quieres cambiar de journal, solo cambias el ISSN.

# --- Journal activo ---
JOURNAL_NAME = "Journal of Development Economics"
JOURNAL_ABBR = "JDE"
JOURNAL_ISSN = "0304-3878"

# --- Cuántos papers procesar por issue ---
TOP_N = 5  # los 5 más citados por issue

# --- Email para OpenAlex (aumenta el rate limit) ---
OPENALEX_EMAIL = "hristo.banos@alum.udep.edu.pe"  # cambia esto por tu email UDEP

# --- Modelo LLM para resúmenes (paso 5) ---
LLM_MODEL = "claude-sonnet-4-6"

# --- Rutas de output ---
ISSUES_PATH = f"journals/{JOURNAL_ABBR}/issues"
DATA_PATH   = f"journals/{JOURNAL_ABBR}/data"