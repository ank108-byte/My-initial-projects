import requests
base_url="https://pokeapi.co/api/v2/"
def get_info(name):
   actual_url=f"{base_url}pokemon/{name}"
   response=requests.get(actual_url)
   if response.status_code==200:
      print("Data retrieved")
      gathered_data=response.json()
      return gathered_data
   else: 
      print(f"Error {response.status_code}")
name=input("Enter the name of your pokemon to see its properties: ")
outcome=get_info(name)
print(f"Properties of {name}:")
print(f"Height: {outcome["height"]}")
print(f"Weight: {outcome["weight"]}")
print(f"Base experience: {outcome["base_experience"]}")
print("\nAbilities:")
for ability in outcome["abilities"]:
    print(ability["ability"]["name"])
