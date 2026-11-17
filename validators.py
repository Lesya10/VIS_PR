def correct_full_name(fio):
    return " ".join(part.strip() for part in fio.split()).title()

def count_full_name(fio):
    return len(fio.split())

def parse_fio(raw):
    fio = correct_full_name(raw)
    if count_full_name(fio) < 2:
        return None, "в ФИО меньше двух слов"
    return fio, None

def parse_mail(raw):
    mail = raw.strip().lower()
    if mail.count("@") != 1:
        return None, f"почта неверная: {mail}"
    local, domain = mail.split("@")
    if not local or not domain:
        return None, f"почта неверная: {mail}"
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return None, f"почта неверная: {mail}"
    return mail, None

def parse_phone(raw):
    digits = ""
    for char in raw:
        if char.isdigit():
            digits += char

    if len(digits) != 11:
        return None, f"телефон неверный: {raw.strip()}"
    if digits[0] not in ("7", "8"):
        return None, f"телефон неверный: {raw.strip()}"

    phone = f"+7 ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:11]}"
    return phone, None

def parse_group(raw):
    group = raw.replace(" ", "").lower()
    if not group:
        return None, "пустая группа"
    return group, None

def parse_line(line):
    fields = line.split(";")
    if len(fields) != 4:
        return None, f"полей не четыре (а {len(fields)})"

    fio, err = parse_fio(fields[0])
    if err:
        return None, err

    mail, err = parse_mail(fields[1])
    if err:
        return None, err

    phone, err = parse_phone(fields[2])
    if err:
        return None, err

    group, err = parse_group(fields[3])
    if err:
        return None, err

    return {"fio": fio, "mail": mail, "phone": phone, "group": group}, None