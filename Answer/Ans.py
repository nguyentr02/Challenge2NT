import cv2
import pandas as pd
import numpy as np



def split_image(image):
    r = len(image) // questions * questions 
    c = len(image[0]) // answers * answers
    image = image[:r, :c]
    rows = np.vsplit(image, questions)
    boxes = []
    for row in rows:
        cols = np.hsplit(row, answers)
        for box in cols:
            boxes.append(box)

    return boxes

def ResultOut(j): 
    if (j == 0):
        return("A")
    elif (j == 1):
        return("B")
    elif (j == 2):
        return("C")
    elif (j == 3):
        return("D")
    elif (j == 4):
        return("E")   


height = 800
width = 600
green = (0 , 255, 0)
red = (0,0,255)
white = (255,255,255)
questions = 5
answers = 5
correct_ans = [0,2,3,3,1]

s1=[]
s = ""
df = pd.DataFrame(columns = ['Ans'])
name = "5B.png"
img = cv2.imread('Answer/' + name)
# img = cv2.imread("C:\\Users\\steven\\Desktop\\CODE\\Challenge2\\Answer\\5B.png")
# cv2.imshow('',img)
# cv2.waitKey()
img = cv2.resize(img, (width, height))

#LeftSide
for num in range(0,6):
    roi = img[(123+(num*108)):(213+(num*108)),107:260]
    gray_img = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (5,5),0)
    edge_img = cv2.Canny(blur_img,10,70)

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)

    boxes = split_image(thresh)

    for i in range(0, questions):
        user_answer = None
    
        for j in range(answers):
            pixels = cv2.countNonZero(boxes[j + i * 5])
            if user_answer is None or pixels > user_answer[1]:
                user_answer = (j, pixels)
                final = j 
        s = ResultOut(final)
        s1.insert(len(s1),s)


s=""
for i in range(0,6):
    roi = img[(123+(num*108)):(213+(num*108)),378:525]
    gray_img = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (5,5),0)
    edge_img = cv2.Canny(blur_img,10,70)

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)

    boxes = split_image(thresh)

    for i in range(0, questions):
        user_answer = None
    
        for j in range(answers):
            pixels = cv2.countNonZero(boxes[j + i * 5])
            if user_answer is None or pixels > user_answer[1]:
                user_answer = (j, pixels)
                final = j 
        s = ResultOut(final)
        s1.insert(len(s1),s)

for i in range(0,len(s1)):
    #In here, I count from 1 to 60 instead of 0 to 59 as normal. 
    #This is because it would be probly easier to grade 
    df.loc[i+1,'Ans'] = s1[i]

df.to_csv('Answer.csv')

