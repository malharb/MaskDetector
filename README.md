# MaskDetector

ARTICLE: https://medium.com/p/80fbc04827bb/edit

A Python program that detects whether a person(s) is wearing a mask. 
Detection algorithm built using a Convolutional Neural Network. *Tensorflow 2.0* framework used.

# About Dataset
Dataset from *Kaggle*
(https://www.kaggle.com/ashishjangra27/face-mask-12k-images-dataset)

Training Data:
**10,000** images: 
**5000** - *With Mask*
**5000** - *Without Mask*

 Test Data:
 **992** images:
 **453** - With Mask
 **509** - Without Mask
 
Validation Data:
**800** images: 
**398** - *With Mask*
**402** - *Without Mask*

# IMAGE PREPROCESSING
Resized to: **80** x **80**
Colour: Black and White
Reshaped to: 4 Dimensional *NumPy* Array - (**-1,SIZE,SIZE,1**)

# NEURAL NETWORK MODEL
Convolutional Neural Netwok of **11** layers
________
**Layer Breakdown**:
**Layer 1 (Input Layer)**:
Type: Conv2D
No. of Filters: 64
Filter Matrix Size: 3x3
Activation: Rectified Linear Unit/ReLu

**Layer 2**:
Type: MaxPooling2D
Pool Size: 2 x 2

**Layer 3**:
Type: Conv2D
No. of Filters: 32
Filter Matrix Size: 3x3
Activation: Rectified Linear Unit/ReLu

**Layer 4**:
Type: MaxPooling2D
Pool Size: 2 x 2

**Layer 5**:
Type: Conv2D
No. of Filters: 64
Filter Matrix Size: 3x3
Activation: Rectified Linear Unit/ReLu

**Layer 6**:
Type: MaxPooling2D
Pool Size: 2 x 2

**Layer 7**:
Type: Flatten

**Layer 8**:
Type: Dense
No. of Perceptrons: 64
Activation: Rectified Linear Unit/ReLu

**Layer 9**:
Type: Dropout
Rate: 0.5

**Layer 10**:
Type: Dense
No. of Perceptrons: 32
ActivationL Rectified Linear Unit/ReLu

**Layer 11 (Output Layer)**:
Type: Dense
No. of Perceptrons: 1
Activation: Sigmoid
____________

**Additional Information:** 
Optimizer: ADAM
Loss Function: Binary Crossentropy
Callback(s):  EarlyStopping  (Monitoring: Validation Loss, Mode: Minimum, Patience: 3)
Epochs: 10
____
**Output** :

    Train on 10000 samples, validate on 992 samples 
    Epoch 1/10 10000/10000 [==============================] - 47s 5ms/sample - loss: 0.2557 - accuracy: 0.8842 - val_loss: 0.0733 - val_accuracy: 0.9698 
    Epoch 2/10 10000/10000 [==============================] - 50s 5ms/sample - loss: 0.1059 - accuracy: 0.9663 - val_loss: 0.0712 - val_accuracy: 0.9758 
    Epoch 3/10 10000/10000 [==============================] - 50s 5ms/sample - loss: 0.0845 - accuracy: 0.9728 - val_loss: 0.0524 - val_accuracy: 0.9758 
    Epoch 4/10 10000/10000 [==============================] - 51s 5ms/sample - loss: 0.0631 - accuracy: 0.9798 - val_loss: 0.0584 - val_accuracy: 0.9758 
    Epoch 5/10 10000/10000 [==============================] - 51s 5ms/sample - loss: 0.0515 - accuracy: 0.9829 - val_loss: 0.0653 - val_accuracy: 0.9758 
    Epoch 6/10 10000/10000 [==============================] - 52s 5ms/sample - loss: 0.0477 - accuracy: 0.9839 - val_loss: 0.0336 - val_accuracy: 0.9819 
    Epoch 7/10 10000/10000 [==============================] - 52s 5ms/sample - loss: 0.0504 - accuracy: 0.9822 - val_loss: 0.0339 - val_accuracy: 0.9879 
    Epoch 8/10 10000/10000 [==============================] - 52s 5ms/sample - loss: 0.0381 - accuracy: 0.9874 - val_loss: 0.0309 - val_accuracy: 0.9839 
    Epoch 9/10 10000/10000 [==============================] - 50s 5ms/sample - loss: 0.0308 - accuracy: 0.9889 - val_loss: 0.0324 - val_accuracy: 0.9869 
    Epoch 10/10 10000/10000 [==============================] - 51s 5ms/sample - loss: 0.0319 - accuracy: 0.9875 - val_loss: 0.0278 - val_accuracy: 0.9869

<tensorflow.python.keras.callbacks.History at 0x2069ebad408>
___
**Evaluation**:

With **Test** Data:

    992/992 [==============================] 
    - 1s 1ms/sample - loss: 0.0278 - accuracy: 0.9869

[0.027769554041198366, 0.98689514]

1 milisecond per image
Accuracy: 98.69%
Loss: 0.0278

Confusion Matrix:

    [[506 3] 
    [ 10 473]]


Classification Report:

      
		      precision    recall    f1-score      support
     0   		0.98        0.99         0.99         509 
     1   		0.99        0.98 	 0.99 	      483
     
      macro av  	 0.99        0.99         0.99         992 
      weighted av	 0.99        0.99         0.99         992
      
      accuracy 		0.99 992 
___

With **Validation** Data:

    800/800 [==============================] 
    - 1s 1ms/sample - loss: 0.0282 - accuracy: 0.9875

[0.028228099095867945, 0.9875]

1 milisecond per image
Accuracy: 98.75%
Loss: 0.0282

Confusion Matrix:

    [[396 6] 
    [ 4 394]]

Classification Report:

		     precision 		recall 		f1-score 	support 
    0 			0.99 	          0.99 		  0.99 		  402 
    1 			0.98 		  0.99            0.99            398 
    
    macro av      	0.99 		  0.99            0.99 		  800 
    weighted av         0.99 	          0.99 		  0.99 		  800
    
    accuracy 	  0.99 800 










 
 
      



