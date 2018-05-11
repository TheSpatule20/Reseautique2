#!/usr/bin/env python

print("Prénom: ", end="")
Prenom = input()

print("Nom: ", end="")
nom = input()

print("Age: ", end="")
age = input()

print("nom de ton animal: ", end="")
animal = input()

print("nom de ton amant: ", end="")
amant = input()

print("nom de ta mêre: ", end="")
mere = input()

for i in range (0,Prenom.__len__()):
    for j in range(0,Prenom.__len__()):
        print(Prenom[j]+Prenom[i]+age+ animal[1]+animal[2]+animal[3]+amant[1]+amant[2]+amant[3])

for i in range (0,amant.__len__()):
    for j in range(0,amant.__len__()):
        print( Prenom+amant[i]+amant[j]+age)

for i in range (0,animal.__len__()):
    for j in range(0,animal.__len__()):
        for k in range(0,animal.__len__()):
            print(age+ animal[i]+animal[j]+animal[k]+nom)

input()
