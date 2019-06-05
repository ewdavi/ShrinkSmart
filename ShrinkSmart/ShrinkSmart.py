#!/usr/bin/python3
import pandas as pd

cities = ['Altoona, IA', 'Lake Park, IA', 'Williamsburg, IA', 'Batavia, IA', 'Buffalo Center, IA', 'Epworth, IA',
          'Le Claire, IA', 'St. Charles, IA', 'Fruitland, IA', 'Le Mars, IA', 'University Park, IA',
          'Columbus Junction, IA', 'Correctionville, IA', 'Pacific Junction, IA', 'Sac City, IA', 'Elma, IA', 
          'Hamburg, IA', 'Everly, IA', 'Sheffield, IA', 'Anita, IA', 'Corning, IA', 'Audubon, IA', 
          'Sibley, IA', 'Clarence, IA', 'What Cheer, IA', 'Montezuma, IA', 'Battle Creek, IA', 'Albert City, IA',
          'Bayard, IA', 'Murray, IA', 'Sabula, IA']

categories = ['grow-thrive', 'grow-thrive', 'grow-thrive', 'grow-thrive', 'grow-thrive', 'grow-thrive', 'grow-thrive', 'grow-wither', 'grow-wither', 'grow-wither', 'grow-wither', 'grow-wither', 'shrink-thrive', 'shrink-thrive', 'shrink-thrive', 'shrink-thrive', 'shrink-thrive', 'shrink-thrive', 'shrink-thrive', 'shrink-wither', 'shrink-wither', 'shrink-wither', 'shrink-wither', 'shrink-wither', 'shrink-wither', 'shrink-wither', 'shrink-wither', 'shrink-wither', 'shrink-wither', 'shrink-wither', 'shrink-wither']

def getCityClass(cityName):
    cityList = [x.lower() for x in cities]
    cityName = cityName.lower()
    if (not cityName in cityList):
        return('N/A')
    idx = cityList.index(cityName)
    return(categories[idx])

def getCities():
    return(cities)

def getLatLong(cityName):
    df = pd.read_csv('city-basics_iowa.csv')
    coordinates = (float(df[df['City'] == cityName]['Lat']), float(df[df['City'] == cityName]['Lon']))
    return(coordinates)