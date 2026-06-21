# ============================================================
#  DAY 2 — Control Flow: if/else, Loops, List Comprehensions
#  Python for Data Analytics — Study Plan
# ============================================================

# ─────────────────────────────────────────────
# SECTION 1: if / elif / else
# ─────────────────────────────────────────────
# Decision making — the backbone of data filtering logic

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")       # ← this runs
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# ── Nested if ──
age = 25
income = 55000

if age >= 18:
    if income >= 50000:
        print("Eligible for premium card")
    else:
        print("Eligible for basic card")
else:
    print("Not eligible")

# ── Ternary (one-line if/else) ──
# value_if_true  if  condition  else  value_if_false
status = "Adult" if age >= 18 else "Minor"
print(status)

# ── Real analytics use case: categorize a value ──
revenue = 120000

category = (
    "High"   if revenue >= 100000 else
    "Medium" if revenue >= 50000  else
    "Low"
)
print(f"Revenue Category: {category}")   # High

# ── Checking None / missing values (critical in data work) ──
value = None

if value is None:
    print("Missing value — handle before analysis")
elif value == 0:
    print("Value is zero")
else:
    print(f"Value: {value}")

# ─────────────────────────────────────────────
# SECTION 2: for LOOPS
# ─────────────────────────────────────────────
# Iterating over data — you'll use this constantly

# Basic for loop over a list
sales = [1200, 3400, 890, 5600, 2300]

for sale in sales:
    print(sale)

# ── range() ──
# range(stop)          → 0 to stop-1
# range(start, stop)   → start to stop-1
# range(start, stop, step)

for i in range(5):
    print(i)        # 0 1 2 3 4

for i in range(1, 6):
    print(i)        # 1 2 3 4 5

for i in range(0, 10, 2):
    print(i)        # 0 2 4 6 8

# ── enumerate() — gives index + value (use instead of range(len())) ──
products = ["Laptop", "Phone", "Tablet"]

for index, product in enumerate(products):
    print(f"{index + 1}. {product}")
# 1. Laptop
# 2. Phone
# 3. Tablet

# ── zip() — loop over two lists together ──
products = ["Laptop", "Phone", "Tablet"]
prices   = [999,      499,     299    ]

for product, price in zip(products, prices):
    print(f"{product}: ${price}")

# ── Looping over a dictionary ──
monthly_sales = {"Jan": 45000, "Feb": 38000, "Mar": 52000}

for month, amount in monthly_sales.items():
    print(f"{month}: ${amount:,}")

# Keys only
for month in monthly_sales.keys():
    print(month)

# Values only
for amount in monthly_sales.values():
    print(amount)

# ── break and continue ──
# break  → stop the loop entirely
# continue → skip current iteration, go to next

numbers = [10, 25, 3, 48, 7, 60]

# Find first number > 40
for num in numbers:
    if num > 40:
        print(f"Found: {num}")
        break               # stops at 48

# Skip negative values (common in data cleaning)
data = [10, -5, 20, -3, 15]

for val in data:
    if val < 0:
        continue            # skip negatives
    print(val)              # prints 10, 20, 15

# ── Accumulating results in a loop ──
sales = [1200, 3400, 890, 5600, 2300]
total = 0
count = 0

for sale in sales:
    total += sale
    count += 1

average = total / count
print(f"Total: ${total:,} | Average: ${average:,.2f}")

# ─────────────────────────────────────────────
# SECTION 3: while LOOPS
# ─────────────────────────────────────────────
# Runs as long as a condition is True
# Use when you don't know how many iterations needed

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1              # ALWAYS update the condition or you get infinite loop!

# ── Practical: keep prompting until valid input ──
# (uncomment to try)
# while True:
#     age = input("Enter age (must be positive): ")
#     if age.isdigit() and int(age) > 0:
#         print(f"Age accepted: {age}")
#         break
#     print("Invalid. Try again.")

# ── while with a counter — processing in batches ──
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
batch_size = 3

while index < len(items):
    batch = items[index : index + batch_size]
    print(f"Processing batch: {batch}")
    index += batch_size

# ─────────────────────────────────────────────
# SECTION 4: LIST COMPREHENSIONS ← very important in analytics
# ─────────────────────────────────────────────
# A fast, Pythonic way to create lists
# Syntax: [expression  for  item  in  iterable  if  condition]

