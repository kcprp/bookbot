def get_num_words(text):
    return len(text.split())  

def count_characters(text):
    character_count = {}
    for char in text:
        if char.lower() not in character_count:
            character_count[char.lower()] = 1
        else:
            character_count[char.lower()] += 1
           
    sorted_count = dict(sorted(character_count.items(), key=lambda x: x[1], reverse=True))
    return sorted_count