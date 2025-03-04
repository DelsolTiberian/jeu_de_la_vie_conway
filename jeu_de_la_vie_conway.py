from os import system, name
from time import sleep
#Jeu de la vie

#Ce jeu a pour vocation d'etre execute dans un terminal, il peut etre executer sur console mais il marchera moins bien, la console ne sera pas clear

def clear():
    """
       Clear la console

    """
    #Pour windows
    if name=='nt':
        system('cls')
    #Pour Mac et Linux
    else:
        system('clear')

def regle():
    """
       Affiche les regles du jeu
    """
    print("\n Le jeu de la vie est un jeu de plateau, visant à reproduire une sorte d'écosysteme binaire. \n En effet, chaque case du plateau est en realité une cellules qui ne peut admettre que 2 états, vivante ou morte.\n")
    print(" L'état d'une cellule est définie par son environnement : \n -Si une cellule est adjacente à exactement 3 cellules vivantes, elle devient vivante\n - Si une cellule est adjacente à 2 cellules, elle reste dans son état actuel\n -Dans tout autre cas, la cellule meurs \n")
    print(" Au début du jeu, vous choisissez les dimensions du plateau et le placement de vos cellules \n Vous les voyez ensuite évoluée selon leur environnement.")
    retourMenu=input(" \n \n Afin de retourner au menu, appuyez sur une touche: \n>>> ")
    clear()

def menu():
    """
        Fonction menu qui affiche un menu simple et demande si l'utilisateur veut jouer
    Sortie:
        rep: (int): 0, 1 ou 2

    """
    #style
    print(35*'=')
    print('|'+10*' '+'JEU DE LA VIE'+10*' '+'|')
    print(35*'=')
    print('|     Que voulez vous faire ?     |\n|- Tappez 1 pour lancer la partie |\n|- Tappez 2 pour voir les règles  |\n|- Tappez autre chose pour quitter|\n'+35*'=')
    rep=input('>>> ')
    if rep=="1":
        rep=1
    elif rep=="2":
        rep=2
    else:
        rep=False
    return rep

def demandeTableau():
    """
       Demande a l'utilisateur les modalites de creation du plateau de jeu et le cree
    Sortie: 
       tableau: list[list[]]: matrice representant le plateau de jeu

    """
    #permet de ne pas depasser une certaine taille de tableau
    valid=False
    while valid==False:
        print("!! Attention, les dimensions du plateau doivent être comprise entre 1 et 99 !!\n")
        xMax= int(input("De quelle largeur voulez vous le tableau? (En nombre de cellules) \n>>> "))
        yMax= int(input("\nDe quelle hauteur voulez vous le tableau? (En nombre de cellules) \n>>> "))
        if 1<=yMax<=99 and 1<=xMax<=99 :
            valid=True
        else:
            clear()
            print("\nVos dimensions ne sont pas conformes, veuillez réessayer !!")
    #Creer le tableau, une liste represente une ligne
    tableau=[[0 for i in range(xMax)] for i in range(yMax)]
    run=True
    while run==True:
        clear()
        affichage(tableau)
        #demande a l'utilisateur ou placer les pions
        xPion=int(input("\nEntrez la colonne de votre cellule: \n>>> "))-1
        yPion=int(input("\nEntrez la ligne de votre cellule: \n>>> "))-1
        tableau[yPion][xPion]=1
        clear()
        affichage(tableau)
        #Demande a l'utilisateur si il veut continuer a poser des pions
        rep=False
        while rep==False:
            continu= input("\nVoulez vous continuer à poser des cellules? oui: O, Non: N \n>>> ")
            continu=  continu.replace(" ","").lower()
            #gestion reponse
            if continu=="n":
               run=False
               rep=True
            elif continu=="o":
                run=True
                rep=True
            #gestion d'erreur
            else:
                print("\nVotre réponse n'est pas conforme à celle attendue et n'a pas été prise en compte, veuillez réessayer!  ")
    return(tableau)

