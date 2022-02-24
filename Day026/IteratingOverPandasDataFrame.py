import pandas as pd

weather_c = {
    'day' : ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    'temp' : [12,14,15,14,21,22,24]
    
}

df = pd.DataFrame(weather_c)
print(df)
for index,data in df.iterrows():
    print(data.temp)