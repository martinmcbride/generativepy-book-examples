from generativepy.color import Color
from generativepy.drawing import make_image, setup, MITER, ROUND, BEVEL
from generativepy.geometry import Square


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))

    Square(ctx).of_corner_size((50, 50), 100).stroke(Color("black"), 30, join=MITER)
    Square(ctx).of_corner_size((200, 50), 100).stroke(Color("black"), 30, join=ROUND)
    Square(ctx).of_corner_size((350, 50), 100).stroke(Color("black"), 30, join=BEVEL)


make_image("corner.png", draw, 500, 200)
