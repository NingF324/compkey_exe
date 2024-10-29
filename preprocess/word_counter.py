from collections import Counter


def count_words(input_file, output_file):
    with open(input_file, encoding='utf-8') as file:
        word_list = [line.strip() for line in file]
    count_result = Counter(word_list)

    with open(output_file, 'w', encoding='utf-8') as file:
        for key, val in count_result.most_common(2000):
            file.write(f"关键字：{key} || 出现次数：{val}\n")
