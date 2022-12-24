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

The app is now functional.
1. Upload a file to be converted to text
2. Upload as many as possible


### MODELS
```Text```
The text model has three columns: the text itself, the filename and the filepath

# Project Report
I used the inbuilt django authentication system for authentication.<br/>
I created views for the home page, authentication pages, list pages, url pages.<br/>
I created url routes to map these views to their templates.<br/>
I used a nanonet model to extract data from the pdf files.

# Challenges Faced
I faced a huge challenge in how to work with the pdf files.
I tried several packages like ```pyPdf2``` but couldn't produce the expected result.
I also attemped to use ```pytesseract ``` but was facing a challenge as to how i would be able to make it work on a remote pc.
<br/>
After several hours of research, i came across a website/company known as **NANONETS** - a platform to automate manual data entry using AI.
<br/>
I used a nanonet model to be able to accomplish the task effectively. Thus, it can be used on remote pcs also.

<br/>

I also faced a challenge as to how to store and retrieve the pdf files uploaded.
 
<br/>

# What i have learnt from the project
I have learn a few important points
1. I have learnt how to use django file storage to store uploaded files.
2. I have learnt to use new packages like pypdf2.
3. I have learnt how important artificial intelligence models are to simplifying problems i will face.
4. I have strengthened my knowledge and skills in using the django framework.
5. I have also learnt to use a virtualenv better.





