from generativepy.color import Color
from generativepy.drawing import make_image, setup
from generativepy.geometry import Rectangle, Square, Triangle, Line

from grid import draw_grid

def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))

    draw_grid(ctx,pixel_width, pixel_height)

    Square(ctx).of_corner_size((50, 50), 100).fill(Color("yellow")).stroke(Color("black"), 12)
    Rectangle(ctx).of_corner_size((200, 50), 150, 75).fill(Color("tomato")).stroke(Color("olive"), 8)
    Triangle(ctx).of_corners((400, 150), (550, 120), (450, 50)).fill(Color("powderblue")).stroke(Color("darkslateblue"), 4)
    Line(ctx).of_start_end((150, 200), (350, 150)).stroke(Color("darkslategrey"), 8)


make_image("simple-shapes.png", draw, 600, 250)
