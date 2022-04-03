"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("invalid score")
    score = float(input("Enter score: "))
if score >= 90:
    print("Excellent")
elif 50 <= score < 90:
    print("Passable")
else:
    print("Bad")
