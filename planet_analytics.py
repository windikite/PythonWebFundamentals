import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    return response.json()['bodies']

def get_planet_info(planets):
    for planet in planets:
        if planet['isPlanet']:
            name = planet["englishName"]
            mass = planet["mass"]["massValue"]
            orbit_period = planet["sideralOrbit"]
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

def find_heaviest_planet(planets):
    planet_name = ""
    highest_mass = 0
    for planet in planets:
        if planet["isPlanet"]:
            mass_value = planet["mass"]["massValue"]
            mass_exponent = planet["mass"]["massExponent"]
            mass = mass_value**mass_exponent
            if mass > highest_mass:
                planet_name = planet["englishName"]
                highest_mass = mass
    print(f"{planet_name} is the heaviest planet with a mass of {highest_mass} kg.")

planets = fetch_planet_data()

get_planet_info(planets)

print("--------------")

find_heaviest_planet(planets)