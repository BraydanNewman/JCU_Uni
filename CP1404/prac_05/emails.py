user_completed = False

emails = {}

while not user_completed:
    email = input("Email: ")
    if email == "":
        user_completed = True
        continue
    name = ' '.join(email.split('@')[0].split('.')).title()
    correct_name = input(f"Is your name {name}? (Y/n)")
    if correct_name != "" and correct_name[0].upper() == 'N':
        name = input("Name: ")
    emails[email] = name

print("")
for i in emails.items():
    print(f"{i[1]} ({i[0]})")
