from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("John")

    def test_init(self):
        self.assertEqual(self.student.name, "John")
        self.assertEqual(self.student.courses, {})

    def test_enroll(self):
        self.student.enroll("Math", ["note1", "note2"])
        self.assertEqual(self.student.courses["Math"], ["note1", "note2"])

    def test_enroll_existing_course(self):
        self.student.enroll("Math", ["note1", "note2"])
        result = self.student.enroll("Math", ["note3"])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses["Math"], ["note1", "note2", "note3"])

    def test_enroll_with_add_course_notes(self):
        result = self.student.enroll("Math", ["note1", "note2"], add_course_notes="Y")
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["Math"], ["note1", "note2"])

    def test_enroll_without_add_course_notes(self):
        result = self.student.enroll("Math", ["note1", "note2"], add_course_notes="N")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.student.courses["Math"], [])

    def test_add_notes(self):
        self.student.enroll("Math", ["note1", "note2"])
        result = self.student.add_notes("Math", "note3")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student.courses["Math"], ["note1", "note2", "note3"])

    def test_add_notes_non_existent_course(self):
        with self.assertRaises(Exception):
            self.student.add_notes("Math", "note3")

    def test_leave_course(self):
        self.student.enroll("Math", ["note1", "note2"])
        result = self.student.leave_course("Math")
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(self.student.courses, {})

    def test_leave_non_existent_course(self):
        with self.assertRaises(Exception):
            self.student.leave_course("Math")


if __name__ == "__main__":
    main()
