package_weight = float(input())
service_type = input()
distance = int(input())

price = 0
additional_charges = 0


if package_weight < 1:
    price = 0.03
    if service_type == 'express':
        additional_charges = package_weight * (price * 0.80)
elif 1 <= package_weight < 10:
    price = 0.05
    if service_type == 'express':
        additional_charges = package_weight * (price * 0.40)
elif 10 <= package_weight < 40:
    price = 0.10
    if service_type == 'express':
        additional_charges = package_weight * (price * 0.05)
elif 40 <= package_weight < 90:
    price = 0.15
    if service_type == 'express':
        additional_charges = package_weight * (price * 0.02)
elif 90 <= package_weight < 150:
    price = 0.20
    if service_type == 'express':
        additional_charges = package_weight * (price * 0.01)


total = (price + additional_charges) * distance

print(f"The delivery of your shipment with weight of {package_weight:.3f} kg. would cost {total:.2f} lv.")
