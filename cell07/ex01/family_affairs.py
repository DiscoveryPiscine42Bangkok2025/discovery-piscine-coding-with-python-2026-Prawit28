def find_the_redheads(person):
    redheads = {f"{first}" for first, last in person.items() if last.lower() == "red"}
    return redheads

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))