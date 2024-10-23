## Локальный запуск
### Требования
- Версия Python 3.12

В папке ```/src```:

1. Скопировать ```.env``` файл

2. Установить менеджер пакетов:
```pip install pipenv```

3. Установить зависимости для разработки:
```pipenv install --dev```

4. Запустить бота
```pipenv run main.py```

## Сборка и запуск в Docker вручную
### Требования
- Docker и плагин docker-compose

1. В папку ```dockerenvs``` поместить файлы:
    - ```bot.env```
    - ```postgres.env```
    - ```redis.env```

2. Из корневой собрать проект:
```docker system prune -f && docker compose up --build```
Чтобы собрать в detached режиме:
```docker system prune -f && docker compose up --build -d```

### Прочее
В проекте есть форматтер black.
Запустить можно командой black <путь до файла> 


