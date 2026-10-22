"""Task01: Inputs, outputs, data types, assumptions."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print("Inputs : farmer ID (str), litres/fat/SNF (Decimal), shift (str), month (int, optional)")
print("Outputs: rate per litre, payment, ten-day total, or validation error")
print("Assumptions: fat 2.0-7.0, SNF 0.0-20.0 (assumed), half-up rounding, bonus only if > 500 L")
