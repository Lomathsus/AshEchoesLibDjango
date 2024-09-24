import re

from dateutil import parser as dateutil


def date_parse(date_str):
    return dateutil.parse(re.sub(r"[年月]", "-", date_str).replace("日", "")).date()