# Regular loop vs list comprehension:

# Old way:
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print(squares)      # [1, 4, 9, 16, 25]

# List comprehension way (same result, one line):
squares = [n ** 2 for n in range(1, 6)]
print(squares)      # [1, 4, 9, 16, 25]

# ── With a condition (filter) ──
numbers = [10, 25, 3, 48, 7, 60, 15, 42]

# Get only numbers greater than 20
big_numbers = [n for n in numbers if n > 20]
print(big_numbers)      # [25, 48, 60, 42]

# ── Transform + filter together ──
prices = [100, 250, 80, 320, 150]
discounted = [p * 0.9 for p in prices if p > 100]
print(discounted)       # [225.0, 288.0, 135.0]

# ── String list comprehension ──
names = ["alice", "bob", "charlie", "diana"]
upper_names = [name.upper() for name in names]
print(upper_names)

# ── Conditional expression in comprehension ──
scores = [85, 42, 91, 60, 75, 38]
grades = ["Pass" if s >= 60 else "Fail" for s in scores]
print(grades)   # ['Pass', 'Fail', 'Pass', 'Pass', 'Pass', 'Fail']

# ── Flatten a nested list ──
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [val for row in matrix for val in row]
print(flat)     # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ── Dictionary comprehension (bonus!) ──
products = ["Laptop", "Phone", "Tablet"]
prices   = [999, 499, 299]
catalog  = {p: pr for p, pr in zip(products, prices)}
print(catalog)  # {'Laptop': 999, 'Phone': 499, 'Tablet': 299}

# ── Set comprehension ──
data = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {n ** 2 for n in data}
print(unique_squares)   # {1, 4, 9, 16}

# ─────────────────────────────────────────────
# SECTION 5: NESTED LOOPS
# ─────────────────────────────────────────────
# Loop inside a loop — useful for matrices and combinations

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="  ")
    print()     # newline after each row

# ── Real analytics: cross-tabulation ──
regions   = ["North", "South", "East"]
quarters  = ["Q1", "Q2", "Q3"]

for region in regions:
    for quarter in quarters:
        print(f"{region} - {quarter}")

# ─────────────────────────────────────────────
# SECTION 6: REAL-WORLD ANALYTICS EXAMPLES
# ─────────────────────────────────────────────

# ── Example 1: Categorize sales data ──
sales_data = [
    {"product": "Laptop",  "revenue": 120000},
    {"product": "Phone",   "revenue": 45000},
    {"product": "Tablet",  "revenue": 78000},
    {"product": "Monitor", "revenue": 22000},
]

for item in sales_data:
    rev = item["revenue"]
    if rev >= 100000:
        label = "High"
    elif rev >= 50000:
        label = "Medium"
    else:
        label = "Low"
    print(f"{item['product']:<10} | ${rev:>8,} | {label}")

# ── Example 2: Find outliers ──
values = [12, 15, 14, 10, 200, 13, 11, 180, 9, 14]
mean   = sum(values) / len(values)
threshold = mean * 2

outliers = [v for v in values if v > threshold]
normal   = [v for v in values if v <= threshold]

print(f"Mean: {mean:.1f}")
print(f"Outliers: {outliers}")
print(f"Clean data: {normal}")

# ── Example 3: Running total (cumulative sum) ──
monthly = [10000, 15000, 12000, 18000, 22000]
cumulative = []
running_total = 0

for amount in monthly:
    running_total += amount
    cumulative.append(running_total)

print(f"Monthly:    {monthly}")
print(f"Cumulative: {cumulative}")

# ─────────────────────────────────────────────
# KEY TAKEAWAYS
# ─────────────────────────────────────────────
# 1. if/elif/else — decision making and data categorization
# 2. Ternary: value = A if condition else B  (one-line if)
# 3. for loops — iterate over any sequence
# 4. enumerate() — get index + value together
# 5. zip() — loop over multiple lists in parallel
# 6. while — repeat until condition is False
# 7. break / continue — control loop flow
# 8. List comprehension — [expr for x in iterable if condition]
# 9. Dict comprehension — {k: v for k, v in iterable}
# 10. Always prefer list comprehensions over loops when building lists
