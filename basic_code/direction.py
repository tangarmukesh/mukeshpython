dir_nam = input("Enter your direction name: ")
def turn_clockwise(dir_nam):
    if dir_nam == "n":
        return "E"
    elif dir_nam == "e":
        return "S"
    elif dir_nam == "s":
        return "W"
    elif dir_nam == "w":
        return  "N"
    else:
        return "Invaild Input"
print(turn_clockwise(dir_nam))