# https://adventofcode.com/2023/day/1
import logging
DAY = "day1"
NUMBERS_AS_STRING = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine") # zero?
NAS_FIRST_LETTERS = set(map(lambda x: x[0], NUMBERS_AS_STRING))
NAS_LAST_LETTERS = set(map(lambda x: x[-1], NUMBERS_AS_STRING))


def get_first_number(data_line):
  for position, char in enumerate(data_line):
    if char.isnumeric():
      return int(char)
      
    if char in NAS_FIRST_LETTERS:
      candidates = [x for x in NUMBERS_AS_STRING if x.startswith(char)]
      for candidate in candidates:
        if candidate == data_line[position: position + len(candidate)]:
          return(NUMBERS_AS_STRING.index(candidate))
          
  raise(Exception(f"No number found in {data_line}..."))
  return None


def get_last_number(data_line):
  for position, char in list(enumerate(data_line))[::-1]:
    if char.isnumeric():
      return int(char)
      
    if char in NAS_LAST_LETTERS:
      candidates = [x for x in NUMBERS_AS_STRING if x.endswith(char)]
      for candidate in candidates:
        if candidate == data_line[1 + position - len(candidate): 1 + position]:
          return(NUMBERS_AS_STRING.index(candidate))
          
  raise(Exception(f"No number found in {data_line}..."))
  return None


def solve_b(data):
  """
  Will use other functions and classes (tbd) to solve part B of today.
  """
  result = solve_a(data)
  return 


def solve_a(data):
  """
  Will use other functions and classes (tbd) to solve part A of today.
  """
  values = list(10 * get_first_number(data_line) + \
    get_last_number(data_line) \
    for data_line in data)
  
  result = sum(values)
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

  partA = False  # Attempt to solve part A?
  partB = True  # Attempt to solve part B?
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
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
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
