import time

import mss
from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw

BOX_COORD = {'top': 300, 'left': 120, 'width': 30, 'height': 40}


# step of grid
layout_step = 100

# width of grid
layout_width = 2


def get_filename():
    filename = 'screenshot_{}.png'.format(int(time.time()))
    return filename


def snapshot():
    # make screenshot, check the scale of monitor to calibrate coefficient in code

    sct = mss.mss()
    m = sct.monitors[0]
    print(m)

    # do screen
    sct_img = sct.grab(m)

    # Create the Image
    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

    draw = ImageDraw.Draw(im=img, mode=img.mode)
    fill = ImageColor.getrgb('red')

    width, height = img.size
    print(f'Screen resolution: X={width}, Y={height}')

    # draw vertical lines every 100px
    for i in range(0, width, layout_step):
        draw.line(xy=((i, 0), (i, height)), fill=fill, width=layout_width)

    # draw horizontal lines every 100px
    for i in range(0, height, layout_step):
        draw.line(xy=((0, i), (width, i)), fill=fill, width=layout_width)

    # draw some coordinates
    draw.line(xy=((0, 0), (layout_step, layout_step)), fill=fill, width=layout_width)

    # draw the box from MSS

    outline = ImageColor.getrgb('green')

    for box in BOX_COORD:
        box_xy = (
        	# BOX_COORD = {'top': 300, 'left': 120, 'width': 30, 'height': 40}
            (150, 300, ),
            ((150 + 30), (300 + 40)),
        )
        draw.rectangle(xy=box_xy, outline=outline, width=4)

    img.save(get_filename())
    print('Screenshot is in your folder!')


if __name__ == '__main__':
    snapshot()
