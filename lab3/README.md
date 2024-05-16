# Практическое задание №3

## Начало работы

Для работы требуется:

- утилита [make](https://www.gnu.org/software/make/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

Для корректной работы приложения необходимо задать данным переменным значения в
файле [docker-compose.yml](docker-compose.yml) для сервиса `back`:

- `PATH_TO_MODEL` - путь к дериктории, где будет сохранена модель.

Запуск приложения в Docker

```shell
make up
```

Остановка контейнеров

```shell
make down
```

## Пример работы:

```curl
curl --location 'http://localhost/predict' \
--header 'Content-Type: application/json' \
--data '{
    "sepalLength": 7.9,
    "sepalWidth": 4.4,
    "petalLength": 6.9,
    "petalWidth": 2.5
}'
```

```
{
    "result": 2
}
```

## Лицензия

[Лицензия MIT](https://mit-license.org/)

Copyright © 2024 Иноземцев И.В.