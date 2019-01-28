# Goal: Write a program that reads a CSV file of cities with rows in the format
#
# Country,City,AccentCity,Region,Population,Latitude,Longitude
#
# and returns an estimate of the top 10 populated countries based on the available data
#
# Sample lines:
# ro,zlatna,Zlatna,02,8393,46.116667,23.216667
# ro,zorleni,Zorleni,38,9511,46.266667,27.716667
# ro,zorlentu mare,Zorlentu Mare,12,1176,45.450556,21.956111
# ro,zvoristea,Zvoristea,34,6275,47.833333,26.283333
# rs,ada,Ada,00,10259,45.8025,20.125833
# rs,aleksinac,Aleksinac,02,16652,43.541667,21.707778
# rs,alibunar,Alibunar,00,3353,45.080833,20.965833
# rs,apatin,Apatin,02,19677,45.671111,18.984722

import csv


def read_cities_file(_filename):
    all_cities = []
    with open(_filename) as file:
        for row in csv.reader(file):
            if row[0] == "Country":
                continue
            country_code = row[0]
            city_name = row[1]
            population = int(row[4])
            all_cities.append([country_code, city_name, population])
    return all_cities


def get_all_countries(all_cities):
    all_countries = []
    for city in all_cities:
        if city[0] not in all_countries:
            all_countries.append(city[0])
    return all_countries


def estimate_country_population(cities, country_code):
    population = 0
    for city in cities:
        if city[0] == country_code:
            population += city[2]
    return population


def get_population_estimates(countries, cities):
    populations = []
    for country in countries:
        populations.append([country, estimate_country_population(cities, country)])
    return populations


def cmp(item):
    return item[1]


def read_country_names_file(filename):
    code_to_name = {}
    with open(filename) as names_file:
        for line in names_file:
            if line.startswith(";;;"):
                continue
            splits = line.strip().split(';')
            code_to_name[splits[1]] = splits[0]
    return code_to_name


def get_names(country_codes):
    codes_filename = "cities/country_codes.txt"
    code_to_name = read_country_names_file(codes_filename)
    country_names = []
    for code in country_codes:
        country_names.append(code_to_name[code.upper()])
    return country_names


def sort_by_population(cities_filename):
    # load the file into a data structure
    cities = read_cities_file(cities_filename)

    # find all unique countries
    all_countries = get_all_countries(cities)

    # find the population of each country
    country_populations = get_population_estimates(all_countries, cities)

    # sort countries by population
    country_populations.sort(key=cmp, reverse=True)

    # get country codes of top ten countries by population
    top_ten_codes = []
    for i in range(10):
        top_ten_codes.append(country_populations[i][0])

    # get names from codes
    top_ten_names = get_names(top_ten_codes)

    # print the top 10 list
    for country in top_ten_names:
        print(country)


filename = "cities/WorldCitiesPop.csv"
sort_by_population(filename)
