#TRY & EXCEPT-
try:
    length = 25
    width = 0
    length/width
except Exception:
    print("Division by zero is invalid!kindly change your input")

#
try:

    width = 0
    width/length
except NameError:
    print("VARIABLE HAS TO BE USED BEFORE DIFINING IT ")

#
try:

    width = 0
    width/length
except ZeroDivisionError:
    print("Division by zero is invalid!kindly change your input")
except NameError:
    print("VARIABLE HAS TO BE USED BEFORE DIFINING IT")
except Exception:
    print("Have caught a new error")
finally:
    print("Finally block executed")

##
try:
    length = 25
    width = 0
    length / width
except ZeroDivisionError:
    print("Division by zero is invalid!kindly change your input")
except NameError:
    print("VARIABLE HAS TO BE USED BEFORE DIFINING IT")
except Exception:
    print("Have caught a new error")
finally:
    print("Finally block executed")

##FUNCTIONS-

