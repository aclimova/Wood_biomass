from bs4 import BeautifulSoup
import json

def parse_character_json(json_html):
    soup = BeautifulSoup(f"<pre>{json_html}</pre>", "html.parser")
    json_text = soup.pre.get_text()
    data = json.loads(json_text)

    character = {
        "id": data["id"],
        "name": data["name"],
        "status": data["status"],
        "species": data["species"],
        "type": data["type"],
        "gender": data["gender"],
        "origin": data["origin"]["name"],
        "location": data["location"]["name"],
        "image": data["image"],
        "episode_count": len(data["episode"]),
        "url": data["url"]
    }
    return character

if __name__ == "__main__":
    with open("character_108.json", "r", encoding="utf-8") as f:
        json_html = f.read()

    character_data = parse_character_json(json_html)
    print(character_data)