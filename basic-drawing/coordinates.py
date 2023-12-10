import math

from generativepy.drawing import make_image, setup, BUTT
from generativepy.color import Color
from generativepy.geometry import Rectangle, Transform, Text, Line


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):

    setup(ctx, pixel_width, pixel_height, background=Color(1))

    with Transform(ctx).translate(75, 75):
        Rectangle(ctx).of_corner_size((0, 0), 500, 400).fill(Color("grey"))
        Rectangle(ctx).of_corner_size((100, 150), 250, 200).fill(Color("orange"))

        Text(ctx).of("500 pixels", (250, -25)).size(30).align_center().fill(Color(0))
        Text(ctx).of("(0, 0)", (-5, -5)).size(25).align_right().fill(Color(0))
        Line(ctx).of_start_end((100, 0), (100, 150)).stroke(Color(0), 4, dash=[8, 8], cap=BUTT)
        Text(ctx).of("150", (110, 75)).size(25).align_left().align_middle().fill(Color(0))
        Line(ctx).of_start_end((0, 150), (100, 150)).stroke(Color(0), 4, dash=[8, 8], cap=BUTT)
        Text(ctx).of("100", (50, 160)).size(25).align_center().align_top().fill(Color(0))
        with Transform(ctx).translate(-25, 200).rotate(math.radians(-90)):
            Text(ctx).of("400 pixels", (0, 0)).size(30).align_center().fill(Color(0))



make_image("coordinates.png", draw, 600, 500)
