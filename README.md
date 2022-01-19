tsuki!'s fork of guweb, taking changes from a lot of different gulag instances and combining them.
also fixes CORS issues for newcomers.

requirements
------

- vps with ubuntu (perferably ubuntu 20.04)
- is not an idiot

setup
------
do not run any of this as root. create a new user `adduser [username]` and give them sudo `adduser [username] sudo`.
```sh
# installs python >=3.9 and the latest version of pip.
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9 python3.9-dev python3.9-distutils && wget https://bootstrap.pypa.io/get-pip.py
python3.9 get-pip.py && rm get-pip.py

# installs mysql and nginx, clones this repository, goes into the guweb directory and initalises oppai.
sudo apt install mysql-server nginx && git clone https://github.com/tsuuki/guweb.git && cd guweb && git submodule init && git submodule update

# install requirements from pip.
python3.9 -m pip install -r ext/requirements.txt

# adds, configures, and symlinks guweb's nginx config to your nginx/sites-enabled.
# obviously, change tski.moe to your domain.
sudo ln -r -s ext/nginx.conf /etc/nginx/sites-enabled/guweb.conf && sudo nano ext/nginx.conf

# reloads guweb's nginx configuration. do this every time you make a change to it.
sudo nginx -s reload

# configure guweb to your liking.
cp ext/config.sample.py config.py & nano config.py

# run guweb.
python3.9 main.py # run directly to access debug features for development! (port 5000)
hypercorn main.py # run this command when in production. (port 8000)
```

directory structure
------

    .
    ├── blueprints   # modular routes such as the API, frontend, or admin Panel.
    ├── ext          # external files from guweb's primary operation.
    ├── objects      # code for representing privileges, global objects, and more.
    ├── static       # code or content that is not modified or processed by guweb itself.
    ├── templates    # HTML that contains content that is rendered after the page has loaded.
        ├── admin    # templated content for the admin panel (/admin).
        ├── settings # templated content for settings (/settings).
        └ ...         # templated content for all of guweb (/).
