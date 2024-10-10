import numpy as np
from sklearn.model_selection import train_test_split
from PIL import Image
import os

def load_images(path, limit=None):
    """Load images from a directory and return as a numpy array"""
    images = []
    labels = []
    
    for filename in os.listdir(path)[:limit]:  # Limit images for prototype
        if filename.endswith(".png"):  # Assuming images are PNGs
            img = Image.open(os.path.join(path, filename)).convert('L')  # Convert to grayscale
            img = img.resize((28, 28))  # Resize to 28x28 for example
            images.append(np.array(img).flatten())  # Flatten the image
            label = int(filename[0])  # Assuming the filename starts with the label (e.g., 0_1.png)
            labels.append(label)
    
    return np.array(images), np.array(labels)

# Load limited image dataset
X, y = load_images('random_images', limit=100)  # Load only 100 images for prototype

# Split into training, validation, and testing sets (70% training, 15% validation, 15% testing)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Print the sizes of each set to verify the split
print(f"Training set size: {X_train.shape[0]}")
print(f"Validation set size: {X_val.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")
