import datetime

now = datetime.datetime.now()
hour = now.hour

# 08:00–21:59 — работаем; 22:00 и позже, а также до 08:00 — выходим
if not (8 <= hour < 22):
    print(f"Skipping run: current hour is {hour}, outside allowed window (08–22).")
    exit(0)

from news_collector.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
