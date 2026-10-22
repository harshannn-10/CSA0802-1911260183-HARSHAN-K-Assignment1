"""Task03: Constants."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import milkrate as m
for n in ("BASE_RATE","FAT_STEP_VALUE","SNF_STEP_VALUE","STANDARD_FAT","STANDARD_SNF","MIN_FAT","MAX_FAT",
          "SEASONAL_BASE_RATE","SEASONAL_FAT_STEP_VALUE","BONUS_THRESHOLD_LITRES","BONUS_PER_LITRE"):
    print(f"{n:26}= {getattr(m, n)}")
