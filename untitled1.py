# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:24:12 2021

@author: Mohamed
"""
import re

def full_name(str_arg:str)->str:
    """
    

    Parameters
    ----------
    str_arg : str
        chaine de caractère de type ‘nom prenom’.

    Returns
    -------
    str
    la même chaîne avec le nom en majuscule et le prénom 
    avec la première lettre seulement en majuscule..
    
    """
    prenom="" #prenom
    nom="" #nom
    chaine=str_arg.split(" ")
    chaine[0]=chaine[0].upper()
    chaine[1]=chaine[1].capitalize()
    return " ".join(chaine) 

def is_mail(str_arg : str) -> tuple:
    """Fonction qui prend en paramètre une chaine de caractère
    de type adresse mail et qui renvoie un tuple."""

    tuple_check = (0, 0) #Correspond au code (validité, erreur)
    
    regex_mail = re.search("[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}",str_arg)

    mail_check_lst = str_arg.split("@")
    
    if regex_mail:
        tuple_check = (1, "x")
    elif(mail_check_lst[0] == ""):
        tuple_check = (0,1)
    elif(not "@" in str_arg):
        tuple_check = (0,2)
    elif(mail_check_lst[1].split == ""):
        tuple_check = (0,3)
    elif(not "." in mail_check_lst[1]):
        tuple_check = (0,4)
    return tuple_check

def mots_Nlettres(lst_mot:list, n:int)->list:
    lst_mot_n=[]
    for i in range(len(lst_mot)):
        if n==len(lst_mot[i]):
            lst_mot_n.append(lst_mot[i])
    return lst_mot_n

def commence_par(mot:str,prefixe:str)->bool:
    result=True
    for i in range(len(prefixe)):
        if prefixe[i]!=mot[i]:
            result=False
    return result

def finit_par(mot:str,suffixe:str)->bool:
    result=True
    len_fin=len(mot)-len(suffixe)#ça me permet de savoir ou je peux commencer la comparaison
    for i in range(len(suffixe)):
        print(mot[len_fin])
        if suffixe[i]!=mot[len_fin]:
            result=False
        len_fin+=1
    return result

def  finissent_par(lst_mot:list, suffixe:str)->list:
    lst_mot_suffixe=[]
    for i in range(len(lst_mot)):
        if finit_par(lst_mot[i],suffixe)==True:
            lst_mot_suffixe.append(lst_mot[i])
    return lst_mot_suffixe
        
def commencent_par(lst_mot:list, prefixe:str)->list:
    lst_mot_prefixe=[]
    for i in range(len(lst_mot)):
        if commence_par(lst_mot[i], prefixe)==True:
            lst_mot_prefixe.append(lst_mot[i])
    return lst_mot_prefixe
    
def liste_mots(lst_mot:list, prefixe:str, suffixe:str, n:int)->list:
    return (finissent_par(mots_Nlettres(lst_mot, n), suffixe) + commencent_par(mots_Nlettres(lst_mot, n), prefixe))


def dictionnaire(fichier)->list:
    lst_mot_pre_fich=[]
    # ouverture du fichier en lecture (r=read)
    f=open(fichier,"r")
    c=f.readline() #lecture d'une ligne dans une chaine de caractères
    print("** Contenu du fichier **")
    while c!="" :
        lst_mot_pre_fich.append(c)
        c=f.readline()
    return lst_mot_pre_fich

    
    
    
    
    
str_variable2test = "bisgambiglia paul"
print(full_name(str_variable2test))
str_variable2test = "bisgambiglia_paul@univ-corse.fr"
print(is_mail(str_variable2test))
lst_mot=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
"finir", "aimer"]
n=5
print(mots_Nlettres(lst_mot,n))

mot="abiter"
print(commence_par(mot, "abi"))
mot="activiste"
print(finit_par(mot, "iste"))
print(finit_par("test", "test"))
lst_mot=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
"finir", "aimer"]
#print(finissent_par(lst_mot,"ir"))
#print(commencent_par(lst_mot, "au"))
print(liste_mots(lst_mot, "ai", "ir", 5))
dictionnaire("littre.txt")