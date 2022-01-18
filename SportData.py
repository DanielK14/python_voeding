import pandas as pd

df = pd.read_csv('food composition//SportDatasetkg.csv', delimiter = ',')

# new_df = df.copy()

# new_df.rename(columns={'130 lb': 'Burned Calories (59 kg)', '155 lb': 'Burned Calories (70 kg)', '180 lb': 'Burned Calories (82 kg)', '205 lb': 'Burned Calories (93 kg)'}, inplace=True)
# oefening met gedeeltelijke tekst in kolom opzoeken
# b = "Uni"
# a = new_df["Activity, Exercise or Sport (1 hour)"].str.contains(b)

def burned_calories(kg, sport, time_in_hours, dataframe):

    cal_per_kg = 0

    
    for i, activity in dataframe.iterrows():
        
        if activity["Activity, Exercise or Sport (1 hour)"] == sport:
            cal_per_kg += activity["Calories per kg"]
            return("You burned: ", ((cal_per_kg * kg) * time_in_hours), "calories!")
    
print(burned_calories(80, "Unicycling", 0.5, df))



