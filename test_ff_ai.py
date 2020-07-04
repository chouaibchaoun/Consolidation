#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


# # Codages des fonctions utiles

def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][col])





def match_2lists(L,I,ratio = True , Nospliter = True , st_spliter = ' ', nd_spliter = ' '):
    """ Cette fonction est basée sur la méthode de Levenshtein, et prend en paramètre deux liste de stings
    et essaie de trouver le bon matching entre ses élements. elle retourne ce match sous forme d'un dict
    ses options sont :
    ratio : cette option est activée par défault et elle permet de décider si le dict contiendera le ratio
    ou non.
    Nospliter: cette option permet de controler si on veut comparer les élements de la liste en les séparant
    ou bien en les gardans tels qu'ils sont.
    """
    #creating an empty disctionnary
    R = {}
    #mapping all the elements of both lists
    for elt1 in L :
        for elt2 in I :
            #making sure that the elements are comparable : both have a str value
            if not elt1==str(elt1) or not elt2==str(elt2) : continue
            #calculating levenshtein ration
            l= levenshtein_ratio_and_distance(elt1.lower(),elt2.lower(),ratio_calc=True)
            #setting a level of acceptance and saving the wanted data in the dictionnary
            #giving the option of saving the ratio or not, to assure more simpicity to the data in the dictionnary
            if l>0.8 :
                if elt1 in R.keys() :
                        if ratio : R[elt1] += (elt2,l)
                        else : R[elt1] += elt2
                        continue
                if ratio : R[elt1] = (elt2,l)
                else : R[elt1] = elt2
                continue
            #enhacing our research to elements of the elemnts (optional)
            if Nospliter : continue
            i=0
            for el1 in elt1.split(st_spliter):
                for el2 in elt2.split(nd_spliter):
                    l=levenshtein_ratio_and_distance(el1.lower(),el2.lower(),ratio_calc = True)
                    i = max(l,i)
            #setting a level of acceptance and saving the wanted data in the dictionnary
            #giving the option of saving the ratio or not, to assure more simpicity to the data in the dictionnary
            if i>0.8 :
                if elt1 in R.keys() :
                        if ratio : R[elt1] += (elt2,l)
                        else : R[elt1] += elt2
                        continue
                if ratio : R[elt1] = (elt2,l)
                else : R[elt1] = elt2
    #the funtion retun a dictionnary associating elements of the two lists
    return R


   



    ########################################## Consolider des bases de données

def calcul_source4 (ss,s4) :
    #Utilisation de l'index convenable
    ss.set_index('siret',inplace = True)
    s4.set_index('siret', inplace = True)
    #Update des données
    ss.update(s4)
    #préparation à sauvegarder la BD
    ss.reset_index(level=0, inplace=True)
    return ss


