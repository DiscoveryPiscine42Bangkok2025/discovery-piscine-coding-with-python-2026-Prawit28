def array_of_names(person):
    full_name = {f"{first.capitalize()} {last.capitalize()}" for first, last in person.items()}
    return full_name

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))