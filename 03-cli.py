from ai import get_personality_analysis
print("# AI 관상가입니다. 얼굴 특징을 입력해주시면 성격과 미래를 전망해드립니다.")
line = input("").strip()
if not line:
    print(repr(line))
