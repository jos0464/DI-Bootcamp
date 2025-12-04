# ==========================================
# Exercises XP+
# Last Updated: October 7th, 2025
# ==========================================

# ================================================================
# Exercise 1 : Student Grade Summary
# ================================================================

print("\n--- Exercise 1: Student Grade Summary ---")

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = {}
student_letter_grades = {}

# 1 - Calcul des moyennes et attribution des lettres
for name, grades in student_grades.items():
    avg = sum(grades) / len(grades)
    student_averages[name] = avg

    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    else:
        letter = "F"

    student_letter_grades[name] = letter

# 2 - Calcul de la moyenne de la classe
class_average = sum(student_averages.values()) / len(student_averages)

# 3 - Affichage du résumé
print("\nStudent Grade Report:")
for name in student_grades.keys():
    print(f"{name}: Average = {student_averages[name]:.2f}, Grade = {student_letter_grades[name]}")

print(f"\nClass Average: {class_average:.2f}")

# Résumé final
print("\nDictionaries generated:")
print("student_averages =", student_averages)
print("student_letter_grades =", student_letter_grades)


# ================================================================
# Exercise 2 : Advanced Data Manipulation and Analysis
# ================================================================

print("\n--- Exercise 2: Advanced Data Manipulation and Analysis ---")

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# ------------------------------------------------
# 1 - Total Sales Calculation per Product
# ------------------------------------------------
total_sales = {}

for sale in sales_data:
    product = sale["product"]
    revenue = sale["price"] * sale["quantity"]
    total_sales[product] = total_sales.get(product, 0) + revenue

print("\nTotal Sales per Product:")
for product, total in total_sales.items():
    print(f"{product}: ${total}")

# ------------------------------------------------
# 2 - Customer Spending Profile
# ------------------------------------------------
customer_spending = {}

for sale in sales_data:
    customer_id = sale["customer_id"]
    revenue = sale["price"] * sale["quantity"]
    customer_spending[customer_id] = customer_spending.get(customer_id, 0) + revenue

print("\nTotal Spending per Customer:")
for cid, total in customer_spending.items():
    print(f"Customer {cid}: ${total}")

# ------------------------------------------------
# 3 - Add “total_price” to each transaction
# ------------------------------------------------
for sale in sales_data:
    sale["total_price"] = sale["price"] * sale["quantity"]

print("\nEnhanced Sales Data (with total_price):")
for sale in sales_data:
    print(sale)

# ------------------------------------------------
# 4 - High-Value Transactions (> $500)
# ------------------------------------------------
high_value_sales = sorted(
    [s for s in sales_data if s["total_price"] > 500],
    key=lambda x: x["total_price"],
    reverse=True
)

print("\nHigh-Value Transactions (> $500):")
for sale in high_value_sales:
    print(sale)

# ------------------------------------------------
# 5 - Customer Loyalty (more than one purchase)
# ------------------------------------------------
purchase_count = {}
for sale in sales_data:
    cid = sale["customer_id"]
    purchase_count[cid] = purchase_count.get(cid, 0) + 1

loyal_customers = [cid for cid, count in purchase_count.items() if count > 1]

print("\nLoyal Customers (more than one purchase):", loyal_customers)

# ------------------------------------------------
# 6 - Bonus Insights
# ------------------------------------------------
# Average transaction value per product
avg_transaction_value = {}
transaction_counts = {}

for sale in sales_data:
    product = sale["product"]
    total_price = sale["total_price"]
    avg_transaction_value[product] = avg_transaction_value.get(product, 0) + total_price
    transaction_counts[product] = transaction_counts.get(product, 0) + 1

for product in avg_transaction_value:
    avg_transaction_value[product] /= transaction_counts[product]

print("\nAverage Transaction Value per Product:")
for product, avg_value in avg_transaction_value.items():
    print(f"{product}: ${avg_value:.2f}")

# Most popular product by quantity sold
product_quantities = {}
for sale in sales_data:
    product = sale["product"]
    product_quantities[product] = product_quantities.get(product, 0) + sale["quantity"]

most_popular = max(product_quantities, key=product_quantities.get)
print(f"\nMost Popular Product: {most_popular} ({product_quantities[most_popular]} units sold)")

# ------------------------------------------------
# 7 - Insights Summary
# ------------------------------------------------
print("\nMarketing Insights:")
print("- Focus on promoting high-value products like Laptops and Smartphones.")
print("- Reward loyal customers:", loyal_customers)
print("- Consider bundle offers on Headphones to increase Smartphone cross-sales.")
