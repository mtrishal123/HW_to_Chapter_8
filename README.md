# Neural Network Training with Image Dataset

This project implements a prototype for training, validation, and testing of a neural network using a synthetic image dataset. The project also demonstrates how to generate random images and split them into training, validation, and testing sets for future neural network training.

## Prerequisites

Before running the project, ensure you have the following installed on your system:

- Python 3.x
- `pip` for Python package management

### Required Libraries

The following Python libraries are required:
- `numpy`
- `scikit-learn`
- `Pillow`

You can install these libraries using the following command:

```bash
pip install numpy scikit-learn pillow
Setup Instructions
Clone the repository (if applicable) or download the project files.

Generate Random Images: In the project directory, ensure you have a script named dataset.py. This script will generate random images and store them in the specified directory (random_images by default).

The output will look like output.png


Directory Structure: After generating random images, ensure your directory structure looks like this:


project-directory/
├── dataset.py
├── dataset_split.py
├── random_images/
│   ├── 0_1.png
│   ├── 1_2.png
│   ├── ...
├── train/
├── validation/
└── test/
Run the Image Split Script: The dataset_split.py file contains code to split the randomly generated images into training, validation, and test sets. To execute it, run the following command:

python dataset_split.py
Training, Validation, and Testing:

Images will be automatically split into the train, validation, and test folders.
You can adjust the proportions for splitting in the dataset_split.py script.
Important Notes
Ensure that the path_to_images in dataset_split.py is set to point to your random_images folder.
The limit parameter in dataset_split.py controls how many images are used in each set. You can adjust it to change the dataset size.
Troubleshooting
If you encounter issues with missing libraries, ensure you have installed all the dependencies using the pip install command above.
Ensure Python is correctly set up on your system by typing python --version in the terminal to check if Python is recognized.
You may need to update pip if you encounter any warning messages related to package management.
