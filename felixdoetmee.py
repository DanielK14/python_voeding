from xml.etree.ElementInclude import include
import pandas
import numpy as np
from collections import Counter
#print("test")

dfhb = pandas.read_csv("food composition/Food_composition_dataset.csv",sep=";")
print(dfhb.columns)
#print(dfheelbestand["COUNTRY"])

def heelBestandDoorzoekenOpLand(bestand, country, aantalRecords, startnummer = 0):
    allesVanLand = []
    counter = 0
    for i, x in bestand.iterrows():
        #print(x["COUNTRY"]) # Om te checken welke landen er zijn
        if x["COUNTRY"] == country:
            allesVanLand.append(x)
        counter += 1
        if counter > aantalRecords + startnummer:
            print(allesVanLand)
            return allesVanLand

heelBestandDoorzoekenOpLand(dfhb, "Netherlands", 10) # mag groter

print(  dfhb.head(25))
print(  dfhb.head())
print(  sorted(dfhb.columns)  )
print(  dfhb.columns  )
print(  dfhb.columns[:5]  )
print(  dfhb["COUNTRY"]  )
print(  dfhb[dfhb.columns[:3]]  )
print(  list(dfhb.columns[5:]) + list(dfhb.columns[:5]) )
# verschuiven

print(  len( dfhb ))
print(  len( dfhb.columns ))
print(  dfhb.dtypes  )
print(  dfhb["NUTRIENT_ID"].max()  )
print(  dfhb["NUTRIENT_ID"].mean() )
#print(  dfhb.mean()  ) duurt lang
print(   dfhb.describe() )

dfpk = pandas.read_csv("food composition/Pokemon.csv")
print(  dfpk.describe()   )
print(  dfpk.dtypes  )
print(  dfpk.columns   )

#min max std describe 

dfps = pandas.read_csv("food composition/102_cleaned_header.csv", date_parser=True)
print(  dfps.describe()  )
print(  dfps.dtypes  )
print(  dfps["birth_date"] )
dfpstemp = dfps.copy(deep=True)
dfpstemp["birth_date"] = pandas.to_datetime(dfps.birth_date).dt.strftime('%m-%B-%Y')
print(  dfpstemp["birth_date"] )

dfpstemp["birth_date"] = pandas.to_datetime(dfps.birth_date).dt.year
print(  dfpstemp["birth_date"] )
print(  dfpstemp.describe(include='all') )
print(  dfpstemp["first_name"].mode()  )

print(  Counter(dfps["first_name"]) )
print(  Counter(dfps["first_name"])['Chloe'] )
print(  Counter(dfps["first_name"]).most_common(5)  )

onlydates = dfps[['birth_date', 'date_first_purchase']]
print(onlydates)