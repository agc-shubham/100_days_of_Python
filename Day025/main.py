# # import csv

# # with open('weather_data.csv') as f:
# #     data = csv.reader(f)
# #     temperature = []
    
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperature.append(int(row[1]))
# #     print(temperature)

# import pandas as pd

# data = pd.read_csv('weather_data.csv') ## Convets data into a dataframe
# # print(data)
# # print(data['temp']) ## Convets data into a series
# # print(data['temp'].mean())
# # temp_sum = sum(data['temp'].to_list())
# # avg_temp = temp_sum /len(data['temp'].to_list())
# # print(avg_temp)

# # # Find max temp
# # print(data['temp'].max())

# # # print rows using filter
# # print(data[data.day == 'Monday'])

# # # Print row where temperature is maximum
# # print(data[data.temp == data.temp.max()])

# # Print monday's temperature in farenheit

# celcius =  int(data[data.day == 'Monday'].temp)
# print(celcius*9/5+32)

import pandas as pd

data = pd.read_csv('Squirrel_Data.csv')
squirrel_count = data['Primary Fur Color'].value_counts()
print(type(squirrel_count))
dict = {
    "Fur color" : ['gray','cinnammon','black'],
    "Count" : [squirrel_count[0],squirrel_count[1],squirrel_count[2]]
}

df = pd.DataFrame(dict)
df.to_csv('new_data.csv',index=False)