#fonction d'affichage du tableau
def affichage(tableau):
    """
        Fonction qui prends une matrice et l'affiche comme un tableau
    Args:
        tableau : list[list]: matrice compose de 0 et/ou un autre caractere

    """
    #permet de rajouter une ligne de style si le nombre de colonne du tableau depasse 10
    if (len(tableau[0]))>=10:
        #style
        print('\n   |',end='')
        for colonne in range(len(tableau[0])):
            if colonne<9:
                #s'il n'y a pas de chiffre des dizaine on affiche un espace
                print(' '+'|',end='')
            else:
                #prends uniquement le chiffre des dizaines et l'affiche
                print(str(colonne+1)[0]+'|',end='')
    print('\n __|',end='')
    for colonne in range(len(tableau[0])):
        if colonne<9:
            #affiche le nombre de la colonne +1 (pour faciliter la comprehension de l'utilisateur)
            print(str(colonne+1)+'|',end='')
        else:
            #prends uniquement le chiffre des unites et l'affiche
            print(str(colonne+1)[1]+'|',end='')
    for lignes in range(len(tableau)):
        #mise en forme du tableau si le numero de la ligne est > 10 on ne met pas d'espace entre le numéro et la barre sinon on en met un
        print('\n',str(lignes+1)+(len(str(lignes+1))%2)*' ', end='|')
        for element in tableau[lignes]:
            #en fonction de la valeur de l'element que l'on regarde un certain symbole sera affiche
            if element==0:
                #si l'element est un 0 alors on affichera un espace (cellule morte)
                print(' ', end='|')
            else:
                #sinon on affichera un diese (cellule vivante)
                print('#', end='|')


def checkCellule(xPion, yPion,tableau):
    """
       Check combien de cellules sont vivant autour d'une cellule aux coordonnees x et y
    Args:
        xPion :(int): coordonnee en x de la cellule
        yPion :(int): coordonnee en y de la cellule
    Sortie: 
        nbVivantes : (int): nombres de cellules vivantes autour de la cellule

    """
    nbVivantes=0
    #y est l'axe des ordonnees du tableau
    for y in range(-1, 2):
        #Regarde si la position est possible dans le tableau pour eviter un out of range()
        if not(y+yPion<0) and not(y+yPion>=len(tableau)):
            #y est l'axe des abscisses du tableau
            for x in range(-1, 2):
                #Regarde si la position est possible dans le tableau pour eviter un out of range()
                if not(x+xPion<0) and not(x+xPion>=len(tableau[y])) and not(x==0 and y==0):
                    #Un 1 dans le tableau represente une cellule vivante
                    if tableau[y+yPion ][x+xPion]==1:
                        nbVivantes+=1
    return(nbVivantes)

def update(tableau):
    """
        Fonction qui met à jour regarde le tableau donne et lui applique sa mise a jour
    Args: 
        tableau : list[list]: matrice compose de 0 et/ou un autre caractere
    Sortie:
        tableau : list[list]: matrice compose de 0 et/ou un autre caractere
       
    """
    #appel fonction creation de tableau pour creer le meme tableau mais vide
    Test=[]
    for y in range(len(tableau)):
        tmp=[]
        for x in range(len(tableau[y])):
            Vietmp=checkCellule(x,y,tableau)
            #regarde en fonction du nombre de cellule proche si la cellule doit rester en vie, mourir ou naitre
            if Vietmp==3:
                tmp.append(1)
            elif Vietmp==2 and tableau[y][x]==1:
                tmp.append(1)
            else:
                tmp.append(0)
        #creation petit a petit de la mise a jour de la grille lignes par lignes
        Test.append(tmp)
    if Test!=tableau:
        #application sur la grille de jeu
        tableau=Test
    #si le tableau est pareil il est donc inutile de continuer le programme car rien ne changera plus
    else:
        tableau=False
    return  tableau


#Boucle de Jeu
run=True
while run==True:
    choix= menu()
    #permet de savoir si l'utilisateur veut quitter
    if choix== False:
        run=False
    elif choix== 2:
        regle()
    else:
        plateau=demandeTableau()
        continu=True
        nbTours=0
        #boucle qui continue tant que le tableau peut encore être mis a jour (qu'il n'est pas pareil entre 2 tours)
        while continu==True:
            nbTours+=1
            #permet de suivre la progression a un rythme fluide
            sleep(0.5)
            clear()
            affichage(plateau)
            plateau=update(plateau)
            #Tout les 20 tours, demander si le joueur veut arreter 
            if nbTours%20==0:
                rep=input("\nVoulez vous continuer l'éxecution? Oui: O, Non: Autres\n>>> ")
                rep=rep.replace(" ","").lower()
                if rep != "o":
                    continu=False
            #si le tableau est pareil il est donc inutile de continuer le programme car rien ne changera plus
            if plateau==False:
                input("\nAppuyez sur une touche pour revenir au menu\n>>> ")
                continu=False