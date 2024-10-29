
import os
import matplotlib.pyplot as plt

import jieba
from snownlp import SnowNLP
import thulac
import time

# 设置字体以支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 文件路径
file_path = '../data/re_filter.txt'

# 检查文件是否存在
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} does not exist.")

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 用于存储分词时间的字典
time_results = {
    'jieba': 0,
    'SnowNLP': 0,
    'THULAC': 0
}

# 1. jieba 分词
start_time = time.time()
for line in lines:
    list(jieba.cut(line))
end_time = time.time()
time_results['jieba'] = end_time - start_time

# 2. SnowNLP 分词
start_time = time.time()
for line in lines:
    s = SnowNLP(line)
    s.words
end_time = time.time()
time_results['SnowNLP'] = end_time - start_time

# 3. THULAC 分词
thu = thulac.thulac(seg_only=True)  # 只进行分词，不进行词性标注
start_time = time.time()
for line in lines:
    thu.cut(line, text=True)
end_time = time.time()
time_results['THULAC'] = end_time - start_time

# 结果展示
print("分词效率对比 (单位：秒):")
for lib, duration in time_results.items():
    print(f"{lib}: {duration:.4f} seconds")

# 绘图
plt.figure(figsize=(10, 6))
plt.bar(time_results.keys(), time_results.values(), color=['blue', 'green', 'red'])
plt.xlabel('分词库')
plt.ylabel('分词耗时 (秒)')
plt.title('jieba、SnowNLP、THULAC 分词效率对比')
plt.show()
