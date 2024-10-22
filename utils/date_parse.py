import re

from dateutil import parser as dateutil
from datetime import datetime


def date_parse_timestamp(date_str):
    return int(
        dateutil.parse(re.sub(r"[年月]", "-", date_str).replace("日", "")).timestamp()
    )


def parse_chinese_date(date_string: str) -> datetime:
    """
    将包含中文日期字符串解析为 datetime 对象。

    参数:
        date_string (str): 中文日期字符串，例如 '2024年04月18日'。

    返回:
        datetime: 解析后的 datetime 对象。
    """
    # 替换中文日期分隔字符为适合解析的字符
    formatted_date_string = (
        date_string.replace("年", "-").replace("月", "-").replace("日", "")
    )

    # 解析并返回 datetime 对象
    return dateutil.parse(formatted_date_string)
