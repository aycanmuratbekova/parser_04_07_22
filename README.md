Парсер

Краткое содержание ТЗ

Создать parser новостей:

<ul>новости</ul>
<ul>Поля новостей которые нужно с парсить</ul>
    <li>id</li>
    <li>id_site</li>
    <li>title</li>
    <li>category</li>
    <li>category_id</li>
    <li>desc</li>
    <li>dt</li>
    <li>img</li>
    <li>link</li>
    <li>date</li>
    <li>site_name</li>
<ul>Сохранить в json</ul></br>

Откуда нужно парсить:</br>
http://newsline.kg/getNews.php?limit=30&last_dt=2022-07-04%2007:57:33.933739</br>

limit = количество записей для получения
last_dt = дата записи
B итоге мы должны получить json объекты с сегоднешней датой, с возможностью задавать лимит записей


Техническое задание





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
