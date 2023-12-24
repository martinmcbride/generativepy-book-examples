import math

from generativepy.color import Color
from generativepy.drawing import make_image, setup, CENTER, MIDDLE
from generativepy.geometry import Circle, Text, Transform, Line

from grid import draw_grid


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))

    r = 125
    a = 45
    angles = [a * i for i in range(-3, 5)]
    points = [
        (r * math.cos(math.radians(x)), r * math.sin(math.radians(x))) for x in angles
    ]

    with Transform(ctx).translate(225, 225):
        for a, p in zip(angles, points):
            (
                Text(ctx)
                .of(f"{a}°", p)
                .size(25)
                .offset_towards((0, 0), -30)
                .align(CENTER, MIDDLE)
                .fill(Color("black"))
            )
            Line(ctx).of_start_end((0, 0), p).stroke(Color("black"), 4, dash=(6, 6))


make_image("arc-angles.png", draw, 450, 450)


def draw(ctx, pixel_width, pixel_height, frame_no, frame_count):
    setup(ctx, pixel_width, pixel_height, background=Color(1))

    with Transform(ctx).translate(75, 150):
        (
            Circle(ctx)
            .of_center_radius((0, 0), 100)
            .as_sector(math.radians(-45), math.radians(90))
            .fill(Color("yellow"))
            .stroke(Color("black"), 6)
        )
    with Transform(ctx).translate(325, 150):
        (
            Circle(ctx)
            .of_center_radius((0, 0), 100)
            .as_sector(math.radians(90), math.radians(-45))
            .fill(Color("yellow"))
            .stroke(Color("black"), 6)
        )


make_image("arc-angles2.png", draw, 450, 300)
