from math import sin, cos, radians

from argparse import ArgumentParser

from PIL import Image, ImageDraw


def midpoint(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def drawGon(value, size=300):
    """Take a single 0 to 24 number and create a single image to composite"""

    img = Image.new("RGBA", (size, size))  # Create a new blank image

    a = size / 2
    lineWidth = int(size / 25)
    pa = (a + a, 0 + a)
    pb = (a * cos(radians(60)) + a, a * sin(radians(60)) + a)
    pc = (a * cos(radians(120)) + a, a * sin(radians(120)) + a)
    pd = (-a + a, 0 + a)
    pe = (a * cos(radians(240)) + a, a * sin(radians(240)) + a)
    pf = (a * cos(radians(300)) + a, a * sin(radians(300)) + a)
    cen = (a, a)

    # Setup a canvas
    draw = ImageDraw.Draw(img)

    # Draw our regular outlines
    cords = [
        pe,
        pf,
        pa,
        pb,
        pc,
        pd,
        pe,
        cen,
        pd,
    ]

    lastCord = cords[0]
    for cord in cords:
        draw.line([lastCord, cord], fill="black", width=lineWidth)
        lastCord = cord

    # Now we can draw the specific cords
    if value % 6 == 1:
        draw.polygon([pe, cen, pf], fill="black")  # Draw a 1
    if value % 6 == 2:
        draw.polygon([pf, cen, pa], fill="black")  # Draw a 2
    if value % 6 == 3:
        draw.polygon([pa, cen, pb], fill="black")  # Draw a 3
    if value % 6 == 4:
        draw.polygon([pb, cen, pc], fill="black")  # Draw a 4
    if value % 6 == 5:
        draw.polygon([pc, cen, pd], fill="black")  # Draw a 5

    # Special 4x6 symbols
    # (0 is blank)

    # Representation for 6
    if value >= 6 and value < 12:
        draw.line([pe, (pe[0], a)], fill="black", width=lineWidth)
    # Representation for 12
    if value >= 12 and value < 18:
        triCen = (pe[0], a / 1.5)  # Center of the little triangle
        draw.line([triCen, midpoint(pe, cen)], fill="black", width=lineWidth)
        draw.line([triCen, midpoint(pd, pe)], fill="black", width=lineWidth)
        draw.line([triCen, midpoint(pd, cen)], fill="black", width=lineWidth)
    # Representation for 18
    if value >= 18 and value < 24:
        quadCen = (pe[0], a / 1.75)  # Center of the little triangle
        draw.line([quadCen, pe], fill="black", width=lineWidth)
        draw.line([quadCen, midpoint(pd, pe)], fill="black", width=lineWidth)
        draw.line([quadCen, midpoint(pe, cen)], fill="black", width=lineWidth)
        draw.line([quadCen, midpoint(pd, cen)], fill="black", width=lineWidth)

    return img


def main():
    parser = ArgumentParser(prog="base24")

    parser.add_argument(
        "value",
        help="The base10 number to represent",
    )

    parser.add_argument(
        "output",
        help="The file to produce",
    )

    args = parser.parse_args()
    print("Hello, %s!" % args.value)

    for i in range(0, 24):
        drawGon(i).save(f"/tmp/base24/base24_{i}.png")


if __name__ == "__main__":
    main()
