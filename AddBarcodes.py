import pandas as pd

path = "food composition//foodDatasetBarcode.csv"

df = pd.read_csv(path, sep=",")

testdf = df.copy()

testdfhead = testdf.head(20)

# De code hieronder loopt door de rijen van testdf heen en zoekt naar EDAM en CHEESE in de Discription
# Wanneer die een match heeft vervangt x de barcode met de barcode die erachter geschreven is waarna 
# testdfhead.loc[17] (de locatie van EDAM CHEESE) wordt vervangen voor de waarden die in x staan.

# for i, x in testdf.iterrows():
#     if "EDAM" in x["Description"] and "CHEESE" in x["Description"]:
#         x = x.replace(x["Barcodes"], 5900512110165)
#         testdfhead.loc[17] = x
        
# print(testdfhead)

#       Hieronder is alles in een methode geschreven
def barcode_modifier(new_barcode, prod_name, dataframe = testdf):
    prod_name = prod_name.upper()
    for i, x in dataframe.iterrows():
        if prod_name in x["Description"]:
            x = x.replace(x["Barcodes"], new_barcode)
            dataframe.loc[i] = x

barcode_modifier(5900512110165, "edam", testdf)
print(testdf.head(20))







# for i, x in testdfhead.iterrows():

#     if "BUTTER" in x["Description"]:
#         print(x["Barcodes"])
#         a = testdfhead.replace(x["Barcodes"], 6752)
#         print(a)

# EDAM barcode 5900512110165

# print(testdf.head(5))

# x = testdf["Barcodes"].replace([1265], 6752)

# print(x.head(10))

