from generativepy.color import Color
from generativepy.drawing import make_image, setup
from generativepy.geometry import Rectangle, Circle


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))

    Rectangle(ctx).of_corner_size((50, 50), 300, 200).stroke(Color("black"), 30)
    Rectangle(ctx).of_corner_size((50, 50), 300, 200).stroke(Color("white"), 2, dash=[8, 8])
    Circle(ctx).of_center_radius((50, 50), 4).fill(Color("red"))
    Circle(ctx).of_center_radius((350, 50), 4).fill(Color("red"))
    Circle(ctx).of_center_radius((50, 250), 4).fill(Color("red"))
    Circle(ctx).of_center_radius((350, 250), 4).fill(Color("red"))


make_image("stroke-boundary.png", draw, 400, 300)
