import cairo

def draw_grid(context, width, height, spacing=50):
    """
    Draws a grid with coordinate labels on the given Cairo context.

    Parameters:
    - context: Cairo context to draw on.
    - width: Width of the drawing surface.
    - height: Height of the drawing surface.
    - spacing: Distance between grid lines (default is 50).
    """
    # Set grid line color
    context.set_source_rgb(0.9, 0.9, 0.9)  # Light gray color for grid lines

    # Draw vertical grid lines
    for x in range(0, width, spacing):
        context.move_to(x, 0)
        context.line_to(x, height)
        context.stroke()

    # Draw horizontal grid lines
    for y in range(0, height, spacing):
        context.move_to(0, y)
        context.line_to(width, y)
        context.stroke()

    # Set font for labels
    context.set_source_rgb(0, 0, 0)  # Black color for text
    context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    context.set_font_size(10)

    # Draw coordinate labels
    for x in range(0, width, spacing):
        for y in range(0, height, spacing):
            label = f"({x},{y})"
            context.move_to(x + 2, y + 12)  # Offset text slightly for readability
            context.show_text(label)


# Main drawing setup
width, height = 1000, 800
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Background color
context.set_source_rgb(1, 1, 1)  # White background
context.paint()

draw_grid(context, width, height)

surface.write_to_png("grid.png")
print("Grid with labels added and saved as 'grid.png'")
