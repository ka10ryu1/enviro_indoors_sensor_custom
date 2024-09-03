#!/usr/bin/env python3

import logging
import time
import argparse
from pathlib import Path

from bme280 import BME280
from smbus2 import SMBus


def command():
    parser = argparse.ArgumentParser(description='温湿度気圧を取得する')
    parser.add_argument(
        '-a',
        '--average_num',
        type=int,
        default=3,
        metavar='COUNT',
        help='平均値を取得するための計測階数 [default:%(default)s]',
    )
    parser.add_argument(
        '-i',
        '--interval',
        type=int,
        default=5,
        metavar='TIME',
        help='計測する間隔（秒） [default:%(default)s]',
    )
    return parser.parse_args()


def mean(a: list):
    return sum(a) / len(a)


def get_value(bme, cnt: int, interval: int):
    temperature = []
    pressure = []
    humidity = []
    for _ in range(cnt):
        temperature.append(bme.get_temperature())
        pressure.append(bme.get_pressure())
        humidity.append(bme.get_humidity())
        time.sleep(interval)

    return mean(temperature), mean(pressure), mean(humidity)


def main(args):

    bus = SMBus(1)
    bme280 = BME280(i2c_dev=bus)

    while True:
        temperature, pressure, humidity = get_value(bme280, args.average_num, args.interval)
        logging.info(
            f"""Temperature: {temperature:05.2f} °C
            Pressure: {pressure:05.2f} hPa
            Relative humidity: {humidity:05.2f} %
            """
        )


if __name__ == '__main__':
    logging.basicConfig(
        format="%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.info(
        """weather.py - Print readings from the BME280 weather sensor.
    Press Ctrl+C to exit!
    """
    )
    main(command())
