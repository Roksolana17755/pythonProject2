# try:
#     amount = int(input("Enter amoun items: "))
#     items_type = input("ENTER TYPE ITEMS: ")
# except (ValueError, ZeroDivisionError, IndexError):
#     print("Valuerror or ZeroDivisionError")
# except  IndexError:
#     print("index error")
# finally:
#     print("програма без помилок")

# try:
#     dilnik = float(input("Enter the dilnik: "))
#     dilene = float(input("Enter the dilene: "))
#     if dilene == 0:
#         raise ZeroDivisionError("Division by zero is not allowed")
#     res = dilnik / dilene
#     print("The result is: ", res)
# except ZeroDivisionError:
#     print("Error:")

try:
    num = int(input("введіть число:"))
    if num < 0:
        raise Exception("боже, під коренем не може бути від'ємне число!!!!!!!!!")
except (ZeroDivisionError, ValueError):
    print("kys")
except Exception:
    pass
finally:
    ("урааа ти не неук!!!)")
try:
    res = num ** 0.5
    print(res)
except NameError:
    print("тидурак,якиймінс?")