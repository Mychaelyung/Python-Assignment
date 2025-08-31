print("Creating a sample file called 'my_file.txt'...")
with open("my_file.txt", "w") as file:
    file.write("Hello World!\n")
    file.write("Thank you PLP.\n")
    file.write("Python is fun!\n")
print("Sample file created! ✅")

print("\n" + "=" * 50)

filename = input("Enter a filename to read (or press Enter to use 'my_file.txt'): ")

if filename == "":
    filename = "my_file.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
    
    print(f"\n📖 Contents of '{filename}':")
    print("-" * 30)
    print(content)
    
    lines = content.split("\n")
    modified_lines = []
    
    for line in lines:
        if line.strip():
            modified_lines.append("MODIFIED: " + line) # type: ignore
        else:
            modified_lines.append(line)
    
    modified_content = "\n".join(modified_lines)
    
    new_filename = "modified_" + filename
    with open(new_filename, "w") as file:
        file.write(modified_content)
    
    print(f"\n✅ Modified file saved as '{new_filename}'")
    print(f"\n📝 Contents of modified file:")
    print("-" * 30)
    print(modified_content)

except FileNotFoundError:
    print(f"\n❌ Oops! The file '{filename}' was not found.")
    print("Make sure you typed the filename correctly!")

except PermissionError:
    print(f"\n❌ Sorry! I don't have permission to read '{filename}'.")
    print("Try a different file.")

except Exception as e:
    print(f"\n❌ Something went wrong: {e}")
    print("Don't worry, this happens sometimes!")

print("\n🎉 Program finished!")
print("Thanks for trying file operations!")