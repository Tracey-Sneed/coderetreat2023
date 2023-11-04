
def main():
  print("Hello Welcome to Code Retreat 2023")
  name = input("What is your name?")
  try:
    print(f"Hello {name}!, welcome to Code Retreat 2023")
  except ValueError:
    print("invalid input")
    pass
