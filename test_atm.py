import unittest
from atm import ATM


class TestATM(unittest.TestCase):

    def setUp(self) -> None:
        self.atm = ATM()

    def test_initial_balance(self) -> None:
        self.assertEqual(self.atm.check_balance(), 0.0)

    def test_deposit(self) -> None:
        self.atm.deposit(100)
        self.assertEqual(self.atm.check_balance(), 100.0)

    def test_deposit_invalid(self) -> None:
        with self.assertRaises(ValueError):
            self.atm.deposit(-50)

    def test_withdraw(self) -> None:
        self.atm.deposit(200)
        self.atm.withdraw(50)
        self.assertEqual(self.atm.check_balance(), 150.0)

    def test_withdraw_insufficient_funds(self) -> None:
        with self.assertRaises(ValueError):
            self.atm.withdraw(100)

    def test_withdraw_invalid_amount(self) -> None:
        with self.assertRaises(ValueError):
            self.atm.withdraw(-10)


if __name__ == "__main__":
    unittest.main()
