import cairo
import math

def draw_grid(context, width, height, spacing=50):
    context.set_source_rgb(0.9, 0.9, 0.9)

    for x in range(0, width, spacing):
        context.move_to(x, 0)
        context.line_to(x, height)
        context.stroke()

    for y in range(0, height, spacing):
        context.move_to(0, y)
        context.line_to(width, y)
        context.stroke()

def draw_base1(ctx):
    ctx.move_to(400, 750)
    ctx.line_to(900, 750)
    ctx.line_to(900, 350)
    ctx.line_to(650, 200)
    ctx.line_to(400, 350)
    ctx.close_path()

    ctx.set_source_rgb(0.9, 0.9, 0.9)
    ctx.fill_preserve()
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

def draw_base2(ctx):
    ctx.move_to(400, 750)
    ctx.line_to(100, 650)
    ctx.line_to(100, 250)
    ctx.line_to(400, 350)

    ctx.set_source_rgb(0.9, 0.9, 0.9)
    ctx.fill_preserve()
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

def draw_door(ctx):
    ctx.rectangle(500, 450, 125, 300)
    ctx.set_source_rgb(0.4, 0.2, 0)
    ctx.fill_preserve()
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

def draw_door_knob(ctx):
    ctx.arc(515, 600, 5, 0, 2 * math.pi)
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

def draw_right_window(ctx):
    ctx.rectangle(675, 500, 200, 150)
    ctx.set_source_rgb(0.4, 0.2, 0)
    ctx.fill_preserve()
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

    ctx.rectangle(687.5, 512.5, 75, 125)
    ctx.set_source_rgb(0.5, 0.8, 1)
    ctx.fill()

    ctx.rectangle(787.5, 512.5, 75, 125)
    ctx.set_source_rgb(0.5, 0.8, 1)
    ctx.fill()

def draw_left_window1(ctx):
    ctx.move_to(375, 650)
    ctx.line_to(250, 600)
    ctx.line_to(250, 450)
    ctx.line_to(375, 500)
    ctx.close_path()

    ctx.set_source_rgb(0.4, 0.2, 0)
    ctx.fill_preserve()
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

    ctx.move_to(362.5, 631.25)
    ctx.line_to(362.5, 512.5)
    ctx.line_to(312.5, 493.25)
    ctx.line_to(312.5, 612.5)
    ctx.close_path()
    ctx.set_source_rgb(0.5, 0.8, 1)
    ctx.fill()

def draw_left_window2(ctx):
    ctx.move_to(225, 587.5)
    ctx.line_to(125, 550)
    ctx.line_to(125, 400)
    ctx.line_to(225, 437.5)
    ctx.close_path()

    ctx.set_source_rgb(0.4, 0.2, 0)
    ctx.fill_preserve()
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

# Main drawing setup
width, height = 1000, 800
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Background color
context.set_source_rgb(1, 1, 1)
context.paint()

draw_grid(context, width, height)
draw_base1(context)
draw_base2(context)
draw_door(context)
draw_door_knob(context)
draw_right_window(context)
draw_left_window1(context)
draw_left_window2(context)

# context.set_source_rgb(0.8, 0.8, 0.8)  # Light gray color
# context.set_source_rgb(0.4, 0.2, 0)  # Brown color
# Door handle (small black circle)
# context.set_source_rgb(0, 0, 0)  # Black color
# context.arc(215, 215, 3, 0, 2 * 3.14159)
# context.set_source_rgb(0.5, 0.8, 1)  # Light blue color for window
# context.set_source_rgb(0.3, 0.2, 0)  # Brown border for window

# Save the image
surface.write_to_png("colored_house.png")
