def remove_stop_words(word_file, stop_words_file, output_file):
    with open(stop_words_file, 'r', encoding='utf-8') as file:
        stop_words_list = file.read().splitlines()

    word_list = []
    with open(word_file, encoding='utf-8') as data:
        for word in data:
            word = word.strip()
            if word not in stop_words_list:
                word_list.append(word)

    with open(output_file, 'w', encoding='utf-8') as file:
        for word in word_list:
            file.write(word + '\n')
