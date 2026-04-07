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

#--------FONCTIONS DE GÉNÉRATION (LOGIQUE ORIGINALE + QUESTIONS)--------  

def equation_premier_degre():
    a=random.randint(1,10)
    b=random.randint(-10,10)
    c=random.randint(-10,20)
    solution=(c-b)/a
    
    signe_b = "+" if b >= 0 else "-"
    val_b = abs(b)
    terme_a = "x" if a == 1 else f"{a}x"
    
    # On remet la question claire
    st.write(f"Résous l'équation de premier degré suivante :")
    st.latex(rf"{terme_a} {signe_b} {val_b} = {c}")
        
    return solution  

def equation_second_degre():
    a=random.randint(1,10)
    b=random.randint(-10,10)
    c=random.randint(-10,10)
    delta=b**2-4*a*c
    
    st.write("Trouve les racines réelles de l'équation suivante :")
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
        return [] 

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
    st.write("Donne la solution générale de l'équation différentielle :")
    st.latex(rf"y' = {a}y")
    return f"C * e^({a}x)"

def equa_diff_2():
    a = random.randint(1, 20)
    st.write("Trouve la valeur de la racine positive $r$ de l'équation caractéristique associée à :")
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
    # Affichage des champs de saisie
    if type_exercice == "Statistiques":
        st.write(st.session_state.question)
        reponse = st.number_input("Votre réponse", format="%.2f")
    elif type_exercice == "Équation de second dégré":
        sol = st.session_state.solution
        if len(sol) == 0:
            st.write("Cette équation n'a pas de solution réelle.")
            reponse_vide = st.checkbox("Cocher ici s'il n'y a pas de solution")
        elif len(sol) == 1:
            x1 = st.number_input("Solution unique (x0)", format="%.2f")
        else:
            col1, col2 = st.columns(2)
            with col1:
                x1 = st.number_input("x1", format="%.2f")
            with col2:
                x2 = st.number_input("x2", format="%.2f")
    elif type_exercice == "Équation différentielle 1er ordre":
        reponse = st.text_input("Solution générale (ex: C * e^(2x))")
    elif type_exercice == "Équation différentielle 2nd ordre":
        reponse = st.number_input("Valeur de r", format="%.2f")
    else:
        reponse = st.number_input("Votre réponse", format="%.2f")

    if st.button("Valider"):
        sol = st.session_state.solution
        temps = round(time.time() - st.session_state.start_time, 2)
        
        # Logique de validation (Inchangée)
        if type_exercice in ["Équation du premier degré", "Statistiques", "Équation différentielle 2nd ordre"]:
            if type_exercice == "Équation différentielle 2nd ordre":
                check = abs(reponse - sol) < 0.01
            else:
                check = abs(reponse - sol) < 0.01
            
            if check:
                st.success("Bonne réponse !")
                st.session_state.score += 1
                if type_exercice == "Équation différentielle 2nd ordre":
                     st.write(f"La solution est bien $r = \pm {round(sol, 2)}$.")
            else:
                st.error(f"La solution était : {round(sol, 2) if not isinstance(sol, list) else sol}")
        
        elif type_exercice == "Équation de second dégré":
            if len(sol) == 0:
                if reponse_vide:
                    st.success("Bonne réponse !")
                    st.session_state.score += 1
                else:
                    st.error("Il n'y avait pas de solution réelle.")
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

        st.write(f"Temps de réponse : `{temps}` secondes")
