import os
import numpy as np
from PIL import Image

# Function to create random images
def create_random_images(directory, num_images=100, img_size=(28, 28)):
    os.makedirs(directory, exist_ok=True)
    for i in range(num_images):
        # Create a random grayscale image
        random_image = np.random.randint(0, 255, img_size, dtype=np.uint8)
        
        # Create label as the first number (for example, 0_1.png)
        label = np.random.randint(0, 10)  # Assuming 10 classes, digits 0-9
        img_name = f"{label}_{i}.png"
        
        # Save image
        img_path = os.path.join(directory, img_name)
        img = Image.fromarray(random_image)
        img.save(img_path)

# Example usage
create_random_images('random_images', num_images=100, img_size=(28, 28))
