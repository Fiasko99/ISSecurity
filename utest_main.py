import unittest
import datetime
import main


class CalcTest(unittest.TestCase):
    def test_count_months(self):
        self.assertEqual(main.count_months("12.12.2021", "12.12.2020"), 12)
        self.assertEqual(main.count_months("12.12.2024", "12.12.2020"), 48)
        self.assertEqual(main.count_months("12.12.2020", "12.12.2020"), 0)

    def test_date_format(self):
        self.assertEqual(main.date_format("12.12.2022"), datetime.date(2022, 12, 12))
        self.assertEqual(main.date_format("2020.12.12"), datetime.date(2022, 12, 12))
        self.assertEqual(main.date_format("12.2020.12"), datetime.date(2022, 12, 12))

    def test_mod_months(self):
        self.assertEqual(main.mod_days("12.12.2024"), datetime.timedelta(days=1651))
        self.assertEqual(main.mod_days("12.12.2224"), datetime.timedelta(days=74699))
        self.assertEqual(main.mod_days("05.06.2020"), datetime.timedelta(days=0))


if __name__ == '__main__':
    unittest.main()
