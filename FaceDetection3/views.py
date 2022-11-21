from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

def detect():
    import cv2

    face_cascade = cv2.CascadeClassifier(os.path.join(BASE_DIR,'static/haarcascade_frontalface_alt_tree.xml'))
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file = filedialog.askopenfilename(initialdir=os.path.join(BASE_DIR,'static'), title="Select An Image", filetypes=(("jpg files", "*.jpg"), ("jpeg files", "*.jpeg*"), ("png files", "*.png")))
    root.destroy()
    image = cv2.imread(file)
    # image = cv2.imread("/media/hardik/49F9-340F/Final_project/DjangoProjectFinal/static/test_image3.jpg")
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(grayImage)
    
    if len(faces) == 0:
        return 0
    
    else:
        print("Number of faces detected: " + str(faces.shape[0]))
        total_faces = faces.shape[0]
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),5)
    
        cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
        cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
    
        # cv2.imshow('Image with faces',image)
        cv2.imwrite(os.path.join(BASE_DIR,"static/out.jpeg"), image)  
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return total_faces

# Create your views here.
def index(request):
    print('JSR')
    return render(request,'index.html')

def output(request):
    print('done')
    total_faces = detect()
    print(total_faces,'Jai Shri Ram')
    variableMap = {
        'total_faces': total_faces,
        'flag': 1
    }
    return render(request,'index.html',variableMap)
