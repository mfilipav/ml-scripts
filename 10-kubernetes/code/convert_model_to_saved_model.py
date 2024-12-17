import tensorflow as tf
import tf_keras as keras


print("hello")
model = keras.models.load_model('./clothing-model.h5')
print("done, model")

# model.save(model, 'clothing-model-saved')
model.save(model, 'clothing-model')
