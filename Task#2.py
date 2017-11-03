parensAll = iter('(){}[]')
parensDict = dict(zip(parensAll,parensAll))
closingValues = parensDict.values()

def balancedBraces(givenString):
    stack = []
    for char in givenString:
        charClosed = parensDict.get(char, None)
        if charClosed:
            stack.append(charClosed)
        elif char in closingValues:
            if not stack or char != stack.pop():
                return False
    return not stack


if __name__ == "__main__":

    if balanced('''Python {is an easy to [learn]}, (powerful programming language. It)
                has efficient high­level [(data structures) and a simple but
                effective approach to object­oriented programming]. Python’s elegant
                syntax and dynamic typing, together with its {interpreted nature,
                make it an ideal language (for) scripting and rapid} application
                development in many areas on most platforms.''') == True:
        print("Braces are balanced.")
    else:
        print("Braces are not balanced")