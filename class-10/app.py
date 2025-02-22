try:
  user_input = int(input("enter"))
  print(type(user_input))
  user_input /0

# except ValueError:
#   print("invalid input")

except KeyboardInterrupt:
  print("keyboard interrupt")

except Exception as e:
  print("error")
  print(e)
