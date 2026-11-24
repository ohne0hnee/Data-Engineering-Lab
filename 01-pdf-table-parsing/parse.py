import pdfplumber
import pandas as pd

PDF_PATH = "report.pdf"   # 실제 파일 이름으로 바꾸기

# 1단계: 첫 페이지 텍스트 확인
with pdfplumber.open(PDF_PATH) as pdf:
    print("페이지 수:", len(pdf.pages))
    print("----- 1페이지 텍스트 -----")
    print(pdf.pages[0].extract_text())

# 2단계: 전체 페이지 표 추출 → CSV 저장
rows = []
with pdfplumber.open(PDF_PATH) as pdf:
    for i, page in enumerate(pdf.pages):
        for table in page.extract_tables():
            for row in table:
                rows.append([i + 1] + row)   # 맨 앞에 페이지 번호

df = pd.DataFrame(rows)
df = df.dropna(how="all")                          # 빈 행 제거
df = df.replace(r"\n", " ", regex=True)            # 셀 안 줄바꿈 정리
df.to_csv("tables.csv", index=False, encoding="utf-8-sig")

print("----- 추출한 표 (앞 20행) -----")
print(df.head(20))
print("표 행 수:", len(df))
