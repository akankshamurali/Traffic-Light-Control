import cv2
import matplotlib.pyplot as plt
import time
from colorama import Fore
img = cv2.imread('emptyroad.jpeg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
A=cv2.resize(edges,(20,10))
diff=cv2.subtract(A,A)
cv2.destroyAllWindows()

img_input= str(input("enter the name of the image file: "))
img1 = cv2.imread(img_input)
img_gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img_blur1 = cv2.GaussianBlur(img_gray1, (3,3), 0)
edges1 = cv2.Canny(image=img_blur1, threshold1=100, threshold2=200) # Canny Edge Detection
B=cv2.resize(edges1,(20,10))
histogram1 = cv2.calcHist([B], [0],None, [256], [0, 256])
cv2.destroyAllWindows()
difference=cv2.subtract(B,A)

img_input1= str(input("enter the name of the second image file: "))
img2 = cv2.imread(img_input1)
img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img_blur2 = cv2.GaussianBlur(img_gray2, (3,3), 0)
edges2 = cv2.Canny(image=img_blur2, threshold1=100, threshold2=200) # Canny Edge Detection
C=cv2.resize(edges2,(20,10))
histogram2 = cv2.calcHist([C], [0],None, [256], [0, 256])
cv2.destroyAllWindows()
difference1=cv2.subtract(C,A)

img_input2= str(input("enter the name of the third image file: "))
img3 = cv2.imread(img_input2)
img_gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
img_blur3 = cv2.GaussianBlur(img_gray3, (3,3), 0)
edges3 = cv2.Canny(image=img_blur3, threshold1=100, threshold2=200) # Canny Edge Detection
D=cv2.resize(edges3,(20,10))
histogram3 = cv2.calcHist([D], [0],None, [256], [0, 256])
cv2.destroyAllWindows()
difference2=cv2.subtract(D,A)

fig = plt.figure(figsize=(20, 10))
# setting values to rows and column variables
rows = 2
columns = 2
fig.add_subplot(rows, columns, 1)
plt.imshow(edges)
plt.title("lane1")
fig.add_subplot(rows, columns, 2)
plt.imshow(edges1)
plt.title("lane2")
fig.add_subplot(rows, columns, 3)
plt.imshow(edges2)
plt.title("lane3")
fig.add_subplot(rows, columns, 4)
plt.imshow(edges3)
plt.title("lane4")
plt.show()

print('lane1',diff)
result0 = [sum(e for e in lst if e > 0) for lst in diff]
f=0
for i in range(0,len(result0)):
    f=f+result0[i]
print('sum of lane1',f)

print('lane2',difference)
result = [sum(e for e in lst if e > 0) for lst in difference]
s=0
for i in range(0,len(result)):
    s=s+result[i]
print('sum of lane2',s)
print('lane3',difference1)
result1 = [sum(e1 for e1 in lst1 if e1 > 0) for lst1 in difference1]
v=0
for i in range(0,len(result1)):
    v=v+result1[i]
print('sum of lane3',v)

print('lane4',difference2)
result2 = [sum(e for e in lst if e > 0) for lst in difference2]
w=0
for i in range(0,len(result2)):
    w=w+result2[i]
print('sum of lane4',w)

stop_light_1 =f
stop_light_2=s
stop_light_3=v
stop_light_4=w
while stop_light_1 < 1000:
    if (stop_light_1>= 0 and stop_light_1 < 100) and (stop_light_2>=600 and stop_light_2<675) and (stop_light_3>=675 and stop_light_3<750) and (stop_light_4>=800 and stop_light_4<1000):
        print(Fore.RED+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.YELLOW+"lane3" )
        print(Fore.GREEN+"lane4")
        time.sleep(40)
        print(Fore.RED+"lane1") 
        print(Fore.YELLOW+"lane2")
        print(Fore.GREEN+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(30)
        print(Fore.YELLOW+"lane1") 
        print(Fore.GREEN+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(20)  
        print(Fore.GREEN+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(10) 
    elif (stop_light_1>=0 and stop_light_1 <100) and (stop_light_2>=800 and stop_light_2<1000) and (stop_light_3>=600 and stop_light_3<675) and (stop_light_4>=675 and stop_light_4<750):
        print(Fore.RED+"lane1") 
        print(Fore.GREEN+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.YELLOW+"lane4")
        time.sleep(40)
        print(Fore.RED+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.YELLOW+"lane3" )
        print(Fore.GREEN+"lane4")
        time.sleep(30)
        print(Fore.YELLOW+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.GREEN+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(20)
        print(Fore.GREEN+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(10)  
    elif (stop_light_1>= 0 and stop_light_1 < 100) and (stop_light_2>=675 and stop_light_2<750) and (stop_light_3>=600 and stop_light_3<675) and (stop_light_4>=800 and stop_light_4<1000):
        print(Fore.RED+"lane1") 
        print(Fore.YELLOW+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.GREEN+"lane4")
        time.sleep(40)
        print(Fore.RED+"lane1") 
        print(Fore.GREEN+"lane2")
        print(Fore.YELLOW+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(30)
        print(Fore.YELLOW+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.GREEN+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(20)
        print(Fore.GREEN+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(10)          
    elif (stop_light_1>= 0 and stop_light_1 < 100) and (stop_light_2>=800 and stop_light_2<1000) and (stop_light_3>=675 and stop_light_3<750) and (stop_light_4>=600 and stop_light_4<675):
        print(Fore.RED+"lane1") 
        print(Fore.GREEN+"lane2")
        print(Fore.YELLOW+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(40)
        print('Red Light:lane 1\nRed light:lane2\nGreen light:lane 3\nRed light:lane 4')
        print(Fore.RED+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.GREEN+"lane3" )
        print(Fore.YELLOW+"lane4")
        time.sleep(30)
        print(Fore.YELLOW+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.GREEN+"lane4")
        time.sleep(20)
        print(Fore.GREEN+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(10) 
    elif (stop_light_1>= 0 and stop_light_1 < 100) and (stop_light_2>=600 and stop_light_2<675) and (stop_light_3>=800 and stop_light_3<1000) and (stop_light_4>=675 and stop_light_4<750):
        print(Fore.RED+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.GREEN+"lane3" )
        print(Fore.YELLOW+"lane4")
        time.sleep(40)
        print(Fore.RED+"lane1") 
        print(Fore.YELLOW+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.GREEN+"lane4")
        time.sleep(30)
        print(Fore.YELLOW+"lane1") 
        print(Fore.GREEN+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(20)
        print(Fore.GREEN+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(10)  
    elif (stop_light_1>= 0 and stop_light_1 < 100) and (stop_light_2>=675 and stop_light_2<750) and (stop_light_3>=800 and stop_light_3<1000) and (stop_light_4>=600 and stop_light_4<675):
        print(Fore.RED+"lane1") 
        print(Fore.YELLOW+"lane2")
        print(Fore.GREEN+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(40)
        print(Fore.RED+"lane1") 
        print(Fore.GREEN+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.YELLOW+"lane4")
        time.sleep(30)
        print(Fore.YELLOW+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.GREEN+"lane4")
        time.sleep(20)
        print(Fore.GREEN+"lane1") 
        print(Fore.RED+"lane2")
        print(Fore.RED+"lane3" )
        print(Fore.RED+"lane4")
        time.sleep(10)      
    break

