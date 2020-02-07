# WIKIO DJANGO VERSION

This is a very, very, very amateur version of Wikio APP, originally built with Express.JS, React and MongoDB that can be found in:
</br>
https://pure-ocean-87159.herokuapp.com/
</br>
I built this project just to learn the basics of Django. So there are zero concerns of production environments and all aditional security and performance details of a production application should have.
</br>

# CONFIGURATION INSTRUCTIONS

Once it uses Django and SQLite, you need to have Python, Pip and Sqlite installed in your machine.

# Python

```
sudo apt-get install python
```

# PIP

```
sudo apt-get install python3-pip
```

# SQLite Browser

```
sudo apt-get install sqlitebrowser
```

</br>
Now follow these steps:
<ul>
  <li>Clone this repo into a new directory and navigate to the root folder</li>
  <li>Open a terminal (in root) and run: <strong>pip install -r requirements.txt</strong></li>
  <li>Wait all dependencies to be installed.</li>
  <li>Still in your terminal run: <strong>python3 manage.py migrate</strong></li>
  <li>And now: <strong>python3 manage.py runserver</strong></li>
  <li>We are done.</li>
</ul>

# USAGE

You can add a admin user to the app by running the command:

```
python3 manage.py createsuperuser
```

Fill the username and password.

Now you can just access the admin panel in <strong>localhost/admin</strong> and add Movies and Genres.

# API

This project exposes a Movies endpoint accessible via <strong>localhost/api/movies</strong>
