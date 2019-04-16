import cv2
import numpy as np

imgJogador = cv2.imread("soccer.jpg")

print(imgJogador.shape) #mostrar alturar, largura, num cor 
print(imgJogador.item(0,0 ,0),imgJogador.item(0,0 ,1),imgJogador.item(0,0 ,2))

imgJogador.itemset((0,0,2), 255)
imgJogador.itemset((0,0,1), 0)
imgJogador.itemset((0,0,0), 0)

cv2.imwrite("soccer2.jpg",imgJogador)
bola = imgJogador[180:250, 250:315]

cv2.imwrite("bola.jpg",bola)
imgJogador[130:200, 200:265] = bola

cv2.imwrite("soccer2.jpg",imgJogador)
