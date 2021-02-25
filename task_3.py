input_data = input()
input_data = input_data.replace('=', '==')
if eval(input_data):
    print("true")
if not eval(input_data):
    print("false")
