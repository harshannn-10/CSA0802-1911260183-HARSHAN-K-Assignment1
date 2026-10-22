"""Task04: Expressions: rate and payment."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from milkrate import rate_per_litre, payout
for litres, fat, snf in [(10,"3.5","8.5"),(8.5,"4.2","8.7"),(12,"3.1","8.3")]:
    print(litres, fat, snf, "-> rate", rate_per_litre(fat, snf), "pay", payout(litres, fat, snf))
