# Amir Shahbazi - 9812033

from PIL import Image
import numpy as np
import IPython.display

image_name = input()
image = Image.open(image_name).convert("L")
w, h = image.size
print(f'The Number of Elements is: {w*h}')
print('\n')
 
matrix = np.array(image)
m = len(matrix[:,0])
n = len(matrix[0,:])

U, S, V = np.linalg.svd(matrix)
U = U[:,:n]

max_k = int(input('Enter the maximum value of k: '))

for k in range(1,max_k+1):
    sec_mat = S[0]*np.matmul(U[:,0].reshape((m,1)),V[0,:].reshape((1,n)))
    for i in range(1,k):
        sec_mat = np.add(sec_mat,S[i]*np.matmul(U[:,i].reshape((m,1)),V[i,:].reshape((1,n))))
    img = Image.fromarray(sec_mat).convert("L")
    name = f'{image_name}_{k}.jpg' 
    img.save(name)
    a = len(sec_mat[:,0])
    b = len(sec_mat[0,:])
    IPython.display.display(Image.open(name))
    print(f'The Number of Elements for k={k} is {(a+b)*k}.')
    print("\n")

