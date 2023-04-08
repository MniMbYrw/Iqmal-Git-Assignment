# Iqmal
# function to calculate area of rectangular prism

from Emily import rect_area


def rect_surface_area(length, width, height):
    area_1 = rect_area(length, width)
    area_2 = rect_area(width, height)
    area_3 = rect_area(length,height)
    # for test
    # print(area_3, area_2, area_1)
    return 2 * ( area_1 + area_2 + area_3)

# as test
# print(rect_surface_area(5, 4, 3))

