import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Define the model architecture
model = keras.Sequential(
    [
        layers.InputLayer(input_shape=(128, 128, 3)),
        layers.Conv2D(16, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ]
)

# Compile the model
model.compile(
    loss=keras.losses.BinaryCrossentropy(from_logits=True),
    optimizer=keras.optimizers.Adam(lr=0.001),
    metrics=["accuracy"],
)

# Load and preprocess the data
train_data = keras.preprocessing.image_dataset_from_directory(
    "path/to/training/data",
    labels="inferred",
    label_mode="binary",
    image_size=(128, 128),
    batch_size=32,
)
test_data = keras.preprocessing.image_dataset_from_directory(
    "path/to/test/data",
    labels="inferred",
    label_mode="binary",
    image_size=(128, 128),
    batch_size=32,
)

# Train the model
model.fit(train_data, epochs=10, validation_data=test_data)
