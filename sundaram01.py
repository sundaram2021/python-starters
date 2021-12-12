def word(name):
    if len(name) >= 4:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        'name is too short'
print(word('adarsh'))
