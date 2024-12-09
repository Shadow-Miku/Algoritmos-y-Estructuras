def reverse_string(input_str):
    input_str = list(input_str)
    stack = []
    for i in range(len(input_str)):
        stack.append(input_str.pop())
    return ''.join(stack)


if __name__ == "__main__":
    input_str = input("Enter a string: ")
    print("Reversed string:", reverse_string(input_str))