#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    return math.fsum([a, b, c]) / 3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return math.radians(angle_degs + angle_mins / 60 + angle_secs / 3600)


def to_degrees(angle_rads: float) -> tuple:
    degrees = math.degrees(angle_rads)
    degrees_mins = math.modf(degrees)[0] * 60
    degrees_secs = math.modf(degrees_mins)[0] * 60

    return int(degrees), int(degrees_mins), degrees_secs


def to_celsius(temperature: float) -> float:
    return (temperature - 32) / 1.8


def to_farenheit(temperature: float) -> float:
    return temperature * 1.8 + 32


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
