# -*- coding: utf-8 -*-
"""
Created on Sat Oct 01 14:01:01 2022

@author: Séléna Laval
selena.laval@u-bordeaux.fr
laval.selena@gmail.com
"""

import numpy as np;
import pylab as plt;
import re as re;

file = open("Aston.dat", "rt");

liste_A = np.array([]);
liste_energy = np.array([]);

for i, line in enumerate(file):
    #Expression régulière pour attraper les valeurs de A et de binding energy
    pattern = re.compile(r'^[0-9-]*\s*[0-9-]+\s*[0-9-]+\s*[0-9-]+\s*([0-9-]+)\s*[a-zA-Z]+\s*[a-z0-9-]*\s*[0-9.#-]+\s*[0-9.#-]+\s*([0-9.-]+)#?');
    finds = re.match(pattern, line);
    
    if finds and len(finds.groups()) == 2: #Si l'expression régulière trouve bien A et energy on ajoute au tableau
        liste_A = np.append(liste_A, float(finds.group(1)));
        liste_energy = np.append(liste_energy, float(finds.group(2)));
        
print(liste_A);
print(liste_energy);

assert len(liste_A) == len(liste_energy); #Au cas où les deux tableaux A et energy ne sont pas egaux on arrête

#On trace le graphique
plt.plot(liste_A, liste_energy, 'r+');
plt.title('Courbe d\'Aston ');
plt.xlabel('A')
plt.ylabel('binding energy (KeV)')
plt.show();
plt.savefig("plot.png");