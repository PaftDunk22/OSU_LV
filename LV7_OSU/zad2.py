import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("imgs\\test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

# inicijalizacija algoritma K srednjih vrijednosti
km = KMeans ( n_clusters =5 , init ='random',n_init =5 , random_state =0 )
# pokretanje grupiranja primjera
km . fit ( img_array_aprox )
# dodijeljivanje grupe svakom primjeru
labels = km . predict ( img_array_aprox )

centroids = km.cluster_centers_

img_array_aprox[:, 0] = centroids[labels][:, 0]
img_array_aprox[:, 1] = centroids[labels][:, 1]
img_array_aprox[:, 2] = centroids[labels][:, 2]
img_array_aprox = np.reshape(img_array_aprox, (w, h, d))




