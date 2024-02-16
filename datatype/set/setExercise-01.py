speak_french = {"Coraline", "Delphine", "Quincy", "Alexandre", "Guillaume", "Juliette", "Camille", "Elodie", "Windsor"}
speak_german = {"Andreas", "Windsor", "Emmeline", "Frieda", "Delphine", "Maude", "Oliver", "Juliette"}

### speak both french, german:
speak_both = speak_french.intersection(speak_german)
print("List of student who can speak both French and German")
for student in speak_both:
    print(student)

### speak only French
speak_only_french = speak_french.difference(speak_german)
print("List of student who can speak only French")
for student in speak_only_french:
    print(student)

### speak only German
speak_only_german = speak_german.difference(speak_french)
print("List of student who can speak only German")
for student in speak_only_german:
    print(student)

#### speak at least one langue
speak_at_least_one = speak_french.union(speak_german)
print("List of student who can speak at least one langue")
for student in speak_at_least_one:
    ln = None
    if (student in speak_french) and (student in speak_german):
        ln = "French and German"
    elif student in speak_french:
        ln = "French"
    elif student in speak_german:
        ln = "German"

    print(f"{student} speak {ln}")

#### speak at least only one langue
speak_only_one = speak_french.symmetric_difference(speak_german)
print("List of student who can speak only one langue")
for student in speak_only_one:
    ln = f"{'French' if student in speak_french else 'German'}"
    print(f"{student} only speak {ln}")

