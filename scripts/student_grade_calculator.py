# grade_module.py

# Requirements covered:
# - collect student name and marks (3 subjects)
# - compute total and average using arithmetic
# - conditional grade mapping:
#   Avg >= 85 -> A
#   70–84     -> B
#   50–69     -> C
#   < 50      -> Fail
# - function calculate_grade(...) returns the grade
# - neat printed results with formatting
# - comments and good naming
#---------------------------------------------------------------------------------------------------------------------------------------------------------


from typing import Tuple

def calculate_grade(avg: float) -> str:
    """
    Map average marks to grade per assignment rules.
    """
    if avg >= 85:
        return "A"
    elif 70 <= avg <= 84:
        return "B"
    elif 50 <= avg <= 69:
        return "C"
    else:
        return "Fail"

def read_mark(prompt: str) -> float:
    """
    Read one subject mark between 0 and 100 (inclusive).
    Re-prompts until valid.
    """
    while True:
        try:
            val = float(input(prompt))
            if 0 <= val <= 100:
                return val
            print("Enter a number from 0 to 100.")
        except ValueError:
            print("Invalid number. Try again.")

def compute_results(m1: float, m2: float, m3: float) -> Tuple[float, float, str]:
    """
    Return (total, average, grade).
    """
    total = m1 + m2 + m3
    avg = total / 3.0
    grade = calculate_grade(avg)
    return total, avg, grade

def main():
    print("Student Grade Calculator")
    name = input("Enter student name: ").strip() or "Unknown"

    s1 = read_mark("Enter marks for Subject 1: ")
    s2 = read_mark("Enter marks for Subject 2: ")
    s3 = read_mark("Enter marks for Subject 3: ")

    total, avg, grade = compute_results(s1, s2, s3)

    print("\nResult")
    print(f"Name   : {name}")
    print(f"Marks  : {s1:.1f}, {s2:.1f}, {s3:.1f}")
    print(f"Total  : {total:.2f}")
    print(f"Average: {avg:.2f}")
    print(f"Grade  : {grade}")

if __name__ == "__main__":
    main()
