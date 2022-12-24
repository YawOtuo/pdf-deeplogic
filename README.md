# pdf-deeplogic


Pdf-Deeplogic is a web application built in django

One uploads a scanned pdf or image to the web app and the resulting page displays the text on the image. The functionality is based on Optical Character Technology(OCR)


## How does it work

Pdf-deeplogic uses a Nanonets model to convert 
images to text.
You may upload pdfs or any image extensions

## How to start the project
```
pip install virtualenv
```
```
virtualenv <name>
```
```
.\<name>\Scripts\activate
```
```
pip install requirements.txt
```

Create a **.env** file in the root folder.
Supply the following details: 
**DB_NAME**, **DB_USER**, **DB_USER** , **DB_HOST**, **DB_PORT**.

You may register or a personal api key on nanogets.com
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```
