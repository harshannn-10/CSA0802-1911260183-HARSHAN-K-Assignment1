"""Interactive command-line milk payment calculator (single entry or ten-day run)."""
from decimal import Decimal
from milkrate import (
    validate_entry, rate_per_litre, payout, ten_day_summary, to_decimal,
)


def read_decimal(prompt):
    """Read a finite decimal value; retry until the user enters a valid number."""
    while True:
        raw = input(prompt).strip()
        try:
            return to_decimal(raw)
        except ValueError:
            print("Invalid number. Enter a value such as 8.5.")


def read_month():
    """Read an optional month number (1-12); None means standard rates."""
    while True:
        raw = input("Month number (1-12; press Enter for standard rates): ").strip()
        if not raw:
            return None
        try:
            month = int(raw)
            if 1 <= month <= 12:
                return month
        except ValueError:
            pass
        print("Invalid month. Use 1 to 12.")


def read_entry():
    """Read and validate one milk entry. Retries until it is valid."""
    while True:
        litres = read_decimal("Milk quantity (litres): ")
        fat = read_decimal("Fat percentage: ")
        snf = read_decimal("SNF percentage: ")
        shift = input("Shift (Morning/Evening): ").strip()
        try:
            validate_entry("-", litres, fat, snf, shift)
            return litres, fat, snf, shift
        except ValueError as error:
            print("Invalid entry:", error, "- please re-enter.")


def single_entry():
    farmer_id = input("Farmer ID: ").strip()
    if not farmer_id:
        print("Invalid entry: Farmer ID cannot be empty.")
        return
    litres, fat, snf, shift = read_entry()
    month = read_month()
    rate = rate_per_litre(fat, snf, month)
    amount = payout(litres, fat, snf, month)
    print("\nPayment details")
    print(f"Farmer ID : {farmer_id}")
    print(f"Shift     : {shift.title()}")
    print(f"Rate/L    : ₹{rate:.2f}")
    print(f"Payment   : ₹{amount:.2f}")


def ten_day_run():
    farmer_id = input("Farmer ID: ").strip()
    if not farmer_id:
        print("Invalid entry: Farmer ID cannot be empty.")
        return
    month = read_month()
    entries = []
    print("Enter each collection for this farmer.")
    while True:
        entries.append(read_entry()[:3])
        if input("Add another entry? (y/n): ").strip().lower() != "y":
            break
    total_litres, payments, total = ten_day_summary(entries, month)
    print(f"\nFarmer {farmer_id}: {len(entries)} entries, {total_litres} L")
    for i, ((litres, fat, snf), pay) in enumerate(zip(entries, payments), 1):
        print(f"  {i:2}. {litres} L  fat {fat}  snf {snf}  -> ₹{pay:.2f}")
    bonus = "YES (> 500 L)" if total_litres > Decimal("500") else "no"
    print(f"Bonus applied: {bonus}")
    print(f"Ten-day total: ₹{total:.2f}")


def main():
    print("Ksheera Village Milk Co-operative — Payment Calculator")
    choice = input("1) Single entry  2) Ten-day total with bonus  [1/2]: ").strip()
    if choice == "2":
        ten_day_run()
    else:
        single_entry()


if __name__ == "__main__":
    main()
