"""Task06: Functions."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import milkrate
print([n for n in dir(milkrate) if callable(getattr(milkrate, n)) and not n.startswith("_") and n[0].islower()])
