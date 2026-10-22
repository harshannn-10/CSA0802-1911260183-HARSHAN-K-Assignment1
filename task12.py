"""Task12: Seasonal rates and bonus."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from milkrate import rate_per_litre, ten_day_payment
print("Jan 4.2/8.7 :", rate_per_litre("4.2","8.7",1))
print("Apr 4.2/8.7 :", rate_per_litre("4.2","8.7",4))
print("Apr 10 L, 500 L total:", ten_day_payment(10,"3.5","8.5",4,500))
print("Apr 10 L, 501 L total:", ten_day_payment(10,"3.5","8.5",4,501))
