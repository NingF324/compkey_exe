from collections import Counter
from word_similarity import word_similarity

def seedwords_file(seedword, input_file, output_file):
    with open(input_file, encoding='utf-8') as origin_data, open(output_file, 'w', encoding='utf-8') as result_data:
        for sentence in origin_data:
            if seedword in sentence:
                result_data.write(sentence)


def get_s_sa(seedword, agencyword, search_info_file):
    s_num = sa_num = 0
    with open(search_info_file, encoding='utf-8') as origin_data:
        for sentence in origin_data:
            if seedword in sentence:
                s_num += 1
            if agencyword in sentence:
                sa_num += 1
    return s_num, sa_num


def seed_agent(output_file, seedword, stopwords_filtered_file, search_info_file):
    word_list = []
    with open(stopwords_filtered_file, encoding='utf-8') as data:
        for word in data:
            word_list.append(word.strip())

    count_result = Counter(word_list)
    result = []

    for key, val in count_result.most_common(100):
        if word_similarity(seedword, key):
            continue
        s_num, sa_num = get_s_sa(seedword, key, search_info_file)

        if key == seedword:
            key_val = f"关键字：{key} || 出现次数：{val}"
        else:
            weight = round(sa_num / s_num, 8) if s_num else 0
            key_val = f"关键字：{key} || 出现次数：{val} || 中介关键词权重：{weight}"
        result.append(key_val)

    # 按中介关键词权重降序排列
    result.sort(key=lambda x: float(x.split("中介关键词权重：")[-1]) if "中介关键词权重：" in x else 0, reverse=True)

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in result:
            file.write(line + '\n')