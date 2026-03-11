# cours_streamlit.py
import streamlit as st
import statistics as stats

# Titre général
st.title("📚 Mini-cours de mathématiques")

# Menu latéral pour choisir la notion
notion = st.sidebar.selectbox(
    "Choisis une notion",
    [
        "Équations de premier degré",
        "Équations de second degré",
        "Statistiques",
        "Équations différentielles de premier ordre",
        "Équations différentielles de second ordre"
    ]
)

# 1️⃣ Équations de premier degré
if notion == "Équations de premier degré":
    st.header("Équations de premier degré")
    st.markdown("""
**Définition :**  
Une équation de premier degré est une équation où l'inconnue n'est élevée qu'à la puissance 1.  
Exemple : 3x + 5 = 11

**Méthode de résolution :**  
1. Isoler x : 3x = 11 - 5  
2. Diviser par le coefficient devant x : x = 6 / 3 = 2  

**Exemple supplémentaire :**  
7x - 4 = 17 → 7x = 21 → x = 3
    """)

# 2️⃣ Équations de second degré
elif notion == "Équations de second degré":
    st.header("Équations de second degré")
    st.markdown("""
**Définition :**  
Une équation de second degré est de la forme : ax² + bx + c = 0 avec a ≠ 0

**Méthode :**  
1. Calculer le discriminant : Δ = b² - 4ac  
2. Solutions selon Δ :  
   - Δ > 0 : x1 = (-b - √Δ)/(2a), x2 = (-b + √Δ)/(2a)  
   - Δ = 0 : x = -b/(2a)  
   - Δ < 0 : pas de solution réelle  

**Exemple :**  
x² - 5x + 6 = 0 → Δ = 25 - 24 = 1  
x1 = 2, x2 = 3
    """)

# 3️⃣ Statistiques
elif notion == "Statistiques":
    st.header("Statistiques")
    st.markdown("""
**Moyenne :**  
Moyenne = (x1 + x2 + ... + xn) / n

**Médiane :**  
Valeur qui sépare la série en deux parties égales.

**Mode :**  
Valeur la plus fréquente dans la série.

**Étendue :**  
Étendue = valeur max - valeur min

**Variance (population) :**  
Variance = [(x1 - Moyenne)^2 + (x2 - Moyenne)^2 + ... + (xn - Moyenne)^2] / n

**Écart-type :**  
Écart-type = racine carrée de la variance
""")


    # Exemple interactif
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

# 4️⃣ Équations différentielles de premier ordre
elif notion == "Équations différentielles de premier ordre":
    st.header("Équations différentielles de premier ordre")
    st.markdown("""
**Définition :**  
Une équation différentielle de premier ordre contient la dérivée première : dy/dx = f(x,y)

**Exemple :**  
dy/dx = 3y  
Solution générale : y = C * e^(3x)
    """)

# 5️⃣ Équations différentielles de second ordre
elif notion == "Équations différentielles de second ordre":
    st.header("Équations différentielles de second ordre")
    st.markdown("""
**Définition :**  
Contient la dérivée seconde : y'' + a y' + b y = 0

**Méthode :**  
1. Écrire l'équation caractéristique : r² + a r + b = 0  
2. Solutions :  
   - Deux racines réelles distinctes r1,r2 : y = C1 e^(r1 x) + C2 e^(r2 x)  
   - Double racine r : y = (C1 + C2 x) e^(r x)  
   - Racines complexes α ± iβ : y = e^(α x) (C1 cos(β x) + C2 sin(β x))  

**Exemple :**  
y'' - 5y' + 6y = 0  
Équation caractéristique : r² - 5r + 6 = 0  
Solutions : r = 2, 3  
y = C1 e^(2x) + C2 e^(3x)
    """)
