# Write your code here.
def hello():
    return "Hello!"

def greet(name):
    return f"Hello, {name}!"

def calc(val1, val2, operator="multiply"):
    try:
        match operator:
            case "add":
                return val1 + val2
            case "subtract":
                return val1 - val2
            case "multiply":
                return val1 * val2
            case "divide":
                return val1 / val2
            case "modulo":
                return val1 % val2
            case "int_divide":
                return val1 // val2
            case "power":
                return val1 ** val2
            case _:
                return "Invalid operator"

    except ZeroDivisionError:
        return "You can't divide by 0!"

    except TypeError:
        return "You can't multiply those values!"
    


def data_type_conversion(value, data_type):
    try:
        if data_type == "float":
            return float(value)
        elif data_type == "int":
            return int(value)
        elif data_type == "str":
            return str(value)
        else:
            return "Invalid data type"

    except ValueError:
        return f"You can't convert {value} into a {data_type}."



def grade(*args):
    try:
        avg = sum(args) / len(args)

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
        
    except TypeError:
        return "Invalid data was provided."
    

def repeat(string,count):
    new_string = ""

    for char in range(count):
        new_string += string

    return new_string


def student_scores(option, **kwargs):
    if option == "best":
        best_student = ""
        highest_score = -1

        for student, score in kwargs.items():
            if score > highest_score:
                highest_score = score
                best_student = student

        return best_student

    elif option == "mean":
        return sum(kwargs.values()) / len(kwargs)
    


def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word.lower() in little_words:
            words[i] = word.lower()
        else:
            words[i] = word.capitalize()

    return " ".join(words)



def hangman(secret, guess):
    result = ""

    for char in secret:
        if char in guess:
            result += char
        else:
            result += "_"

    return result



def pig_latin(string):
    vowels = "aeiou"
    result = []
    lowered_string = string.lower()
    words = lowered_string.split()

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            for idx, char in enumerate(word):
                if char == "u" and word[idx - 1] == "q":
                    result.append(word[idx + 1:] + word[:idx+1] + "ay")
                    break
                if char in vowels:
                    result.append(word[idx:] + word[:idx] + "ay")
                    break

    return " ".join(result)

    

