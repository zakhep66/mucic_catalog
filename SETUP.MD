# Музыкальный каталог
### Инструкция по установке и запуску проекта

# Установка

Для запуска на ПК должны быть установлены:
[Python 3.10](https://www.python.org/downloads/);
[Git](https://git-scm.com/);

### Клонируйте репозиторий

```sh
$ git clone https://github.com/zakhep66/music_catalog.git
```

### 1) Настройка Django

В корне проекта создайте виртуальное окружение и активируйте его

```sh
$ python -m venv venv (для Linux: python3 -m venv venv)
$ .\venv\Scripts\activate (для Linux: source ./venv/bin/activate)
```

#### Все последующие действия производить внутри виртуального окружения

Установите все необходимые зависимости для работы Django

```sh
$ pip install -r req.txt
```

Создайте суперпользователя для работы с админкой или продолжите работу со стандартным пользователем
(логин: admin, пароль: 1)

```sh
$ python manage.py createsuperuser (для Linux: python3 manage.py createsuperuser)
```

Запустите проект

```sh
$ python manage.py runserver (для Linux: python3 manage.py runserver)
```
