# Image-Search-from-Database

## Internship Report and Final Presentation

  - [:point_right: Internship Report](https://github.com/kampaitees/Web-App-for-Image-Search/blob/master/KSP%20Internship%20Report.pdf)
  - [:point_right: Final Presentation](https://github.com/kampaitees/Web-App-for-Image-Search/blob/master/KSP%20Internship%20ppt.pdf)

<p align="center">
  <img src = "https://github.com/kampaitees/Web-App-for-Image-Search/blob/master/ksp/media/2019-07-13%20(6).png"/>
  <img src = "https://github.com/kampaitees/Web-App-for-Image-Search/blob/master/ksp/media/2019-07-13%20(8).png"/>
  <img src = "https://github.com/kampaitees/Web-App-for-Image-Search/blob/master/ksp/media/2019-07-13%20(10).png"/>
</p>

This project is a website which is used to do image search from the database. It takes in an image and name of image
as an input and asks for number of similar image you want to see as output and after clicking on "Upload" option it will
show the similar images as output.

## Demo

### Input Image
<p align="center">
  <img src = "https://github.com/kampaitees/Web-App-for-Image-Search/blob/master/ksp/media/15.jpg"/>
</p>

### Output
<p align="center">
  <img src = "https://github.com/kampaitees/Web-App-for-Image-Search/blob/master/ksp/media/2019-07-20%20(2).png"/>
</p>

## Demo Video
[:point_right: Watch it here](https://drive.google.com/open?id=1iw-bVxwMIuGMh9eGh7p7fQYo-XU_Esr0)

### Motivation
This website I had created as this was my Internship task which I was doing in Bengaluru at KSP computer wing and working
under IISC professor Mr. Ambedkar. Task was to create a website to do criminal image search from database, thereby saving
there time instead of searching manually.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
See deployment for notes on how to deploy the project on a live system.

## Prerequisites

### What things you need to install the software and how to install them

#### Following are the dependencies of python which you have to install in your system
 ``` 
  - python 3.6.8 
  - python pip 
 ```
#### After installing python and pip you have to just write  
 
“`pip install 'below library names'`” 
 
#### To install below dependencies
 ```
  - Django==2.2.2 
  - djangorestframework==3.9.4 
  - Keras==2.2.4 
  - Keras-Applications==1.0.8
  - Keras-Preprocessing==1.1.0 
  - numpy==1.16.1 
  - opencv-contrib-python==3.2.0.7 
  - opencv-python==3.1.0.5 
  - Pillow==6.0.0 
  - psycopg2==2.8.3 
  - requests==2.22.0 
  - scipy==1.3.0 
  - tensorflow-estimator==1.13.0 
  - tensorflow==1.10.0 
  - termcolor==1.1.0 
  - urllib3==1.25.3 
  - virtualenv==16.6.1 
 ```
 
#### For the following below dependencies you have download them separately 
```
  - cmake==3.14.4 
  - dlib==19.17.0 
  - Microsoft Visual Studio code(For running the code you can use your own editor if you want)
  - Postgresql(For database purpose, storing images, 128d encodings and name of images
```

 ## Deployment
 I tried to deploy the website on Heroku platform but as this project includes dlib library which requires cmake to be installed
 so I'm getting errors while installing the library so I'm not able to deploy the website till now.
 
 ## Built With
 
  - [Django](https://www.djangoproject.com/) - Framework used
  - [Facenet.h5](https://drive.google.com/drive/folders/1pwQ3H4aJ8a6yyJHZkTwtjcL4wYWQb7bn) - Model used for predicting encodings
  - [Dlib model](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) - 68 Landmark Predictor
  - [Haarcascades](https://github.com/anaustinbeing/haar-cascade-files) - For face detection and then face extraction
  - [Open Cv](https://opencv.org/) - Image processing
  - [Keras](https://keras.io/) - Loading model and embedding prediction
  - [Numpy](https://numpy.org/) - For mathematical operation
  - [Pillow](https://pypi.org/project/Pillow/) - For opening images
  - [Dlib](http://dlib.net/) - For facial alignment
  - [Postgresql](https://www.postgresql.org/) - Database handling

### Folder structure

```
.
└── KSP
    ├── __pycache__
    ├── ksp
    │   ├── __pycache__
    │   └── __init__.py
    |   └── settings.py
    |   └── urls.py
    |   └──wsgi.py
    ├── models
    |   └── shape_predictor_68_face_landmarks.dat
    |   └── facenet_keras.h5
    |   └── haarcascade_frontalface_default.xml
    ├── pages
    │   ├── __pycache__
    │   └── migrations
    |       ├── __pycache__
    |       └── ...
    │   └── _init__.py
    │   └── admin.py
    │   └── apps.py
    │   └── forms.py
    │   └── models.py
    │   └── tests.py
    │   └── urls.py
    │   └── views.py
    |
    ├── media
    │   ├── search
    |       └── ...
    │   └── database
    |       └── ... 
    │   └── video_diamond.mp4
    │   └── video_pink.mp4
    │   └── video_round.mp4
    |
    ├── static
    │   ├── css
    │   └── fonts
    │   └── img
    │   └── js
    │   └── scss
    |
    ├── templates
    │	├── about.html
    | └── blog-home.html
    │	└── blog-single.html
    │ └── contact.html
    │ └── home.html
    │ └── res.html
    │ └── search_image.html
    │ └── team.html
    │ └── upload_database.html
    |
    └── manage.py
```

## Run

#### After downloading all the dependencies you have to open the folder in VS code and run the following commands on the terminal:- 
 ```
   1. python manage.py makemigrations 
   2. python manage.py sqlmigrate pages 0001 
   3. python manage.py migrate 
   4. python manage.py runserver
 ```
 
## Knowledge Transfer Report

[:point_right: More Details here](https://github.com/kampaitees/Web-App-for-Image-Search/blob/master/KSP%20Knowledge%20Transfer.pdf)

## Author
  - [Rishi Sharma](https://github.com/kampaitees)

See also the other [contributor](https://github.com/Vampboy) who helped me in this project.

## License
  
  Apache  © [Rishi Sharma](https://github.com/kampaitees)
