import re

input_data = input()
if not re.search(r'\d{,3}[+|\-|\*|=|/]\d{,3}[+|-|\*|=|/]\d{,3}', input_data):
    print("error")
else:
    input_data = input_data.replace('=', '==')
    if eval(input_data):
        print("true")
    if not eval(input_data):
        print("false")
