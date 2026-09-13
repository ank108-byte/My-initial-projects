import requests
base_url="https://countries.dev/name/"
def get_info(name):
   actual_url=f"{base_url}{name}"
   response=requests.get(actual_url)
   if response.status_code==200:
      print("Data retrieved")
      gathered_data=response.json()
      #print(gathered_data)
      return gathered_data
   else: 
      print(f"Error {response.status_code}")
name=input("Enter the name of the country to dive into its insights: ")
name=name.capitalize()
#get_info(name)
outcome=get_info(name)
print(f"About {name}:")
if outcome[0]["name"].lower()==name.lower():
    print("******************************")
    print(f"Area: {outcome[0]["area"]}")
    print(f"Region: {outcome[0]["region"]}")
    print(f"Capital: {outcome[0]["capital"]}")
    print(f"Sub Region: {outcome[0]["subregion"]}")
    print(f"Time Zone: {outcome[0]["timezones"]}")
    print(f"Currency: {outcome[0]["currencies"]}")
    print(f"Native Name: {outcome[0]["nativeName"]}")
    print(f"Population: {outcome[0]["population"]}")
    print(f"Independent: {outcome[0]["independent"]}")
    print(f"Calling Codes: {outcome[0]["callingCodes"]}")
    print(f"Top-level Domain: {outcome[0]["topLevelDomain"]}")
    print("******************************")
else:
   print("Something went wrong!")
#print(f"Weight: {outcome["weight"]}")
#print(f"Base experience: {outcome["base_experience"]}")
#print("\nAbilities:")
#for ability in outcome["abilities"]:
#   print(ability["ability"]["name"])
