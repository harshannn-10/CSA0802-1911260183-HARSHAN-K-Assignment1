"""Task02: Types and monetary precision."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from decimal import Decimal
print(type(1), type(1.5), type("x"), type(True), type([1]))
print("7/2 =", 7/2, " 7//2 =", 7//2, " 7%2 =", 7%2)
print("0.1+0.2 == 0.3 ->", 0.1+0.2 == 0.3)
print("Decimal('0.1')+Decimal('0.2') == Decimal('0.3') ->", Decimal("0.1")+Decimal("0.2") == Decimal("0.3"))
