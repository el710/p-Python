import os

os.system('cls')
print("Work with sets of arguments - same-root words\n")

def single_root_words(root_word, *other_words):
    same_words = []

    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichaclum', 'cheers', 'richies')
print(f'Same-root words for "rich":', result1)

result1 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(f'Same-root words for "Disablement":', result1)

input("\npress <Enter> to leave...")