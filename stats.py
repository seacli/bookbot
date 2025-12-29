def count_words(content):
    # clean = content.translate(str.maketrans('', '', string.punctuation))
    # return len(clean.split())
    return len(content.split())

def count_characters(content):
    counts = {}
    for char in content.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    
    # Convert to list of dicts for sorting
    result = [{"char": c, "num": n} for c, n in counts.items()]
    result.sort(reverse=True, key=lambda x: x["num"])
    return result