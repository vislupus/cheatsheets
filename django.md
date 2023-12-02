`django-admin --version`   

`django-admin startproject <project_name>`  
`django-admin startproject <project_name> .`  

`python manage.py startapp <app_name>`

`cd .\<project_name>`   
`cd ..\`   

`python manage.py runserver`

`python manage.py makemigrations <app_name>` - make migrations based on the changes that you made to the models     
`python manage.py migrate` - apply the changes from the models to the database     
`python manage.py sqlmigrate <app_name> 0001` - view the generated SQL based on the model     
`python manage.py showmigrations` - list all migrations and their status in the project    

`python manage.py shell`

```python
from projects.models import Project

p = Project(
  title='My First Project',
  description='A web development project.',
  technology='Django',
  image='img/project1.png'
)
p.save()

```

`python manage.py createsuperuser`    

`python manage.py collectstatic`



https://docs.djangoproject.com/en/4.2/topics/http/urls/     
https://docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters     
