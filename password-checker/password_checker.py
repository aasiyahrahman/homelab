#!/usr/bin/env python3
import re

def score_password(pw):
    score = 0
    if len(pw) >= 8:
        score += 1
    if re.search(r"[a-z]", pw):
        score += 1
    if re.search(r"[A-Z]", pw):
        score += 1
    if re.search(r"[0-9]", pw):
        score += 1
    if re.search(r"[!@#\$%\^&\*\(\)_\+\-=\[\]\{\};:'\",<\.>\/\?\\\|`~]", pw):
        score += 1
    return score

def strength_label(score): 
    return {0: "Very Weak", 1: "Weak", 2: "Okay", 3: "Good", 4: "Strong", 5: "Very Strong"}.get(score, "Unknown")

def main():
    pw = input("Enter password to check: ")
    s = score_password(pw)
    print(f"Score: {s}/5 - {strength_label(s)}")
    if s < 3:
        print("Tip: use at least 8 chars, mix upper/lower, numbers and symbols.")

if __name__ == "__main__":
    main()
