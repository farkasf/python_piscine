import sys
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    '''
    Inverts the color of the image received.
    '''
    img_arr = array.copy()

    img_arr[:, :, 0] = 255 - img_arr[:, :, 0]
    img_arr[:, :, 1] = 255 - img_arr[:, :, 1]
    img_arr[:, :, 2] = 255 - img_arr[:, :, 2]

    print_image(img_arr, "invert")
    return img_arr


def ft_red(array: np.ndarray) -> np.ndarray:
    '''
    Removes the green and blue color channels from the image.
    '''
    img_arr = array.copy()

    img_arr[:, :, 1] = 0
    img_arr[:, :, 2] = 0

    print_image(img_arr, "red")
    return img_arr


def ft_green(array: np.ndarray) -> np.ndarray:
    '''
    Removes the red and blue color channels from the image.
    '''
    img_arr = array.copy()

    img_arr[:, :, 0] = 0
    img_arr[:, :, 2] = 0

    print_image(img_arr, "green")
    return img_arr


def ft_blue(array: np.ndarray) -> np.ndarray:
    '''
    Removes the red and green color channels from the image.
    '''
    img_arr = array.copy()

    img_arr[:, :, 0] = 0
    img_arr[:, :, 1] = 0

    print_image(img_arr, "blue")
    return img_arr


def ft_grey(array: np.ndarray) -> np.ndarray:
    '''
    Averages the color channels to create a grayscale image.
    '''
    img_arr = array.copy()

    img_arr[:, :, 0] = img_arr[:, :, 0] / 3
    img_arr[:, :, 1] = img_arr[:, :, 1] / 3
    img_arr[:, :, 2] = img_arr[:, :, 2] / 3

    img_arr = np.sum(img_arr, axis=2)
    img_arr = np.stack([img_arr, img_arr, img_arr], axis=2)

    print_image(img_arr.astype(np.uint8), "grey")
    return img_arr.astype(np.uint8)


def print_image(img: np.ndarray, name: str) -> None:
    '''
    [PRINT_IMAGE] displays the image passed as a parameter with a
    corresponding title
    '''
    plt.imshow(img)
    plt.gcf().canvas.manager.set_window_title(f"ex05: {name}")
    plt.show()
    plt.close()


def apply_filter(value: str, img: np.ndarray) -> None:
    '''
    [APPLY_FILTER] checks the user input and applies a chosen
    filter to the image
    '''
    if value == "default":
        print_image(img, "default")
    elif value == "invert":
        ft_invert(img)
    elif value == "red":
        ft_red(img)
    elif value == "green":
        ft_green(img)
    elif value == "blue":
        ft_blue(img)
    elif value == "grey":
        ft_grey(img)
    else:
        raise AssertionError("no such an option")


def main():
    '''
    [MAIN] opens an image and calls apply_filter() to apply the
    chosen filter to it
    '''
    path = "landscape.jpg"

    try:
        img = ft_load(path)
        if img is None:
            raise AssertionError("image failed to load")

        menu = ["default", "invert", "red", "green", "blue", "grey"]
        print("\n\033[1m\033[91mwhich filter do you want to apply?\033[0m")
        print(menu)
        value = input()
        apply_filter(value, img)

    except EOFError as e:
        print(f"EOFError: {e}")
        sys.exit(1)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except IndexError as e:
        print(f"IndexError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
