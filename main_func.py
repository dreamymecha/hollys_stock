# 할리스 재고 관리 프로그램
# 베이커리는 더 이상 해동시키지 않아도 되는 듯

# 할리스 재고 관리 프로그램
# 베이커리는 더 이상 해동시키지 않아도 되는 듯

import requests, json
import time
import datetime
from dateutil.relativedelta import relativedelta

class Cleaning():
    def __init__(self):
        # 변수 설정
        self.pro_name = None
        self.method = None
        self.crit = None
        self.exp = None
        self.defro_start = None
        self.defro_end = None
        self.open_date = None
        self.hold_time = None

        # 노션 Setting
        self.token = 'secret_nseqnEbZWiM1dPJyrWqX1neTEOnGcdobO5d6xQI1Wnt'
        self.id_database = 'bc4349b14ba04fa1a4cd76c35213f844'
        self.headers = {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json",
            "Notion-Version": "2021-05-13"
        }

    def main(self, code):
        # 실질적인 데이터 섹션
        self.code = code
        if self.code == 1:
            self.pro_name = "플레인 얼음"
            self.method = "냉동"
            self.crit = input("제조일?(예: 2021-05-05)?: ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=3)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 2:
            self.method = "냉장"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=2) - relativedelta(days=1)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "밀크베이스(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "밀크베이스"
                self.hold_time = self.exp
        
        if self.code == 3:
            self.method = "냉장"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                div = int(input("소분했는가(예는 1, 아니오는 2)?: "))
                if div == 1:
                    self.pro_name = "빙수용 애플망고 베이스(드리즐통 소분)"
                    today = datetime.datetime.now()
                    self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                    hold_crit = today + datetime.timedelta(days=7)
                    self.hold_time = hold_crit.strftime("%Y-%m-%dT%H:%M+09:00")
                if div == 2:
                    self.pro_name = "빙수용 애플망고 베이스(개봉)"
                    today = datetime.datetime.now()
                    self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                    hold_crit = today + datetime.timedelta(days=30)
                    self.hold_time = hold_crit.strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "빙수용 애플망고 베이스"
                self.hold_time = self.exp
        
        if self.code == 4:
            self.method = "냉장"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                div = int(input("소분했는가(예는 1, 아니오는 2)?: "))
                if div == 1:
                    self.pro_name = "복숭아 베이스(드리즐통 소분)"
                    today = datetime.datetime.now()
                    self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                    hold_crit = today + datetime.timedelta(days=7)
                    self.hold_time = hold_crit.strftime("%Y-%m-%dT%H:%M+09:00")
                if div == 2:
                    self.pro_name = "복숭아 베이스(개봉)"
                    today = datetime.datetime.now()
                    self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                    hold_crit = today + datetime.timedelta(days=30)
                    self.hold_time = hold_crit.strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "복숭아 베이스"
                self.hold_time = self.exp
        
        if self.code == 5:
            self.method = "상온"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=3) - relativedelta(days=1)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "단팥(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                hold_crit = today + datetime.timedelta(days=5)
                self.hold_time = hold_crit.strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "단팥"
                self.hold_time = self.exp
        
        if self.code == 6:
            self.method = "상온"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                div = int(input("소분했는가(예는 1, 아니오는 2)?: "))
                if div == 1:
                    self.pro_name = "19곡물파우더(토핑통 소분)"
                    today = datetime.datetime.now()
                    self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                    hold_crit = today + datetime.timedelta(hours=72)
                    self.hold_time = hold_crit.strftime("%Y-%m-%dT%H:%M+09:00")
                if div == 2:
                    self.pro_name = "19곡물파우더(개봉)"
                    self.hold_time = self.exp
            if open == 2:
                self.pro_name = "19곡물파우더"
                self.hold_time = self.exp
        
        if self.code == 7:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "빙수떡(해동)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=4) + relativedelta(days=7)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "빙수떡"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 8:
            self.method = "실온"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "그래놀라믹스(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(days=30)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "그래놀라믹스"
                self.hold_time = self.exp
        
        if self.code == 9:
            self.method = "냉동"
            self.pro_name = "냉동딸기다이스"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=3) - relativedelta(days=1)).strftime("%Y-%m-%d")
        
        if self.code == 10:
            self.method = "상온"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "백도 통조림(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(days=5)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "백도 통조림"
                self.hold_time = self.exp
        
        if self.code == 11:
            self.method = "상온"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "화이트펄(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "화이트펄"
                self.hold_time = self.exp
        
        if self.code == 12:
            self.method = "상온"
            self.pro_name = "딸기파우더"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 13:
            self.method = "냉동"
            self.pro_name = "냉동망고슬라이스"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 14:
            self.method = "상온"
            self.pro_name = "코코넛 슬라이스"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 15:
            self.method = "냉동"
            self.pro_name = "애플망고 아이스크림"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 16:
            self.method = "냉동"
            div = int(input("소분했는가(예는 1, 아니오는 2)?: "))
            if div == 1:
                self.pro_name = "요거트 아이스크림(소분)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(days=5)).strftime("%Y-%m-%dT%H:%M+09:00")
            if div == 2:
                self.pro_name = "요거트 아이스크림"
                self.hold_time = self.exp

        if self.code == 17:
            self.method = "실온"
            self.pro_name = "나뭇잎코인"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 18:
            self.method = "실온"
            self.pro_name = "장식용 초코코인"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 19:
            self.method = "냉동"
            self.pro_name = "크로플"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 20:
            self.method = "냉동"
            self.pro_name = "크림치즈 비스켓"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 21:
            self.method = "냉장"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + datetime.timedelta(weeks=5)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "디카페인 커피 원액(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=72)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "디카페인 커피 원액"
                self.hold_time = self.exp
        
        if self.code == 22:
            self.method = "냉동"
            self.pro_name = "애플망고 스무디"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 23:
            self.method = "냉장"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "애플망고 베이스(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(days=20)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "애플망고 베이스"
                self.hold_time = self.exp
        
        if self.code == 24:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=10) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2/냉장 해동만)?: "))
            if defro == 1:
                self.pro_name = "오렌지 당근 착즙주스(냉장 해동)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=12)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=12) + datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "오렌지 당근 착즙주스"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 25:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=10) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2/냉장 해동만)?: "))
            if defro == 1:
                self.pro_name = "사과 비트 착즙주스(냉장 해동)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=12)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=12) + datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "사과 비트 착즙주스"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 26:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=3) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "애플망고 다이스(해동)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=6) + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "애플망고 다이스"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 27:
            self.method = "냉동"
            self.pro_name = "크로플"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=2) - relativedelta(days=1)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 28:
            self.method = "상온"
            self.pro_name = "슈가파우더"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 29:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=7) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "마스카포네 티라미스(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "마스카포네 티라미스"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 30:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=7) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "쿠키&치즈(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "쿠키&치즈"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 31:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=7) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "뉴욕 치즈(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "뉴욕 치즈"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 32:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "리얼 벨지안 초코(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "리얼 벨지안 초코"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 33:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "딸기 생크림(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "딸기 생크림"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 34:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "블루베리 치즈 라운드(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "블루베리 치즈 라운드"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 35:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "초코벨벳 라운드(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "초코벨벳 라운드"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 36:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "티라미스 라운드(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "티라미스 라운드"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 37:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "표곰이 하우스(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=4) + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "표곰이 하우스"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 38:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "산딸기 빅카롱(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=1) + datetime.timedelta(days=5)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "산딸기 빅카롱"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 39:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "초코 빅카롱(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=1) + datetime.timedelta(days=5)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "초코 빅카롱"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 40:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=3) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "뉴 크로크무슈(해동)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "뉴 크로크무슈"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 41:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "페스토 햄 모짜렐라 샌드위치(해동)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=9)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "페스토 햄 모짜렐라 샌드위치"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 42:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "올리브 베이컨 치아바타 샌드위치(해동)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=9)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "올리브 베이컨 치아바타"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 43:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "미트볼 칠리 치즈 샌드위치(해동)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=9)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "미트볼 칠리 치즈 샌드위치"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 44:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "샌드위치 식빵(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "샌드위치 식빵"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 45:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "오곡 식빵(쇼케이스)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "오곡 식빵"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 46:
            self.method = "냉장"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "뿌셔먹는 에그샐러드(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(days=2)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "뿌셔먹는 에그샐러드"
                self.hold_time = self.exp
        
        # 이 부분에 대해서는 논의 요망
        if self.code == 47:
            self.method = "냉장"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(days=3)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "뿌셔먹는 에그샐러드(으깬 거, 개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(days=2)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "뿌셔먹는 에그샐러드(으깬 거)"
                self.hold_time = self.exp
        
        if self.code == 48:
            self.method = "냉장"
            self.pro_name = "에그마요"
            today = datetime.datetime.now()
            self.hold_time = (today + datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M+09:00")
        
        if self.code == 49:
            self.method = "냉장"
            self.pro_name = "반반마요"
            today = datetime.datetime.now()
            self.hold_time = (today + datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M+09:00")
        
        if self.code == 50:
            self.pro_name = "사라다 샐러드"
            self.method = "냉장"
            self.crit = input("제조일?(예: 2021-05-05)?: ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(days=40)).strftime("%Y-%m-%d")
            self.hold_time = self.exp
        
        if self.code == 51:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "바삭불고기 & 트리플치즈치킨(해동)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "바삭불고기 & 트리플치즈치킨"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 52:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "매콤닭갈비 & 바베큐포크(해동)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "매콤닭갈비 & 바베큐포크"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 53:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "베이컨 에그데니쉬(해동)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=9)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "베이컨 에그데니쉬"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 54:
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=6) - relativedelta(days=1)).strftime("%Y-%m-%d")
            defro = int(input("해동을 시작했는가(예는 1, 아니오는 2)?: "))
            if defro == 1:
                self.pro_name = "스위트콘 에그데니쉬(해동)"
                self.method = "냉장"
                today = datetime.datetime.now()
                self.defro_start = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.defro_end = (today + datetime.timedelta(hours=9)).strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=36)).strftime("%Y-%m-%dT%H:%M+09:00")
            if defro == 2:
                self.pro_name = "스위트콘 에그데니쉬"
                self.method = "냉동"
                self.hold_time = self.exp
        
        if self.code == 76:
            self.method = "냉장"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = datetime.date(y, m, d) + datetime.timedelta(weeks=5)
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "콜드브루 원액(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(hours=72)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "콜드브루 원액"
        
        # 커피의 개봉 여부는 어떻게 판단을 할지?
        if self.code == 77:
            self.method = "상온"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "에스프레소 로스트(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "에스프레소 로스트"
        
        if self.code == 78:
            self.method = "상온"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "프리미엄 블렌드(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "프리미엄 블렌드"
        
        if self.code == 79:
            self.method = "상온"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = datetime.date(y, m, d) + relativedelta(years=1) - relativedelta(days=1)
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "메뉴 제조용 MD 커피(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "메뉴 제조용 MD 커피"
        
        if self.code == 80:
            self.method = "냉장"
            self.pro_name = "일반 우유"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = datetime.date(y, m, d) + datetime.timedelta(days=14)
        
        if self.code == 81:
            self.method = "냉장"
            self.pro_name = "저지방 우유"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = datetime.date(y, m, d) + datetime.timedelta(days=12)
        
        if self.code == 82:
            self.method = "냉장"
            self.crit = input("제조일?(예: 2021-05-05): ")
            self.crit_split = self.crit.split('-')
            y = int(self.crit_split[0])
            m = int(self.crit_split[1])
            d = int(self.crit_split[2])
            self.exp = (datetime.date(y, m, d) + relativedelta(months=8) - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            open = int(input("개봉했는가(예는 1, 아니오는 2)?: "))
            if open == 1:
                self.pro_name = "스프레이형 휘핑기(개봉)"
                today = datetime.datetime.now()
                self.open_date = today.strftime("%Y-%m-%dT%H:%M+09:00")
                self.hold_time = (today + datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M+09:00")
            if open == 2:
                self.pro_name = "스프레이형 휘핑기"
                self.hold_time = self.exp

    def add_notion(self):
        # 노션 작동
        self.createURL = 'https://api.notion.com/v1/pages'
        if self.defro_start == None:
            if self.exp == None:
                if self.hold_time == None:
                    newPageData = {
                    "parent": {"database_id": self.id_database},
                    "properties": {
                        "상품명": {"title": [{"text": {"content": self.pro_name}}]},
                        "보관법": {"select": {"name": self.method}}
                        }
                    }
                else:
                    newPageData = {
                        "parent": {"database_id": self.id_database},
                        "properties": {
                            "상품명": {"title": [{"text": {"content": self.pro_name}}]},
                            "보관법": {"select": {"name": self.method}},
                            "홀딩 타임": {"date": {"start": self.hold_time}}
                        }
                    }
            else:
                if self.open_date == None:
                    newPageData = {
                        "parent": {"database_id": self.id_database},
                        "properties": {
                            "유통기한": {"date": {"start": self.exp}},
                            "홀딩 타임": {"date": {"start": self.hold_time}},
                            "상품명": {"title": [{"text": {"content": self.pro_name}}]},
                            "보관법": {"select": {"name": self.method}}
                        }
                    }
                else:
                    newPageData = {
                        "parent": {"database_id": self.id_database},
                        "properties": {
                            "유통기한": {"date": {"start": self.exp}},
                            "개봉일": {"date": {"start": self.open_date}},
                            "홀딩 타임": {"date": {"start": self.hold_time}},
                            "상품명": {"title": [{"text": {"content": self.pro_name}}]},
                            "보관법": {"select": {"name": self.method}}
                        }
                    }
        else:
            newPageData = {
                "parent": {"database_id": self.id_database},
                "properties": {
                    "유통기한": {"date": {"start": self.exp}},
                    "해동 시작 시간": {"date": {"start": self.defro_start}},
                    "해동 종료 시간": {"date": {"start": self.defro_end}},
                    "홀딩 타임": {"date": {"start": self.hold_time}},
                    "상품명": {"title": [{"text": {"content": self.pro_name}}]},
                    "보관법": {"select": {"name": self.method}}
                }
            }
        
        data = json.dumps(newPageData)
        self.res = requests.request("POST", self.createURL, headers=self.headers, data=data)

        if self.res.status_code == 200:
            print("기록 성공")
        else:
            print("기록 실패...")
        print("결과:", self.pro_name, self.method, self.exp, self.open_date, self.defro_start, self.defro_end, self.hold_time)