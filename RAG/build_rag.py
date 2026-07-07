import os
import sys

print("Current working directory:", os.getcwd())
print("\nPython search path:")
for p in sys.path:
    print(p)


from chunking import build_vector_database

build_vector_database()