import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    '''
    [FT_LOAD] checks the format (JPG/JPEG) and path of a specified
    file, then loads an image and returns it as a an array.
    '''
    try:
        if path[-4:] != ".jpg" and path[-5:] != ".jpeg":
            raise AssertionError("file format not accepted")
        if not os.path.exists(path):
            raise AssertionError(f"{path}: no such file")
        img = np.array(Image.open(path))
        print(f"The shape of the image is: {img.shape}")
        return img

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return None
