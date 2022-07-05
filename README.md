<h2>Парсер новостей</h3>
Парсер берет данные с сайта newsline.kg и сохраняет новости<br/> 
в файле  creation_date_dd_mm_yyyy.json в виде json.<br/><br/>

Генерируем URL с лимитом и датой:<br>
URL = f'http://newsline.kg/getNews.php?limit={limit}&last_dt={datetime.now()}'<br/>

в ссылке значение limit возвращает количество статей на сайте<br/> 
last_dt указывает на текущую дату.<br/>

К примеру задаем limit = 2  -   который получит только два объекта<br/>

При запуске программы срабатывает функция main()<br/>
которая вызывает collect_data()

<h5>collect_data() получает response-ответ по URL запросу<br/>
    открывает файл с названием  creation_date_04_07_2022.json<br/>
    записывает туда response в формате json файла<br/>
