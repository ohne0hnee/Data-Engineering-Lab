import re
import pandas as pd

# 1) 앞에서 만든 CSV 읽기 (모든 값을 문자열로)
df = pd.read_csv("tables.csv", dtype=str).fillna("")
df.columns = ["page", "c1", "학과", "지역균형", "일반", "기회균형", "합계", "c7", "c8", "c9"]

# 2) 9~11페이지 모집인원 표만, 헤더·소계·학과명 없는 행은 빼기
t = df[df["page"].isin(["9", "10", "11"])]
t = t[(t["학과"] != "") & (t["학과"] != "소계") & (t["지역균형"] != "지역균형전형")]

# 3) 숫자 정제: 각주 "(42))" 지우기, 쉼표 지우기, "·"는 0
def to_num(s):
    s = re.sub(r"\(.*", "", s).replace(",", "").strip()
    return 0 if s in ("·", "") else int(s)

# 4) 한 셀에 뭉친 값을 공백으로 쪼개서 학과별 행으로 펼치기
rows, check = [], []
for _, r in t.iterrows():
    names = r["학과"].split()
    cols = [r["지역균형"].split(), r["일반"].split(), r["기회균형"].split()]
    if all(len(c) == len(names) for c in cols):        # 개수가 맞으면 펼치기
        for i, name in enumerate(names):
            rows.append([r["page"], name] + [to_num(c[i]) for c in cols])
    else:                                              # 안 맞으면 따로 모아 두기
        check.append([r["page"], r["학과"], len(names), [len(c) for c in cols]])

out = pd.DataFrame(rows, columns=["page", "학과", "지역균형", "일반", "기회균형"])
out["합계"] = out[["지역균형", "일반", "기회균형"]].sum(axis=1)
out.to_csv("모집인원_정제.csv", index=False, encoding="utf-8-sig")

print(out.head(20))
print("정제된 학과 수:", len(out))
print("\n----- 개수가 안 맞아 확인이 필요한 행 -----")
for c in check:
    print(f"p{c[0]} | 학과 {c[2]}개 vs 숫자 {c[3]}개 | {c[1][:40]}")
