# Email Reader

## Описание

Email Reader - это проект, разработанный для управления и обработки электронной почты. Он позволяет пользователям
получать, отправлять и управлять электронными письмами через удобный интерфейс. Проект использует Django и Django
Channels для обеспечения асинхронной обработки запросов и работы в реальном времени с веб-сокетами.

## Установка

Чтобы установить проект, выполните следующие шаги:

1. Клонируйте репозиторий:

```bash
   git clone https://github.com/ваш_пользователь/email_reader.git
   cd email_reader
```

2. Создайте виртуальное окружение и установите зависимости:

```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
```

3. Настройте базу данных:Создайте базу данных и выполните миграции:

```bash
   python manage.py migrate
```

4. Создайте суперпользователя (опционально):

```bash
   python manage.py createsuperuser
```

5. Запустите веб-сервер:

```bash
   daphne -u /tmp/daphne.sock email_reader.asgi:application
```

6. Откройте браузер и перейдите по следующему адресу:

```bash
   http://localhost:8000
```
