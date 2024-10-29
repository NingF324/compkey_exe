import re

def filter_logs(input_file, output_file, encoding='utf-8'):
    with open(input_file, 'r', encoding=encoding) as data, open(output_file, 'w', encoding='utf-8') as file:
        pattern = r'https?://\S+|www\.\S+|[\w.-]+@[\w.-]+|'
        for word in data:
            filtered_line = re.sub(pattern, '', word)
            if filtered_line.strip():  # 检查过滤后的行是否不为空
                file.write(filtered_line)

