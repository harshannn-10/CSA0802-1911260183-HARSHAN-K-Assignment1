"""Task10: float vs Decimal accumulation of Rs 33.40 payments (timed with perf_counter)."""
import time
from decimal import Decimal

RATE_STR = "33.40"

def float_total(n):
    total = 0.0
    for _ in range(n):
        total += 33.40
    return total

def decimal_total(n):
    total = Decimal("0.00")
    step = Decimal(RATE_STR)
    for _ in range(n):
        total += step
    return total

def main():
    print(f"{'Entries':>8} {'Expected':>16} {'Float total':>22} {'Float s':>10} {'Decimal total':>16} {'Decimal s':>10}")
    for n in (300, 6000, 150000):
        expected = Decimal(RATE_STR) * n
        t0 = time.perf_counter(); f = float_total(n); t1 = time.perf_counter()
        d = decimal_total(n); t2 = time.perf_counter()
        print(f"{n:>8} {expected:>16,.2f} {f:>22.10f} {t1-t0:>10.6f} {d:>16,.2f} {t2-t1:>10.6f}")

if __name__ == "__main__":
    main()
