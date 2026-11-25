# Case study 35: Text Compression Using Character Runs
# Only letters are used so that counts can be distinguished from text.

text = input("Enter text (letters only): ")
if text and not text.isalpha():
    print("Invalid input: use letters only.")
else:
    encoded = ""
    if text:
        count = 1
        for index in range(1, len(text)):
            if text[index] == text[index - 1]:
                count += 1
            else:
                encoded += text[index - 1] + str(count)
                count = 1
        encoded += text[-1] + str(count)

    print("Original:", text)
    print("Encoded:", encoded)
    print("Original length:", len(text))
    print("Encoded length:", len(encoded))
    if len(encoded) < len(text):
        print("Compression is beneficial.")
    else:
        print("Compression is not beneficial.")
