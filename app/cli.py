from math import sin, cos, radians

from argparse import ArgumentParser

from PIL import Image, ImageDraw


def drawGon(value, size=200):
    """Take a single 0 to 24 number and create a single image to composite"""

    img = Image.new("RGBA", (size, size))  # Create a new blank image

    a = size / 2
    pa = (a + a, 0 + a)
    pb = (a * cos(radians(60)) + a, a * sin(radians(60)) + a)
    pc = (a * cos(radians(120)) + a, a * sin(radians(120)) + a)
    pd = (-a + a, 0 + a)
    pe = (a * cos(radians(240)) + a, a * sin(radians(240)) + a)
    pf = (a * cos(radians(300)) + a, a * sin(radians(300)) + a)

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
        (a, a),  # Center
        pd,
    ]

    lastCord = cords[0]
    for cord in cords:
        print(cord)
        draw.line([lastCord, cord], fill="black", width=10)
        lastCord = cord

    # Now we can draw the specific cords
    draw.polygon([pa, pb, pc], fill="black")

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

    drawGon(5).save("/tmp/tmp.png")


if __name__ == "__main__":
    main()
