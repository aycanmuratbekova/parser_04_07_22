Парсер

Краткое содержание ТЗ

Создать parser новостей:

<li>Поля новостей которые нужно с парсить</li>
    <ul>id</ul>
    <ul>id_site</ul>
    <ul>title</ul>
    <ul>category</ul>
    <ul>category_id</ul>
    <ul>desc</ul>
    <ul>dt</ul>
    <ul>img</ul>
    <ul>link</ul>
    <ul>date</ul>
    <ul>site_name</ul>
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
