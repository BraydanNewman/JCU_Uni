"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

HIGH_BOUNDARY = 90
MEDIUM_BOUNDARY = 50


def main():
    score = float(input("Enter score: "))
    print(results(score))
    print(results(random.randint(0, 100)))


def results(score):
    if 0 < score < 100:
        if score >= HIGH_BOUNDARY:
            return "Excellent"
        elif score >= 50:
            return "Pass"
        else:
            return "Bad"


if __name__ == "__main__":
    main()
