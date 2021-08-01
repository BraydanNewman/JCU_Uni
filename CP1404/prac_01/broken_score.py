"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

HIGH_BOUNDARY = 90
MEDIUM_BOUNDARY = 50

score = float(input("Enter score: "))
if 0 < score < 100:
    if score >= HIGH_BOUNDARY:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Bad")