import unittest

from convert_to_geojson import dms_str_to_decimal

class TestDms(unittest.TestCase):
    def test_dms_str_to_decimal(self):
        self.assertEqual(
            dms_str_to_decimal(
                "45 deg 32' 59.17\" N, 73 deg 36' 53.00\" W'"),
            (45.549769, -73.614722))