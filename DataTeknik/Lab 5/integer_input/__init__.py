def get_integer_input(prompt="Enter an integer: "):
    while True:
        user_input = input(prompt)
        try:
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("personnummer inehåler bara heltal")

if __name__ == "__main__":
    integer_value = get_integer_input()








