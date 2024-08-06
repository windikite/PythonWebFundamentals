import requests, json

def fetch_data(url):
    response = requests.get(url)
    json_data = response.text
    return json.loads(json_data)

def get_ability_info(poke_data):
    abilities = poke_data["abilities"]
    ability_strings = []
    
    for ability in abilities:
        ability_url = ability["ability"]["url"]
        ability_text = json.loads(requests.get(ability_url).text)["flavor_text_entries"][3]["flavor_text"]
        ability_strings.append(f"{ability["ability"]["name"]} - {ability_text}")

    return ability_strings

def calculate_average_weight(weights):
    return sum(weights) / len(weights)

def get_poke_data(urls):
    weights = []
    for url in urls:
        data = fetch_data(url)
        ability_strings = get_ability_info(data)
        print(data["name"])
        for string in ability_strings:
            print(string)
        weights.append(data["weight"])
        print("-----------------")
    
    print("Average weight:", calculate_average_weight(weights))

pokemon_urls = ["https://www.pokeapi.co/api/v2/pokemon/gastly", 
           "https://www.pokeapi.co/api/v2/pokemon/haunter", 
           "https://www.pokeapi.co/api/v2/pokemon/gengar"]

get_poke_data(pokemon_urls)
