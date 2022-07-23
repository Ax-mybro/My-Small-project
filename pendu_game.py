import time
import random
banque_de_mots=["accordéon","âne","acheter","animal","admirer","appeler""âge","approcher",
"aile","arbre","aller","arracher","arrêter","allumer","assiette","allumette","auto","amener","avec",
"ami","amie","avion","amusant","amusante","avoir","amuser"]
def reglement():
    print("___________________________________________________________________________")
   
    print("******** Bienvenue dans le jeu du Pendu *********")
    print("les règle sont simples:")
    print("1.Vous devez utilisé que des lettres en Majuscules")
    print("2 Pas le droit au espace vous devez utitlisé des tirets pour espacé votre mots ")
    print("3.La triche est formellement interdit")
    print("!!!!!!Amusez vous bien!!!!!!!!!!")
    print("___________________________________________________________________________")
def ecran_de_fin_win():
    print("___________________________________________________________________________")
    print("")
    print("*********Bravo vous avez Gagné***********")
    print("___________________________________________________________________________")
    
def mode_un_joueur():
    hasard=random.choice(banque_de_mots)
    guess_wrd=hasard
    nombre_de_tentative=int(input("combien voulez-vous qu'il y'ai de tentative "))
    jeux(guess_wrd,nombre_de_tentative)
def mode_deux_joeur():
    nombre_de_tentative=int(input("combien voulez-vous qu'il y'ai de tentative "))
    guess_wrd=input("Quel mots sera a deviné ")
    jeux(guess_wrd,nombre_de_tentative)
def jeux(guess_wrd,nombre_de_tentative):
    Affichage=["_"]
    Tableau=Affichage*len(guess_wrd)
    for x in range(nombre_de_tentative) :
        time.sleep(2)
        print("vous avez ",nombre_de_tentative," tentative(s) ")
        print(*Tableau,sep="")
        choix=0
        condition=[1,2]
        while choix not in condition :
            choix=int(input("1. mot entier \n2. lettre \n"))
        
        if choix==1:
            print("ok")
            essaie=input("Vous pensez a quelle lettre ou quelle (mot/lettre) ? ")
            if guess_wrd==essaie or essaie==guess_wrd or str(Tableau):
                print("vous avez gagné")
                ecran_de_fin_win()
            else:
                print("c'est faux essaye encore")
        elif choix==2:
            essaie=input("Vous pensez a quelle lettre ou quelle (mot/lettre) ? ")
            if essaie in guess_wrd:
                print("bien joué")
                response=[]
                for x in range(len(guess_wrd)):
                    if guess_wrd[x] == essaie:
                        response.append(x)
                for x in range(len(response)):
                    Tableau[response[x]]=essaie              
            if Tableau==list(guess_wrd):
                ecran_de_fin_win()
                
        nombre_de_tentative=nombre_de_tentative-1
        
    print("perdu vous n'avez plus d'essaie disponible")
        
reglement()
while True:
    a=int(input("1) pour le mode solo \n2) pour le mode deux joeur\n"))
    if a==1:
        mode_un_joueur()
    elif a==2:
        mode_deux_joeur()