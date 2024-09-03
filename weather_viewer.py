#!/usr/bin/env python3

import logging
import time
import argparse
from pathlib import Path

from bme280 import BME280
from smbus2 import SMBus

from weather_custom import command, device_setup, get_value
from display_text import DisplayText


def main(args):

    bme280 = device_setup()
    display = DisplayText()
    # 最初の値は捨てる
    get_value(bme280, 2, 1)
    logging.info("Setup finished. Start reading values...")
    display.draw_text("Setup finished.", y_pos=30)

    try:
        while True:
            temperature, pressure, humidity = get_value(bme280, args.average_num, args.interval)
            logging.info(
                f"Temperature: {temperature:5.2f} °C / Pressure: {pressure:7.2f} hPa / Relative humidity: {humidity:5.2f} %"
            )
            display.draw_text(f"{int(temperature)} °C / {int(humidity)} %\n{int(pressure)} hPa")

    except KeyboardInterrupt:
        logging.info("Exit.")
        display.display_clear()


if __name__ == '__main__':
    logging.basicConfig(
        format="%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.info(
        "weather.py - Print readings from the BME280 weather sensor. Press Ctrl+C to exit!"
    )
    main(command())
