#!/usr/bin/python3

from dataclasses import dataclass

@dataclass
class Voiture:
    couleur: str
    marque: str
    vitesse: int = 0
    
    def accelerer(self, vitesse: int) -> None:
        self.vitesse += vitesse
    
    def freiner(self, vitesse: int) -> None:
        self.vitesse -= vitesse
        
        if self.vitesse < 0:
            self.vitesse = 0

if __name__ == '__main__':
    voiture = Voiture('bleu', 'BMW')
    voiture.accelerer(20)
    voiture.freiner(100)
    print(voiture)
