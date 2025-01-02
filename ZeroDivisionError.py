x=int(input("enter number"))
try:
  y=x/0
  print(y)
except ZeroDivisionError:
  print("Zero Division Error")
