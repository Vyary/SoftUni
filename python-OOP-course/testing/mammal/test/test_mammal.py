from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test Mammal", "Test", "sound check")

    def test_mammal_initialization(self):
        self.assertEqual(self.mammal.name, "Test Mammal")
        self.assertEqual(self.mammal.type, "Test")
        self.assertEqual(self.mammal.sound, "sound check")

    def test_mammal_make_sound_return_message(self):
        self.assertEqual(self.mammal.make_sound(), "Test Mammal makes sound check")

    def test_mammal_get_kingdom_correct_message(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_mammal_info_return_message(self):
        self.assertEqual(self.mammal.info(), "Test Mammal is of type Test")


if __name__ == "__main__":
    main()
