from enum import Enum


class StatuEmprunt(Enum):
    Reserver = 1
    Non_Rendue = 2
    Libre = 3
    En_Attente = 4
