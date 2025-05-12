Python Conditional Expressions (Ternary Operator)
This repository demonstrates conditional expressions (ternary operators) in Python—a concise way to write if-else logic in a single line.

📌 Syntax
python
value_if_true if condition else value_if_false
🚀 Examples
1. Basic Usage
python
# Check if a number is even or odd  
num = 10  
result = "Even" if num % 2 == 0 else "Odd"  
print(result)  # Output: "Even"  
2. Comparing Values
python
# Find the maximum of two numbers  
a, b = 5, 8  
max_val = a if a > b else b  
print(max_val)  # Output: 8  
3. Nested Ternary
python
# Categorize a number as "Positive", "Negative", or "Zero"  
num = -3  
sign = "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")  
print(sign)  # Output: "Negative"  
4. Inline Usage (e.g., Function Arguments)
python
# Pass a default value based on a condition  
def greet(name):  
    return f"Hello, {name if name else 'Guest'}!"  

print(greet("Alice"))  # Output: "Hello, Alice!"  
print(greet(""))       # Output: "Hello, Guest!"  
🛠️ How to Run
Clone the repo:

bash
git clone https://github.com/your-username/python-conditional-expressions.git
Execute the examples:

bash
python ternary_operator.py
📜 License
This project is open-source under the MIT License.

Key Features of This README:
Clean formatting with emojis and code blocks.

Practical examples covering basic to nested usage.

Quick-run instructions for beginners.
