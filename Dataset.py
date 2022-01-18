import pandas as pd 

path = "food composition//NutrientDataset.csv"
df = pd.read_csv(path, delimiter = ',',index_col = "ID", error_bad_lines = False, dtype = str, quotechar = '"')

print(df.head(10))

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