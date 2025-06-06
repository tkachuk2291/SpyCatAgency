# SpyCatAgency

###  Install  and create db
```shell
git clone https://github.com/tkachuk2291/SpyCatAgency.git
``` 
```shell
cd SpyCatAgency
```
```shell
python3 -m venv venv  
``` 
```shell
source venv/bin/activate  
```
```shell
pip install -r requirements.txt  
```
### Setting up Environment Variables
```shell
touch .env  
```
### Example of environment variables
``` 
 .env.sample 
```
**Here you can generate your secret key** 
https://djecrety.ir/ 
``` 
set DJANGO_SECRET_KEY='your_secret_key'
set DATABASE_URL="secret_key" (if you are developer please contact with me i'll give you a key)
```


If use Docker follow commands:

```shell
docker build -t SpyCatAgency . 
```

```shell
docker-compose up
```

```shell
python manage.py migrate  
```
```shell
python manage.py runserver 8001 
```

### Local
http://127.0.0.1:8000/

### SpyCatAgency endpoint 

**SpyCatAgency endpoint**

 "spy-cat": "http://127.0.0.1:8000/system/spy-cat/",
 "breed": "http://127.0.0.1:8000/system/breed/"

** Missions | Target endpoint**
    "mission": "http://127.0.0.1:8000/system-mission/mission/",
    "target": "http://127.0.0.1:8000/system-mission/target/"



When the back end server ready follow a link and configure the front end server:
https://github.com/tkachuk2291/spy-cat-agency-frontend





