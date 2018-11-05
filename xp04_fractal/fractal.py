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
        self.weights = [[], []]
        xweight, yweight = min_x, min_y
        for x in range(width):
            xweight = xweight + xstep
            self.weights[0].append(xweight)
        for y in range(height):
            yweight = yweight + ystep
            self.weights[1].append(yweight)

    def compute(self):
        """Create the fractal by computing every pixel value."""
        draw = ImageDraw.Draw(self.image)
        for x, xweight in enumerate(self.weights[0]):
            for y, yweight in enumerate(self.weights[1]):
                # self.pixels[(x, y)] = self.pixel_value((xweight, yweight))
                iterations = self.pixel_value((xweight, yweight)) * 2
                value = 255
                if iterations >= 255:
                    iterations = 0
                    value = 0
                draw.point((x, y), (iterations, 255, value))
        # for pixel, iterations in self.pixels.items():
        #     iterations = iterations * 2
        #     value = 255
        #     if iterations >= 255:
        #         iterations = 0
        #         value = 0
        #     draw.point(pixel, (iterations, 255, value))

    def pixel_value(self, pixel):  # to pass test this should just be pixel that goes in x, y 0 to width/height -1
        """
        Return the number of iterations it took for the pixel to go out of bounds.

        Arguments:
        pixel -- the pixel coordinate (x, y)

        Returns:
        the number of iterations of computation it took to go out of bounds as integer.
        """
        x, y = pixel
        pixel = (self.weights[0][x], self.weights[1][y])
        return self.iteration_computer(pixel)

    def save_image(self, filename):
        """
        Save the image to hard drive.

        Arguments:
        filename -- the file name to save the file to as a string.
        """
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
        c = complex(real, imag)
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

    # mandelbrot = Fractal((750 * 32, 600 * 32), [(-2, -1.2), (1, 1.2)], mandelbrot_computation)
    # mandelbrot.compute()
    # mandelbrot.save_image("mandelbrot.png")
    # del mandelbrot

    juliasize = (int(4000 * 4.5), int(4000 * 4.5))

    real, imag = -0.2, 0.66
    julia1 = Fractal(juliasize, [(-2, -2), (2, 2)], julia_computation)
    julia1.compute()
    julia1.save_image("julia1.png")
    del julia1

    real, imag = -0.14, -0.65
    julia2 = Fractal(juliasize, [(-2, -2), (2, 2)], julia_computation)
    julia2.compute()
    julia2.save_image("julia2.png")
    del julia2

    real, imag = -0.14, -0.69
    julia3 = Fractal(juliasize, [(-2, -2), (2, 2)], julia_computation)
    julia3.compute()
    julia3.save_image("julia3.png")
    del julia3

    real, imag = -0.21, 0.76
    julia4 = Fractal(juliasize, [(-2, -2), (2, 2)], julia_computation)
    julia4.compute()
    julia4.save_image("julia4.png")
    del julia4

    real, imag = -0.23, -0.83
    julia5 = Fractal(juliasize, [(-2, -2), (2, 2)], julia_computation)
    julia5.compute()
    julia5.save_image("julia5.png")
    del julia5

    real, imag = -0.68, 0.32
    julia6 = Fractal(juliasize, [(-2, -2), (2, 2)], julia_computation)
    julia6.compute()
    julia6.save_image("julia6.png")
    del julia6

    real, imag = -0.72, 0.26
    julia7 = Fractal(juliasize, [(-2, -2), (2, 2)], julia_computation)
    julia7.compute()
    julia7.save_image("julia7.png")
    del julia7

    real, imag = -0.77, 0.12
    julia8 = Fractal(juliasize, [(-2, -2), (2, 2)], julia_computation)
    julia8.compute()
    julia8.save_image("julia8.png")
    del julia8

    real, imag = -0.84, -0.08
    julia9 = Fractal(juliasize, [(-2, -2), (2, 2)], julia_computation)
    julia9.compute()
    julia9.save_image("julia9.png")

    # mandelbrot = Fractal((1000, 1000), [(-2, -2), (2, 2)], julia_computation)
    # mandelbrot.compute()
    # mandelbrot.save_image("other one.png")
    # mandelbrot2 = Fractal((1000, 1000), [(-0.74877, 0.065053), (-0.74872, 0.065103)], mandelbrot_computation)
    # mandelbrot2.compute()
    # mandelbrot2.save_image("mandelbrot2.png")
