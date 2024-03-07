def read_file(filename):
  """Reads the contents of a text file and returns them as a string.

  Args:
    filename: The name of the text file to read.

  Returns:
    The contents of the file as a string.
  """
  try:
    with open(filename, 'r') as file:
      contents = file.read()
      return contents
  except FileNotFoundError:
    print(f"Error: The file '{filename}' could not be found.")
    return ""

def count_words(filename):
  """Counts the number of words in a text file and prints the word count to the console.

  Args:
    filename: The name of the text file to read.
  """
  try:
    with open(filename, 'r') as file:
      contents = file.read()
      word_count = len(contents.split())
      print(f"Word count: {word_count}")
  except FileNotFoundError:
    print(f"Error: The file '{filename}' could not be found.")

def character_count(text):
  """
  This function takes a string of text and returns a dictionary containing the number of times each character appears in the string.

  Args:
    text: The string of text to analyze.

  Returns:
    A dictionary containing the character counts.
  """
  character_counts = {}
  for char in text.lower():
    if char.isalpha():
      if char in character_counts:
        character_counts[char] += 1
      else:
        character_counts[char] = 1
  return character_counts

def generate_report(filename):
  """
  Reads the contents of a file, counts words and characters,
  and prints a formatted report to the console.

  Args:
    filename: The name of the text file to analyze.
  """
  contents = read_file(filename)
  if not contents:
    return

  word_count = len(contents.split())
  character_counts = character_count(contents)

  print("--- Begin report of", filename, "---")
  print(f"{word_count} words found in the document")
  print("The character counts:")
  for char, count in sorted(character_counts.items()):
    print(f"\tThe '{char}' character was found {count} times")
  print("--- End report ---")

# Generate report for the book
generate_report("books/frankenstein.txt")