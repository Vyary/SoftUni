from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.truck_driver = TruckDriver("Trucky", 50)

    def test_truck_driver_correct_initialization(self):
        self.assertEqual(self.truck_driver.name, "Trucky")
        self.assertEqual(self.truck_driver.money_per_mile, 50)
        self.assertEqual(self.truck_driver.available_cargos, {})
        self.assertEqual(self.truck_driver.earned_money, 0)
        self.assertEqual(self.truck_driver.miles, 0)

    def test_earned_money_getter(self):
        self.assertEqual(self.truck_driver.earned_money, 0)

    def test_earned_money_setter_positive(self):
        self.truck_driver.earned_money = 100
        self.assertEqual(self.truck_driver.earned_money, 100)

    def test_truck_driver_bankrupt_exception(self):
        with self.assertRaises(Exception) as context:
            self.truck_driver.earned_money = -10

        self.assertEqual(str(context.exception), "Trucky went bankrupt.")

    def test_truck_driver_add_cargo_offer_exception(self):
        self.truck_driver.add_cargo_offer("Test", 10)

        with self.assertRaises(Exception) as context:
            self.truck_driver.add_cargo_offer("Test", 10)

        self.assertEqual(str(context.exception), "Cargo offer is already added.")

    def test_truck_driver_add_cargo_offer_success(self):
        test_offer = self.truck_driver.add_cargo_offer("Test", 10)
        self.assertEqual(test_offer, "Cargo for 10 to Test was added as an offer.")
        self.assertEqual(self.truck_driver.available_cargos, {"Test": 10})

    def test_truck_driver_drive_best_cargo_offer_exception(self):
        context = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(context, "There are no offers available.")
        self.assertEqual(self.truck_driver.earned_money, 0)
        self.assertEqual(self.truck_driver.miles, 0)

    def test_truck_driver_drive_best_cargo_offer_max_miles(self):
        self.truck_driver.available_cargos["Test1"] = 10
        self.truck_driver.available_cargos["Test2"] = 8
        self.truck_driver.available_cargos["Test3"] = 9

        drive = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(self.truck_driver.earned_money, 500)
        self.assertEqual(self.truck_driver.miles, 10)
        self.assertEqual(drive, "Trucky is driving 10 to Test1.")

    def test_drive_best_cargo_offer_earned_money_and_miles(self):
        driver = TruckDriver("John", 0.5)
        driver.add_cargo_offer("New York", 1000)
        driver.drive_best_cargo_offer()
        self.assertEqual(driver.earned_money, 375)
        self.assertEqual(driver.miles, 1000)

    def test_truck_driver_eat_functions_with_250_miles(self):
        self.truck_driver.earned_money = 100
        self.truck_driver.eat(250)
        self.assertEqual(self.truck_driver.earned_money, 80)

    def test_truck_driver_eat_functions_with_less_than_250_miles(self):
        self.truck_driver.earned_money = 100
        self.truck_driver.eat(240)
        self.assertEqual(self.truck_driver.earned_money, 100)

    def test_truck_driver_sleep_function_with_1000_miles(self):
        self.truck_driver.earned_money = 100
        self.truck_driver.sleep(1000)
        self.assertEqual(self.truck_driver.earned_money, 55)

    def test_truck_driver_sleep_function_with_less_than_1000_miles(self):
        self.truck_driver.earned_money = 100
        self.truck_driver.sleep(90)
        self.assertEqual(self.truck_driver.earned_money, 100)

    def test_truck_driver_pump_gas_function_with_1500_miles(self):
        self.truck_driver.earned_money = 600
        self.truck_driver.pump_gas(1500)
        self.assertEqual(self.truck_driver.earned_money, 100)

    def test_truck_driver_pump_gas_function_with_less_than_1500_miles(self):
        self.truck_driver.earned_money = 600
        self.truck_driver.pump_gas(800)
        self.assertEqual(self.truck_driver.earned_money, 600)

    def test_truck_driver_repair_truck_function_with_10000_miles(self):
        self.truck_driver.earned_money = 7500
        self.truck_driver.repair_truck(10000)
        self.assertEqual(self.truck_driver.earned_money, 0)

    def test_truck_driver_repair_truck_function_with_less_than_10000_miles(self):
        self.truck_driver.earned_money = 7500
        self.truck_driver.repair_truck(800)
        self.assertEqual(self.truck_driver.earned_money, 7500)

    def test_truck_driver_represent(self):
        self.assertEqual(str(self.truck_driver), "Trucky has 0 miles behind his back.")

    def test_truck_driver_check_for_activities(self):
        self.truck_driver.earned_money = 15_000
        self.truck_driver.check_for_activities(10_000)
        self.assertEqual(self.truck_driver.earned_money, 3250)


if __name__ == "__main__":
    main()
