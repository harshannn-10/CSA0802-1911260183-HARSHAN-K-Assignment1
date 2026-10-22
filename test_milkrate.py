"""Automated regression tests for the milk payment calculator."""
import unittest
from decimal import Decimal
from milkrate import (rate_per_litre, payout, ten_day_total, validate_entry,
                      ten_day_payment, ten_day_summary)

class MilkRateTests(unittest.TestCase):
    def test_standard_rate(self):
        self.assertEqual(rate_per_litre("3.5", "8.5"), Decimal("30.00"))
    def test_above_standard(self):
        self.assertEqual(rate_per_litre("4.2", "8.7"), Decimal("33.40"))
        self.assertEqual(payout("8.5", "4.2", "8.7"), Decimal("283.90"))
    def test_below_standard(self):
        self.assertEqual(rate_per_litre("3.1", "8.3"), Decimal("27.80"))
        self.assertEqual(payout("12", "3.1", "8.3"), Decimal("333.60"))
    def test_fat_boundaries(self):
        self.assertTrue(validate_entry("F1", 1, 2.0, 8.5, "Morning"))
        self.assertTrue(validate_entry("F1", 1, 7.0, 8.5, "Evening"))
    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            validate_entry("F1", -1, 3.5, 8.5, "Morning")
    def test_invalid_fat(self):
        with self.assertRaises(ValueError):
            validate_entry("F1", 1, 7.1, 8.5, "Morning")
    def test_invalid_shift(self):
        with self.assertRaises(ValueError):
            validate_entry("F1", 1, 3.5, 8.5, "Night")
    def test_ten_day_total(self):
        self.assertEqual(ten_day_total(["300.00", "283.90", "333.60"]), Decimal("917.50"))
    def test_seasonal_rates(self):
        self.assertEqual(rate_per_litre("4.2", "8.7", 4), Decimal("35.75"))
        self.assertEqual(rate_per_litre("4.2", "8.7", 1), Decimal("33.40"))
    def test_bonus_strictly_over_500(self):
        self.assertEqual(ten_day_payment(10, 3.5, 8.5, 4, 500), Decimal("320.00"))
        self.assertEqual(ten_day_payment(10, 3.5, 8.5, 4, 501), Decimal("325.00"))

    def test_non_numeric_and_nan_rejected_as_valueerror(self):
        for bad in ("abc", "NaN", "Infinity"):
            with self.assertRaises(ValueError):
                validate_entry("F1", 1, bad, 8.5, "Morning")
            with self.assertRaises(ValueError):
                validate_entry("F1", bad, 3.5, 8.5, "Morning")

    def test_empty_farmer_id(self):
        with self.assertRaises(ValueError):
            validate_entry("  ", 1, 3.5, 8.5, "Morning")

    def test_ten_day_summary_bonus(self):
        litres, pays, total = ten_day_summary([(300, 3.5, 8.5), (201, 3.5, 8.5)])
        self.assertEqual(litres, Decimal("501"))
        self.assertEqual(total, Decimal("15030.00") + Decimal("250.50"))
        litres, pays, total = ten_day_summary([(250, 3.5, 8.5), (250, 3.5, 8.5)])
        self.assertEqual(total, Decimal("15000.00"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
