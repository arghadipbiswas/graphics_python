import phonenumbers
from test import number

from phonenumbers import geocoder
ch_no=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_no,"en"))

from phonenumbers import carrier
service=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service,"en"))

