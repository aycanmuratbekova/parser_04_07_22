import requests
import json
from datetime import datetime


limit = 2
URL = f'http://newsline.kg/getNews.php?limit={limit}&last_dt={datetime.now()}'


def collect_data():
    """
    Функция collect_data() получает response-ответ по URL запросу
    открывает файл с названием  creation_date_04_07_2022.json
    записывает туда response в формате json файла
    """
    last_dt = datetime.now().strftime('%d_%m_%Y')
    response = requests.get(url=URL)
    with open(f'creation_date_{last_dt}.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def main():
    collect_data()


if __name__ == '__main__':
    main()


