import unittest
from event_log_user_report import Event, get_event_date, current_users, generate_report
import sys
from io import StringIO

class TestEventProcessing(unittest.TestCase):

    def test_event_processing(self):
        # Create sample events
        events = [
            Event("2023-01-01", "login", "Machine1", "User1"),
            Event("2023-01-02", "login", "Machine2", "User2"),
            Event("2023-01-03", "login", "Machine1", "User3"),
            Event("2023-01-04", "logout", "Machine2", "User2"),
            Event("2023-01-05", "logout", "Machine1", "User1"),
        ]

        # Test get_event_date function
        self.assertEqual(get_event_date(events[0]), "2023-01-01")

        # Test current_users function
        machines_result = current_users(events)
        expected_result = {'Machine1': {'User3'}, 'Machine2': set()}
        self.assertEqual(machines_result, expected_result)

        # Test generate_report function
        # Redirect stdout to capture print output
       
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        generate_report(machines_result)
        output = sys.stdout.getvalue().strip()

        # Reset redirect.
        sys.stdout = original_stdout

        expected_output = "Machine1: User3\nMachine2:"

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
