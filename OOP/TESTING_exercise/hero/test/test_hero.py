from unittest import TestCase

from TESTING_exercise.hero.project.hero import Hero
# from project.hero import Hero


class HeroTest(TestCase):

    def setUp(self):
        self.hero = Hero("Kotodae", 1, 100, 50)
        self.enemy_hero = Hero('Enemy', 1, 50, 25)

    def test_correct_initialization(self):
        self.assertEqual('Kotodae', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(50, self.hero.damage)

    def test_raise_exception_enemy_name_equals_hero_name(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_raise_value_error_hero_health_too_low_for_battle(self):
        with self.assertRaises(ValueError) as ve:
            self.hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_raise_value_error_enemy_hero_health_too_low_for_battle(self):
        with self.assertRaises(ValueError) as ve:
            self.enemy_hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test_correct_hero_health_change_after_battle(self):
        self.hero.battle(self.enemy_hero)
        self.assertEqual(80, self.hero.health)
        self.assertEqual(0, self.enemy_hero.health)

    def test_correct_stats_change_after_winning_battle(self):
        self.hero.battle(self.enemy_hero)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(80, self.hero.health)
        self.assertEqual(55, self.hero.damage)

    def test_correct_stats_change_after_losing_battle(self):
        self.enemy_hero.damage = 95
        self.enemy_hero.health = 100
        self.hero.battle(self.enemy_hero)
        self.assertEqual(2, self.enemy_hero.level)
        self.assertEqual(55, self.enemy_hero.health)
        self.assertEqual(100, self.enemy_hero.damage)

    def test_correct_draw_after_battle(self):
        self.hero.health = 1
        self.enemy_hero.health = 1
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("Draw", result)

    def test_correct_winning_message_after_battle(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You win", result)

    def test_correct_loosing_message_after_battle(self):
        self.hero.health = 10
        self.enemy_hero.health = 100
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You lose", result)

    def test_correct__str__method(self):
        result = self.hero.__str__()
        self.assertEqual("Hero Kotodae: 1 lvl\n"
                         "Health: 100\n"
                         "Damage: 50\n",
                         result
                         )
