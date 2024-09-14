def constrained_hash(s: str) -> int:
    """
    A hash function that generates a number strictly under 13
    based on the input string. It uses character values and a
    simple weighted scheme to ensure distinct outputs.
    """
    hash_value = 0

    for char in s:
        hash_value = (hash_value + ord(char))*68 / 37
    
    hash_value //= 1
    hash_value %= 13
    return int(hash_value)
# List of words to hash
words = [
    "Games Played",
    "Goals",
    "Assists",
    "Tackles",
    "Interceptions",
    "Star Skill",
    "Weak Foot Ability",
    "Weight",
    "Height"
]

# Print each word with its corresponding hash value
for word in words:
    hash_value = constrained_hash(word)
    print(f"{word}: {hash_value}")
