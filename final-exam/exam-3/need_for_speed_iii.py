TANK_MAXIMUM = 75


def drive(cars, car, distance, fuel_needed):
    if cars[car]["fuel"] < int(fuel_needed):
        print("Not enough fuel to make that ride")
    else:
        cars[car]["fuel"] -= int(fuel_needed)
        cars[car]["mileage"] += int(distance)
        print(
            f"{car} driven for {distance} kilometers. "
            f"{fuel_needed} liters of fuel consumed."
        )
        if cars[car]["mileage"] >= 100_000:
            print(f"Time to sell the {car}!")
            del cars[car]


def refuel(cars, car, refill_amount):
    if (cars[car]["fuel"] + int(refill_amount)) > TANK_MAXIMUM:
        refilled = TANK_MAXIMUM - cars[car]["fuel"]
        cars[car]["fuel"] = TANK_MAXIMUM
    else:
        cars[car]["fuel"] += int(refill_amount)
        refilled = refill_amount
    print(f"{car} refueled with {refilled} liters")


def revert(cars, car, kilometers):
    cars[car]["mileage"] -= int(kilometers)
    if cars[car]["mileage"] < 10_000:
        cars[car]["mileage"] = 10_000
        return
    print(f"{car} mileage decreased by {kilometers} kilometers")


def print_all(cars):
    for car in cars:
        print(
            f"{car} -> Mileage: {cars[car]['mileage']} kms, "
            f"Fuel in the tank: {cars[car]['fuel']} lt."
        )


def main():
    number_of_cars = int(input())
    cars = {}
    for _ in range(number_of_cars):
        car_info = input().split("|")
        car, mileage, fuel = car_info
        cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

    while True:
        command = input().split(" : ")
        if command[0] == "Stop":
            break

        action, car, dis_fuel_km = command[:3]
        if action == "Drive":
            fuel_needed = command[3]
            drive(cars, car, dis_fuel_km, fuel_needed)
        elif action == "Refuel":
            refuel(cars, car, dis_fuel_km)
        elif action == "Revert":
            revert(cars, car, dis_fuel_km)
    print_all(cars)


if __name__ == "__main__":
    main()


"""                     Task:
You have just bought the latest and greatest computer game – Need for Seed III. 
Pick your favorite cars and drive them all you want! We know that you can't wait to 
start playing.

On the first line of the standard input, you will receive an integer n – the number of 
cars that you can obtain. On the next n lines, the cars themselves will follow with 
their mileage and fuel available, separated by "|" in the following format:
"{car}|{mileage}|{fuel}"

Then, you will be receiving different commands, each on a new line, 
    separated by " : ", until the "Stop" command is given:
"Drive : {car} : {distance} : {fuel}":
    You need to drive the given distance, and you will need the given fuel to do that. 
        If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
    If the car has the required fuel available in the tank, increase its mileage with 
        the given distance, decrease its fuel with the given fuel, and print: 
        "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
    You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it 
        from the collection(s) and print: "Time to sell the {car}!"
"Refuel : {car} : {fuel}":
    Refill the tank of your car. 
    Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is
        more than you can fit in the tank, take only what is required to fill it up. 
    Print a message in the following format: "{car} refueled with {fuel} liters"
"Revert : {car} : {kilometers}":
    Decrease the mileage of the given car with the given kilometers and print the 
        kilometers you have decreased it with in the following format:
        "{car} mileage decreased by {amount reverted} kilometers"
If the mileage becomes less than 10 000km after it is decreased, 
    just set it to 10 000km and DO NOT print anything.

Upon receiving the "Stop" command, you need to print all cars in your possession in the
 following format: "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."

Input/Constraints
    The mileage and fuel of the cars will be valid, 32-bit integers, 
        and will never be negative.
    The fuel and distance amounts in the commands will never be negative.
    The car names in the commands will always be valid cars in your possession.
Output
    All the output messages with the appropriate formats are 
        described in the problem description.
Examples
        Input	                                   Output
3
Audi A6|38000|62                        
Mercedes CLS|11000|35                   
Volkswagen Passat CC|45678|5            
Drive : Audi A6 : 543 : 47              Audi A6 driven for 543 kilometers. 
                                            47 liters of fuel consumed.
Drive : Mercedes CLS : 94 : 11          Mercedes CLS driven for 94 kilometers. 11 liters
                                            of fuel consumed.
Drive : Volkswagen Passat CC : 69 : 8   Not enough fuel to make that ride
Refuel : Audi A6 : 50                   Audi A6 refueled with 50 liters
Revert : Mercedes CLS : 500             Mercedes CLS mileage decreased by 500 kilometers
Revert : Audi A6 : 30000
Stop                                    Audi A6 -> Mileage: 10000 kms, 
                                            Fuel in the tank: 65 lt.
                                        Mercedes CLS -> Mileage: 10594 kms, 
                                            Fuel in the tank: 24 lt.
                                        Volkswagen Passat CC -> Mileage: 45678 kms, 
                                            Fuel in the tank: 5 lt.
"""
