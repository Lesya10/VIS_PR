from validators import parse_line
from report import print_table, print_errors, print_groups, save_ok, save_errors

ANKETA_FILE = "anketa.txt"

def main():
    try:
        with open(ANKETA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Файл {ANKETA_FILE} не найден")
        return

    good = []
    errors = []
    total_lines = 0

    for lineno, raw in enumerate(lines, 1):
        line = raw.strip()
        if not line:
            continue
        total_lines += 1
        anketa, err = parse_line(line)
        if err:
            errors.append((lineno, raw.rstrip("\n"), err))
        else:
            good.append(anketa)

    good.sort(key=lambda a: a["fio"])

    stat = {}
    for a in good:
        stat[a["group"]] = stat.get(a["group"], 0) + 1

    print_table(good)
    print_errors(errors)
    print(f"\nВсего строк в файле: {total_lines}")
    print(f"Принято: {len(good)} | Отклонено: {len(errors)}")
    print_groups(stat)

    save_ok(good)
    save_errors(errors)

if __name__ == "__main__":
    main()