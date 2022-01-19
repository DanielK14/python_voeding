import pandas as pd

df = pd.read_csv('food composition//SportDatasetkg.csv', delimiter = ',')

# Hieronder is een copy van de dataframe gemaakt en de kolommen die in lb stonden vervangen voor kg.
# new_df = df.copy()

# new_df.rename(columns={'130 lb': 'Burned Calories (59 kg)', '155 lb': 'Burned Calories (70 kg)', '180 lb': 'Burned Calories (82 kg)', '205 lb': 'Burned Calories (93 kg)'}, inplace=True)


def burned_calories(kg, sport, time_in_hours, dataframe):

    cal_per_kg = 0

    
    for i, activity in dataframe.iterrows():
                  
        if sport in activity["Activity, Exercise or Sport (1 hour)"]:
            cal_per_kg += activity["Calories per kg"]
            print("You burned: ", round(((cal_per_kg * kg) * time_in_hours), 0), "calories!")
    
print(burned_calories(80, "Skiing", 0.5, df))



