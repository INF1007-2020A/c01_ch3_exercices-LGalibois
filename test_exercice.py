#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
    def test_average(self):
        values = [
            (2, 4, 6),
            (-1, 0, 1),
            (-1, -2, -4)
        ]

        output = [exercice.average(*v) for v in values]
        answer = [sum(v) / len(v) for v in values]

        self.assertListEqual(
            output,
            answer,
            'Mauvais calcul de la moyenne'
        )
    
    def test_to_radians(self):
        values = [
            (-5, 2, 0),
            (10.0, 4, 59),
            (360, 1, 3),
            (400, 55, 6)
        ]

        output = [exercice.to_radians(*v) for v in values]
        answer = [math.radians(v[0] + (v[1] + (v[2] / 60)) / 60) for v in values]

        self.assertListEqual(
            output,
            answer,
            'Mauvais calcul de degres -> radians'
        )

    def test_to_degrees(self):
        def __to_degrees(rad: float) -> tuple:
            degrees = math.degrees(rad)
            minutes = (degrees % 1) * 60
            seconds = (minutes % 1) * 60

            return degrees - minutes, minutes - seconds, seconds
            
        values = [2, -4, 5, 4.09]

        output = [exercice.to_degrees(v) for v in values]
        answer = [__to_degrees(v) for v in values]

        self.assertListEqual(
            output,
            answer,
            'Mauvais calcul de radians -> degres'
        )

    def test_to_celsius(self):
        values = [0, -25, 451]

        output = [exercice.to_celsius(v) for v in values]
        answer = [(v - 32) / 1.8 for v in values]

        self.assertListEqual(
            output,
            answer,
            'Mauvais calcul de farenheit -> celsius'
        )

    def test_to_farenheit(self):
        values = [0, -25, 451]

        output = [exercice.to_farenheit(v) for v in values]
        answer = [v * 1.8 + 32 for v in values]

        self.assertListEqual(
            output,
            answer,
            'Mauvais calcul de celsius -> farenheit'
        )


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
