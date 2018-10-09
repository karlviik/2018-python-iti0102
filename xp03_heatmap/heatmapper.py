import topo
# import some image processing library here

def generate_map(topo_data, width, height, filename):
    """
    Generates (heat)map into an image file.

    topo_data comes from topo module. The data is a list
    where every element contains latitude, longitude and altitude (in meters).
    The function should treat coordinates as regular y and x (flat world).
    The image should fill the whole width, height. Every "point" in the data
    should be represented as a rectangle on the image.

    For example, if topo_data has 12 elements (latitude, longitude, altitude):
    10, 10, 1
    10, 12, 1
    10, 14, 2
    12, 10, 1
    12, 12, 3
    12, 14, 1
    14, 10, 6
    14, 12, 9
    14, 14, 12
    16, 10, 1
    16, 12, 1
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
    return True

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
    return True


if __name__ == '__main__':
    # topo_data = topo.get_topo_data_from_string(topo.read_json_from_web(58, 59, 10, 24, 25, 10))
    # generate_map(topo_data, 100, 100, "mymap.png")

    generate_map_with_coordinates((57.5, 60, 0, 22, 29, 0), 1500, 1000, "eesti.png")
    generate_map_with_coordinates((-89.9, 90, 0, -180, 179.9, 0), 600, 400, "world.png")