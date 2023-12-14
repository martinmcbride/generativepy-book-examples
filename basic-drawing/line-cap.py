from generativepy.color import Color
from generativepy.drawing import make_image, setup, MITER, ROUND, BEVEL, SQUARE, BUTT
from generativepy.geometry import Square, Line, Circle


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))

    Line(ctx).of_start_end((50, 50), (350, 50)).stroke(Color("black"), 30, cap=SQUARE)
    Circle(ctx).of_center_radius((50, 50), 4).fill(Color("red"))
    Circle(ctx).of_center_radius((350, 50), 4).fill(Color("red"))

    Line(ctx).of_start_end((50, 150), (350, 150)).stroke(Color("black"), 30, cap=BUTT)
    Circle(ctx).of_center_radius((50, 150), 4).fill(Color("red"))
    Circle(ctx).of_center_radius((350, 150), 4).fill(Color("red"))

    Line(ctx).of_start_end((50, 250), (350, 250)).stroke(Color("black"), 30, cap=ROUND)
    Circle(ctx).of_center_radius((50, 250), 4).fill(Color("red"))
    Circle(ctx).of_center_radius((350, 250), 4).fill(Color("red"))


make_image("line-cap.png", draw, 400, 300)
