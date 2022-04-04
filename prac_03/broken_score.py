"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("invalid score")
        score = float(input("Enter score: "))
    print(judge_score(score))
    print(generate_random_score())


def judge_score(score):
    """ Return a grade to score"""
    if score >= 90:
        return "Excellent"
    elif 50 <= score < 90:
        return "Passable"
    else:
        return "Bad"


def generate_random_score():
    """ return a random inclusive score"""
    score = random.randint(1, 100)
    return score


main()
