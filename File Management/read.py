file = open("Sample.txt", "r")
content = file.read()
file.close()
print(f"Content of the file: {content}")