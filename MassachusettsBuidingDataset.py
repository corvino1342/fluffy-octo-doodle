# %%
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

# %%

image = Image.open('datasets/massachusetts-buildings-dataset/tiff/train/22678915_15.tiff')

# Plot the image
plt.imshow(image)
plt.axis('off')  # optional, hides the axes
plt.show()