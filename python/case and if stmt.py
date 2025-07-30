x = int(input("Enter the value of x: "))  #x is the variable to match

match x:
    case 0: #if x is zero
        print("The value is zero")

    case _ if x < 0:
        print("The value is Negative")

    case _ if x > 0:
        print("The value is Positive")

    case _ if x != 0:    # agar statment upar aj sachu thay jai to e niche na badha ne ignore kre che
        print("The value is not Zero")
