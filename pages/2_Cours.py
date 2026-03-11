import streamlit as st
import statistics as stats

st.title("📚 Mini-cours de statistiques")

st.header("Statistiques : définitions et formules")

st.markdown(r"""
**Moyenne :**  
\[
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
\]

**Médiane :**  
Valeur qui sépare la série en deux parties égales.

**Mode :**  
Valeur la plus fréquente dans la série.

**Étendue :**  
\[
E = x_{\max} - x_{\min}
\]

**Variance (population) :**  
\[
\text{Var}(X) = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2
\]

**Écart-type :**  
\[
\sigma = \sqrt{\text{Var}(X)}
\]
""")

st.subheader("Exemple interactif")

data_input = st.text_input(
    "Entrez une série de nombres séparés par des virgules",
    "2,4,6,6,8"
)

if data_input:
    try:
        data = [float(x.strip()) for x in data_input.split(",")]
        moyenne = stats.mean(data)
        mediane = stats.median(data)
        mode = stats.mode(data)
        etendue = max(data) - min(data)
        variance = stats.pvariance(data)  # variance populationnelle
        ecart_type = stats.pstdev(data)  # écart-type populationnel

        st.write("**Données :**", data)
        st.write("**Moyenne :**", moyenne)
        st.write("**Médiane :**", mediane)
        st.write("**Mode :**", mode)
        st.write("**Étendue :**", etendue)
        st.write("**Variance :**", variance)
        st.write("**Écart-type :**", ecart_type)
    except:
        st.error("Erreur dans la saisie des données. Utilisez des nombres séparés par des virgules.")
