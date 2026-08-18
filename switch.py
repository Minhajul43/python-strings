# Switch statement in python
# Python does not have a built-in switch statement, but we can simulate it using a dictionary

def switch_case(case):
    switcher = {
        1: "Case 1",
        2: "Case 2",
        3: "Case 3",
        4: "Case 4",
        5: "Case 5"
    }
    return switcher.get(case, "Invalid case")

case_number = int(input("Enter a case number (1-5): "))
result = switch_case(case_number)
print(result)


# printin result using match-case statement (Python 3.10 and above)
def match_case(case):
    match case:
        case 1:
            return "Case 1"
        case 2:
            return "Case 2"
        case 3:
            return "Case 3"
        case 4:
            return "Case 4"
        case 5:
            return "Case 5"
        case _:
            return "Invalid case"

case_number = int(input("Enter a case number (1-5): "))
result = match_case(case_number)
print(result)