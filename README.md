# Near-Hack-Hackaton

# Як запустити проект?

1. Клонувати репозиторій на свій ПК и перейти в папку з цим проектом:
```
git clone https://github.com/zaharfsk/Near-Hack-Hackaton.git
cd Near-Hack-Hackaton
```

2. В цій деректорії виконати установку потрібних бібліотек.
```
pip install -r requirements.txt
```

3. Після установки переходимо в директорію `cd cryptogochi`

4. Щоб все працювало виконуємо міграції баз данних.
```
python manage.py migrate
```
5. Після міграцій можемо запускати наш тестовий сервер:
```
python manage.py runserver
```

