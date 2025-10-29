import requests 
import os

def fetch_character_data(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text 

if __name__ == "__main__":
    save_dir = os.path.join("data", "API_and_parse")  
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, "character_108.json")

    json_str = fetch_character_data(108)
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(json_str)

    print(f"Данные загружены и сохранены в {save_path}")