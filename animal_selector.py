animals = {
    "rock":None,
    "plant":None,
    "dog":None,
    "cat":None,
    "cow":None,
    "giraffe":None,
    "fish":None,
    "bunny":None,
    "hedgehog":None,
    "chicken":None,
    "pink dolphin":None,
    "dolphin":None,
    "llama":None,
}

def ask_question(question):
    q = input(question + " ")
    if q.lower() == "y" or q.lower() == "yes":
        return True
    elif q.lower() == "n" or q.lower() == "no":
        return False
    else:
        raise ValueError("Invalid")


def print_options_str(options):
    options_str = "\n"
    for idx, option in enumerate(options):
        options_str += f"{idx+1}) {option}\n"
    return options_str

                   
def ask_options(question, options):
    q = input(question + print_options_str(options))
    try:
        q = int(q)
    except ValueError:
        raise ValueError("Not an int")
    if q < 1 or q > len(options):
        raise ValueError("Number out of range")
    else:
        return q - 1 


def get_underwater_pet(ask_question):
    big = ask_question("Do you want a big pet?")
    if big:
        pink = ask_question("Do you want a pink pet? (Blue = n)")
        if pink:
            return "pink dolphin"
        else:
            return "dolphin"
    else:
        hot = ask_question("Do you prefer summer or winter?")
        if hot:
            return "guppy"
        else:
            return "goldfish"

def get_land_pet(ask_question, ask_options):
    farm = ask_question("Do you like the farm?")
    if farm:
        clever = ask_question("Are you clever?")
        if clever:
            return "cow"
        else:
            return "chicken"
    else:
        hours_spent = ask_options("How many hours do you want to spend with your pet?", ["all of them", "many hours", "a few", "a little"])
        if hours_spent == 0:
            return "dog"
        elif hours_spent == 1:
            yellow = ask_question("Do you prefer yellow over white?")
            if yellow:
                return "giraffe"
            else:
                return "llama"
        elif hours_spent == 2:
            return "cat"
        else:
            furry = ask_question("Do you prefer fur over prickles?")           
            if furry:
                return "bunny"
            else:
                return "hedgehog"


def get_animal(ask_question, ask_options):
    want_a_pet = ask_question("Do you want a pet?")
    if want_a_pet:
        underwater = ask_question("Do you want an underwater pet?")
        if underwater:
            return get_underwater_pet(ask_question)
        else:
            return get_land_pet(ask_question, ask_options)

    else:
        want_responsibility = ask_question("Are you responsible?")
        if want_responsibility:
            return "plant"
        else:
            return "rock"
    

if __name__ == "__main__":
    print(get_animal(ask_question, ask_options))