while True:
    myPass = input("Enter the password you want to encode: ").lower()

    myDict = {
        "a": "b%",
        "b": "dfc",
        "c": "58d",
        "d": "22$&",
        "e": "@",
        "f": "5@%",
        "g": "dd@%",
        "h": "(*)",
        "i": "+_$",
        "j": "fg++",
        "k": "#@R",
        "l": "ff#&",
        "m": "26f$",
        "n": "12!@",
        "o": "E#@%",
        "p": "+_)",
        "q": "!@^",
        "r": "rr$+_)",
        "s": "F4^",
        "t": "+&L",
        "u": "dd$^*",
        "v": "\]a",
        "w": "Q\.",
        "x": "\]-*",
        "y": "XX$)",
        "z": " ",
        " ": "@#(*",
    }
    newstr = ""

    for letter in myPass:
        x = True
        for key, value in myDict.items():
            if letter == key:
                newstr += value
                x = False
        if x == True:
            newstr += "*/#"
    print(f"Encrypted pass : {newstr}")
