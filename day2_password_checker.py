print("--Basic Password Checker--")
password = input("Enter a password to test : ")
# The len() tool counts characters are there in the password
length= len(password)
if length < 8:
  print("Security level is LOW, hacker can easily crack it :/")
elif length >=8 and length < 12:
  print("Security level is MODERATE, could make it stronger")
else:
  print("Security level is STRONG, Great JOBBBBB!!")
