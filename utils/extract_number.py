import re


def extract_number(text):
    # 使用正则表达式提取字符串中的数字，包括小数
    match = re.search(r"\d+(\.\d+)?", text)
    if match:
        number_str = match.group()
        # 判断是否包含小数点
        if "." in number_str:
            return float(number_str)
        else:
            return int(number_str)
    else:
        raise ValueError(f"No valid number found in input text: {text}")
