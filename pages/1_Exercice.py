import streamlit as st 
import numpy as np
import random  
import time
import pandas as pd

st.title("Exercice de Mathématiques")  

if "solution" not in st.session_state:
    st.session_state.solution=None
if "score" not in st.session_state:
    st.session_state.score=0
if "total" not in st.session_state:
    st.session_state.total=0

type_exercice=st.sidebar.selectbox(
    "Choisir un exercice",
    ["Équation du premier degré","Équation de second dégré","Statistiques","Équation différentielle 1er ordre",
"Équation différentielle 2nd ordre"]  )  

#--------FONCTIONS DE GÉNÉRATION (LOGIQUE ORIGINALE RESTAURÉE)--------  

def equation_premier_degre():
    a=random.randint(1,10)
    b=random.randint(-10,10)
    c=random.randint(-10,20)
    solution=(c-b)/a
    
    # Rendu LaTeX pour l'affichage
    signe_b = "+" if b >= 0 else "-"
    val_b = abs(b)
    if a == 1:
        st.latex(rf"x {signe_b} {val_b} = {c}")
    else:
        st.latex(rf"{a}x {signe_b} {val_b} = {c}")
        
    return solution  

def equation_second_degre():
    # Retour à ta logique sans boucle while : toutes les valeurs de delta sont possibles
    a=random.randint(1,10)
    b=random.randint(-10,10)
    c=random.randint(-10,10)
    delta=b**2-4*a*c
    
    # Rendu LaTeX
    sb = "+" if b >= 0 else ""
    sc = "+" if c >= 0 else ""
    st.latex(rf"{a}x^2 {sb} {b}x {sc} {c} = 0")
    
    if delta > 0:
        sol1=(-b+np.sqrt(delta))/(2*a)
        sol2=(-b-np.sqrt(delta))/(2*a)
        return [sol1, sol2]
    elif delta == 0:
        sol = -b/(2*a)
        return [sol]
    else:
        return [] # Pas de solution réelle

def probleme_statistique():
    donnees = [random.randint(1, 20) for _ in range(6)]
    st.write("**Série de données :**")
    st.info(", ".join(map(str, donnees))) 
    st.bar_chart(donnees)
    
    type_stat = random.choice(["moyenne", "médiane", "étendue"])
    if type_stat == "moyenne":
        sol = np.mean(donnees)
        quest = "Calculez la moyenne de cette série"
    elif type_stat == "médiane":
        sol = np.median(donnees)
        quest = "Calculez la médiane de cette série"
    else:
        sol = np.max(donnees) - np.min(donnees)
        quest = "Calculez l'étendue de cette série"
    return quest, sol

def equa_diff_1():
    a = random.randint(1, 10)
    st.latex(rf"y' = {a}y")
    return f"C * e^({a}x)"

def equa_diff_2():
    a = random.randint(1, 20)
    st.latex(rf"y'' - {a}y = 0")
    return np.sqrt(a)

#--------INTERFACE ET VALIDATION--------

if st.button("Nouvelle question"):
    st.session_state.total += 1
    st.session_state.start_time = time.time()
    if type_exercice == "Équation du premier degré":
        st.session_state.solution = equation_premier_degre()
    elif type_exercice == "Équation de second dégré":
        st.session_state.solution = equation_second_degre()
    elif type_exercice == "Statistiques":
        st.session_state.question, st.session_state.solution = probleme_statistique()
    elif type_exercice == "Équation différentielle 1er ordre":
        st.session_state.solution = equa_diff_1()
    elif type_exercice == "Équation différentielle 2nd ordre":
        st.session_state.solution = equa_diff_2()

if st.session_state.solution is not None:
    if type_exercice == "Statistiques":
        st.write(st.session_state.question)
        reponse = st.number_input("Votre réponse", format="%.2f")
    elif type_exercice == "Équation de second dégré":
        sol = st.session_state.solution
        if len(sol) == 0:
            st.write("Cette équation n'a pas de solution réelle. Cochez la case si vous êtes d'accord.")
            reponse_vide = st.checkbox("Pas de solution")
        elif len(sol) == 1:
            x1 = st.number_input("Solution unique (x0)", format="%.2f")
        else:
            col1, col2 = st.columns(2)
            with col1:
                x1 = st.number_input("x1", format="%.2f")
            with col2:
                x2 = st.number_input("x2", format="%.2f")
    elif type_exercice == "Équation différentielle 1er ordre":
        reponse = st.text_input("Donner la solution générale (ex: C * e^(2x))")
    elif type_exercice == "Équation différentielle 2nd ordre":
        st.write("Donner la valeur de r.")
        reponse = st.number_input("Votre réponse", format="%.2f")
    else:
        reponse = st.number_input("Votre réponse", format="%.2f")

    if st.button("Valider"):
        sol = st.session_state.solution
        temps = round(time.time() - st.session_state.start_time, 2)
        
        if type_exercice == "Équation du premier degré" or type_exercice == "Statistiques":
            if abs(reponse - sol) < 0.01:
                st.success("Bonne réponse !")
                st.session_state.score += 1
            else:
                st.error(f"La solution était : {round(sol, 2)}")
        
        elif type_exercice == "Équation de second dégré":
            if len(sol) == 0:
                if reponse_vide:
                    st.success("Bonne réponse ! (Pas de solution réelle)")
                    st.session_state.score += 1
                else:
                    st.error("Mauvaise réponse, il n'y avait pas de solution.")
            elif len(sol) == 1:
                if abs(x1 - sol[0]) < 0.01:
                    st.success("Bonne réponse !")
                    st.session_state.score += 1
                else:
                    st.error(f"La solution était : {round(sol[0], 2)}")
            else:
                if (abs(x1-sol[0])<0.01 and abs(x2-sol[1])<0.01) or (abs(x1-sol[1])<0.01 and abs(x2-sol[0])<0.01):
                    st.success("Bonne réponse !")
                    st.session_state.score += 1
                else:
                    st.error(f"Les solutions étaient : {round(sol[0], 2)} et {round(sol[1], 2)}")
        
        elif type_exercice == "Équation différentielle 1er ordre":
            if sol in reponse:
                st.success("Bonne réponse !")
                st.session_state.score += 1
            else:
                st.error(f"La solution est : {sol}")
        
        elif type_exercice == "Équation différentielle 2nd ordre":
            if abs(reponse - sol) < 0.01:
                st.success("Bonne réponse !")
                st.session_state.score += 1
                st.write("### Solution mathématique :")
                st.latex(rf"r = \pm {round(sol, 2)}")
                st.write(f"Donc la solution générale est : $y = C_1 e^{{{round(sol, 2)}x}} + C_2 e^{{{round(-sol, 2)}x}}$")
            else:
                st.error("Mauvaise réponse")

        st.write(f"Temps de réponse : `{temps}` secondes")
