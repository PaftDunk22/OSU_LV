import numpy as np
import tensorflow
from tensorflow import keras
from keras.models import Model
from tensorflow.keras import layers
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

img = mpimg.imread("test.png")
plt.imshow(img)
plt.show()

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()


# skaliranje slike na raspon [0,1]
x_img = img.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
#x_train_s = np.expand_dims(x_train_s, -1)

#load model
model = tensorflow.keras.models.load_model("FCN/")
model . summary ()

