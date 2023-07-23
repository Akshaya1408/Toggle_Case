def toggle_case(A):
    result = ""
    for char in A:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result

A = input()
print(toggle_case(A)) 
