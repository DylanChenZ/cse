valid_colors = ["yellow", "red", "blue"]

possible_mix = {
    frozenset(("yellow", "red")): "orange",
    frozenset(("yellow", "blue")): "green",
    frozenset(("red", "blue")): "purple",
}

print("Give me two colo, it must be either yellow, red, or blue \n")

color1 = str(input("color 1: "))
color2 = str(input("color 2: "))

if color1 not in valid_colors or color2 not in valid_colors:
    raise ValueError("Give me a valid color ")

if possible_mix.get(frozenset((color1, color2))):
    resulting_color = possible_mix.get(frozenset((color1, color2)))
    print(f"When you mix {color1} and {color2}, you get {resulting_color}.")
else:
    print("BAD COLOR!")
