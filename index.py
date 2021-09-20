import cv2
import pandas as pd
import numpy as np
import csv
import os

def Q2():

	df = pd.DataFrame(columns = ['StudentID','Surname','Firstname','Code'])
	list = os.listdir('Data/')

	s1 = []
	s3 = []
	s_Sur = []
	s_Fi = []
	for i in range(0,len(list)):
	    s = list[i]
	    j = 0
	    s1.append("")
	    while (s[j] != "_"):
	        s1[i] = s1[i] + s[j]
	        j += 1
	    j+=1
	    s2 = ""
	    for m in range (j,len(s)):
	        if s[m] == "_":
	            j = m + 1
	            break
	        s2 = s2 + s[m]        
	    s3.append("")
	    while (j<len(s)):
	        s3[i] = s3[i] + s[j]
	        j += 1
	    s3[i] = s3[i][0:2]
	        
	    #get Firstname and Surname
	    j = len(s2)-1
	    SurName,FirstName=getName(s2,j)
	    
	    s_Sur.append("")
	    s_Fi.append("")
	    s_Fi[i]=s_Fi[i]+FirstName
	    s_Sur[i] = s_Sur[i]+SurName

	    df.loc[i,'StudentID'] = s1[i]
	    df.loc[i,'Code'] = s3[i]
	    df.loc[i,'Surname'] = s_Sur[i]
	    df.loc[i,'Firstname'] = s_Fi[i]

	df.to_csv('student.csv')

def getName(s2,j):
    SurName=""
    while (s2[j].isupper() == False):
        SurName = s2[j] + SurName
        j -= 1
    SurName = s2[j] + SurName    
    FirstName = ""
    for r in range(j):
        FirstName = FirstName + s2[r]
    return(SurName,FirstName)

def Q3():
	#Choose 2000102_NguyenTruongBao_3A.png
	name = "2000404_NguyenQuangHao_5B.png"
	img = cv2.imread('Data/' + name)
	img = cv2.resize(img, (600, 800))
	img = img[123:213,107:260]
	
	gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	blur_img = cv2.GaussianBlur(gray_img, (5,5),0)
	edge_img = cv2.Canny(blur_img,10,70)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)

	boxes = split_image(thresh)

	for i in range(0,5):
	 	user_answer = None
	 	for j in range(5):
	 		pixels = cv2.countNonZero(boxes[j + i * 5])
	 		if user_answer is None or pixels > user_answer[1]:
	 			user_answer = (j, pixels)
	 			final = j 
	 	ResultOut3(final)

def ResultOut3(j):
    if (j == 0):
        print("A")
    elif (j == 1):
        print("B")
    elif (j == 2):
        print("C")
    elif (j == 3):
        print("D")
    elif (j == 4):
        print("E")   

def Q4():
	name = "2000404_NguyenQuangHao_5B.png"
	img = cv2.imread('Data/' + name)
	img = cv2.resize(img, (600, 800))
	for i in range(0,6):
		cutL(i,img)
	for i in range(0,6):
		cutR(i,img)

def cutR(num,img):
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
        ResultOut4(final)

def cutL(num,img):
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
        ResultOut4(final)

def ResultOut4(j):
    if (j == 0):
        print("A")
    elif (j == 1):
        print("B")
    elif (j == 2):
        print("C")
    elif (j == 3):
        print("D")
    elif (j == 4):
        print("E")   

def Q5_6():
	Q = []
	for i in range(0,60):
		Q.append(0)
	ans = []
	name = "Answer.csv"
	file_ans = pd.read_csv('Answer/' + name)
	
	#Get Answers from file into an array 
	for i in range(0,60):
		ans.append("")
		ans[i] = ans[i] + file_ans.loc[i,'Ans']

	#Create grading.csv file:
	Id = pd.read_csv('student.csv')
	df = pd.DataFrame(columns = ['StudentID','Grading'])
	for i in range(0,len(Id)):
	    df.loc[i,'StudentID']=Id.loc[i,'StudentID']

	path = "Data/"
	dirs = os.listdir(path)

	s = ""
	m = 0
	for file in dirs:
		s = path + "\\" + file
		
		img = cv2.imread(s)
		img = cv2.resize(img,(width,height))
		anst = []
		for i in range(0,6):
			anst.append(cutL5(i,img))
		for i in range(0,6):
			anst.append(cutR5(i,img))

		#Checking Process:
		grade = 0
		for i in range(0,12):
			for j in range(0,5):
				if anst[i][j] == ans[i*5+j]:
					grade+=1
				else :
					Q[i*5+j]+=1
		df.loc[m,'Grading'] = grade
		m += 1
	df.to_csv('grading.csv')

	#Question6:
	Q_s = []
	for i in range(len(Q)):
	    Q_s.append(Q[i])

	Q.sort(reverse=True)
	print("The 3 hardest questions are : ")
	count = 0
	j = 0;
	# print(Q)
	# print(Q_s)

	for i in range(0,3):
		j = 0 
		while j<len(Q_s):
			if Q[i] == Q_s[j]:
				print("Question",j + 1)
				j+=1
				Q_s[j-1] = -1
				break
			else:
				j+=1
    
def cutR5(num,img):
    ans=[]
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
        ans.append(ResultOut5(final))
    return ans

def cutL5(num,img):
    ans = []
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
        ans.append(ResultOut5(final))
    return ans

def ResultOut5(j):
    if (j == 0):
        return "A"
    elif (j == 1):
        return "B"
    elif (j == 2):
        return "C"
    elif (j == 3):
        return "D"
    elif (j == 4):
        return "E"

def Q7():
	df = pd.read_csv('student.csv')
	df['Pass/Fall'] = None
	df2 = pd.read_csv('grading.csv')

	for i in range(len(df)):
		if df2.loc[i,'Grading'] > 25:
			df.loc[i,'Pass/Fall'] = "Pass"
		else:
			df.loc[i,'Pass/Fall'] = "Fall"
	df.to_csv('student.csv')


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

height = 800
width = 600
green = (0 , 255, 0)
red = (0,0,255)
white = (255,255,255)
questions = 5
answers = 5



#Question2:
Q2()

#Question3:
print("Question3 :")
Q3()
print('\n')

#Question4:
print("Question4 :")
Q4()
print('\n')

#Question5 + 6:
Q5_6()
print('\n')

#Question7:
Q7()