# ============================================================
#  DAY 2 — PRACTICE EXERCISES
#  Control Flow: if/else, Loops, List Comprehensions
# ============================================================

# ─────────────────────────────────────────────
# EXERCISE 1: Grade Classifier
# ─────────────────────────────────────────────
# Given a list of student scores, print each score with its grade:
# >= 90 → "A", >= 80 → "B", >= 70 → "C", >= 60 → "D", else → "F"
# Also print how many students passed (grade != F)

scores = [92, 45, 78, 85, 61, 55, 90, 73, 48, 88]

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 2: FizzBuzz (Data Edition)
# ─────────────────────────────────────────────
# For numbers 1 to 30:
#   - If divisible by 3 AND 5 → print "DataAnalyst"
#   - If divisible by 3 only  → print "Data"
#   - If divisible by 5 only  → print "Analyst"
#   - Otherwise               → print the number

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 3: Sales Summary with Loop
# ─────────────────────────────────────────────
# Given this sales data, using a loop calculate:
# 1. Total revenue
# 2. Average revenue
# 3. Highest sale (and which product)
# 4. Lowest sale (and which product)
# 5. Number of products with revenue > 50000

sales = {
    "Laptop":   120000,
    "Phone":    45000,
    "Tablet":   78000,
    "Monitor":  22000,
    "Keyboard": 15000,
    "Headphones": 61000,
}

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 4: List Comprehension Workout
# ─────────────────────────────────────────────
# Use list comprehensions (NOT regular loops) for ALL of these:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["hello", "world", "python", "data", "analytics", "is", "fun"]
temperatures_c = [0, 20, 37, 100, -10, 25]

# 1. Get all even numbers from 'numbers'
# 2. Get squares of odd numbers from 'numbers'
# 3. Get words longer than 4 characters from 'words', in UPPERCASE
# 4. Convert celsius to fahrenheit: F = (C * 9/5) + 32
# 5. Get only positive temperatures (in Fahrenheit) from result of #4

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 5: Data Cleaning Loop
# ─────────────────────────────────────────────
# This list simulates raw data from a CSV (messy!)
# Clean it and build a proper list of valid numbers

raw_data = ["123", "45.6", "N/A", "78", "null", "200", "", "55.5", "NA", "90"]

# 1. Loop through raw_data
# 2. Skip values that are: "N/A", "null", "NA", or empty string ""
# 3. Convert valid ones to float
# 4. Store valid numbers in a clean list
# 5. Print: count of valid, count of skipped, and the clean list

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 6: Pattern Printer
# ─────────────────────────────────────────────
# Use nested loops to print these two patterns:

# Pattern A (triangle):
# *
# **
# ***
# ****
# *****

# Pattern B (multiplication table 1–5 x 1–5):
# 1  2  3  4  5
# 2  4  6  8  10
# 3  6  9  12 15
# ... etc

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 7: Running Statistics
# ─────────────────────────────────────────────
# Given daily website visitors for 2 weeks:
visitors = [1200, 1450, 980, 1600, 2100, 1800, 950,
            1100, 1350, 1250, 1700, 2200, 1900, 1050]

# Using loops (no built-in sum/max/min):
# 1. Calculate total visitors
# 2. Calculate average daily visitors
# 3. Find the highest day and its day number (Day 1, Day 2...)
# 4. Find the lowest day and its day number
# 5. Count days with above-average visitors
# 6. Print a simple bar chart using * symbol:
#    Day 1  | ************ (1 * per 100 visitors, rounded)
#    Day 2  | **************

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 8: Dictionary Comprehension + Logic
# ─────────────────────────────────────────────
# Given employee data:
employees = [
    {"name": "Alice",   "dept": "Sales",   "salary": 72000},
    {"name": "Bob",     "dept": "IT",      "salary": 95000},
    {"name": "Carol",   "dept": "Sales",   "salary": 68000},
    {"name": "David",   "dept": "HR",      "salary": 58000},
    {"name": "Eve",     "dept": "IT",      "salary": 105000},
    {"name": "Frank",   "dept": "HR",      "salary": 62000},
    {"name": "Grace",   "dept": "Sales",   "salary": 81000},
]

# 1. Create a list of names earning > $70,000 (list comprehension)
# 2. Create a dict: {name: salary} for IT department only (dict comprehension)
# 3. Using a loop, calculate average salary per department
# 4. Print which department has the highest average salary

# YOUR CODE HERE:


# ============================================================
#  SOLUTIONS
# ============================================================

