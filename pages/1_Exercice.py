import streamlit as st 
import numpy as np
import random  


st.title("Exercice de Mathématiques")  
if "solution" not in st.session_state:
    st.session_state.solution=None
if "score" not in st.session_state:
    st.session_state.score=0
if "total" not in st.session_state:
    st.session_state.total=0

type_exercice=st.sidebar.selectbox(
    "Choisir un exercice",
    ["Équation du premier degré","Équation de second dégré","Statistiques"] )  
#--------EQUATIONS--------  
def equation_premier_degre():
    a=random.randint(1,10)
    b=random.randint(-10,10)
    c=random.randint(-10,20)
    solution=(c-b)/a
    if a==1:
        terme_a=f"x"
    else:
        terme_a=f"{a}x"
    if b>=0:
        terme_b=f"+ {b}"
    else:
        terme_b=f"-{abs(b)}"

    question=f"Résous l'équation de premier dégré suivant: {terme_a}{terme_b}={c}"
    return question,solution  

def equation_second_degre():
    a=random.randint(1,10)
    b=random.randint(-10,10)
    c=random.randint(-10,10)
    D=b**2-4*a*c
    if a==1:
        terme_a=f"x²"
    else:
        terme_a=f"{a}x²"
    if b>=0:
        terme_b=f"+ {b}x"
    else:
        terme_b=f"-{abs(b)}x"
    if c>=0:
        terme_c=f"+ {c}"
    else:
        terme_c=f"-{abs(c)}"
    question=f"Résous l'équation de second dégré suivant: {terme_a}{terme_b}{terme_c}=0"
    
    if D>0:
        x_1=((-b+np.sqrt(D))/(2*a))
        x_2=((-b-np.sqrt(D))/(2*a))
        solution=(x_1 ,x_2 )

    elif D==0:
        x=-b/(2*a)
        solution=(x, )

    else:
        solution=None
        
    return question,solution
    


 #--------STATISTIQUES-------- 
def probleme_statistique():
    donnees=[random.randint(1,20)for _ in range(6)]
    type_question=random.choice(["moyenne","mediane","etendue","mode","variance","écart-type"])
    
    if type_question=="moyenne":
        solution=sum(donnees)/len(donnees)
        question=f"Série:{donnees}\n\nCalculez la moyenne de cette série"
    
    elif type_question=="mediane":
        d=sorted(donnees)
        m=len(d)
        if m%2==1:
          solution=d[m//2]
        else:
            solution=(d[m//2-1]+d[m//2])/2
        question=f"Série:{donnees}\n\nCalculez la médiane de cette série"
    elif type_question=="etendue":
        solution=max(donnees)-min(donnees)
        question=f"Série:{donnees}\n\nCalculez l'étendue de cette série"
    elif type_question=="variance":
        mean=np.mean(donnees)
        solution=sum((x-mean)**2 for x in donnees)/len(donnees)
        question=f"Série:{donnees}\n\nCalculez la variance de cette série"
    elif type_question=="écart-type":
        solution=np.std(donnees)
        question=f"Série:{donnees}\n\nCalculez l'écart-type de cette série"
    else:
        solution=max(set(donnees),key=donnees.count)
        question=f"Série:{donnees}\n\nCalculez la mode de cette série"
    return question,solution  
 #--------GENERER QUESTION--------  
if st.button("Nouvelle question"):
    if type_exercice=="Équation du premier degré":
        question,solution=equation_premier_degre()
    elif type_exercice=="Équation de second dégré":
        question,solution=equation_second_degre()
    else:question,solution=probleme_statistique()
    st.session_state.solution=solution
    st.session_state.question=question  
#Afficherlaquestion 
if"question"in st.session_state:
    st.write(st.session_state.question)  
#Réponse utilisateur 
reponse=None
x1=None
x2=None
if type_exercice=="Équation de premier dégré": 
    reponse=st.number_input("Votre réponse",step=0.1) 
elif type_exercice=="Équation de second dégré":
    sol=st.session_state.solution
    if sol is None:
        st.write("Cette équation n'a pas de solution réelle")
    elif len(sol)==1:
        x=st.number_input("x",step=0.1)
    else:
        x1=st.number_input("x1",step=0.1)
        x2=st.number_input("x2",step=0.1)
else:
    reponse=st.number_input("Votre réponse",step=0.1)
#Vérification 
if st.button("Valider"):
    st.session_state.total+=1
    if type_exercice=="Équation de premier dégré":
        if abs(reponse-st.session_state.solution)<0.01:
            st.success("Bonne réponse!")
            st.session_state.score +=1
        else:
            st.error(f"La solution était{st.session_state.solution}")

    
    elif type_exercice=="Équation de second dégré":
        sol=st.session_state.solution
        if sol is None:
            st.warning("Pas de solution réelle")
        elif len(sol)==1:
            if abs(x-sol[0])<0.01:
                st.success("Bonne réponse!")
                st.session_state.score +=1
            else:
                st.error(f"La solution était: {sol[0]}")
        else:
            if (abs(x1-sol[0])<0.01 and abs(x2-sol[1])<0.01)or (abs(x1-sol[1])<0.01 and abs(x2-sol[0])<0.01):
                st.success("Bonne réponse!")
                st.session_state.score+=1
            else:
                st.error(f"Les solutions étaient: {sol[0]} et {sol[1]}")
    else :
        if abs(reponse-st.session_state.solution)<0.01:
            st.success("Bonne réponse!")
            st.session_state.score+=1
        else:
            st.error(f"La solution était: {st.session_state.solution}")

    st.session_state.valide=True
