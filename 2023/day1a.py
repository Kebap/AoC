# https://adventofcode.com/2023/day/1
import logging
DAY = "day1"

def get_first_number(data_line):
  for char in data_line:
    if char.isnumeric():
      return int(char)
  return None


def get_last_number(data_line):
  for char in data_line[::-1]:
    if char.isnumeric():
      return int(char)
  return None


def solve_b(data):
  """
  Will use other functions and classes (tbd) to solve part B of today.
  """
  result = ...
  return f"{result} is the soltion here!"


def solve_a(data):
  """
  Will use other functions and classes (tbd) to solve part A of today.
  """
  result = ...
  result = sum(10 * get_first_number(data_line) + 
  get_last_number(data_line)
  for data_line in data)
  return f"{result} is the solution here!"


def sanitize_data_of_today(data_from_file: list) -> list:
  """
  Can be adjusted to further enhance puzzle data.
  Handy, if the data should not be just a simple string for each line.
  Does not create complex objects but only some sane lists, dicts, etc.
  Complex objects will be created from this in the solve_* functions.
  """
  sanitized_data = data_from_file # or modify before
  return sanitized_data 


def main(): 
  """
  Will solve puzzle A and/or B for example and/or real data.
  """  
  logging.basicConfig(filename=f'{DAY}.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

  partA = True  # Attempt to solve part A?
  partB = False # Attempt to solve part B?
  TestData = True  # Run with test data?
  RealData = True # Run with real data?

  if partA:
    if TestData:
      solution = solve_a(get_data(False))
      print(f"Solution for part A with example data is:\n{solution}\n")
    if RealData:
      solution = solve_a(get_data(True))
      print(f"Solution for part A with real data is:\n{solution}\n")

  if partB:
    if TestData:
      solution = solve_a(get_data(False))
      print(f"Solution for part B with example data is:\n{solution}\n")
    if RealData:
      solution = solve_a(get_data(True))
      print(f"Solution for part B with real data is:\n{solution}\n")


def get_data(use_real_input = False) -> list:
  """
  Reads either the example data given in this very function,
  or the real puzzle input data given in a file of its own.
  Will return a list of said data with each line as an item.
  """
  example_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
  if not use_real_input:
    used_input = example_input

  else:
    with open(f"input_data/{DAY}.txt", "r") as input_file:
      used_input = input_file.read()

  used_input = used_input.strip().split("\n")
  return sanitize_data_of_today(used_input)


if __name__ == "__main__":
  main()
