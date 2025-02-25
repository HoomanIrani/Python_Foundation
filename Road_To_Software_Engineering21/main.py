# Multithreading -  Used to perform multiple task concurrently. Good to use with API fetching
import threading
import time

def walk_dog(first, last):
    time.sleep(7)
    print(f"You finish walking the {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(3)
    print("You get the mail")

chore1 = threading.Thread(target=walk_dog,args=("Scooby", "Doo"))
chore1.start()
chore2 = threading.Thread(target=take_out_trash())
chore2.start()
chore3 = threading.Thread(target=get_mail())
chore3.start()

# join waits for each method to finish before jumping into the next step which is print statement
chore1.join()
chore2.join()
chore3.join()

print("You are done with all the chores!")
print()

# How to connect to an API using Python
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokeman_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

def main():
    pokeman_name = input("Enter your favorite Pokemon name: ")
    pokemon_info = get_pokeman_info(pokeman_name)

    print(f"Name: {pokemon_info["name"]}".capitalize())
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")

if __name__ == "__main__":
    main()

