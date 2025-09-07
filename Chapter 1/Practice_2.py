import os

path = r"C:\Users\Abdul Ahad\Downloads"  # use raw string to avoid \ escapes

try:
    files = os.listdir(path)
except FileNotFoundError:
    print(f"Path not found: {path!r}")
else:
    for item in files:
        print(item)
