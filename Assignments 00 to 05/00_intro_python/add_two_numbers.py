def main():
  try:
    num1 = (input("Enter the first number"))
    num1 = int(num1)
    num2 = (input("Enter the second number"))
    num2 = int(num2)
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")
  except ValueError:
    print("Invalid input! Please enter number only.")  
main()
