from generativepy.color import Color
from generativepy.drawing import make_image, setup, ROUND
from generativepy.geometry import Polygon

from grid import draw_grid


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))

    draw_grid(ctx, pixel_width, pixel_height)

    (
        Polygon(ctx)
        .of_points(((100, 50), (150, 100), (130, 200), (70, 200), (50, 100)))
        .fill(Color("firebrick"))
        .stroke(Color("seagreen"), 6)
    )
    (
        Polygon(ctx)
        .of_points(
            ((200, 50), (300, 200), (400, 50), (400, 150), (300, 100), (200, 200))
        )
        .fill(Color("yellow"))
        .stroke(Color("goldenrod"), 4)
    )
    (
        Polygon(ctx)
        .of_points(((50, 400), (100, 300), (150, 250), (250, 300), (250, 400)))
        .open()
        .stroke(Color("darkred"), 8, cap=ROUND)
    )
    (
        Polygon(ctx)
        .of_points(((300, 250), (400, 250), (400, 350), (350, 400)))
        .open(True)
        .fill(Color("lightblue"))
        .stroke(Color("darkcyan"), 6)
    )


make_image("polygons.png", draw, 450, 450)
