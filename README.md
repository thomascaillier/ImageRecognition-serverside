# Image Recognition
**Objective** : send an image from mobile (android) to a server which automatically detect any brand logo, retrieve and send back information about the detected logo.

**Context** : school project from IMT Lille-Douai,  class INGED2

**Collaborators** : El Yazid Benbella & Thomas Caillier

# Server-side application
This repository is only dedicated to the server-side part of the project

## Technology
**Language** : Python 3

**Framework** : Django 2

**SGBD** : SQLite 3	

## Quick start on Windows
### Prerequires
 - Python 3.4, 3.5, 3.6 version 64 bits
 - git
 - pip

### 1) Clone the project
    git clone https://github.com/thomascaillier/ImageRecognition-serverside
### 2) Virtual environment
    cd ImageRecognition-serverside
    python -m venv venv
	venv\Scripts\activate
### 3) Install dependencies
	pip install -r requirements.txt
### 4) Prepare DB
    python manage.py migrate
To visualize database, we recommend [DB Browser for SQLite](https://sqlitebrowser.org/)
### 5) Run server
    python manage.py runserver
