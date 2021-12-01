'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''

#start writing your code below

month = str(input("enter a month: "))

if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month =="december":
  print(31)
elif month == "april" or month == "june" or month =="september" or month == "november":
  print(30)
elif month == "february":
  print("28 or 29")
else:
  print("not a month")


'''
i started this to test my memory of lists

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

days = [ 31, "28 or 29", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

print(list(months))
print(list(days))

for i in range(12):
  if month(i) == month:
    print(days(i))
  else:
    print("not a month.")
'''