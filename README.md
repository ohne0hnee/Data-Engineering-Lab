# 🧪 Data Engineering Lab

데이터 수집 · 정제 · 적재 · 분석을 직접 해 보며 정리하는 개인 실습 저장소입니다.

<sub>실습마다 폴더를 나누고, 각 폴더의 README에 과정 · 문제 · 결과 · 배운 점을 정리합니다.</sub>

<br>

## 📚 실습 목록

| <sub>#</sub> | <sub>실습</sub> | <sub>내용</sub> | <sub>기술</sub> |
|:--:|:--|:--|:--|
| <sub>01</sub> | <sub>[PDF 표 데이터 파싱](./01-pdf-table-parsing)</sub> | <sub>모집요강 PDF에서 표를 추출하고, 뭉친 셀 · 각주 · 숫자 표기를 정제 · 검증</sub> | <sub>`Python` `pdfplumber` `pandas` `정규식`</sub> |

<br>

## 📁 구조

```
Data-Engineering-Lab/
├── README.md                 ← 전체 목차 (이 파일)
└── 01-pdf-table-parsing/     ← 실습별 폴더
    ├── README.md
    ├── parse.py
    ├── clean.py
    └── 모집인원_정제.csv
```

<sub>원본 문서(PDF)와 중간 산출물은 저장소에 포함하지 않습니다.</sub>
