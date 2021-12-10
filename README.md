# emotion-detection

## Описание
- Был использован flask в качестве веб сервера
- Один POST эндпоинт с параметром s
- s = Строка для анализа

## Запуск
- git clone
- python3 -m venv ./venv
- source ./venv/bin/activate
- pip install -r requirements.txt
- python3 main.py
- Отправить POST запрос на /emotion-detection с параметром s (строка для анализа)

## Ответ
- JSON Object
- s = строка, которая была послана
- out = JSON Array в котором содержатся label и score

## Пример ответа
```
{
    "out": [{
            "label": "sadness",
            "score": 0.003062216565012932
        },
        {
            "label": "joy",
            "score": 0.3765401244163513
        },
        {
            "label": "love",
            "score": 0.616303026676178
        },
        {
            "label": "anger",
            "score": 0.002215272979810834
        },
        {
            "label": "fear",
            "score": 0.0009349784231744707
        },
        {
            "label": "surprise",
            "score": 0.0009443357703275979
        }
    ],
    "s": "I love you"
}
```
