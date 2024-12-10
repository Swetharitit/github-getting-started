import sys

def PowerOf2(n):
    print(f"Table of powers of 2 less than or equal to 2^{n}:")
    
    for i in range(n + 1):
        print(f"2^{i} = {2**i}")

# Main program: check if a command-line argument is provided
if len(sys.argv) != 2:
    print("Please provide a single integer argument for n.")
else:
    try:
        # Convert the command-line argument to an integer
        n = int(sys.argv[1])
        PowerOf2(n)
    except ValueError:
        print("Please provide a valid integer.")
