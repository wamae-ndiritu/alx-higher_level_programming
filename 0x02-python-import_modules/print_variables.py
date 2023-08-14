#!/usr/bin/python3

# Executed both  directly as a standalone script and when imported
from variable_load_5 import a

print(f"Variable a executed on import: {a}")

if __name__ == "__main__":
    # Executed only as a standalone script
    from variable_load_5 import a
    print(f"Variable a executed directly: {a}")
