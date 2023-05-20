import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Conv2D, Flatten
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array
model = VGG16(weights='imagenet')
data_generator = ImageDataGenerator(preprocessing_function=preprocess_input)

def preprocess_image(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

dataset_path = ##############
image_paths = []  #################

preprocessed_images = []
for image_path in image_paths:
    img = preprocess_image(image_path)
    preprocessed_images.append(img)

disease_predictions = []
for img in preprocessed_images:
    prediction = model.predict(img)
    decoded_predictions = decode_predictions(prediction, top=1)[0]
    disease_predictions.append(decoded_predictions)

def determine_plant_disease(predictions, target_disease):
    for pred in predictions:
        for disease in pred:
            if disease.lower() == target_disease.lower():
                return True
    return False  