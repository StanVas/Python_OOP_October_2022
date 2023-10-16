from unittest import TestCase, main

from TESTING_exercise.student.project.student import Student
# from project.student import Student


class StudentTest(TestCase):

    def setUp(self):
        self.student = Student('Gosho')
        self.student_with_course = Student("Rapuncel", {'math': ['what is math']})

    def test_correct_initialization(self):
        self.assertEqual('Gosho', self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({'math': ['what is math']}, self.student_with_course.courses)

    def test_correct_add_notes_to_existing_course_with_enroll(self):
        self.student_with_course.enroll('math', ['math is not so bad', 'I love math'])
        self.assertEqual({'math': ['what is math', 'math is not so bad', 'I love math']}, self.student_with_course.courses)

    def test_correct_message_after_updating_notes_with_enroll(self):
        result = self.student_with_course.enroll('math', 'math is not so bad', "Y")
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_correct_message_after_adding_course_and_updating_notes_with_enroll_and_y(self):
        result = self.student_with_course.enroll('programming', 'fuck exel', "Y")
        self.assertEqual("Course and course notes have been added.", result)

    def test_correct_message_after_adding_course_and_updating_notes_with_enroll_and_empty_string(self):
        result = self.student_with_course.enroll('programming', 'fuck exel', "")
        self.assertEqual("Course and course notes have been added.", result)

    def test_correct_key_value_if_add_course_notes_is_different(self):
        result = self.student_with_course.enroll('programming', 'fuck exel', "N")
        self.assertEqual({'math': ['what is math'], 'programming': []}, self.student_with_course.courses)
        self.assertEqual("Course has been added.", result)

    def test_correct_add_notes_to_existing_course(self):
        result = self.student_with_course.add_notes('math', 'i love pi')
        self.assertEqual("Notes have been updated", result)

    def test_raise_exception_trying_to_add_notes_to_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('programming', 'idk programming')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_correct_leave_course(self):
        result = self.student_with_course.leave_course('math')
        self.assertEqual("Course has been removed", result)

    def test_raise_exception_trying_to_leave_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('english')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
