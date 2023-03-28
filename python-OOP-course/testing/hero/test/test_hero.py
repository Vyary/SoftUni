from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Test Hero", 10, 100, 100)
        self.enemy = Hero("Test Enemy", 10, 100, 100)

    def test_correct_initialization(self):
        self.assertEqual(self.hero.username, "Test Hero")
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 100)

    def test_battle_function_fighting_yourself_exception(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.hero)

        self.assertEqual(str(context.exception), "You cannot fight yourself")

    def test_battle_function_if_hero_health_is_zero(self):
        self.hero.health = 0

        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy)

        self.assertEqual(
            str(context.exception),
            "Your health is lower than or equal to 0. You need to rest",
        )

    def test_battle_function_if_hero_health_less_than_zero(self):
        self.hero.health = -20

        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy)

        self.assertEqual(
            str(context.exception),
            "Your health is lower than or equal to 0. You need to rest",
        )

    def test_battle_function_if_enemy_health_is_zero(self):
        self.enemy.health = 0

        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy)

        self.assertEqual(
            str(context.exception), "You cannot fight Test Enemy. He needs to rest"
        )

    def test_battle_function_if_enemy_health_is_less_than_zero(self):
        self.enemy.health = -20

        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy)

        self.assertEqual(
            str(context.exception), "You cannot fight Test Enemy. He needs to rest"
        )

    def test_battle_function_draw_case(self):
        self.hero.health = 10
        self.enemy.health = 10

        self.assertEqual(self.hero.battle(self.enemy), "Draw")

    def test_battle_function_if_hero_wins(self):
        self.hero.health = 10000

        self.assertEqual(self.hero.battle(self.enemy), "You win")
        self.assertEqual(self.hero.level, 11)
        self.assertEqual(self.hero.health, 9005)
        self.assertEqual(self.hero.damage, 105)

    def test_battle_function_if_hero_loses(self):
        self.enemy.health = 10000

        self.assertEqual(self.hero.battle(self.enemy), "You lose")
        self.assertEqual(self.enemy.level, 11)
        self.assertEqual(self.enemy.health, 9005)
        self.assertEqual(self.enemy.damage, 105)

    def test_string_representation(self):
        self.assertEqual(
            str(self.hero), "Hero Test Hero: 10 lvl\nHealth: 100\nDamage: 100\n"
        )


if __name__ == "__main__":
    main()
