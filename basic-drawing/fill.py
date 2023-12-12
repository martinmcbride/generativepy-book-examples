from generativepy.color import Color
from generativepy.drawing import make_image, setup
from generativepy.geometry import Rectangle, Circle


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))

    Rectangle(ctx).of_corner_size((50, 50), 300, 200).fill(Color("dodgerblue"))
    Circle(ctx).of_center_radius((250, 250), 75).fill(Color("maroon"))
    Rectangle(ctx).of_corner_size((100, 300), 350, 50).fill(Color("grey", 0.7))


make_image("fill.png", draw, 500, 400)
