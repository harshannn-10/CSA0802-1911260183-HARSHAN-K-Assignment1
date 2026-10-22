"""Task07: Modules and __main__ guard."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import milkrate   # importing prints nothing
print("Imported milkrate silently; __name__ here is", __name__)
