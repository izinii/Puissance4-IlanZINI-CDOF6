import numpy as np


class Puissance4:
    def __init__(self):
        self.grille = np.zeros((6, 7), dtype=int)  # Grille 6x7 remplie de 0

    def afficher_grille(self):
        # Affichage de la grille en remplaçant les 0 par des espaces
        print("\n".join(" | ".join(map(str, ligne)) for ligne in self.grille))
        print("\n")

    def placer_jeton(self, colonne, joueur):
        # Trouver la première ligne vide dans la colonne
        lignes_vides = np.where(self.grille[:, colonne] == 0)[0]  # Indices des lignes vides
        if lignes_vides.size > 0:  # Si au moins une ligne vide existe
            self.grille[lignes_vides[-1], colonne] = joueur
            return True
        return False

    def verifier_victoire(self, joueur):
        # Horizontal
        for row in range(6):
            if self._check_sequence(self.grille[row, :], joueur):
                return True
        # Vertical
        for col in range(7):
            if self._check_sequence(self.grille[:, col], joueur):
                return True
        # Diagonales
        for row in range(3):
            for col in range(4):
                # Diagonale ascendante
                if all(self.grille[row + i, col + i] == joueur for i in range(4)):
                    return True
                # Diagonale descendante
                if all(self.grille[row + 3 - i, col + i] == joueur for i in range(4)):
                    return True
        return False

    def _check_sequence(self, ligne, joueur):
        # Vérifie s'il existe une séquence de 4 jetons du joueur
        compteur = 0
        for value in ligne:
            if value == joueur:
                compteur += 1
                if compteur == 4:
                    return True
            else:
                compteur = 0
        return False
from fonctions import *
import itertools


def gagner(dictionnaire):
    dico_de_base = dico(plateau())
    pos_j1 = []
    liste_tuple_1 = []
    liste_tuple_2 = []
    liste_tuple_3 = []
    pos_j2 = []
    for x in dictionnaire.keys():
        if dictionnaire[x] != dico_de_base[x]:
            if dictionnaire[x] == "O":
                pos_j1.append(x)
            if dictionnaire[x] == "X":
                pos_j2.append(x)

    if len(pos_j1) >= 4:
        for lol in itertools.combinations(pos_j1, 2):
            if lol[0] - lol[1] == 2 or lol[0] - lol[1] == -2:
                liste_tuple_1.append(lol)
            if lol[0] - lol[1] == 30 or lol[0] - lol[1] == -30:
                liste_tuple_2.append(lol)
            if lol[0] - lol[1] == 32 or lol[0] - lol[1] == -32:
                liste_tuple_3.append(lol)
        if len(liste_tuple_1) >= 3:
            return True
        if len(liste_tuple_2) >= 3:
            return True
        if len(liste_tuple_3) >= 3:
            return True

    liste_tuple_3 = []
    liste_tuple_1 = []
    liste_tuple_2 = []
    if len(pos_j2) >= 4:
        for lol in itertools.combinations(pos_j2, 2):
            if lol[0] - lol[1] == 2 or lol[0] - lol[1] == -2:
                liste_tuple_1.append(lol)
            if lol[0] - lol[1] == 30 or lol[0] - lol[1] == -30:
                liste_tuple_2.append(lol)
            if lol[0] - lol[1] == 32 or lol[0] - lol[1] == -32:
                liste_tuple_3.append(lol)
        if len(liste_tuple_1) >= 3:
            return True
        if len(liste_tuple_2) >= 3:
            return True
        if len(liste_tuple_3) >= 3:
            return True
