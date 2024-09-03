#!/usr/bin/env python3
import st7735
from fonts.ttf import RobotoMedium as UserFont
from PIL import Image, ImageDraw, ImageFont


class DisplayText:
    def __init__(self):
        # Create LCD class instance.
        self.disp = st7735.ST7735(
            port=0, cs=1, dc="GPIO9", backlight="GPIO12", rotation=270, spi_speed_hz=10_000_000
        )
        # Initialize display.
        self.disp.begin()

        self.img = None
        self.draw = None

    def draw_text(self, text, canvas_color=(0, 0, 0)):
        # Width and height to calculate text position.
        img_size = (self.disp.width, self.disp.height)

        # New canvas to draw on.
        self.img = Image.new("RGB", img_size, color=canvas_color)
        self.draw = ImageDraw.Draw(self.img)

        # Text settings.
        font_size = 25
        font = ImageFont.truetype(UserFont, font_size)
        text_color = (255, 255, 255)
        back_color = (0, 170, 170)

        x1, y1, x2, y2 = font.getbbox(text)
        size_x = x2 - x1
        size_y = y2 - y1

        # Calculate text position
        w, h = self.img.size
        x = (w - size_x) / 2
        y = (h / 2) - (size_y / 2)

        # Draw background rectangle and write text.
        self.draw.rectangle((0, 0, 160, 80), back_color)
        self.draw.text((x, y), text, font=font, fill=text_color)
        self.disp.display(self.img)
        return 0

    def display_clear(self):
        self.disp.set_backlight(0)
        return 0
