#10769 행복한지 슬픈지

emo = input()
good = emo.count(":-)")
bad = emo.count(":-(")
if good == bad == 0:
    print("none")
elif good > bad:
    print("happy")
elif good < bad:
    print("sad")
else:
    print("unsure")