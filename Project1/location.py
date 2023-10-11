import phonenumbers
from phonenumbers import timezone, geocoder, carrier
num = input("enter your phone number with +91: ")
phone = phonenumbers.parse(num)
time = timezone._country_level_time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
print(phone)
print(time)
print(car)
print(reg)