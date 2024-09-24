import re


def extract_numbers(input_string):
    # 使用正则表达式提取字符串中的所有数字
    numbers = re.findall(r"\d+", input_string)
    # 将提取到的数字从字符串转换为整数
    numbers = [int(num) for num in numbers]
    return numbers
