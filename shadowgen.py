import pyfiglet
import random
from datetime import datetime
from colorama import *

def showBanner():
    intro = pyfiglet.figlet_format("ShadowGen", font="slant")
    print(Fore.GREEN + "\n--------------------------------------------------------")
    print(intro + '\t       < Corporative Nightmare >')
    print("--------------------------------------------------------")
    print("             [+] Coded By AbyssWatcher [+]")

def showHelp():
    print("\nShadowGen usage ->")
    print("-help\t\t\tShows this help message visualizing the commands")
    print("-basic act\t\tGenerates a card number based on the basic activation method")
    print("-basic sim\t\tGenerates a card number based on the basic similarity method")
    print("-advance\t\tGenerates a card number based on the advance extrapolation method")
    print("-logindent\t\tGenerates a card number based on the logic indent method")
    print("-exit\t\t\tExits the program\n")
    print("--------------------------------------------------------")

def generate_new_number(number):
    base = number[:-6]
    new_digits = ''.join(str(random.randint(0, 9)) for _ in range(6))
    return base + new_digits

def generate_random_date():
    month = random.randint(1, 12)
    year = random.randint(datetime.now().year + 1, datetime.now().year + 4)
    return f"{month:02d}/{year}"

def generate_three_digits():
    return random.randint(100, 999)

def generate_six_digits():
    return random.randint(100000, 999999)

def basicActivation(original_number):
    original_number = original_number.replace(" ", "")
    new_number = generate_new_number(original_number)
    formatted_number = format_card_number(new_number)
    random_date = generate_random_date()
    three_digits = generate_three_digits()
    print("\nNew number:", formatted_number)
    print("Random date (mm/year):", random_date)
    print("Three digits number:", three_digits)

def basicSimilarity(number1, number2):
    if number1[:9] != number2[:9]:
        print("The first six digits are not the same.")
        return None

    first_digits = number1[:9]
    last_ten_1 = number1[10:].replace(" ", "")
    last_ten_2 = number2[10:].replace(" ", "")

    result = first_digits
    for i in range(len(last_ten_1)):
        if last_ten_1[i] == last_ten_2[i]:
            result += last_ten_1[i]
        else:
            result += str(random.randint(0, 9))

    result = format_card_number(result)
    random_date = generate_random_date()
    three_digits = generate_three_digits()
    return random_date, three_digits, result

def advanceExtrapolation(number1, number2):
    if number1[:9] != number2[:9]:
        print("The first six digits are not the same.")
        return None

    digits1 = number1.replace(" ", "")[9:11]
    digits2 = number2.replace(" ", "")[9:11]

    sum1 = int(digits1[0]) + int(digits2[0])
    sum2 = int(digits1[1]) + int(digits2[1])

    result1 = (sum1 / 2) * 5
    result2 = (sum2 / 2) * 5

    final_result = int(result1) + int(result2)

    six_digits = generate_six_digits()
    final_number = number1[:9] + f"{final_result:02d}{six_digits}"
    formatted_number = format_card_number(final_number)
    random_date = generate_random_date()
    three_digits = generate_three_digits()
    return random_date, three_digits, formatted_number

def format_card_number(number):
    number = number.replace(" ", "")
    return ' '.join(number[i:i+4] for i in range(0, len(number), 4))

def logic_indent(card_number):
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16:
        print("Invalid card number length.")
        return None

    first_six = card_number[:6]
    second_group = card_number[6:]

    part1 = second_group[:3]  
    part2 = second_group[3:7] 
    part3 = second_group[7:]  

    transformed_part1 = part1[0] + str(random.randint(0, 9)) + part1[2]
    transformed_part2 = part2[0] + str(random.randint(0, 9)) + str(random.randint(0, 9)) + part2[3]
    transformed_part3 = part3[0] + str(random.randint(0, 9)) + part3[2]

    final_number = first_six + transformed_part1 + transformed_part2 + transformed_part3

    formatted_number = format_card_number(final_number)

    random_date = generate_random_date()
    three_digits = generate_three_digits()

    return random_date, three_digits, formatted_number

def main():
    showBanner()
    showHelp()

    while True:
        command = input("\nShadowGen:~$ ")

        if command == "-help":
            showHelp()

        elif command == "-exit":
            print("\nStay Low Key My Friend...\n")
            break

        elif command == "-basic act":
            original_number = input("\nEnter the original card number in format XXXX XXXX XXXX XXXX: ")
            basicActivation(original_number)

        elif command == "-basic sim":
            number1 = input("\nEnter the first original card number in format XXXX XXXX XXXX XXXX: ")
            number2 = input("Enter the second original card number in format XXXX XXXX XXXX XXXX: ")
            result = basicSimilarity(number1, number2)
            if result:
                random_date, three_digits, number = result
                print("\nGenerated number:", number)
                print("Random date (mm/year):", random_date)
                print("Three digits number:", three_digits)

        elif command == "-advance":
            number1 = input("\nEnter the first original card number in format XXXX XXXX XXXX XXXX: ")
            number2 = input("Enter the second original card number in format XXXX XXXX XXXX XXXX: ")
            result = advanceExtrapolation(number1, number2)
            if result:
                random_date, three_digits, number = result
                print("\nGenerated number:", number)
                print("Random date (mm/year):", random_date)
                print("Three digits number:", three_digits)

        elif command == "-logindent":
            original_number = input("\nEnter the original card number in format XXXX XXXX XXXX XXXX: ")
            result = logic_indent(original_number)
            if result:
                random_date, three_digits, number = result
                print("\nGenerated number:", number)
                print("Random date (mm/year):", random_date)
                print("Three digits number:", three_digits)

        else:
            print("\nInvalid command...")
            showHelp()

if __name__ == '__main__':
    main()
