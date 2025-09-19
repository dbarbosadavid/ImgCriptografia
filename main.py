import cv2
import matplotlib.pyplot as plt
import random
 
image_path = "cat.jpg"
img = cv2.imread(image_path,0)
imgCriptada = cv2.imread(image_path,0)

plt.imshow(img, cmap='gray')
plt.show()

text = "ba"
arrayInt = []

linha = random.sample(range(0, len(imgCriptada)), len(text))
coluna = random.sample(range(0, len(imgCriptada[0])), len(text))


for char in range(len(text)):
    imgCriptada[linha, coluna] = ord(text[char])

            
for i in range(len(imgCriptada)):
    for j in range(len(imgCriptada[0])):
        if(imgCriptada[i, j] != img[i, j]):
            arrayInt.append(imgCriptada[i, j])



print(arrayInt)
textDecriptado = "".join(map(chr, arrayInt))

print(textDecriptado)

plt.imshow(imgCriptada, cmap='gray')
plt.show()


        

