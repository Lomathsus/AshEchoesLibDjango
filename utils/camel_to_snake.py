import re


def camel_to_snake(name):
    """
    将大驼峰命名法转换为下划线命名法。
    例如：CamelCase -> camel_case
    """
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
