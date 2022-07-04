Импортировала библиотеки  requests, requests, datetime

limit = 2  -   для количества новостных обектов

Генерируем URL с лимитом и датой

URL = f'http://newsline.kg/getNews.php?limit={limit}&last_dt={datetime.now()}'

При запуске программы срабатывает функция main()  и вызывает collect_data()
def main():
    collect_data()


def collect_data():
    """
    Функция collect_data() получает response-ответ по URL запросу
    открывает файл с названием  creation_date_04_07_2022.json
    записывает туда response в формате json файла
    """
