# ============================================================
#  DAY 1 — PRACTICE EXERCISES
#  Attempt each exercise yourself before looking at hints!
# ============================================================

# ─────────────────────────────────────────────
# EXERCISE 1: Create a Customer Profile
# ─────────────────────────────────────────────
# Create variables for a customer:
#   - name (string)
#   - age (int)
#   - account_balance (float)
#   - is_premium_member (bool)
#   - last_purchase (set it to None)
#
# Then print a summary using an f-string like:
# "Customer: Alice | Age: 30 | Balance: $1500.75 | Premium: True"

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 2: Type Inspector
# ─────────────────────────────────────────────
# Given these variables, print the type of each one using type()
# AND check using isinstance() if it is the correct type

data = [42, 3.14, "analyst", True, None]

# YOUR CODE HERE (loop through data and print type of each):


# ─────────────────────────────────────────────
# EXERCISE 3: Data Cleaning Simulation
# ─────────────────────────────────────────────
# In real data, numbers often come in as strings.
# Convert these and perform calculations:

units_str = "150"
price_str = "29.99"
discount_str = "0.15"

# 1. Convert all three to the correct numeric types
# 2. Calculate: total = units * price
# 3. Calculate: discounted_total = total - (total * discount)
# 4. Print: "Total: $XXXX.XX | After Discount: $XXXX.XX"

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 4: String Operations
# ─────────────────────────────────────────────
# Given this messy customer name from a database:
raw_name = "   john SMITH   "

# 1. Strip whitespace
# 2. Convert to proper title case (John Smith)
# 3. Split into first and last name
# 4. Print: "First: John | Last: Smith"

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 5: Sales Calculator
# ─────────────────────────────────────────────
# A store has:
#   - product = "Laptop"
#   - original_price = 1200
#   - discount_percent = 20
#   - tax_percent = 8
#   - quantity = 3

# Calculate and print:
#   1. Discount amount
#   2. Price after discount
#   3. Tax amount (on discounted price)
#   4. Final price per unit (after discount + tax)
#   5. Total for all units
#   Format all money values to 2 decimal places using f-strings

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 6: Eligibility Checker
# ─────────────────────────────────────────────
# Write conditions to check:
# A customer is eligible for a loan if:
#   - age >= 21
#   - income >= 30000
#   - credit_score >= 700
#   - has_existing_loan is False

age = 25
income = 45000
credit_score = 720
has_existing_loan = False

# 1. Create a boolean variable: is_eligible
# 2. Print: "Eligible for loan: True/False"
# 3. BONUS: print WHY they are not eligible if is_eligible is False

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 7: Modulo Magic
# ─────────────────────────────────────────────
# Use the modulo operator (%) to:
# 1. Check if 847 is even or odd
# 2. Check if 2025 is a leap year
#    (leap year: divisible by 4, but not 100, UNLESS also divisible by 400)
# 3. Find the remainder when 1000 is divided by 7

year = 2025
number = 847
value = 1000

# YOUR CODE HERE:


# ─────────────────────────────────────────────
# EXERCISE 8: Mini Analytics Report
# ─────────────────────────────────────────────
# Given monthly sales data as strings (as if read from a text file):
jan = "45000"
feb = "38000"
mar = "52000"

# 1. Convert all to integers
# 2. Calculate: total, average, highest month, lowest month
# 3. Print a formatted report:
#    === Q1 Sales Report ===
#    January  : $45,000
#    February : $38,000
#    March    : $52,000
#    ----------------------
#    Total    : $135,000
#    Average  : $45,000
#    Best Month: March

# YOUR CODE HERE:


# ============================================================
#  SOLUTIONS — only read after attempting!
# ============================================================

def show_solutions():

    print("\n" + "="*50)
    print("SOLUTION 1: Customer Profile")
    print("="*50)
    name = "Alice"
    age = 30
    account_balance = 1500.75
    is_premium_member = True
    last_purchase = None
    print(f"Customer: {name} | Age: {age} | Balance: ${account_balance} | Premium: {is_premium_member}")

    print("\n" + "="*50)
    print("SOLUTION 2: Type Inspector")
    print("="*50)
    data = [42, 3.14, "analyst", True, None]
    expected = [int, float, str, bool, type(None)]
    for val, exp in zip(data, expected):
        print(f"Value: {repr(val):12} | Type: {type(val).__name__:10} | isinstance check: {isinstance(val, exp)}")

    print("\n" + "="*50)
    print("SOLUTION 3: Data Cleaning")
    print("="*50)
    units = int("150")
    price = float("29.99")
    discount = float("0.15")
    total = units * price
    discounted = total - (total * discount)
    print(f"Total: ${total:,.2f} | After Discount: ${discounted:,.2f}")

    print("\n" + "="*50)
    print("SOLUTION 4: String Operations")
    print("="*50)
    raw = "   john SMITH   "
    clean = raw.strip().title()
    parts = clean.split()
    print(f"First: {parts[0]} | Last: {parts[1]}")

    print("\n" + "="*50)
    print("SOLUTION 5: Sales Calculator")
    print("="*50)
    product = "Laptop"
    original_price = 1200
    discount_percent = 20
    tax_percent = 8
    quantity = 3
    discount_amount = original_price * discount_percent / 100
    after_discount = original_price - discount_amount
    tax_amount = after_discount * tax_percent / 100
    final_price = after_discount + tax_amount
    total_price = final_price * quantity
    print(f"Product: {product}")
    print(f"Discount Amount   : ${discount_amount:.2f}")
    print(f"After Discount    : ${after_discount:.2f}")
    print(f"Tax Amount        : ${tax_amount:.2f}")
    print(f"Final Price/Unit  : ${final_price:.2f}")
    print(f"Total ({quantity} units)  : ${total_price:.2f}")

    print("\n" + "="*50)
    print("SOLUTION 6: Eligibility Checker")
    print("="*50)
    age = 25; income = 45000; credit_score = 720; has_existing_loan = False
    is_eligible = age >= 21 and income >= 30000 and credit_score >= 700 and not has_existing_loan
    print(f"Eligible for loan: {is_eligible}")

    print("\n" + "="*50)
    print("SOLUTION 7: Modulo Magic")
    print("="*50)
    print(f"847 is {'even' if 847 % 2 == 0 else 'odd'}")
    y = 2025
    is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    print(f"2025 is a leap year: {is_leap}")
    print(f"1000 % 7 = {1000 % 7}")

    print("\n" + "="*50)
    print("SOLUTION 8: Mini Analytics Report")
    print("="*50)
    jan, feb, mar = int("45000"), int("38000"), int("52000")
    total = jan + feb + mar
    avg = total // 3
    months = {"January": jan, "February": feb, "March": mar}
    best = max(months, key=months.get)
    print("=== Q1 Sales Report ===")
    for month, val in months.items():
        print(f"{month:<10}: ${val:,}")
    print("-" * 24)
    print(f"{'Total':<10}: ${total:,}")
    print(f"{'Average':<10}: ${avg:,}")
    print(f"Best Month: {best}")


# Uncomment the line below when ready to check your answers:
# show_solutions()
