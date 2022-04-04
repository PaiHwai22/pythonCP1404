"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))

    while score < 0 or score > 100:
        print("invalid score")
        score = float(input("Enter score: "))
    print(judge_score(score))


def judge_score(score):
    if score >= 90:
        return "Excellent"
    elif 50 <= score < 90:
        return "Passable"
    else:
        return "Bad"


main()
