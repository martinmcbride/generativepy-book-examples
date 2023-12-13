from generativepy.color import Color
from generativepy.drawing import make_image, setup
from generativepy.geometry import Rectangle, Circle, Square


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))

    Square(ctx).of_corner_size((50, 50), 200).stroke(Color("red"), 1)
    Circle(ctx).of_center_radius((250, 250), 75).stroke(Color("blue"), 8)
    Rectangle(ctx).of_corner_size((100, 300), 350, 50).fill(Color("orange")).stroke(Color("black"), 4)


make_image("stroke.png", draw, 500, 400)
