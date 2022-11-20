with open("Input/Names/invited_names.txt", "r") as mektup:
    names = mektup.readlines()

for i in range(len(names)):
    with open("Input/Letters/starting_letter.txt") as mektup:
        yazi = mektup.read()
        new_name = names[i].strip("\n")
        edited = yazi.replace("[name],", f"{new_name},")
        with open(f"Output/ReadyToSend/{new_name}.txt", 'w') as new:
            new.write(edited)
