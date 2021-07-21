import numpy as np
import matplotlib.pyplot as plt
import random as rd

T = 1.5               # factor kT/J
n = 150               # número de spines
n_steps = int(2e7)    # número de pasos de MC
n_block = n_steps/1000

directory = "C:\Users\renec\Downloads\isi\carpeta"    # (frames) modificar el directorio
                                             # y que sea una carpeta vacía                                              
pathIn  = directory + '/'
pathOut = "C:\Users\renec\Downloads\isi"  # (video) modificar el directorio

s = np.zeros((n,n))  # matriz de spines
l = 0
m = 0

for i in range (n):  # se llena de 1 y -1 la matriz de spines aleatoriamente
    for j in range (n):
        s[i,j] = (-1)**(rd.randint(1, 2))

file_name = "{:03d}_ising.jpg"

# Inicia el ciclo principal de modelo de Ising
for k in range (n_steps):
    
    i = rd.randint(1, n-1)
    j = rd.randint(1, n-1)
    
    if (i == 0):
        if (j == 0):
            E = -s[i,j] * (s[i+1,j] + s[i,j+1])
        else:
            E = -s[i,j] * (s[i+1,j] + s[i,j+1] + s[i,j-1])
    elif (i == n-1):
        if (j == n-1):
            E = -s[i,j] * (s[i-1,j] + s[i,j-1])
        else:
            E = -s[i,j] * (s[i-1,j] + s[i,j+1] + s[i,j-1])
            
    elif (j == 0):
        E = -s[i,j] * (s[i+1,j] + s[i,j+1] + s[i-1,j])
    elif (j == n-1):
        E = -s[i,j] * (s[i+1,j] + s[i-1,j] + s[i,j-1])
        
    else:            
        E = -s[i,j] * (s[i+1,j] + s[i-1,j] + s[i,j+1] + s[i,j-1])
    
    if (E > 0):
        s[i,j] = -s[i,j]
    else:
        r = rd.random()
        if (r < np.exp(2*E/T)):
            s[i,j] = -s[i,j]
            
    if (k % n_block == 0):
        
        plt.imshow(s, cmap="gist_gray")
        plt.title("MC step:"+str(k)+", kT/J ="+str(T)+", #s = "+str(n*n),fontsize=10)
        #plt.savefig(directory + '/' + file_name.format(l)) # descomentar para video
        l = l + 1                
        if (l % 100 == 0):
            if(m < 5):
                n_block = 2*n_block
                print(k)
                m = m + 1
        plt.show()
              
print(l,k)

import cv2
import os
from os.path import isfile, join

def convertToVideo(pathIn, pathOut, fps, time):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #files.sort(key=lambda x: int((x.split(".")[0]).split(" ")[1]))#REORDENA FRAMES
    for i in range(len(files)):
        
        filename = pathIn+files[i]
        print(filename)
        img=cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)

        for k in range (time):
            frame_array.append(img)

    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    
    for i in range(len(frame_array)):        
        out.write(frame_array[i])
        
    out.release()
    print("TASK COMPLETED")

#EJECUTAMOS  FUNCIÓN. (Descomentar para exportar video)
fps = 60
time = 5
#convertToVideo(pathIn, pathOut, fps, time)
