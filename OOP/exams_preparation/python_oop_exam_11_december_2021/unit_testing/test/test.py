# from exams_preparation.python_oop_exam_11_december_2021.unit_testing.project.team import Team
from decorators_09_not_done.project import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team('Gosho')
        self.second_team = Team('ASDC')

    def test_correct_initialization(self):
        self.assertEqual('Gosho', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_raising_value_error_name_setter_with_numbers(self):
        with self.assertRaises(ValueError) as ve:
            team = Team('Gosho99')
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_correct_add_member_method(self):
        members = {'Ivan': 22}
        result = self.team.add_member(**members)
        self.assertEqual({'Ivan': 22}, self.team.members)
        self.assertEqual("Successfully added: Ivan", result)

    def test_trying_to_add_member_that_is_already_in_members_list(self):
        members = {'Ivan': 22}
        self.team.add_member(**members)

        result = self.team.add_member(**members)
        self.assertEqual('Successfully added: ', result)

    def test_correct_remove_member_method(self):
        members = {'Ivan': 22}
        self.team.add_member(**members)
        result = self.team.remove_member('Ivan')
        self.assertEqual("Member Ivan removed", result)
        self.assertEqual({}, self.team.members)

    def test_incorrect_remove_member_method(self):
        members = {'Ivan': 22}
        self.team.add_member(**members)
        result = self.team.remove_member('Gosho')
        self.assertEqual("Member with name Gosho does not exist", result)
        self.assertEqual({'Ivan': 22}, self.team.members)

    def test__gt__return_true(self):
        self.team.add_member(**{'Ivan': 22, 'Petkan': 29})
        self.second_team.add_member(**{'Gosho': 23})
        result = self.team.__gt__(self.second_team)
        self.assertEqual(True, result)
        self.assertEqual({'Ivan': 22, 'Petkan': 29}, self.team.members)
        self.assertEqual({'Gosho': 23}, self.second_team.members)

    def test__gt__return_false(self):
        self.second_team.add_member(**{'Ivan': 22, 'Petkan': 29})
        self.team.add_member(**{'Gosho': 23})
        result = self.team.__gt__(self.second_team)
        self.assertEqual(False, result)
        self.assertEqual({'Ivan': 22, 'Petkan': 29}, self.second_team.members)
        self.assertEqual({'Gosho': 23}, self.team.members)

    def test__len__method(self):
        self.team.add_member(**{'Ivan': 22, 'Petkan': 29})
        result = self.team.__len__()
        self.assertEqual(2, result)
        self.assertEqual({'Ivan': 22, 'Petkan': 29}, self.team.members)

    def test__add__method(self):
        self.team.add_member(**{'Ivan': 22})
        self.second_team.add_member(**{'Petkan': 29})
        new_team = self.team.__add__(self.second_team)
        self.assertEqual('GoshoASDC', new_team.name)
        self.assertEqual({'Ivan': 22, 'Petkan': 29}, new_team.members)
        self.assertEqual("Team name: GoshoASDC\nMember: Petkan - 29-years old\nMember: Ivan - 22-years old", new_team.__str__())

    def test__str__method(self):
        self.team.add_member(**{'Petkan': 29})
        output = self.team.__str__()
        self.assertEqual("Team name: Gosho\nMember: Petkan - 29-years old", output)


if __name__ == '__main__':
    main()
