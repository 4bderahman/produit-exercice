# Hadchi b'ssah kaysahel 3lina la gestion dyal comptes bancaires

# Bditna b'definir la classe de base Compte
class Compte:
    # Constructeur b'shahadat dyal compte (numéro, propriétaire, solde, dateOuverture)
    def __init__(self, numero, proprietaire, solde, date_ouverture):
        self._numero = numero  # Numéro dyal compte
        self._proprietaire = proprietaire  # Smiya dyal mol compte
        self._solde = solde  # Flouss li kayen f compte
        self._date_ouverture = date_ouverture  # Date ftahna fih compte

    # Getters bach njibou l'informations dyal compte
    @property
    def numero(self):
        return self._numero

    @property
    def proprietaire(self):
        return self._proprietaire

    @property
    def solde(self):
        return self._solde

    @property
    def date_ouverture(self):
        return self._date_ouverture

    # Methode __str__ bach n'affichiw l'informations dyal compte
    def __str__(self):
        return f"Compte Numéro: {self._numero}, Propriétaire: {self._proprietaire}, " \
               f"Solde: {self._solde}, Date d'Ouverture: {self._date_ouverture}"

# Classe CompteCourant li kayweret mn Compte
class CompteCourant(Compte):
    # Constructeur dyal CompteCourant b'zidat montantDecouvertAutorise
    def __init__(self, numero, proprietaire, solde, date_ouverture, montant_decouvert_autorise):
        super().__init__(numero, proprietaire, solde, date_ouverture)
        self._montant_decouvert_autorise = montant_decouvert_autorise  # L'argent li yemken n'dozou fih

    # Getter dyal montantDecouvertAutorise
    @property
    def montant_decouvert_autorise(self):
        return self._montant_decouvert_autorise

    # Methode __str__ bach n'affichiw l'informations dyal CompteCourant
    def __str__(self):
        return super().__str__() + f", Montant Découvert Autorisé: {self._montant_decouvert_autorise}"

# Classe CompteEpargne li kayweret mn Compte
class CompteEpargne(Compte):
    # Constructeur dyal CompteEpargne b'zidat interet
    def __init__(self, numero, proprietaire, solde, date_ouverture, interet):
        super().__init__(numero, proprietaire, solde, date_ouverture)
        self._interet = interet  # Interet li kay3ti l'banque

    # Getter dyal interet
    @property
    def interet(self):
        return self._interet

    # Methode __str__ bach n'affichiw l'informations dyal CompteEpargne
    def __str__(self):
        return super().__str__() + f", Intérêt: {self._interet}"

# Creina chi comptes bshakl dyal examples
compte_normal = Compte("12345A", "John Doe", 1000.0, "2023-01-01")
compte_courant = CompteCourant("12345B", "Jane Doe", 2000.0, "2023-01-02", 500.0)
compte_epargne = CompteEpargne("12345C", "Jim Doe", 3000.0, "2023-01-03", 0.02)

# N'affichiwhom bach nchoufou kif kaynin
print(compte_normal)
print(compte_courant)
print(compte_epargne)
