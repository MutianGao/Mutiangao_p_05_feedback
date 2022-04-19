COLOR_TO_NAME = {"Absolute Zero": "#0048ba",
                 "Acid Green": "#b0bf1a",
                 "AliceBlue": "#f0f8ff",
                 "Alizarin crimson": "#e32636",
                 "Amaranth": "#e52b50",
                 "Amber": "#ffbf00",
                 "Amethyst": "#9966cc",
                 "AntiqueWhite": "#faebd7",
                 "Aqua": "#00ffff",
                 "Arylide Yellow": "#e9d66b"}
for i in COLOR_TO_NAME:
    print(i, "code is", COLOR_TO_NAME[i])

color_code = input("Enter color: ").upper()
while color_code != "":
    if color_code in COLOR_TO_NAME:
        print(color_code, "is", COLOR_TO_NAME[color_code])
    else:
        print("Invalid short state")
    state_code = input("Enter color: ")
