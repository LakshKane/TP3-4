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

    def evaluer(self,dico):
        if isinstance(self.valeur,str):
            if len(self.enfant) == 2:
                if isinstance(self.enfant[0].valeur,str):
                    a = dico[self.enfant[0].valeur]
                else: 
                    a = self.enfant[0].valeur

                if isinstance(self.enfant[1].valeur,str):
                    b = dico[self.enfant[1].valeur]
                else: 
                    b = self.enfant[1].valeur
                    
                if self.valeur == "+":
                    resultat = float(a) + float(b)
                elif self.valeur == "-":
                    resultat = float(a) - float(b)
                elif self.valeur == "*":
                    resultat = float(a) * float(b)
            else :
                resultat = dico[self.valeur]

                
        return resultat
    
  #  def tracer(self,variable,liste):
