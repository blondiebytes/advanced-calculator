class ScienceCalculator:
  def sin(self, angle):
    return math.sin(math.radians(angle))

  def cos(self, angle):
    return math.cos(math.radians(angle))

if __name__ == "__main__":
  calculator = ScientificCalculator()
  try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (sin, cos): ")
    if operator in {'sin', 'cos'}:
      angle = float(input("Enter the angle in degrees: "))
      result = getattr(calculator, operator)(angle)
    else:
      result = "Invalid operator"
    print(f"Result: {result}")

  except ValueError as e:
    print(f"Error: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
