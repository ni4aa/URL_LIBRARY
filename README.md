<h1>Url Library</h1>

<h2>Документация записана в docs.yaml с помощью swagger</h2>

<h2>Cпособы запуска приложения </h2>
<h3>Через консоль</h3>

1. Клонировать проект
   
3. Создать виртуальное окружение
   
3. Создать базу данных

4. Написать .env

5. Скачать все библиотеки из requirement.txt
    * pip install -r requirement.txt

6. Скачать библиотеку psycopg2 (нет в requirement.txt, так как не коректно работает docker)
    * pip install psycopg2

7. Провести миграции
   * python.py manage.py migrate

8. Запустить сервер на удобном порту
   * python.py manage.py runserver "port"


<h3>Docker-compose</h3>

1. Зайти в папку с docker-compose
   * cd .\docker-compose\
2. Запустить docker-compose
   * docker-compose up
     
**Сервер будет доступен по пути localhost:8001 или localhost:80 через nginx**

