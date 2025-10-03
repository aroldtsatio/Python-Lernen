#coding:utf-8

print("Hello, World!") 



agePersonne = 25
taillePersonne = 1.75
poidsPersonne = 70.5


texte = "j ai {} ans, je mesure {} m et je pèse {} kg"
print(texte.format(agePersonne, taillePersonne, poidsPersonne))


nomDuJoueur = input("Quel est ton nom ? ")
print("Bonjour " + nomDuJoueur + ", bienvenue dans le jeu !")