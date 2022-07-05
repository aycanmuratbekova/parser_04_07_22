Парсер берет данные с сайта newsline.kg и сохраняет новости 
в файле  creation_date_dd_mm_yyyy.json в виде json.

Генерируем URL с лимитом и датой
URL = f'http://newsline.kg/getNews.php?limit={limit}&last_dt={datetime.now()}'

в ссылке значение limit возвращает количество статей на сайте 
last_dt указывает на текущую дату.

К примеру задаем limit = 2  -   который получит только два объекта

При запуске программы срабатывает функция main()  и вызывает collect_data()
def main():
    collect_data()

def collect_data():
    """
    Функция collect_data() получает response-ответ по URL запросу
    открывает файл с названием  creation_date_04_07_2022.json
    записывает туда response в формате json файла
    """
