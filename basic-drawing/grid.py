from generativepy.geometry import Line, Text
from generativepy.color import Color

def draw_grid(ctx, width, height, gap=50):
    color = Color("black")
    for i in range(gap, width, gap):
        Line(ctx).of_start_end((i, 0), (i, height)).stroke(color)
        Text(ctx).of(str(i), (i, 0)).align_top().offset(5, 5).size(10).fill(color)
    for i in range(gap, height, gap):
        Line(ctx).of_start_end((0, i), (width, i)).stroke(color)
        Text(ctx).of(str(i), (0, i)).align_top().offset(5, 5).size(10).fill(color)