def show_solutions():

    print("\n" + "="*55)
    print("SOLUTION 1: Grade Classifier")
    print("="*55)
    scores = [92, 45, 78, 85, 61, 55, 90, 73, 48, 88]
    passed = 0
    for s in scores:
        grade = "A" if s >= 90 else "B" if s >= 80 else "C" if s >= 70 else "D" if s >= 60 else "F"
        if grade != "F":
            passed += 1
        print(f"Score: {s} → Grade: {grade}")
    print(f"Passed: {passed}/{len(scores)}")

    print("\n" + "="*55)
    print("SOLUTION 2: FizzBuzz Data Edition")
    print("="*55)
    for n in range(1, 31):
        if n % 3 == 0 and n % 5 == 0:
            print("DataAnalyst")
        elif n % 3 == 0:
            print("Data")
        elif n % 5 == 0:
            print("Analyst")
        else:
            print(n)

    print("\n" + "="*55)
    print("SOLUTION 3: Sales Summary")
    print("="*55)
    sales = {"Laptop": 120000, "Phone": 45000, "Tablet": 78000,
             "Monitor": 22000, "Keyboard": 15000, "Headphones": 61000}
    total = 0
    high_product, high_val = "", 0
    low_product,  low_val  = "", float("inf")
    above_50k = 0
    for product, rev in sales.items():
        total += rev
        if rev > high_val: high_val, high_product = rev, product
        if rev < low_val:  low_val,  low_product  = rev, product
        if rev > 50000: above_50k += 1
    avg = total / len(sales)
    print(f"Total Revenue   : ${total:,}")
    print(f"Average Revenue : ${avg:,.2f}")
    print(f"Highest Sale    : {high_product} (${high_val:,})")
    print(f"Lowest Sale     : {low_product} (${low_val:,})")
    print(f"Products > $50k : {above_50k}")

    print("\n" + "="*55)
    print("SOLUTION 4: List Comprehensions")
    print("="*55)
    numbers = list(range(1, 11))
    words = ["hello", "world", "python", "data", "analytics", "is", "fun"]
    temps_c = [0, 20, 37, 100, -10, 25]
    print([n for n in numbers if n % 2 == 0])
    print([n**2 for n in numbers if n % 2 != 0])
    print([w.upper() for w in words if len(w) > 4])
    temps_f = [(c * 9/5) + 32 for c in temps_c]
    print(temps_f)
    print([f for f in temps_f if f > 32])

    print("\n" + "="*55)
    print("SOLUTION 5: Data Cleaning")
    print("="*55)
    raw = ["123", "45.6", "N/A", "78", "null", "200", "", "55.5", "NA", "90"]
    invalid = {"N/A", "null", "NA", ""}
    clean = []
    skipped = 0
    for val in raw:
        if val in invalid:
            skipped += 1
        else:
            clean.append(float(val))
    print(f"Valid: {len(clean)} | Skipped: {skipped}")
    print(f"Clean data: {clean}")

    print("\n" + "="*55)
    print("SOLUTION 6: Patterns")
    print("="*55)
    print("Pattern A:")
    for i in range(1, 6):
        print("*" * i)
    print("Pattern B:")
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i*j:<3}", end="")
        print()

    print("\n" + "="*55)
    print("SOLUTION 7: Running Statistics")
    print("="*55)
    visitors = [1200,1450,980,1600,2100,1800,950,1100,1350,1250,1700,2200,1900,1050]
    total = 0
    for v in visitors: total += v
    avg = total / len(visitors)
    high_day = high_val = 0
    low_day  = 0; low_val = float("inf")
    above_avg = 0
    for i, v in enumerate(visitors):
        if v > high_val: high_val, high_day = v, i + 1
        if v < low_val:  low_val,  low_day  = v, i + 1
        if v > avg: above_avg += 1
    print(f"Total: {total:,} | Average: {avg:,.0f}")
    print(f"Highest: Day {high_day} ({high_val:,})")
    print(f"Lowest : Day {low_day} ({low_val:,})")
    print(f"Above average: {above_avg} days")
    print("\nBar Chart:")
    for i, v in enumerate(visitors):
        bar = "*" * round(v / 100)
        print(f"Day {i+1:>2} | {bar} ({v:,})")

    print("\n" + "="*55)
    print("SOLUTION 8: Employee Analysis")
    print("="*55)
    employees = [
        {"name": "Alice",   "dept": "Sales", "salary": 72000},
        {"name": "Bob",     "dept": "IT",    "salary": 95000},
        {"name": "Carol",   "dept": "Sales", "salary": 68000},
        {"name": "David",   "dept": "HR",    "salary": 58000},
        {"name": "Eve",     "dept": "IT",    "salary": 105000},
        {"name": "Frank",   "dept": "HR",    "salary": 62000},
        {"name": "Grace",   "dept": "Sales", "salary": 81000},
    ]
    high_earners = [e["name"] for e in employees if e["salary"] > 70000]
    it_salaries  = {e["name"]: e["salary"] for e in employees if e["dept"] == "IT"}
    dept_totals  = {}
    dept_counts  = {}
    for e in employees:
        d = e["dept"]
        dept_totals[d] = dept_totals.get(d, 0) + e["salary"]
        dept_counts[d] = dept_counts.get(d, 0) + 1
    dept_avg = {d: dept_totals[d] / dept_counts[d] for d in dept_totals}
    best_dept = max(dept_avg, key=dept_avg.get)
    print(f"Earners > $70k : {high_earners}")
    print(f"IT Salaries    : {it_salaries}")
    print("Avg by Dept    :")
    for dept, avg in dept_avg.items():
        print(f"  {dept:<8}: ${avg:,.2f}")
    print(f"Highest Avg    : {best_dept} (${dept_avg[best_dept]:,.2f})")


# Uncomment when ready to check answers:
# show_solutions()
