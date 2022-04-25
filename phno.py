"""
Created on Mon Mar  7 11:15:23 2022

@author: ayrainc
"""
print("""
Created on Fri Mar  4 22:17:59 2022

@author: ayrainc
""")
# Program to convert input to
# phonenumber format
def phno():
    import phonenumbers
    from phonenumbers import timezone,carrier,geocoder
    Countrycode=input("enter the country code:")
    tel=input("enter telephone no:")
    a=Countrycode+tel
    lan=input("enter the language code:")
# Parsing String to Phone number
# Phone number format: (+Countrycode)xxxxxxxxxx
    phoneNumber = phonenumbers.parse(a)
    timeZone = timezone.time_zones_for_number(phoneNumber)
    Carrier = carrier.name_for_number(phoneNumber, lan)
    Region = geocoder.description_for_number(phoneNumber, lan)
    print("timezone:",timeZone)
# This will print the phone number and
# it's basic details.
    print(phoneNumber)
    print("carrier:",Carrier)
    print("region:",Region)
phno()
