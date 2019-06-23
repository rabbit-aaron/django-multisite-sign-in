## Requirements:
* python 3.6 (with venv installed)
* Django 2.2

## How to setup

```bash
cd PROJECT_PATH
python -m venv venv # you might need to use `python3` instead of `python`
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser # follow the prompt to create an user
```

## How to test
I tested this locally using ngrok. You can download it from [here]([https://ngrok.com/download](https://ngrok.com/download)).

Open two (or more) terminal windows
```bash
./ngork http 8000
```
This should then give you something like this:
```
Session Status                online
Session Expires               7 hours, 57 minutes
Update                        update available (version 2.3.30, Ctrl-U to update
Version                       2.3.27
Region                        United States (us)
Web Interface                 http://127.0.0.1:4042
Forwarding                    http://207e5359.ngrok.io -> http://localhost:8000
Forwarding                    https://207e5359.ngrok.io -> http://localhost:8000
```
We then copy all of the domains (in this case `207e5359.ngrok.io`) into our settings.py file.
```python
DOMAINS = [
    '207e5359.ngrok.io',
    # add all of the domains you get from ngrok here
]
```
Now we can run server
```bash
python manage.py runserver
```

Now goto any one of the domains to login using the username you created, then goto any other domains, you'll see that the user would be logged in in those domains too.
