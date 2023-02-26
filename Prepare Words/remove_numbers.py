with open('words_to_remove_number.txt') as word_file:
    words_with_nums = word_file.readlines()

words = []

for word in words_with_nums:
    split = word.split()
    with open('polishwords.txt', 'a') as f:
        f.write(f"{split[0]}\n")
