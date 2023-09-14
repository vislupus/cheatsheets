`where python`    
`python --version`

`where pip`   
`pip --version`


`mkdir python-project`    
`cd python-project`


`python -m venv venv && source venv/Scripts/activate`   
`python -m venv venv && .\venv\Scripts\activate`

`python -m venv venv`   
`python -m venv ./`

`venv\Scripts\activate`    
`venv\Scripts\activate.bat`

`python -m pip install Django`  
`python -m pip install pyqt6`   
`python -m pip install autopep8` 
python -m pip install numpy
python -m pip install beautifulsoup4
python -m pip install pandas
python -m pip install requests
python -m pip install hvplot jupyterlab matplotlib seaborn numpy
python -m pip install matplotlib

python -m pip install jupyterlab
jupyter-lab

python -m pip install opencv-python
python -m pip install Pillow

python -m pip install -U autopep8
python -m pip install --upgrade pip
python -m pip install --upgrade ipywidgets

python -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116


deactivate
del venv

dir venv

pip list

pip freeze > requirements.txt
pip install -r requirements.txt

python -m pip install pipreqs
pipreqs --encoding utf-8 .\my_tennis_club --force --print

python -m pip install pip-tools
pipreqs .\my_tennis_club --savepath=requirements.in && pip-compile

python -m pip install pigar
pigar gen -f .\my_tennis_club
