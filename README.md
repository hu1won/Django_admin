## How to use it

<br />

> Install the package via `PIP` 
```bash
$ pip install django-admin-black
```

<br />

* Add 'admin_black' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be before 'django.contrib.admin'):

```python
    INSTALLED_APPS = (
        ...
        'admin_black.apps.AdminBlackConfig',
        'django.contrib.admin',
    )
```

* Make sure ``django.template.context_processors.request`` context processor is enabled in settings.py (Django 1.8+ way):

```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.template.context_processors.request',
                    ...
                ],
            },
        },
    ]
```

* Create database tables:

```bash
$ python manage.py migrate admin_black
```

* Collect static if you are in production environment:

```bash
$ python manage.py collectstatic
```

* Clear your browser cache
