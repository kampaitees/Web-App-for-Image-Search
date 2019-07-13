from PIL import Image
from io import BytesIO
from scipy import spatial
from ksp.settings import BASE_DIR
from keras.models import load_model
from .models import Database, Search
import os, cv2, dlib, requests, numpy as np
from django.shortcuts import render, redirect
from .forms import Search_form, Database_form
from django.http import HttpResponse, HttpResponseRedirect
media_path_search = os.path.join(BASE_DIR, 'media/search')
media_path_database = os.path.join(BASE_DIR, 'media/database')


detector = dlib.get_frontal_face_detector()
model = load_model(BASE_DIR+'/models/facenet_keras.h5')
print(model)
model._make_predict_function()
predictor = dlib.shape_predictor(BASE_DIR+'/models/shape_predictor_68_face_landmarks.dat')
face_cascade = cv2.CascadeClassifier(BASE_DIR+'/models/haarcascade_frontalface_default.xml')

def res(request):
    return render(request, 'res.html')

def home(request):
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def blogs(request):
    return render(request, 'blog-home.html')

def contact(request):
    return render(request, 'contact.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def element(request):
    return render(request, 'elements.html')


def clean_up_search(request):
    
    Search.objects.all().delete()

    for img in os.listdir(media_path_search):
        os.remove(os.path.join(media_path_search, img))

    return HttpResponseRedirect('/')

def clean_up_database(request):
    
    Database.objects.all().delete()
    
    for img in os.listdir(media_path_database):
        os.remove(os.path.join(media_path_database, img))

    return HttpResponseRedirect('/')


def upload_to_database(request):
    
    if request.method == 'POST':

        img = Image.open(request.FILES.get('criminal_img'))
        encodings = extract_face_and_get_embedding(np.array(img), 160)

        instance = Database.objects.create(
                                            criminal_img = request.FILES["criminal_img"], 
                                            criminal_name = request.POST["criminal_name"],
                                            encodings = list(encodings.astype('float'))
        )

        instance.save()
        return HttpResponseRedirect('upload-database')

    else:
        form = Database_form()
        
    return render(request, 'upload_database.html', {'form': form})

def extract_face_and_get_embedding(img, required_size):
       
        dets = detector(img, 3)
        num_faces = len(dets)

        if num_faces == 0:

            rects = face_cascade.detectMultiScale(img, minNeighbors = 5)
            if len(rects) != 0:
                
                for x, y, w, h in rects:
                   
                    roi_face = img[y-5:y+h+10, x-5:x+w+10]
                    image = np.array(roi_face)
                    image = cv2.resize(image, (required_size, required_size), interpolation = cv2.INTER_AREA)
                    face_pixels = image.astype('float32')
                    mean, std = face_pixels.mean(), face_pixels.std()
                    face_pixels = (face_pixels - mean) / std
                    samples = np.expand_dims(face_pixels, axis=0)

                    yhat = model.predict(samples)
                    return yhat[0]
                    
            elif len(rects) == 0:
                print('Sorry, there were no faces found in the image')
                
            else:
                print('More than one number of faces found in the image')

        elif num_faces == 1:

            faces = dlib.full_object_detections()
            
            for detection in dets:
                faces.append(predictor(img, detection))

            image = dlib.get_face_chips(img, faces, size = required_size, padding = 0.2)

            image = np.array(image)
            
            image = image.reshape(required_size, required_size, 3)
            face_pixels = image.astype('float32')

            mean, std = face_pixels.mean(), face_pixels.std()
            face_pixels = (face_pixels - mean) / std
            samples = np.expand_dims(face_pixels, axis=0)
            print('Computation going on.....')
            yhat = model.predict(samples)

            return yhat[0]
        
        else:
            
            print('More than one number of faces found in the image')





def prediction(img, num_of_img):
    
        similarity_distance, list_of_similarity, min_dist = {}, [], 10
        encoding_test_image = extract_face_and_get_embedding(img, 160)
        
        if encoding_test_image is None:
                
                list_of_similarity.append((1, None))
                return None, list_of_similarity
        else:

            filenames_from_db = Database.objects.all()

            for i in range(len(filenames_from_db)):
                    
                    database_encodings = filenames_from_db[i].encodings

                    dist = spatial.distance.cosine(database_encodings, encoding_test_image)
                    similarity_distance[filenames_from_db[i].criminal_name] = dist
                    list_of_similarity.append((dist, filenames_from_db[i].criminal_img))

                    if dist < min_dist:
                        min_dist = dist
                
            list_of_images = []
            if len(list_of_similarity) >= 2 :

                list_of_similarity.sort(key = lambda x : x[0])

                for i in range(num_of_img):
                    list_of_images.append(list_of_similarity[i][1])

        return list_of_images

def search_image(request):
    
        if request.method == 'POST':
            
            num_of_img = int(request.POST["num"])
            form = Search_form(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                img = Image.open(request.FILES.get('criminal_img'))
                list_of_images = prediction(np.array(img), num_of_img)
                
                return render(request, 'res.html', {'list_of_images' : list_of_images})
        else:
            form = Search_form()

        return render(request, 'search_image.html', {'form': form})