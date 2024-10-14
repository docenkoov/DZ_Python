from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 13", "+79065537187"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79065537188"))
catalog.append(Smartphone("Google", "Pixel 6", "+79065537189"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79065537190"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79065537191"))

for phone in catalog:
    print(f"Марка - {phone.brand};  Модель - {phone.model};  Номер телефона: {phone.phone_number}.")
