from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 300)

    def test_default_vehicle_consumption(self):
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_vehicle_initialization(self):
        self.assertEqual(self.vehicle.fuel, 100)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, 300)
        self.assertEqual(
            self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION
        )

    def test_vehicle_drive_with_no_enough_fuel_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(1000)

        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_vehicle_drive_with_enough_fuel(self):
        self.vehicle.drive(50)
        self.assertEqual(self.vehicle.fuel, 37.5)

    def test_vehicle_refuel_too_much_fuel_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(1000)
        
        self.assertEqual(str(context.exception), "Too much fuel")

    def test_vehicle_refuel_enough_fuel(self):
        self.vehicle.fuel = 10
        self.vehicle.refuel(50)
        self.assertEqual(self.vehicle.fuel, 60)

    def test_vehicle_string_representation(self):
        self.assertEqual(
            str(self.vehicle),
            "The vehicle has 300 horse power with 100 fuel left and 1.25 fuel consumption",
        )


if __name__ == "__main__":
    main()
