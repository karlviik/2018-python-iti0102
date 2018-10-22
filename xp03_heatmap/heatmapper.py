"""Create nice map based on given parameters."""
import topo
from PIL import Image
from PIL import ImageDraw
import math


def generate_map(topo_data, width, height, filename):
    """
    Generate (heat)map into an image file.

    topo_data comes from topo module. The data is a list
    where every element contains latitude, longitude and altitude (in meters).
    The function should treat coordinates as regular y and x (flat world).
    The image should fill the whole width, height. Every "point" in the data
    should be represented as a rectangle on the image.

    For example, if topo_data has 12 elements (latitude, longitude, altitude):
    10, 10, 1
    10, 12, 1
    16, 14, 3
    and the width = 100, height = 100
    then the first line in data should be represented as a rectangle (0, 0) - (33, 25)
    (x1, y1) - (x2, y2).
    The height is divided into 4, each "point" is 100/4 = 25 pixels high,
    the width is divided into 3, each "point" is 100/3 = 33 pixels wide.
    :param topo_data: list of topography data (from topo module)
    :param width: width of the image
    :param height: height of the image
    :param filename: the file to be written
    :return: True if everything ok, False otherwise
    """
    try:
        data_len = len(topo_data)
        maxlat, minlon, minlat, maxlon = topo_data[0][0], topo_data[0][1], topo_data[data_len - 1][0], topo_data[data_len - 1][1]
        diflat = maxlat - minlat
        diflon = maxlon - minlon
        steplon = topo_data[1][1] - minlon
        datawidth = round(diflon / steplon + 1)
        steplat = maxlat - topo_data[datawidth][0]
        dataheight = round(diflat / steplat + 1)
        datawidthstep = datawidth / width
        dataheightstep = dataheight / height
        minalt, maxalt = 0, 0
        pixellist = []
        for row in range(height):
            rowlist = []
            for column in range(width):
                pixel = topo_data[(math.ceil((row + 1) * dataheightstep) - 1) * datawidth + (math.ceil((column + 1) * datawidthstep) - 1)][2]
                if pixel < minalt:
                    minalt = pixel
                elif pixel > maxalt:
                    maxalt = pixel
                rowlist.append(pixel)
            pixellist.append(rowlist)
        img = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(img)
        for y, row in enumerate(pixellist):
            for x, pixel in enumerate(row):
                if pixel < 0:
                    temp = round(pixel / minalt, 1)
                    R = math.floor(0 - temp * 0)
                    G = math.floor(55 - temp * 45)
                    B = math.floor(160 - temp * 60)
                else:
                    temp = round(pixel / maxalt, 1)
                    R = math.floor(40 + temp * 215)
                    G = math.floor(105 + temp * 150)
                    B = math.floor(30 + temp * 225)

                draw.point((x + 0, y + 0), (R, G, B))
        img.save(filename, "PNG")
        return True
    except TypeError:
        return False


def generate_map_with_coordinates(topo_params, image_width, image_height, filename):
    """
    Given the topo parameters and image parameters, generate map into a file.

    topo_parameters = (min_latitude, max_latitude, latitude_stride, min_longitude, max_longitude, longitude_stride)
    In the case where latitude_stride and/or longitude_stride are 0,
    you have to calculate step yourself, based on the image parameters.
    For example, if image size is 10 x 10, there is no point to query more than 10 x 10 topological points.
    Hint: check the website, there you see "size" for both latitude and longitude.
    Also, read about "stride" (the question mark behind stride in the form).

    Caching:
    if all the topo params are calculated (or given), then it would be wise
    to cache the query results. One implementation could be as follows:
    filename = topo_57-60-3_22-28-1.json
    (where 57 = min_lat, 60 = max_lat, 3 latitude stride etc)
     if file exists:
         topo.read_json_from_file(file)
     else:
         result = topo.read_json_from_web(...)
         with open(filename, 'w'):
             f.write(result)

     ... do the rest


    :param topo_params: tuple with parameters for topo query
    :param image_width: image width in pixels
    :param image_height: image height in pixels
    :param filename: filename to store the image
    :return: True, if everything ok, False otherwise
    """
    step = 0.008333333
    latstep = topo_params[2]
    lonstep = topo_params[5]
    if latstep == 0:
        latrange = topo_params[1] - topo_params[0]
        datalat = latrange / step
        latstep = math.floor(datalat / image_height)
        if latstep == 0:
            latstep = 1
    if lonstep == 0:
        lonrange = topo_params[1] - topo_params[0]
        datalon = lonrange / step
        lonstep = math.floor(datalon / image_width)
        if lonstep == 0:
            lonstep = 1
    file = f"topo_{topo_params[0]}-{topo_params[1]}-{latstep}_{topo_params[3]}-{topo_params[4]}-{lonstep}.json"
    contents = topo.read_json_from_file(file)
    if contents == "" or contents is None:
        contents = topo.read_json_from_web(topo_params[0], topo_params[1], topo_params[2], topo_params[3], topo_params[4], topo_params[5])
        with open(file, "w") as f:
            f.write(contents)
    data = topo.get_topo_data_from_string(contents)
    return generate_map(data, image_width, image_height, filename)


print(generate_map_with_coordinates((1, 2, 1, 1, 2, 1), 100, 100, "aaaahahah.png"))
