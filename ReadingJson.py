import json

f = open("food composition//NutrientDatasetDict.json")
data = json.load(f)

def search_kcal(productnaam, file = data):

    prod_input = productnaam.upper()
    for i in range(len(file)):
        if prod_input in file[i]["ShortDescrip"]:

            print(file[i]["Energy_kcal"])
        else:
            pass

search_kcal('butter')