W_NUM, W_FIO, W_MAIL, W_PHONE, W_GROUP = 3, 35, 21, 19, 8
OK_FILE = "ok.txt"
ERRORS_FILE = "errors.txt"

def mask_phone(phone):
    digits = "".join(c for c in phone if c.isdigit())
    return f"+7 ({digits[1:4]}) ***-**-{digits[-2:]}"

def print_table(anketas):
    print(f"{'№':>{W_NUM}}  {'ФИО':<{W_FIO}} {'Почта':<{W_MAIL}} "
          f"{'Телефон':<{W_PHONE}} {'Группа':<{W_GROUP}}")
    line_w = W_NUM + 2 + W_FIO + 1 + W_MAIL + 1 + W_PHONE + 1 + W_GROUP
    print("-" * line_w)

    for i, a in enumerate(anketas, 1):
        fio = a["fio"]
        if len(fio) > W_FIO:
            fio = fio[:W_FIO - 1] + "…"
        print(f"{i:>{W_NUM}}  {fio:<{W_FIO}} {a['mail']:<{W_MAIL}} "
              f"{mask_phone(a['phone']):<{W_PHONE}} {a['group']:<{W_GROUP}}")

    print("-" * line_w)

def print_errors(errors):
    print(f"\nОтклонено строк: {len(errors)}")
    for lineno, raw, reason in errors:
        print(f"  строка {lineno}: {reason}")
        print(f"      {raw}")

def print_groups(stat):
    print("\nПо группам:")
    for group in sorted(stat):
        print(f"  {group:<{W_GROUP}} {stat[group]}")

def save_ok(anketas):
    with open(OK_FILE, "w", encoding="utf-8") as f:
        for a in anketas:
            f.write(f"{a['fio']};{a['mail']};{a['phone']};{a['group']}\n")

def save_errors(errors):
    with open(ERRORS_FILE, "w", encoding="utf-8") as f:
        for lineno, raw, reason in errors:
            f.write(f"строка {lineno}: {reason}\n{raw}\n")