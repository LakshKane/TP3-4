from Noeud import Noeud
from matplotlib import pyplot as plt

y = Noeud("y")
deux = Noeud(2)
plus = Noeud ("+")

plus.ajout_noeud(y)
plus.ajout_noeud(deux)

exp = Noeud("exp")
exp.ajout_noeud(plus)
print(exp.polonais())

dico = {"y":5}
print(plus.evaluer(dico))
moins = Noeud("-")
moins.ajout_noeud(y)
moins.ajout_noeud(deux)
print(moins.evaluer(dico))
fois = Noeud("*")
fois.ajout_noeud(y)
fois.ajout_noeud(deux)
print(fois.evaluer(dico))
print(y.evaluer(dico))