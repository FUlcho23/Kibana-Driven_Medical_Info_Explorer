'''
Created on 2025. 4. 18.

@author: user
'''
import csv

def format_time(t):
    t = t.strip()
    if not t or not t.isdigit():
        return t  # 공백 또는 숫자 아님은 그대로
    t = t.zfill(4)  # 900 -> 0900
    return f"{int(t[:2])}:{t[2:]}"  # 0900 -> 9:00

time_fields = [  # 정제할 시간 필드들
    "점심시간_평일", "점심시간_토요일", "접수시간_평일", "접수시간_토요일",
    "진료시작시간_일요일", "진료종료시간_일요일",
    "진료시작시간_월요일", "진료종료시간_월요일",
    "진료시작시간_화요일", "진료종료시간_화요일",
    "진료시작시간_수요일", "진료종료시간_수요일",
    "진료시작시간_목요일", "진료종료시간_목요일",
    "진료시작시간_금요일", "진료종료시간_금요일",
    "진료시작시간_토요일", "진료종료시간_토요일"
]

with open('의료기관_정제전.csv', 'r', encoding='utf-8') as infile, \
     open('의료기관_정제.csv', 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        for field in time_fields:
            if field in row:
                row[field] = format_time(row[field])
        writer.writerow(row)
