from xml.etree.ElementInclude import include
import pandas
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
#print("test")

dfhb = pandas.read_csv("food composition/Food_composition_dataset.csv",sep=";")
print(dfhb.columns)
#print(dfheelbestand["COUNTRY"])
def onderbreking(nummer):
    print("======")
    print("")
    print(nummer)
    print("=======++++++")

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
onderbreking(1)

print(  len( dfhb ))
print(  len( dfhb.columns ))
print(  dfhb.dtypes  )
print(  dfhb["NUTRIENT_ID"].max()  )
print(  dfhb["NUTRIENT_ID"].mean() )
#print(  dfhb.mean()  ) duurt lang
print(   dfhb.describe() )
onderbreking(2)

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
onderbreking(3)

dfpstemp["birth_date"] = pandas.to_datetime(dfps.birth_date).dt.year
print(  dfpstemp["birth_date"] )
print(  dfpstemp.describe(include='all') )
print(  dfpstemp["first_name"].mode()  )

print(  Counter(dfps["first_name"]) )
print(  Counter(dfps["first_name"])['Chloe'] )
print(  Counter(dfps["first_name"]).most_common(5)  )
onderbreking(4)

onlydates = dfps[['birth_date', 'date_first_purchase']]
print(onlydates)
onderbreking(5)

print(  dfps[['birth_date', 'date_first_purchase']].dtypes  )
print( dfps.birth_date )
dfps['birth_date'] = pandas.to_datetime(dfps['birth_date'])
print( dfps.birth_date )
print( dfps.dtypes )

print( dfps['birth_date'][0] )
print( dfps['birth_date'][0].month )
# [x for x in dfps['birth_date']] 
print( [x for x in dfps['birth_date'][:7] ]    )
print( [x.month for x in dfps['birth_date'][:7] ]    )

months = []
for bd in dfps['birth_date']:
    months.append(bd.month)

print(months)
dfps['geboortedatum'] = [x.month for x in dfps['birth_date']]
print( dfps )
#print( dfps.columns.index('birth_date')) # werkt niet
print( list(dfps.columns).index('birth_date') )

dfpsneworder = dfps[list(dfps.columns[:list(dfps.columns).index('birth_date')+1]) 
                + [dfps.columns[-1]] 
                + list(dfps.columns[list(dfps.columns).index('birth_date')+1:-1])]

print(  dfps.columns   )
print( dfpsneworder.columns )

onderbreking(6)

dfps = dfps.drop( columns='education' )
print(  dfps.columns  )
print( dfps.head(5) )
dfps = dfps.drop(index=[1,2,3])
print( dfps.head(5) )
dfps.dropna() # handig als je nulwaarden in je data hebt

print( dfps['geboortedatum'].mode() )
c = Counter(dfps['geboortedatum'])
print(  c   )
print(  sorted(c, key=lambda x:c[x])   )
print(   sorted( c.values() ))
print(  c[4]  )
print(   c[10]  ) 
print(  c.keys()  )

onderbreking(  7  )

plt.hist( c )
plt.show()

plt.plot( range(5), range(0,10,2))
plt.show()

plt.scatter( range(5), range(0,10,2))
plt.show()
