import requests
import csv


def main():
    url = "https://ru.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": "Категория:Животные по алфавиту",
        "cmlimit": 500,
        "format": "json"
    }

    animals = []
    continue_token = None

    while True:
        if continue_token:
            params["cmcontinue"] = continue_token

        try:
            response = requests.get(url, params=params)
            data = response.json()

            for member in data["query"]["categorymembers"]:
                animals.append(member["title"])

            if "continue" in data:
                continue_token = data["continue"]["cmcontinue"]
            else:
                break
        except:
            break

    # Подсчет по буквам
    counts = {}
    for animal in animals:
        if animal:
            letter = animal[0].upper()
            if 'А' <= letter <= 'Я':
                counts[letter] = counts.get(letter, 0) + 1

    # Сохранение в CSV
    with open("beasts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for letter in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ":
            if letter in counts:
                writer.writerow([letter, counts[letter]])


if __name__ == "__main__":
    main()