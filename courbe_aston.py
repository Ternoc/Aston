# -*- coding: utf-8 -*-
import matplotlib.pyplot
import pandas

def main():
    # Lecture du fichier
    # Les colonnes sont définies manuellement
    df = pandas.read_fwf(
        "mass20.txt", 
        skiprows=35, 
        colspecs=[
            (0,1),
            (1, 4), 
            (5, 9), 
            (10, 14), 
            (15,19), 
            (20, 22), 
            (23,27), 
            (28, 42), 
            (43, 55), 
            (56,68), 
            (69,78),
            (79, 82),
            (83, 93),
            (94, 104),
            (105, 123),
            (124, 133)
            ],
            header=0,
            names=[
                "Fortran Caracter Control",
                "N-Z",
                "N",
                "Z",
                "A",
                "EL",
                "O",
                "MASS EXCESS - Values",
                "MASS EXCESS - Uncertainty",
                "BINDING ENERGY - Values",
                "BINDING ENERGY - Uncertainty",
                "B",
                "BETA-DECAY ENERGY - Values",
                "BETA-DECAY ENERGY - Uncertainty",
                "ATOMIC MASS - Values",
                "ATOMIC MASS - Uncertainty"
            ])

    # On supprime les caractères # de la colonne BINDING ENERGY - Values et on transtype les données au format float
    df['BINDING ENERGY - Values'] = df['BINDING ENERGY - Values'].map(lambda x: x.rstrip('#')) # type: ignore
    df['BINDING ENERGY - Values'] = df['BINDING ENERGY - Values'].astype("Float64")
    df['A'] = df['A'].astype("Float64")

    # On trace le graphique x=A et y=BINDING ENERGY - Values
    matplotlib.pyplot.plot(df["A"], df[["BINDING ENERGY - Values"]], 'r+')
    matplotlib.pyplot.title("Courbe d'Aston")
    matplotlib.pyplot.xlabel("A")
    matplotlib.pyplot.ylabel("binding energy (KeV)")
    matplotlib.pyplot.savefig("plot.png")
    matplotlib.pyplot.show()
    
if __name__ == "__main__":
    main()