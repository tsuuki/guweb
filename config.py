# -*- coding: utf-8 -*-

# app name
app_name = 'tsuki!'

# secret key
secret_key = 'dekubush44'

#hCaptcha settings:
hCaptcha_sitekey = 'changeme'
hCaptcha_secret = 'changeme'

# domain (used for api, avatar, etc)
domain = 'tski.moe'

# mysql credentials
mysql = {
    'db': 'gulag',
    'host': 'localhost',
    'user': 'tsuki',
    'password': 'dekubush44',
}

# path to gulag root (must have leading and following slash)
path_to_gulag = '/home/tsuki/gulag/'

# enable debug (disable when in production to improve performance)
debug = True

# disallowed names (hardcoded banned usernames)
disallowed_names = {
    'cookiezi', 'rrtyui',
    'hvick225', 'qsc20010'
}

# disallowed passwords (hardcoded banned passwords)
disallowed_passwords = {
    'password', 'minilamp'
}

# enable registration
registration = True

# social links (used throughout guweb)
github = 'https://github.com/tsuuki/guweb'
discord_server = 'https://discord.com/invite/7Fk7Dvhf'
youtube = 'https://youtube.com/'
twitter = 'https://twitter.com/'
instagram = 'https://instagram.com/'
