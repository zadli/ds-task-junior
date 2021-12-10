# image-text-recognition

## Описание
- Был использован flask в качестве веб сервера и easyocr
- Один POST эндпоинт с параметром image
- image = файл для анализа

## Запуск
- git clone
- python3 -m venv ./venv
- source ./venv/bin/activate
- pip install -r requirements.txt
- python3 main.py
- Отправить POST запрос на /image-text-recognition с параметром image (изображение для анализа)
- Или перейти на / и протестировать это в браузере

## Ответ
- JSON Object
- out = JSON Array со строками

## Пример ответа
```
{"out": ["Guideline for new language request", "To request a new language", "we need you to send a PR with the 2", "following files:", "1. In folder easyocr/character, we need yourlanguagecode char txt' that contains list of all characters Please see", "format examples from other files in that folder", "2. In folder easyocr /dict, we need yourlanguagecode txt' that contains list of words in your language On average", "we have ~\u0437\u041e\u041e\u041e\u041e words per language with more than SOOOO words for more", "popular"]}
```
