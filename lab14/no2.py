
filename = input("Enter a filename: ")
old_string = input("Enter the old string to be replaced: ")
new_string = input("Enter the new string to replace it: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    if old_string == new_string:
        raise ValueError("The old and new strings are the same.")

    if old_string == "":
        raise ValueError("The old string cannot be empty.")

    if old_string not in text:
        raise ValueError("The old string was not found.")

    text = text.replace(old_string, new_string)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

    print("Done")

except FileNotFoundError:
    print("Error: File does not exist.")

except ValueError as error:
    print("Error:", error)
