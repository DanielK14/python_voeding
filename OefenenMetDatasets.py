import pandas as pd

import statistics

df = pd.read_csv("food composition\Food_composition_dataset.csv", sep=";", encoding="ISO-8859-1")

#def average(x):
 #   len(x) / 

# Hier zet ik de waardes die hieronder gehaald worden in een lijst per land
popcornFinland = []
popcornSweden = []
popcornItaly = []
popcornGermany = []
popcornFrance = []
popcornUK = []
popcornNetherlands = []

# met test maak ik een proef dataframe aan waarmee ik dingen kan proberen
test = df.head(50)

# hieronder loop ik het dataframe heen en haalt alle waardes op die met het genoemde land overeenkomen. .iterrows() gaat het per rij af
for value in test[["COUNTRY", "LEVEL"]].iterrows():
# aangezien deze nu verdeeld worden in tuples moet je eerst indexeren met integers en daarna weer op naam 
    if value[1]["COUNTRY"] == "Finland":
# De waarde in de dataframe is met een comma geschreven maar python kan alleen rekenen als het een . is waardoor de comma's eerst vervangen worden
        converted1 = value[1]["LEVEL"].replace(",", ".")
# Vervolgens vul je de lijsten die hierboven aangemaakt zijn met de waarde die omgezet is.
        popcornFinland.append(converted1)
    if value[1]["COUNTRY"] == "Sweden":
        converted2 = value[1]["LEVEL"].replace(",", ".")
        popcornSweden.append(converted2)
    if value[1]["COUNTRY"] == "Italy":
        converted3 = value[1]["LEVEL"].replace(",", ".")
        popcornItaly.append(converted3)
    if value[1]["COUNTRY"] == "Germany":
        converted4 = value[1]["LEVEL"].replace(",", ".")
        popcornGermany.append(converted4)
    if value[1]["COUNTRY"] == "France":
        converted5 = value[1]["LEVEL"].replace(",", ".")
        popcornFrance.append(converted5)
    if value[1]["COUNTRY"] == "United Kingdom":
        converted6 = value[1]["LEVEL"].replace(",", ".")
        popcornUK.append(converted6)
    if value[1]["COUNTRY"] == "Netherlands":
        converted7 = value[1]["LEVEL"].replace(",", ".")
        popcornNetherlands.append(converted7)

# omdat de lijst uit strings bestaat moeten deze eerst omgezet worden om er mee te kunnen rekenen. vervolgens wordt het gemiddelde uitgerekend.

print(sum(list(map(float, popcornFinland))) / len(popcornFinland))
print(list(map(float, popcornSweden)))
print(list(map(float, popcornItaly)))
print(list(map(float, popcornGermany)))
print(list(map(float, popcornFrance)))
print(list(map(float, popcornUK)))
print(list(map(float, popcornNetherlands)))

#for value in test["LEVEL"]:
    #print(value)

#print(test.loc[test['COUNTRY'] == "Finland", 'LEVEL'].values[0])

#for value in df["LEVEL"]:

    #if [(shortdf["COUNTRY"] == "Finland") & (shortdf["efsaprodcode2_recoded"] == "Popcorn kernels")]:
            #popcornFinland.append(value)

#print(avg(popcornFinland))

# Which unique nutrient types are in the dataframe
# print(df["NUTRIENT_TEXT"].unique())

# Which countrys are in the dataframe
# print(df["COUNTRY"].unique())
