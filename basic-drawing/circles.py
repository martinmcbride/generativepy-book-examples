import math

from generativepy.color import Color
from generativepy.drawing import make_image, setup
from generativepy.geometry import Circle, Text

from grid import draw_grid


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))

    draw_grid(ctx, pixel_width, pixel_height)

    (
        Circle(ctx)
        .of_center_radius((150, 150), 75)
        .fill(Color("yellow"))
        .stroke(Color("black"), 6)
    )
    Text(ctx).of("A", (75, 75)).size(30).fill(Color("black"))
    (
        Circle(ctx)
        .of_center_radius((300, 150), 75)
        .as_sector(math.radians(0), math.radians(135))
        .fill(Color("yellow"))
        .stroke(Color("black"), 6)
    )
    Text(ctx).of("B", (325, 125)).size(30).fill(Color("black"))
    (
        Circle(ctx)
        .of_center_radius((150, 350), 75)
        .as_segment(math.radians(-90), math.radians(20))
        .fill(Color("yellow"))
        .stroke(Color("black"), 6)
    )
    Text(ctx).of("C", (125, 325)).size(30).fill(Color("black"))
    (
        Circle(ctx)
        .of_center_radius((300, 350), 75)
        .as_arc(math.radians(-90), math.radians(20))
        .stroke(Color("black"), 6)
    )
    Text(ctx).of("D", (300, 325)).size(30).fill(Color("black"))


make_image("circles.png", draw, 450, 450)
