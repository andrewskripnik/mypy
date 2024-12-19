"""
Module for comparing two JSON files and printing the differences.
"""

import json
import sys
from deepdiff import DeepDiff

def load_json(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    return json.load(file)

def compare_json(json1, json2):
  diff = DeepDiff(json1, json2, ignore_order=True)
  if diff:
    return diff
  return None

def main(file1, file2):
  json1 = load_json(file1)
  json2 = load_json(file2)
  
  differences = compare_json(json1, json2)
  if differences:
    print("The JSON files are different.")
    print(differences)
  else:
    print("The JSON files are identical.")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python compare.py <file1> <file2>")
  else:
    main(sys.argv[1], sys.argv[2])