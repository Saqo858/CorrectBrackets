from is_correct_brackets import is_correct_brackets

while True:
    brackets = input('Enter your brackets [({})] or fsyofsyo --> ')
    if brackets == 'fsyo':
        print("Aha ev verj)")
        break
    print(is_correct_brackets(brackets))
