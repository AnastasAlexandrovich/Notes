# Notes
Инструкция по запуску проекта

1. в файле notes\notes\settings.py найдите данную секцию
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'notes_db',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'db',
        'PORT': '5432'
    }
}
поменяйте пароль для пользователя postgres на тот, который используете

2. перейдите в папку notes/notes
3. выполните команду docker-compose up --build
4. перейдите по ссылке localhost:8000/notes-app/index
