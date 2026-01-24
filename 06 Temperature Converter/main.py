
def convert_temperature():
    temperature = float(input("Enter temperature: "))

    print("==== OPTIONS ====")
    print("1. for Fahrenheit to Celsius")
    print("2. for Celsius to Fahrenheit")
    print("=============================")
    print()

    option = input("Select a conversion type: ")

    match(option):
        case "1":
            celsius_temp = (temperature - 32 ) / (9/5)
            print(f"Converted temperature: {celsius_temp:.1f} °C")

        case "2":
            fahrenheit_temp = (temperature * (9/5)) + 32
            print(f"Converted temperature: {fahrenheit_temp:.1f} °F")

        case _:
            print("Wrong option selected, Start Again")

convert_temperature()