import main_def

print("----------재고 정리 작업을 시작합니다----------")
code = int(input("제품 코드 입력(1 ~ ?): "))

BOT = main_def.cleaning()
BOT.input(code)