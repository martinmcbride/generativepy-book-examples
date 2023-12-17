from generativepy.color import Color
from generativepy.drawing import make_image, setup, BUTT, ROUND
from generativepy.geometry import Rectangle, Circle, Square


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))

    Square(ctx).of_corner_size((50, 50), 100).stroke(Color("black"), 8, dash=[16])
    Circle(ctx).of_center_radius((250, 100), 60).stroke(Color("black"), 8, dash=[16], cap=BUTT)
    Square(ctx).of_corner_size((350, 50), 100).stroke(Color("black"), 8, dash=[16], cap=ROUND)
    Square(ctx).of_corner_size((50, 200), 100).stroke(Color("black"), 4, dash=[6, 12], cap=BUTT)
    Circle(ctx).of_center_radius((250, 250), 60).stroke(Color("black"), 6, dash=[0, 10], cap=ROUND)
    Square(ctx).of_corner_size((350, 200), 100).stroke(Color("black"), 4, dash=[0, 10, 3, 7], cap=ROUND)


make_image("dash.png", draw, 500, 350)
