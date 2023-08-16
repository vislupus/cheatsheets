`django-admin --version`   
`django-admin startproject <project_name>`   
`cd .\<project_name>`   
`cd ..\`   
python manage.py runserver
python manage.py startapp <app_name>
python manage.py migrate
python manage.py makemigrations <app_name>
python manage.py sqlmigrate members 0001

python manage.py shell

```python
from projects.models import Project

p1 = Project(
  title='My First Project',
  description='A web development project.',
  technology='Django',
  image='img/project1.png'
)
p1.save()

p2 = Project(
    title='My Second Project',
    description='Another web development project.',
    technology='Flask',
    image='img/project2.png'
)
p2.save()

p3 = Project(
    title='My Third Project',
    description='A final development project.',
    technology='Django',
    image='img/project3.png'
)
p3.save()
```

python manage.py createsuperuser

python manage.py collectstatic
