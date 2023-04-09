import requests

def pokemon_stats():
#Different from one in class it works but I don't know how to get different ids for different pokemon
#So I can't use it because not what I need to do
    res = requests.get('https://pokeapi.co/api/v2/pokemon/501')
    if res.ok:
        data = res.json()

        name = data['name']
        ability = data['abilities'][0]['ability']
        base_experience = data['base_experience']
        image_url = data['sprites']['front_default']
        attack = data['stats'][1]['base_stat']
        defense = data['stats'][2]['base_stat']
        hp = data['stats'][0]['base_stat']
    
        image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/501.png"

        pokemon_data = {
            "name" : name,
            "ability" : ability,
            "base_experience" : base_experience,
            "image_url" : image_url,
            "attack" : attack,
            "defense" : defense,
            "hp" : hp

    }
        
        return pokemon_data 
    else:
        print("Invalid information")
#Similar to the one in class but could not figure it out 
def pokemon_stats():
    res = requests.get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=20')
    if res.ok:
        data = res.json()
        data = data['results']['abilities'][0]['base_experience']['sprites']['stats'][1]['stats'][2]['stats'][0]
        output = {}
        for entry in data:
            pokemon_info = f"{entry['ability']['ability']} {entry['stats']['base_stats[1]']} {entry['stats']['base_stats[2]']} {entry['stats']['base_stats[0]']}"
            output[pokemon_info] = {

            }

x = pokemon_stats()
print(x)

 



