# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get user input
try:
    user_input = int(input("Enter a non-negative integer to calculate its factorial: "))
    
    # Check if the input is non-negative
    if user_input < 0:
        print("Sorry, factorial does not exist for negative numbers.")
    else:
        # Calculate and print factorial
        print(f"The factorial of {user_input} is {factorial(user_input)}.")
        
except ValueError:
    print("Invalid input! Please enter a non-negative integer.")
