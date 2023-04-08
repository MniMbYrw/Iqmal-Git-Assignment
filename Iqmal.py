# Iqmal
# function to calculate area of rectangular prism

from Emily import rect_area


def rect_surface_area(length, width, height):
    area_lw = rect_area(length, width)
    area_wh = rect_area(width, height)
    area_hl = rect_area(height, length)
    # for test
    # print(area_lw, area_wh, area_hl)
    return 2 * (area_lw + area_wh + area_hl)

# as test
# print(rect_surface_area(5, 4, 3))

