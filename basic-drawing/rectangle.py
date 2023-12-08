from generativepy.drawing import make_image, setup
from generativepy.color import Color
from generativepy.geometry import Rectangle

def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):

    setup(ctx, pixel_width, pixel_height, background=Color("grey"))

    Rectangle(ctx).of_corner_size((100, 150), 250, 200).fill(Color("orange"))


make_image("rectangle.png", draw, 500, 400)
