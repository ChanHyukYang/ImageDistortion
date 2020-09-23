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
k1=-0.00001
k2=0.000000000001
k3=0.0000000000000001
for y in range(0,height+1,1):
    for x in range(0,width+1,1):
        xnorm=x-centerwidth
        ynorm=y-centerheight
        r=(((xnorm))**2+((ynorm))**2)**0.5
        xdist=(xnorm)*(1+(k1*r**2)+(k2*r**4)+(k3*r**6))
        ydist=(ynorm)*(1+(k1*r**2)+(k2*r**4)+(k3*r**6))
        newim[round(ydist)+newheight//2,round(xdist)+newwidth//2]=img[y-1,x-1]
print("half")
cv2.imwrite('civadamtest.jpg',newim)
plt.imshow(newim)
plt.show()

ogim=newim
ogdim=ogim.shape
ogheight = ogdim[0]
ogwidth = ogdim[1]
ogcenterheight=ogheight//2
ogcenterwidth=ogwidth//2
newnewim = np.zeros(((ogheight*4),ogwidth*4,3), np.uint8)
newnewheight = ogheight*4
newnewwidth = ogwidth*4
nk1=-k1
nk2=(3*k1**2)-k2
nk3=(-12*k1**2)+8*k1*k2-k3
# for y in range(0,ogheight+1,1):
#     for x in range(0,ogwidth+1,1):
#         xnorm=x-ogcenterwidth
#         ynorm=y-ogcenterheight
#         r=(((xnorm))**2+((ynorm))**2)**0.5
#         xdist=(xnorm)*(1+(nk1*r**2)+(nk2*r**4)+(nk3*r**6))
#         ydist=(ynorm)*(1+(nk1*r**2)+(nk2*r**4)+(nk3*r**6))
#         try:
#             newnewim[round(ydist)+newnewheight//2,round(xdist)+newnewwidth//2]=ogim[y-1,x-1]
#         except:
#             print("oof")
#for y in range(round(newnewheight*0.4),round(newnewheight*0.65),1): #This part is the fix for empty pixels
#    for x in range(round(newnewwidth*0.4),round(newnewwidth*0.6),1):
#        if np.all(newnewim[y,x]==[0,0,0]):
#            newnewim[y,x]=(newnewim[y-1][x-1]//8)+(newnewim[y-1][x]//8)+(newnewim[y-1][x+1]//8)+(newnewim[y][x-1]//8)+(newnewim[y][x+1]//8)+(newnewim[y+1][x-1]//8)+(newnewim[y+1][x]//8)+(newnewim[y+1][x+1]//8)
cv2.imwrite('danielwow.jpg',newnewim)
plt.imshow(newnewim)
plt.show()
#         # ydist=(ynorm)*(1+(k1*r**2)+(k2*r**4)+(k3*r**6))
#         # xdist=(xnorm)*(1+(k1*r**2)+(k2*r**4)+(k3*r**6))
#         # r=(((xnorm))**2+((ynorm))**2)**0.5
#         # ynorm=y-ogcenterheight
#         # xnorm=x-ogcenterwidth
#         # newim[round(ydist)+400,round(xdist)+400]=img[y-1,x-1]

# print('Done!')
