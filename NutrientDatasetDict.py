import pandas
import re

path = "food composition//NutrientDataset.csv"
de_csv = pandas.read_csv(path, sep=";", encoding="ISO-8859-1")

# Getting object values (id, foodgroup, descrip etc.)
values = []
for i, row in de_csv.iterrows():
    values = row.keys()[0].split(',')
    break

products = []
for i, row in de_csv.iterrows():
    product = []
    # split string at commas, but not inside quotes or brackets
    for idx, r in enumerate(re.split(',(?=([^"]*"[^"]*")*[^"]*$)', row[0])):
        # Regex returns weird values on even numbers
        # Only append odd indices from the split string
        if (idx % 2) == 0:
            product.append(r)

    # amount of product information does not match default information
    # something likely went wrong with the regex
    # ignore this item > short-term solution
    if len(product) != len(values):
        pass
    else:
        # turn product information into key_value pairs
        product_dict = {}
        for idx, val in enumerate(values):
            product_dict[str(val)] = str(product[idx])
        product_dict_copy = product_dict.copy()
        products.append(product_dict_copy)

# This shows the first 10 product dictionaries
# show_amt = 10
# for idx, ps in enumerate(products):
#     print(ps)
#     if idx > show_amt:
#         break

# Example code for queries (see final line for possible product keys)
query = "cheese"
for idx, p in enumerate(products):
    if query in p['ShortDescrip'].lower():
        print(f"Found cheese in {p['ID']}, {p['Descrip']}")

# Available product information -> print(values)
# 'ID', 'FoodGroup', 'ShortDescrip', 'Descrip', 'CommonName', 'MfgName', 'ScientificName', 'Energy_kcal', 'Protein_g', 'Fat_g', 'Carb_g', 'Sugar_g', 'Fiber_g', 'VitA_mcg', 'VitB6_mg', 'VitB12_mcg', 'VitC_mg', 'VitE_mg', 'Folate_mcg', 'Niacin_mg', 'Riboflavin_mg', 'Thiamin_mg', 'Calcium_mg', 'Copper_mcg', 'Iron_mg', 'Magnesium_mg', 'Manganese_mg', 'Phosphorus_mg', 'Selenium_mcg', 'Zinc_mg', 'VitA_USRDA', 'VitB6_USRDA', 'VitB12_USRDA', 'VitC_USRDA', 'VitE_USRDA', 'Folate_USRDA', 'Niacin_USRDA', 'Riboflavin_USRDA', 'Thiamin_USRDA', 'Calcium_USRDA', 'Copper_USRDA', 'Magnesium_USRDA', 'Phosphorus_USRDA', 'Selenium_USRDA', 'Zinc_USRDA'