from tempfile import gettempdir
from os.path import join as path_join
import re
from uk_covid19 import Cov19API
from uk_covid19.exceptions import FailedRequestError
import unittest

all_nations = [
    'areaType=nation'
]
test_structure = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate"
}

class TestCov9Api(unittest.TestCase):
    def setUp(self) -> None:
        self.api = Cov19API(
            filters=all_nations,
            structure=test_structure
        )


    def test_api_params(self) -> None:
        from json import dumps

        api_params = {
            "filters": str.join(";", all_nations),
            "structure": dumps(test_structure, separators=(",", ":")),
        }

        self.assertDictEqual(self.api.api_params, api_params)

    def test_last_update(self):
        last_update = self.api.last_update
        self.assertIn("Z", last_update)

    def test_head(self):
        data = self.api.head()
        self.assertIn("Content-Location", data)
        self.assertIn("Last-Modified", data)

    def test_get_csv(self):
        data = self.api.get_csv()
        self.assertIsInstance(data, str)
        self.assertGreater(len(data.split()), 10)
        self.assertEqual(data.split()[0], str.join(",", test_structure.keys()))

        temp_dir = gettempdir()
        temp_path = path_join(temp_dir, "test_data.csv")
        self.api.get_csv(save_as=temp_path)

        with open(temp_path, "r") as pointer:
            file_data = pointer.read().strip()

        self.assertEqual(data.strip(), file_data)

    def test_unsuccessful_request(self):
        bad_structure = {
            "date": "date",
            "areaName": "areaName",
            "areaCode": "areaCode",
            "newCasesByPublishDate": "newCasesByPublishDate",
            "cumCasesByPublishDate": "cumCasesByPublishDate",
            "newDeathsByDeathDate": "newDeathsByDeathDate",
            "cumDeathsByDeathDate": "cumDeathsByDeathDate",
            "newCases": "newCasesBySpecimen"
        }

        pattern = re.compile(r"404\s-\sNot Found.*'newCasesBySpecimenDate'", re.S | re.M)

        api = Cov19API(filters=all_nations,structure=bad_structure)
        with self.assertRaisesRegex(FailedRequestError, pattern):
            api.get_csv()

if __name__ == '__main__':
    unittest.main()