# ToDo App - Django

## Tutorial

1. Create virtual enviroment.

2. Install django.

3. Create django project.

4. Create django app.

5. Create model.

6. Create view and template.

7. Config mysql connection

- Install package:

  `conda install pymysql`

- Add code in **init**.py from main directory

  ```
  import pymysql
  pymysql.install_as_MySQLdb()
  ```

- Edit settings.py

```
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'django_todoapp',
      'USER': 'root',
      'PASSWORD': '123456',
      'HOST': 'localhost',
      'PORT': '3306',
  }
}
```

8. Create and execute migrations

```
python manage.py makemigrations todo
python manage.py migrate todo
```

9. Add test rows (optional)

```
python manage.py shell
```
