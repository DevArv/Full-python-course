from datetime import date

Form = 'Subscription to language school'
print(Form)

name = input("What is your name?\n")
print("Hello " + name)

birth_year = input("Enter your birth year:\n")
current_year = date.today().year
age = current_year - int(birth_year)
print(age)

english_skills = input("Enter your english skills: basic / mid / advanced:\n")
print("Your english level is " + english_skills)

phn_number = input("Enter your contact number:\n")
print(phn_number)

mail_add = input("Enter your mail address:\n")
print("We gonna send your all the communications to " + mail_add)

pay_mode = input("Bank transfer or Paypal:\n")
if pay_mode == "Bank transfer":
    input("What is the name of the bank that you will be using for the payment?:\n")
if pay_mode == "Bank transfer":
    input("Could you provide us with the bank account with which you will be making the transfer?:\n")

else:
    input("Could you provide us with the paypal account with which you will be making the payment?:\n")

print("Your payment method has been saved")

charge = ["*", "**", "***", "****", "*****"]
for item in charge:
    print(item)

print("Congratulations you have completed the registration form, as soon as we receive proof of your "
      "payment we will contact you. ")
print("Thank you for choosing us as your language school.")
