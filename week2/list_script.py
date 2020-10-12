# Wraps input() ensuring that an integer was entered, and is in bounds
def get_int(msg, max):
    x = input(msg)
    try:
        x = int(x)
        if x < 0 or x > max:
            print(f"Error: must be between 0 and {max}")
            return get_int(msg, max)
        return x
    except ValueError:
        print("Error: not an integer")
        return get_int(msg, max)


l = [1, 2, 3]


while True:
    x = get_int(f"Please enter an integer between 0 and {len(l)}: ", len(l))
    if x in range(7, 10):
        break
    else:
        l.insert(x, x)