def get_string_input(prompt="Enter an string: "):
    while True:
        user_input = input(prompt)
        try:
            string_value = str(user_input)
            return string_value
        except ValueError:
            print("Namn inehåller bara bokstäver")

if __name__ == "__main__":
    string_value = get_string_input()
