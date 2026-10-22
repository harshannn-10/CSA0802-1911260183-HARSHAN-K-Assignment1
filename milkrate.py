"""Milk payment calculation module for the Ksheera Village Milk Co-operative.

Money is represented with Decimal. Rates are rounded to two decimal places.
The original design uses the standard rate card; the revised design also
supports April-June seasonal rates and a ten-day volume bonus.
"""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CENT = Decimal("0.01")
STEP_SIZE = Decimal("0.1")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
# SNF bounds were not specified in the brief; set and document these assumptions.
MIN_SNF = Decimal("0.0")
MAX_SNF = Decimal("20.0")

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
SEASONAL_BASE_RATE = Decimal("32.00")
SEASONAL_FAT_STEP_VALUE = Decimal("0.45")
BONUS_THRESHOLD_LITRES = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")

def to_decimal(value, name="Value"):
    """Convert to a finite Decimal or raise ValueError (never InvalidOperation)."""
    try:
        number = Decimal(str(value).strip())
    except (InvalidOperation, ValueError):
        raise ValueError(f"{name} must be a number.") from None
    if not number.is_finite():
        raise ValueError(f"{name} must be a finite number.")
    return number

def money(value):
    """Convert a value safely to Decimal and round to cents."""
    return Decimal(str(value)).quantize(CENT, rounding=ROUND_HALF_UP)

def nearest_step(value):
    """Round a Decimal step count to the nearest integer, half away from zero."""
    return int(value.quantize(Decimal("1"), rounding=ROUND_HALF_UP))

def get_rate_card(month=None):
    """Return a fresh rate card; April (4) through June (6) use seasonal rates."""
    if month is not None and 4 <= int(month) <= 6:
        return {
            "base": SEASONAL_BASE_RATE,
            "fat_step": SEASONAL_FAT_STEP_VALUE,
            "snf_step": SNF_STEP_VALUE,
        }
    return {
        "base": BASE_RATE,
        "fat_step": FAT_STEP_VALUE,
        "snf_step": SNF_STEP_VALUE,
    }

def validate_entry(farmer_id, litres, fat, snf, shift):
    """Raise ValueError if an entry violates the documented input rules."""
    if not str(farmer_id).strip():
        raise ValueError("Farmer ID cannot be empty.")
    litres = to_decimal(litres, "Milk quantity")
    fat = to_decimal(fat, "Fat")
    snf = to_decimal(snf, "SNF")
    if litres < 0:
        raise ValueError("Milk quantity cannot be negative.")
    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError(f"Fat must be between {MIN_FAT} and {MAX_FAT}.")
    if not MIN_SNF <= snf <= MAX_SNF:
        raise ValueError(f"SNF must be between {MIN_SNF} and {MAX_SNF}.")
    if str(shift).strip().lower() not in {"morning", "evening"}:
        raise ValueError("Shift must be Morning or Evening.")
    return True

def rate_per_litre(fat, snf, month=None):
    """Return the rate per litre, rounded to two decimal places."""
    fat, snf = to_decimal(fat, "Fat"), to_decimal(snf, "SNF")
    rates = get_rate_card(month)
    fat_steps = nearest_step((fat - STANDARD_FAT) / STEP_SIZE)
    snf_steps = nearest_step((snf - STANDARD_SNF) / STEP_SIZE)
    rate = (
        rates["base"]
        + Decimal(fat_steps) * rates["fat_step"]
        + Decimal(snf_steps) * rates["snf_step"]
    )
    return money(rate)

def payout(litres, fat, snf, month=None):
    """Return one entry's payment, rounded to cents."""
    litres = to_decimal(litres, "Milk quantity")
    if litres < 0:
        raise ValueError("Milk quantity cannot be negative.")
    return money(litres * rate_per_litre(fat, snf, month))

def ten_day_total(payments):
    """Return the sum of already-rounded payment amounts, rounded to cents."""
    return money(sum((to_decimal(p, "Payment") for p in payments), Decimal("0.00")))

def ten_day_payment(litres, fat, snf, month, ten_day_litres):
    """Calculate one entry's payment, including bonus when ten-day litres > 500."""
    litres = to_decimal(litres, "Milk quantity")
    total_litres = to_decimal(ten_day_litres, "Ten-day litres")
    if litres < 0 or total_litres < 0:
        raise ValueError("Milk quantity cannot be negative.")
    payment = litres * rate_per_litre(fat, snf, month)
    if total_litres > BONUS_THRESHOLD_LITRES:
        payment += litres * BONUS_PER_LITRE
    return money(payment)

def ten_day_summary(entries, month=None):
    """Summarise one farmer's entries for a ten-day period.

    entries: iterable of (litres, fat, snf) tuples. The bonus is decided from the
    period's total litres (strictly > 500 L) and applied to every entry.
    Returns (total_litres, list_of_payments, total_payment).
    """
    entries = [(to_decimal(l, "Milk quantity"), f, s) for l, f, s in entries]
    total_litres = sum((l for l, _, _ in entries), Decimal("0"))
    payments = [ten_day_payment(l, f, s, month, total_litres) for l, f, s in entries]
    return total_litres, payments, ten_day_total(payments)

if __name__ == "__main__":
    examples = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    for litres, fat, snf in examples:
        rate = rate_per_litre(fat, snf)
        print(f"{litres:5} L  fat {fat:>3}  snf {snf:>3}  rate {rate:.2f}  pay {payout(litres, fat, snf):.2f}")
