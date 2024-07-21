def character_count(s):
    return {char: s.count(char) for char in set(s)}

print(character_count("hello world"))
