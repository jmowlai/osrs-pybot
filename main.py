import cv2 as cv
import numpy as np
import sys

haystack_img = cv.imread('spawn-screenshot.jpg', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('spawn-shrub.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

# cv.imshow('Result', result)
# cv.waitKey()

# Grab best match position
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print(max_loc)
print(max_val)

threshold = 0.8
if max_val >= threshold:
    print('Found')

    # get dimensions of the needle image
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(haystack_img, top_left, bottom_right,
                    line_color, thickness=2, lineType = line_type)
    # cv.imshow('Result', haystack_img)
    # cv.waitKey()
    cv.imwrite('result.jpg', haystack_img)

else:
    print('Not found')