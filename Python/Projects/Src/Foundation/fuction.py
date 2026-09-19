while True:
    m=int(input(""))

    if m<=100 and m>=90:
        res="O"
    elif m<90 and m>=80:
        res="A"
    elif m<80 and m>=70:
        res="B"
    elif m<70 and m>=60:
        res="C"
    elif m<60 and m>=40:
        res="D"
    elif m<40 and m>=0:
        res="Fail"

print(f"Your grade is {res}")