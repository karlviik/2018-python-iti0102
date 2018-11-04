"""Make fractals."""
from PIL import Image
from PIL import ImageDraw


class Fractal:
    """Framework for fractal creation."""
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
        xstep = (max_x - min_x) / (width - 1)
        ystep = (max_y - min_y) / (height - 1)
        self.pixels = {}
        self.weights = []
        xweight, yweight = min_x, min_y
        xweights, yweights = [], []
        for x in range(width):
            xweight = xweight + xstep
            xweights.append(xweight)
        self.weights.append(xweights)
        for y in range(height):
            yweight = yweight + ystep
            yweights.append(yweight)
        self.weights.append(yweights)

    def compute(self):
        """Create the fractal by computing every pixel value."""
        for x, xweight in enumerate(self.weights[0]):
            for y, yweight in enumerate(self.weights[1]):
                self.pixels[(x, y)] = self.pixel_value((xweight, yweight))

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
        """Return iteration count for given weights."""
        # x, y = pixel
        # xold, yold = 0, 0
        c = complex(pixel[0], pixel[1])
        z = 0
        for iterations in range(129):
            z = z * z + c
            if abs(z) > 2:
                break
            # Following part is basically the above, but slower and easier to understand.
            # xnew = xold ** 2 - yold ** 2 + x
            # ynew = 2 * xold * yold + y
            # if xnew ** 2 + ynew ** 2 > 4:
            #     break
            # xold, yold = xnew, ynew
        return iterations

    def julia_computation(pixel):
        """Return iteration count for given weights."""
        # x, y = pixel
        # xold, yold = x, y
        c = complex(0.7, 0.11)
        z = complex(pixel[0], pixel[1])
        for iterations in range(129):

            z = z * z + c
            if abs(z) > 2:
                break

            # xnew = xold ** 2 - yold ** 2 - 0.75
            # ynew = 2 * xold * yold + 0.11
            # if xnew ** 2 + ynew ** 2 > 4:
            #     break
            # xold, yold = xnew, ynew
        return iterations

    # mandelbrot = Fractal((750, 600), [(-2, -1.2), (1, 1.2)], mandelbrot_computation)
    # mandelbrot.compute()
    # mandelbrot.save_image("mandelbrot.png")
    # mandelbrot = Fractal((1000, 1000), [(-2, -2), (2, 2)], julia_computation)
    # mandelbrot.compute()
    # mandelbrot.save_image("other one.png")
    # mandelbrot2 = Fractal((1000, 1000), [(-0.74877, 0.065053), (-0.74872, 0.065103)], mandelbrot_computation)
    # mandelbrot2.compute()
    # mandelbrot2.save_image("mandelbrot2.png")
