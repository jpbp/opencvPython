import cv2

imgCarregada=cv2.imread("a.jpg", 0 ) #carregar imagem do disco
cv2.imshow("ImagemCarregada", imgCarregada)# mostrar na tela
cv2.waitKey(0)


cv2.imwrite("imagemsalva.jpg",imgCarregada) #escrever imagem.


