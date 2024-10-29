import jieba


def jieba_segment(input_file, output_file):
    sep_list = []
    with open(input_file, encoding='utf-8') as data:
        for word in data:
            seg_list = list(jieba.cut(word.strip(), cut_all=False))
            sep_list.extend(seg_list)

    with open(output_file, 'w', encoding='utf-8') as file:
        for words in sep_list:
            file.write(words + '\n')
