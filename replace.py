text = input("Enter the item: ")
text = text.lower()
first_char = text[0]
second_found = False
result = ""
for i in range(len(text)):
    if text[i] == first_char:
        if not second_found and i != 0:
            result += "$"
            second_found = True
        else:
            result += text[i]
    else:
        result += text[i]
print("Modified text:", result)
