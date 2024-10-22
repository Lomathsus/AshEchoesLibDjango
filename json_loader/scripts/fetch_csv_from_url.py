import requests
import csv


def fetch_csv_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # 如果请求失败，抛出HTTPError
    content = response.content.decode("utf-8")
    csv_data = csv.DictReader(content)
    # return csv_data
    for row in csv_data:
        print(row["id"])


fetch_csv_from_url("https://seed.qq.com/act/a20240905record/pc/csv/kachi.csv")
