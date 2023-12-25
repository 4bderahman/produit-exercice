from collections import namedtuple, defaultdict, deque
from abc import ABC, abstractmethod

# Redefinina les classes b tariqa li tsahl comprendre l code

class Composition:
    # Constructeur dial Composition: kaysift l produit o quantite dyalou
    def __init__(self, produit, quantite):
        self._produit = produit  # Le produit
        self._quantite = quantite  # Kemmiya dyal le produit

    # Getters o setters dial produit o quantite
    @property
    def produit(self):
        return self._produit

    @produit.setter
    def produit(self, value):
        self._produit = value

    @property
    def quantite(self):
        return self._quantite

    @quantite.setter
    def quantite(self, value):
        self._quantite = value

    # Methode equals bash n'compariw jowj compositions 3la hssab produit o quantite
    def equals(self, other):
        if isinstance(other, Composition):
            return self.produit.equals(other.produit) and self.quantite == other.quantite
        return False

class Produit(ABC):
    # Constructeur dial Produit: kayakhod nom o code
    def __init__(self, nom, code):
        self._nom = nom  # Smiya dyal produit
        self._code = code  # Code dyal produit

    # Getters dial nom o code
    @property
    def nom(self):
        return self._nom

    @property
    def code(self):
        return self._code

    # Methode abstraite li kay3awd n'calculiw prix HT dial produit
    @abstractmethod
    def getPrixHT(self):
        pass

    # Methode equals bash n'compariw si jowj produits homa l istihal
    def equals(self, other):
        if isinstance(other, Produit):
            return self.nom == other.nom and self.code == other.code
        return False

# ProduitElementaire o ProduitCompose: jowj types dial produits

class ProduitElementaire(Produit):
    # Constructeur dial ProduitElementaire: kayakhod nom, code o prixAchat
    def __init__(self, nom, code, prixAchat):
        super().__init__(nom, code)
        self._prixAchat = prixAchat  # Prix d'achat dyal le produit

    # Methode getPrixHT o equals
    def getPrixHT(self):
        return self._prixAchat

    def equals(self, other):
        return super().equals(other) and self._prixAchat == other._prixAchat

class ProduitCompose(Produit):
    # Taux TVA dial ProduitCompose: valeur fixe
    tauxTVA = 0.18

    # Constructeur dial ProduitCompose: kayakhod nom, code o fraisFabrication
    def __init__(self, nom, code, fraisFabrication):
        super().__init__(nom, code)
        self._fraisFabrication = fraisFabrication  # Frais dial fabrication
        self._listeConstituants = []  # Liste dial les constituants dyal produit

    # Ajouter constituant l liste dyal constituants
    def ajouterConstituant(self, constituant):
        self._listeConstituants.append(constituant)

    # Methode getPrixHT o equals
    def getPrixHT(self):
        prixHT = self._fraisFabrication  # Prix HT kaybda b frais dial fabrication
        for constituant in self._listeConstituants:
            prixHT += constituant.produit.getPrixHT() * constituant.quantite  # Zid prix dyal kolla constituant
        return prixHT

    def equals(self, other):
        if not super().equals(other):
            return False
        return self._fraisFabrication == other._fraisFabrication and self.compareConstituants(other._listeConstituants)

    # Comparaison dial les constituants dyal produit
    def compareConstituants(self, otherConstituants):
        if len(self._listeConstituants) != len(otherConstituants):
            return False
        for constituant in self._listeConstituants:
            if not any(constituant.equals(c) for c in otherConstituants):
                return False
        return True

# Creina jowj produits elementaires (p1 o p2) o wa7ed composé (p3)
p1 = ProduitElementaire("Produit 1", "P1", 100)
p2 = ProduitElementaire("Produit 2", "P2", 150)
p3 = ProduitCompose("Produit 3", "P3", 50)
p3.ajouterConstituant(Composition(p1, 2))  # Zidina p1 b 2 fois f p3
p3.ajouterConstituant(Composition(p2, 4))  # Zidina p2 b 4 fois f p3

# Define namedtuple 'Description' pour description dial produits
Description = namedtuple('Description', ['Produit', 'Détail'])

# Creina liste dyal produits
ListeProduit = [p1, p2, p3]

# Creina descriptions dial kolla produit f ListeProduit
descriptions = []
for produit in ListeProduit:
    if isinstance(produit, ProduitElementaire):
        detail = f"{produit.nom} est un produit Élémentaire"  # Si produit elementaire
    elif isinstance(produit, ProduitCompose):
        composants = ', '.join([c.produit.nom for c in produit._listeConstituants])
        detail = f"{produit.nom} est composé de {composants}"  # Si produit composé
    descriptions.append(Description(Produit=produit.nom, Détail=detail))

# Convertina chaque Description l dictionary
description_dicts = [desc._asdict() for desc in descriptions]

# Creina defaultdict fih descriptions dial produits
ListeDescription = defaultdict(list)
for desc in description_dicts:
    ListeDescription[desc['Produit']].append(desc['Détail'])

# Creina deque o zdna fih les éléments men ListeDescription
DeqDescription = deque()
for detail in ListeDescription.values():
    DeqDescription.extend(detail)

# Affichina les résultats
print(description_dicts)
print(dict(ListeDescription))
print(DeqDescription)
