import pandas as pd

data = pd.read_json("food composition//NutrientDatasetDict.json")

df = pd.DataFrame(data)

dfhead = dfhead(10)

print(dfhead)
    