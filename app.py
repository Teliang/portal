import os
# save this as app.py
from flask import Flask, render_template, render_template

app = Flask(__name__)

@app.route("/")
def index():
    path = os.environ.get('NGINX_CONF_PATH','/etc/nginx/conf.d')
    files = os.listdir(path)
    # Filtering only the files.
    files = [path + '/' + f for f in files if os.path.isfile(path+'/'+f)]
    print(*files, sep="\n")

    domains = [];
    for conf_path in files:
        with open(conf_path, 'r') as file:
            for line in file:
                if line.startswith('#'):
                    continue
                if 'server_name' in line:
                    line = line.strip()
                    domain = line.split()[1].rstrip(";")
                    domains.append(domain)
    domains.sort()
    return render_template("index.html", domains=domains)
