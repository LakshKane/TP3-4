from Noeud import Noeud
from matplotlib import pyplot as plt
import numpy as np

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
print(exp.evaluer(dico))

exp.tracer("y", np.linspace(0,100,100))