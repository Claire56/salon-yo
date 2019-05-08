# locate_salon
# Salon-Yo 
This is a simple webapp that uses the google api to find latititudes and longtudes of a place then uses the four square api to find a salon given a need. for example a user can say they want to braid hair and are in kampala Uganda. then they will recieve back the nearest salon, addresss and a picture of the salon

### Salon 
Here the users recieve the closest salon based on their needs <br> <br>

<a href="https://github.com/claire56">
    <img alt="graphs" src="/static/graphs.gif" width="900" height="500">
    </a>

## Table of Contents
* [Overview](#Overview)
* [Tech Stack](#Tech-Stack)
* [Setup and installation](#Setup-and-installation)
* [Demo](#Demo)
* [Future Features](#Future-Features)

## Overview
Looking for the right place to go to get a service can sometimes be frastrating if you are new to the area. Salon-Yo, is designed to help users find the closest salon based on their need.

#### Usage
once the user gets to my homepage, they are required to enter their location and what they need, then they will recieve a salon, address and picture of the salon, if one exists depending on need.



## Tech Stack
Data Wrangling: Pandas <br>
Framework: Flask <br>
Backend: Python, SQLAlchemy, PostgreSQL  <br>
Frontend: Javascript , AJAX, JSON , JQuery, Jinja, HTML, CSS, Bootstrap <br>
Libraries: httplib2

## Demo
### Homepage
Here the users provide the required information
### Salon
Here the user recieves back, the name , address and a picture of the salon.

<a href="https://github.com/claire56">
    <img alt="explore" src="/static/explore1.gif" width="800">
    </a>

### None Found
If no salon is found by the app, thee user recieves an apology 

<a href="https://github.com/claire_kimbugwe">
    <img alt="explore" src="/static/explore3.gif" width="800">
    </a>


<br> <br>
### HOMEPAGE <br>
Below is muy landing page <br><br>

<a href="https://github.com/claire56">
    <img alt="explore" src="/static/home.gif" width="800">
    </a>


## Setup and installation
On local machine, go to desired directory. Clone  repository:

$ git clone https://github.com/Claire56/salon-yo <br>
Create a virtual environment in the directory:

$ virtualenv env<br>
Activate virtual environment:<br>

$ source env/bin/activate<br><br>
Install dependencies:<br>
$ pip install -r requirements.txt <br>
Create database:<br><br>


$ python3 server.py <br>
Navigate to localhost:5000 in browser.


## Future Features
* personalise the search
* be able to provide the best 5 saloons in order based on reviews



