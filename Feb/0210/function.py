# Funtions with Outputs

def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())

format_name("angela", "ANGELA")


def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    print(f"{formated_f_name} {formated_l_name}")

format_name("angela", "YU")

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("AnGElA", "YU")
print(formated_string)

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))