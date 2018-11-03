from PIL import Image
import math


class Fractal:
    def __init__(self, size, scale, computation):
        """Constructor.

        Arguments:
        size -- the size of the image as a tuple (x, y)
        scale -- the scale of x and y as a list of 2-tuple
                 [(minimum_x, minimum_y), (maximum_x, maximum_y)]
        computation -- the function used for computing pixel values as a function
        """
        pass

    def compute(self):
        """
        Create the fractal by computing every pixel value.
        """
        pass

    def pixel_value(self, pixel):
        """
        Return the number of iterations it took for the pixel to go out of bounds.

        Arguments:
        pixel -- the pixel coordinate (x, y)

        Returns:
        the number of iterations of computation it took to go out of bounds as integer.
        """
        pass

    def save_image(self, filename):
        """
        Save the image to hard drive.

        Arguments:
        filename -- the file name to save the file to as a string.
        """
        pass


if __name__ == "__main__":
    def mandelbrot_computation(pixel):
        x, y = pixel
        xold, yold = 0, 0
        for iterations in range(256):
            xnew = xold ** 2 - yold ** 2 + x
            ynew = 2 * xold * yold + y
            if xnew ** 2 + ynew ** 2 > 4:
                break
            xold, yold = xnew, ynew
        return iterations  # returns just one value right now, dunno how to color scheme yet

    print(mandelbrot_computation((0, 0)))
"""
    mandelbrot = Fractal((1000, 1000), [(-2, -2), (2, 2)], mandelbrot_computation)
    mandelbrot.compute()
    mandelbrot.save_image("mandelbrot.png")
    mandelbrot2 = Fractal((1000, 1000), [(-0.74877, 0.065053), (-0.74872, 0.065103)], mandelbrot_computation)
    mandelbrot2.compute()
    mandelbrot2.save_image("mandelbrot2.png")
"""