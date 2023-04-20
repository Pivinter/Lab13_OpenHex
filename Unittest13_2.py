import unittest
from Lab13_2_Opentable import *
class TestNote(unittest.TestCase):
    def test_note_init(self):
        note = Note("Іванов", "Іван", "1234567890", ["01", "01", "2000"])
        self.assertEqual(note.last_name, "Іванов")
        self.assertEqual(note.first_name, "Іван")
        self.assertEqual(note.phone_number, "1234567890")
        self.assertEqual(note.birth_date, ["01", "01", "2000"])

class TestOpenHashTable(unittest.TestCase):
    def setUp(self):
        self.table = OpenHashTable(10)
        self.note1 = Note("Іванов", "Іван", "1234567890", ["01", "01", "2000"])
        self.note2 = Note("Петров", "Петро", "0987654321", ["02", "02", "1990"])

    def test_insert(self):
        self.table.insert(self.note1)
        self.assertIn(self.note1, self.table.data)

    def test_find_by_criteria_name(self):
        self.table.insert(self.note1)
        found_notes = self.table.find_by_criteria("Імя", "Іванов")
        self.assertIn(self.note1, found_notes)

    def test_find_by_criteria_phone(self):
        self.table.insert(self.note1)
        found_notes = self.table.find_by_criteria("Телефон", "1234567890")
        self.assertIn(self.note1, found_notes)

    def test_find_by_criteria_birth_date(self):
        self.table.insert(self.note1)
        found_notes = self.table.find_by_criteria("Дата нородження", ["01", "01", "2000"])
        self.assertIn(self.note1, found_notes)

    def test_remove_by_criteria_phone(self):
        self.table.insert(self.note1)
        removed = self.table.remove_by_criteria("Телефон", "1234567890")
        self.assertTrue(removed)
        self.assertNotIn(self.note1, self.table.data)

    def test_remove_by_criteria_birth_date(self):
        self.table.insert(self.note1)
        removed = self.table.remove_by_criteria("Дата нородження", ["01", "01", "2000"])
        self.assertTrue(removed)
        self.assertNotIn(self.note1, self.table.data)
if __name__ == '__main__':
    unittest.main()
