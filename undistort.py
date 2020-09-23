import cv2
import numpy as np 
img = cv2.imread('civ.jpg')
import matplotlib.pyplot as plt
print(img)
dimensions=img.shape
height = dimensions[0]
width = dimensions[1]
centerheight=height//2
centerwidth=width//2
newim = np.zeros((round(height*2),width*2,3), np.uint8)
newheight = round(height*2)
newwidth = round(width*2)
k1=-0.00000000001
k2=0.0000000000001
k3=0.00000000000000001
for y in range(0,height+1,1):
    for x in range(0,width+1,1):
        xnorm=x-centerwidth
        ynorm=y-centerheight
        r=(((xnorm))**2+((ynorm))**2)**0.5
        xdist=(xnorm)*(1+(k1*r**2)+(k2*r**4)+(k3*r**6))
        ydist=(ynorm)*(1+(k1*r**2)+(k2*r**4)+(k3*r**6))
        try:
            newim[round(ydist)+newheight//2,round(xdist)+newwidth//2]=img[y-1,x-1]
        except:
            print("oof")
print("half")
# for y in range(0,newheight-1,1): #This part is the fix for empty pixels
#     for x in range(0,newwidth-1,1):
#         if np.all(newim[y,x]==[0,0,0]):
#             newim[y,x]=(newim[y-1][x-1]//8)+(newim[y-1][x]//8)+(newim[y-1][x+1]//8)+(newim[y][x-1]//8)+(newim[y][x+1]//8)+(newim[y+1][x-1]//8)+(newim[y+1][x]//8)+(newim[y+1][x+1]//8)
cv2.imwrite('civadamtest.jpg',newim)
plt.imshow(newim)
plt.show()