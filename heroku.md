|-main    
|--site - може и без него     
|---templates    
|----index.html    
|---input.py    
|--virtual    

cd C:\Users\Nikola\Desktop\flask_csv_to_geojson

python -m venv virtual

virtual\Scripts\pip install flask
virtual\Scripts\pip install pathlib
virtual\Scripts\python -m pip install --upgrade pip
virtual\Scripts\pip install gunicorn
virtual\Scripts\pip install pandas
virtual\Scripts\pip install beautifulsoup4
virtual\Scripts\pip install requests
virtual\Scripts\pip install pymongo[srv]


cd C:\Users\Nikola\Desktop\flask_csv_to_geojson
virtual\Scripts\python site\input.py

cd C:\Users\Nikola\Desktop\flask_csv_to_geojson\site

..\virtual\Scripts\pip freeze
..\virtual\Scripts\pip freeze > requirements.txt

remove winkerberos

Create file Procfile
web: gunicorn input:app

//////////////////////////////////////////////////

heroku login

git init

git add .

git commit -m "first commit"

heroku git:remote --app wikicoordinates

git push heroku master

heroku open
heroku logs --tail

heroku config:add TZ="EET"
