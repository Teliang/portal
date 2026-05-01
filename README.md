# portal

## run in docker
```
docker build -t portal .
docker run -p 5000:5000 -v /etc/nginx/conf.d:/etc/nginx/conf.d portal
```

## run in local
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export  NGINX_CONF_PATH=/path/to/NGINX_CONF_PATH
flask run
```
