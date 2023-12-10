try:
    ab = "ab1"
    x = 1 + ab
    print(x)
except NameError as e:
  print("Variable x is not defined", e)
except:
  print("Something else went wrong")
