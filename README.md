# Интернет-магазин

### Описание
Backend-разработка веб-приложения:
- Шаблонизатор Django (теги, фильтры и наследование)
- Спроектировал реляционную базу данных: 
  - на основе PostgreSQL
  - реализовал операции CRUD
  - настроил связи между таблицами
- Реализовал и настроил:
  - интерфейс администратора 
  - регистрацию, авторизацию и личный кабинет для новых пользователей 
  - корзину с товарами
  - кеширование с помощью Redis, разработав нереляционную базу данных
- Реализовал представления и формы через CBV для удобства дальнейшего расширения кода


### Стек технологий
<p>
    <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img
            src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"
            alt="python" width="40" height="40" /></a>
    <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img
            src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40" /></a>
    <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img 
            src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" 
            alt="postgresql" width="40" height="40"/></a>
    <a href="https://redis.io" target="_blank" rel="noreferrer"> <img 
            src="https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original-wordmark.svg" 
            alt="redis" width="40" height="40"/></a>
    <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img
            src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40" /></a>
    <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img
            src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg"
            alt="html5" width="40" height="40" /></a>
</p>

### Локальная разработка

Все действия должны выполняться из корневой директории проекта и только после установки всех зависимостей.

1. Сначала создайте и активируйте новое виртуальное окружение:
   ```bash
   python3.9 -m venv ../venv
   source ../venv/bin/activate
   ```
   
2. Установите пакеты:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Выполните зависимости проекта, миграции, заполните базу данных данными из фикстур и т.д.:
   ```bash
   ./manage.py migrate
   ./manage.py loaddata <path_to_fixture_files>
   ./manage.py runserver 
   ```
   
4. Запустите [Redis Server](https://redis.io/docs/getting-started/installation/):
   ```bash
   redis-server
   ```


