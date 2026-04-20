import datetime

while True:
    choice = input("Encrypt, Decrypt or Brute Force: ")
    if choice.lower() not in ["encrypt", "decrypt", "brute force"]:
        print("Invalid choice")
        exit()
    if choice.lower() != "brute force":
        shift = int(input("Shift number 1 - 25: "))
        if shift < 1 or shift > 25:
            print("Invalid shift number")
            exit()

    if choice.lower() == "decrypt":
        shift = -shift

    message = input("Message: ")

    if choice.lower() == "brute force":
        f = open(f"result_{datetime.datetime.now()}.txt", "w")
        for i in range(1, 26):
            result = ""
            for character in message:
                if character.isalpha():
                    if character.isupper():
                        number = ord(character) - ord("A")
                        shifted_number = (number - i) % 26
                        new_character = chr(shifted_number + ord("A"))
                        result = result + new_character
                    else:
                        number = ord(character) - ord("a")
                        shifted_number = (number - i) % 26
                        new_character = chr(shifted_number + ord("a"))
                        result = result + new_character
                else:
                    result = result + character
            f.write(f"Shift {i}: {result}\n")

    else:
        result = ""
        f = open(f"result_{datetime.datetime.now()}.txt", "w")
        for character in message:
            if character.isalpha():
                if character.isupper():
                    number = ord(character) - ord("A")
                    shifted_number = (number + shift) % 26
                    new_character = chr(shifted_number + ord("A"))
                    result = result + new_character
                else:
                    number = ord(character) - ord("a")
                    shifted_number = (number + shift) % 26
                    new_character = chr(shifted_number + ord("a"))
                    result = result + new_character
            else:
                result = result + character
        f.write(result)

    f.close()
    answer = input("Go again? (y/n): ").lower()
    if answer != "y":
        break