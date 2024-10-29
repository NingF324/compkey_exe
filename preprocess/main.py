import datetime
from encoding_detector import detect_encoding
from log_filter import filter_logs
from jieba_segmentation import jieba_segment
from stop_words_remover import remove_stop_words
from word_counter import count_words
from path_utils import path_check
from search_extraction import seedwords_file
from search_extraction import seed_agent




def main():
    # 开始计时
    start = datetime.datetime.now()

    # Step 1: 检测编码
    filepath = "../data/user_tag_query.1W.TRAIN"
    fileencoding, confidence = detect_encoding(filepath)
    print(f"文件编码: {fileencoding}, 置信度: {confidence}")

    # Step 2: 读取文件并过滤无效内容
    filtered_log_file = "all_logs.txt"
    filter_logs(filepath, filtered_log_file, fileencoding)
    print("无效内容过滤完成")

    # Step 3: 对过滤后的文件进行 jieba 分词
    segmented_file = "jieba_words.txt"
    jieba_segment(filtered_log_file, segmented_file)
    print("jieba 分词完成")

    # Step 4: 移除分词结果中的停用词
    stop_words_file = "../data/stop_words.txt"
    stopwords_filtered_file = "stopwords_filter.txt"
    remove_stop_words(segmented_file, stop_words_file, stopwords_filtered_file)
    print("停用词过滤完成")

    # Step 5: 统计关键词出现次数并保存结果
    counted_file = "seeds_keyvalue.txt"
    count_words(stopwords_filtered_file, counted_file)
    print("关键词计数完成")

    # Step 6: 检查并创建需要的路径
    # 存储与种子关键词相关的中介关键词及其出现次数。每个文件包含一个种子关键词的结果，其中列出了与之相关的中介关键词及其出现频率或权重
    path_check('./seedwords_agencywords/search_info')
    # 存储对包含种子关键词的搜索信息进行 jieba 分词后的结果。每个文件以种子关键词命名，包含对该关键词的相关搜索信息进行分词后的所有词汇
    path_check('./seedwords_agencywords/jieba_search_info')
    # 存储过滤后的搜索信息文件。每个文件以种子关键词命名，包含在原始日志中包含该关键词的所有行
    path_check('./seedwords_agencywords/stop_words_filter')
    # 存储经过停用词清洗后的关键词列表。每个文件以种子关键词命名，包含与该种子关键词相关的词汇，去除了停用词后的结果
    path_check('./seedwords_agencywords/agency_words')
    print("目录检查完成")

    # Step 7: 中介关键词的处理
    seedwords_list = ['手机', '长沙', '汽车', '旅游', '美国', 'lol', '电影', '中国', '淘宝', '小米', '百度', '英语', '支付宝']

    # 对于每个种子关键词，分别生成包含关键词的搜索信息文件、分词结果文件以及停用词过滤文件
    for seedword in seedwords_list:
        # 提取包含种子关键词的搜索信息
        search_info_file = f'./seedwords_agencywords/search_info/seedword_{seedword}.txt'
        seedwords_file(seedword, filtered_log_file, search_info_file)

        # 对搜索信息进行 jieba 分词
        jieba_output_file = f'./seedwords_agencywords/jieba_search_info/seedword_{seedword}.txt'
        jieba_segment(search_info_file, jieba_output_file)

        # 对分词结果进行停用词过滤
        stopwords_filtered_output = f'./seedwords_agencywords/stop_words_filter/seedword_{seedword}.txt'
        remove_stop_words(jieba_output_file, stop_words_file, stopwords_filtered_output)

        # 对关键词计数并计算中介关键词权重
        agency_words_file = f'./seedwords_agencywords/agency_words/seedword_{seedword}.txt'
        seed_agent(agency_words_file, seedword, stopwords_filtered_output, search_info_file)
        print(f"{seedword} 的处理完成")

    # 结束计时
    end = datetime.datetime.now()
    print('运行时间: 0:41:28.052038 秒')
    print('运行时间: %s 秒' % (end - start))


if __name__ == "__main__":
    main()