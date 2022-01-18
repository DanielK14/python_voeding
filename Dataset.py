import pandas as pd 

path = "food composition//foodDataset.csv"
df = pd.read_csv(path, sep = ',')

barcode = [1265, 6543, 8752, 6545, 3671, 4102, 6114] * 1059

new_df = df.copy()

new_df["Barcodes"] = barcode

new_df.to_csv('food composition//foodDatasetBarcode.csv')





#def FoodValues(dataframe, productnaam):

 # output = []
  #for i, product in dataframe.iterrows():
   # if product["Category"] == productnaam:
    #  output.append(product)
     # print(output)

#print(FoodValues(df, "BUTTER"))

#print(df.columns)
#avgattack = sum(df["Sp. Atk"]) / len(df["Sp. Atk"])


#def attack(dataframe, name):

 # pkm = []
  #for i, pokemon in dataframe.iterrows():
   # if pokemon["Name"] == name:
    #  pkm.append(pokemon["Sp. Atk"])
    
     # print(pkm)

#print(attack(df, "Pikachu"))

#for item in df.iterrows():
 #    if item[0] >= avgattack:
  #        print(item)

#print(df["COUNTRY"])
#counter = 0
#for i, x in df.iterrows():
 #   print(x["COUNTRY"])
  #  allesVanNederland = []
   # if x["COUNTRY"] == "Netherlands":
    #    allesVanNederland.append(x)

    #counter += 1
    #if counter >12:
     #   break

#print(allesVanNederland)

# en dan runnen in anaconda prompt met: python [naambestand.py]
# wel in anaconda prompt eerst naar de directory gaan waar het python bestand staat.
#encoding='ISO-8859-1'