import sys
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    '''
    [MAIN] loads the image as an array, slices the array to zoom in,
    transposes it to rotate counterclockwise, and displays the rotated
    image in grayscale
    '''
    path = "animal.jpeg"

    try:
        img = ft_load(path)
        if img is None:
            raise AssertionError("image failed to load")
        print(img)

        x_start, y_start, size = 450, 125, 400
        if y_start + size > img.shape[0] or x_start + size > img.shape[1]:
            raise IndexError("slicing indices are out of image bounds")

        disp = img[y_start:y_start + size, x_start:x_start + size, 2:3]
        print(f"New shape after Transpose: {disp.shape} or {disp.shape[0:2]}")
        print(disp)

        disp_rotated = np.empty((size, size, 1), dtype=disp.dtype)
        for i in range(size):
            for j in range(size):
                disp_rotated[size - 1 - j, i, 0] = disp[i, j, 0]
        print(disp_rotated)

        plt.imshow(disp_rotated, cmap='gray')
        plt.gcf().canvas.manager.set_window_title("ex04: rotate me")
        plt.show()

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except IndexError as e:
        print(f"IndexError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
    finally:
        plt.close('all')


if __name__ == "__main__":
    main()
