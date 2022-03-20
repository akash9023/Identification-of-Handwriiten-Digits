# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OTM7BNf0i3GKbW2D3PaxPwqu6PFZ4hIv
"""

import tensorflow as tf


mnist = tf.keras.datasets.mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

training_images = training_images.reshape(training_images.shape[0],28,28,1)    
test_images = test_images.reshape(test_images.shape[0],28,28,1)
training_images = training_images.astype('float32')
test_images = test_images.astype('float32')


training_images= training_images / 255.0
test_images = test_images / 255.0


#Implementation CNN to classify handwritten digits

model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)), 
  tf.keras.layers.MaxPooling2D((2, 2)),
  
  
  
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  
  
  tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(training_images,training_labels,epochs=10)
test_loss=model.evaluate(test_images, test_labels, verbose=0)

if(test_loss[1]*100>=98.0):
  print("Reached {}% accuracy successfully!".format(test_loss[1]*100))
else:
  print("Did not reach the required accuracy")