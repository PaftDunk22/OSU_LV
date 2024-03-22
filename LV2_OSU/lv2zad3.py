#Zadatak 2.4.3 Skripta zadatak_3.py ucitava sliku ’ ˇ road.jpg’. Manipulacijom odgovarajuce´
#numpy matrice pokušajte:
#a) posvijetliti sliku,
#b) prikazati samo drugu cetvrtinu slike po širini, ˇ
#c) zarotirati sliku za 90 stupnjeva u smjeru kazaljke na satu,
#d) zrcaliti sliku.

import numpy as np
import matplotlib . pyplot as plt

img=plt.imread("road.jpg")
img=img[:,:,0].copy()

plt.figure()
plt.title('a)')
plt.imshow(img, alpha=0.5)
plt.show()

width=len(img[0])
q_width=int(width/4)
plt.title('b)')
plt.imshow(img[:,q_width: 2*q_width],cmap="gray")
plt.show()

rotated_img=np.rot90(img,3)
plt.title('c)')
plt.imshow(rotated_img)
plt.show()

flipped_img=np.flip(img)
plt.title('d)')
plt.imshow(flipped_img)
plt.show()