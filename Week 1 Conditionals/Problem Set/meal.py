def main():
    time = convert(input("What's the time? "))

    if 7.0 <= time <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= time <= 13.0:
        print("It's lunch time!")
    elif  18.0 <= time <= 19.0:
        print("It's dinner time!")
    else:
        print(" ")


def convert(time):
    time = time.split(":")
    return float(time[0]) + float(time[1])/60


if __name__ == "__main__":
    main()