def calcul(s1,s2,s3):    
    
    
    # # Relation entre les columns, si elle existe
    
    # Dictionnaire mettant en relation les columns de s1 à ceux de s2
    D1 = { 'Numéro denregistrement (Siret, Siren)':"siret", 'Nom de lentreprise' : 'nom_etablissement'  ,
        'Rue' : 'adresse' ,
        'Code postal' : 'code_postal'  ,
        'Pays' : 'pays',
        'Email' : 'email' ,
        'Chiffre daffaires brut' : 'ca'  ,
        'Numéro de téléphone' : 'telephone',
        'Site web' : 'web'  }
    # Dictionnaire mettant en relation les columns de s3 à ceux de s2
    D3 = {'nom' :'nom_etablissement',
        "Nombre d'employes" : 'employes' }
    
    #list des columns de s1 non-existants en s2
    R1 = list(s1.columns)
    for i in range(len(list(s1.columns))-1,-1,-1) :
        if R1[i] in D1.values() : R1.remove(R1[i])
    #list des columns de s3 non-existants en s2
    R3 = list(s3.columns)
    for i in range(len(list(s3.columns))-1,-1,-1) :
        if R3[i] in D3.values() : R3.remove(R3[i])
    
    
    # Dictionnaire mettant en relation les columns de s1 à ceux de s3
    D1_3 = match_2lists(R1,R3,ratio=False)
    
    # # Rename the columns the commun names
    
    s1.rename(D1,axis = 1 ,inplace = True)
    s3.rename(D3,axis = 1 ,inplace = True)
    s1.rename({"Numéro denregistrement (Siret, Siren)":'siret'},axis = 1 ,inplace = True)
    
    
    # # Updating s2 and s1, Merging s2 with the rest of s1 and saving the Data in ss
    
    s1.set_index('siret',inplace = True)
    s2.set_index('siret', inplace = True)
    s2.update(s1)
    ss = s2.merge(s1.loc[:,R1], how = 'outer' , left_index = True , right_index = True)
    
    
    # # Updating ss and s3, Merging ss with the rest of s3 and saving the Data in sf
    
    ss.reset_index(level=0, inplace=True)
    
    # using the right index
    
    ss.set_index('nom_etablissement',inplace = True)
    s3.set_index('nom_etablissement', inplace = True)
    
    #making sure the columns have the same names
    
    ss.rename(D1_3,axis = 1 , inplace = True)
    ss.update(s3)
    ss.reset_index(level=0, inplace=True)
    
    return ss


########################    Interface
print("""Ce code permet de consolider 3 bases de données sous forme d'un fichier csv. \n le fichier final sera de même sous forme d'un fichier csv, sa forme sera compatible avec la source 2. \n Si la même information se repète entre les 3 sources, celle dans la source 3 est priorisée sur eux, et celle de la source 1 est priorisée sur celle de la source 2 \n Ce code est version Beta""")

input('Cliquer sur Entrer pour choisir la source 1')
filepath1 = askopenfilename(title = 'choisissez la premiere source' , filetypes = [("Fichiers Excel csv ","*.csv")])


input('Cliquer sur Entrer pour choisir la source 2')
filepath2 = askopenfilename(title = 'choisissez la deuxième source' , filetypes = [("Fichiers Excel csv ","*.csv")])


input('Cliquer sur Entrer pour choisir la source 3')
filepath3 = askopenfilename(title = 'choisissez la troisième source' , filetypes = [("Fichiers Excel csv ","*.csv")])

# # Importation des données
    
s1 = pd.read_csv(filepath1 , encoding = "ISO-8859-1" , delimiter = ';')
s2 = pd.read_csv(filepath2 , encoding = "ISO-8859-1" , delimiter = ';')
s3 = pd.read_csv(filepath3 , encoding = "ISO-8859-1" , delimiter = ';')

ss = calcul(s1,s2,s3)


#Ajout d'une 4ème source sur le choix
print(""" Vous pouver ajouter une 4ème source à votre choix, 
sous prétexte qu'elle aura la même format que la source 4.
Notez bien que ses cette Base sera priorisée sur les autres Bases
""")
b =True
while b == True :
    R = str(input('voulez vous ajouter une 4ème source :(oui ou non)'))
    if R.lower() == "oui" :
        input('Cliquer sur Entrer pour choisir la source 4')
        filepath4 = askopenfilename(title = 'choisissez la quatrième source' , filetypes = [("Fichiers Excel csv ","*.csv")])
        s4 = pd.read_csv(filepath4 , encoding = "ISO-8859-1" , delimiter = ';')
        ss = calcul_source4(ss,s4)
        b = False
        
    elif R.lower() == "non" : b = False
    
    else : print("Entrée non valide !")


#Enregistrement du résultat des calculs en un fichier en externe
input('Cliquer sur Entrer pour enregistrer votre fichier final')
filepath_ss = asksaveasfilename(title = 'Enregistrer votre fichier final' , filetypes = [("Fichiers Excel csv ","*.csv")])

ss.to_csv(filepath_ss+".csv" , encoding = 'ISO-8859-1' , sep = ';',na_rep = 'nan',columns = list(ss.columns))
print("votre fichier a été bien enregistré")

input('Exit ? ')
