"""Task05: Input conversion and validation."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from milkrate import to_decimal, validate_entry
for raw in ["8.5", " 3 ", "abc", "NaN", "inf"]:
    try:
        print(repr(raw), "->", to_decimal(raw))
    except ValueError as e:
        print(repr(raw), "-> rejected:", e)
try:
    validate_entry("F1", 1, 7.1, 8.5, "Morning")
except ValueError as e:
    print("validate_entry:", e)
