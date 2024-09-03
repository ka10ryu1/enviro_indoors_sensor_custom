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
        self.draw_text("Initializing...", font_size=20, y_pos=30)

        self.img = None
        self.draw = None

    def draw_text(self, text, font_size=25, y_pos=10, canvas_color=(0, 0, 0)):
        # Width and height to calculate text position.
        img_size = (self.disp.width, self.disp.height)

        # New canvas to draw on.
        self.img = Image.new("RGB", img_size, color=canvas_color)
        self.draw = ImageDraw.Draw(self.img)

        # Text settings.
        font = ImageFont.truetype(UserFont, font_size)
        text_color = (255, 255, 255)
        back_color = (0, 170, 170)

        # Draw background rectangle and write text.
        self.draw.rectangle((0, 0, 160, 80), back_color)
        self.draw.text((10, y_pos), text, font=font, fill=text_color)
        self.disp.display(self.img)
        return 0

    def display_clear(self):
        self.disp.set_backlight(0)
        return 0
