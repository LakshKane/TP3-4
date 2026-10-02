import numpy as np
import matplotlib as plt
class Noeud: 
    def __init__(self , valeur):
        self.valeur = valeur
        self.enfant = []

    def ajout_noeud(self, noeud):
        self.enfant.append(noeud)

    def polonais(self):
        expression = str(self.valeur)
        for e in self.enfant:
            expression += " " + e.polonais()
        return expression

    def evaluer(self,variables):
        if isinstance(self.valeur,(float,int)):return self.valeur
        if self.valeur in variables : return variables[self.valeur]
        if len(self.enfant)>0:
            if self.valeur == "+": return self.enfant[0].evaluer(variables) + self.enfant[1].evaluer(variables)
            elif self.valeur == 'exp': return np.exp(self.enfant[0].evaluer(variables))
        raise ValueError("Opérateur/Noeud inconnu")

    # def tracer(self,variable,liste):
    #     return None 


