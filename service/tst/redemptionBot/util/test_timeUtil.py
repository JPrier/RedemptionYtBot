import unittest
from datetime import datetime, timezone
import redemptionBot.util.timeUtil as underTest


class TestTimeUtil(unittest.TestCase):
    def test_getCurrentTimestamp_success(self):
        expected = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        result = underTest.getCurrentTimestamp()

        self.assertEqual(result, expected)

    def test_addMinutesToTimestamp_singleHour_success(self):
        inputTime, inputDelta = "2024-11-21T09:00:00Z", 60
        expected = "2024-11-21T10:00:00Z"
        result = underTest.addMinutesToTimestamp(inputTime, inputDelta)

        self.assertEqual(result, expected)

    def test_addMinutesToTimestamp_singleMinute_success(self):
        inputTime, inputDelta = "2024-11-21T10:00:00Z", 1
        expected = "2024-11-21T10:01:00Z"
        result = underTest.addMinutesToTimestamp(inputTime, inputDelta)

        self.assertEqual(result, expected)

    def test_addMinutesToTimestamp_singleDay_success(self):
        inputTime, inputDelta = "2024-11-21T10:00:00Z", 1440
        expected = "2024-11-22T10:00:00Z"
        result = underTest.addMinutesToTimestamp(inputTime, inputDelta)

        self.assertEqual(result, expected)
