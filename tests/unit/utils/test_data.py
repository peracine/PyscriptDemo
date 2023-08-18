import unittest
from datetime import datetime
from src.utils.data import get_timeseries

#>python -m unittest tests/unit/utils/test_data.py
class TestData(unittest.TestCase):
    def test_get_timeseries(self):
        result = get_timeseries(123, datetime(2000, 1, 1), datetime(2000, 12, 31))
        self.assertEqual(53, len(result), f'Invalid array length. Expected: 53, Actual: {len(result)}')

if __name__ == '__main__':
    unittest.main()