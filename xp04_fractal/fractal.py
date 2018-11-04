from PIL import Image
from PIL import ImageDraw
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
        self.iteration_computer = computation
        width, height = size
        self.image = Image.new("HSV", size)
        min_x, min_y = scale[0]
        max_x, max_y = scale[1]
        xrange = max_x - min_x
        xstep = xrange / (width - 1)
        yrange = max_y - min_y
        ystep = yrange / (height - 1)
        self.pixels = {}
        for ycount in range(height):
            yweight = min_y + ystep * ycount
            for xcount in range(width):
                xweight = min_x + xstep * xcount
                self.pixels[(xcount, ycount)] = (xweight, yweight)

    def compute(self):
        """Create the fractal by computing every pixel value."""
        for pixel, weight in self.pixels.items():
            self.pixels[pixel] = self.pixel_value(weight)

    def pixel_value(self, pixel):
        """
        Return the number of iterations it took for the pixel to go out of bounds.

        Arguments:
        pixel -- the pixel coordinate (x, y)

        Returns:
        the number of iterations of computation it took to go out of bounds as integer.
        """
        return self.iteration_computer(pixel)

    def save_image(self, filename):
        """
        Save the image to hard drive.

        Arguments:
        filename -- the file name to save the file to as a string.
        """
        draw = ImageDraw.Draw(self.image)
        for pixel, iterations in self.pixels.items():
            iterations = iterations * 2
            value = 255
            if iterations >= 255:
                iterations = 0
                value = 0
            draw.point(pixel, (iterations, 255, value))
        self.image.convert("RGB").save(filename, "PNG")


if __name__ == "__main__":
    def mandelbrot_computation(pixel):
        x, y = pixel
        xold, yold = 0, 0
        c = complex(pixel[0], pixel[1])
        z = 0
        for iterations in range(129):
            z = z * z + c
            if abs(z) > 2:
                break
            """
            xnew = xold ** 2 - yold ** 2 + x
            ynew = 2 * xold * yold + y
            if xnew ** 2 + ynew ** 2 > 4:
                break
            if xnew == xold and ynew == yold:
                iterations = 128
                break
            xold, yold = xnew, ynew"""
        return iterations


    mandelbrot = Fractal((750, 600), [(-2, -1.2), (1, 1.2)], mandelbrot_computation)
    mandelbrot.compute()
    mandelbrot.save_image("mandelbrot.png")
    #mandelbrot2 = Fractal((1000, 1000), [(-0.74877, 0.065053), (-0.74872, 0.065103)], mandelbrot_computation)
    #mandelbrot2.compute()
    #mandelbrot2.save_image("mandelbrot2.png")

