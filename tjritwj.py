try:
    amount = int(input("Enter amoun items: "))
    items_type = input("ENTER TYPE ITEMS: ")
except (ValueError, ZeroDivisionError, IndexError):
    print("Valuerror or ZeroDivisionError")
except  IndexError:
    print("index error")
finally:
    print("програма без помилок")