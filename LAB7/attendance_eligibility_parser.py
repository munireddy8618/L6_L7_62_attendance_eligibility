def normalize_srn(srn):
    if not isinstance(srn, str):
        return ""
    return srn.strip().replace(' ', '').upper()


def attendance_from_ratio(text):
    if not isinstance(text, str):
        return 0
    try:
        parts = text.strip().split('/')
        if len(parts) != 2:
            return 0

        attended = int(parts[0].strip())
        held = int(parts[1].strip())

        if held <= 0:
            return 0

        return attended * 100 // held
    except (ValueError, TypeError):
        return 0


def attendance_from_register(marks):
    if not isinstance(marks, str):
        return 0

    marks = marks.strip().upper()
    if not marks:
        return 0

    return marks.count('P') * 100 // len(marks)


def main():
    print("==== Running normalize_srn ====")
    value = input("Enter an SRN (e.g. pes1ug23cs001): ")
    print("Normalized SRN:", normalize_srn(value))

    print("\n==== Running attendance_from_ratio ====")
    value = input("Enter classes attended and held (e.g. 30/40): ")
    print("Attendance percent:", attendance_from_ratio(value))

    print("\n==== Running attendance_from_register ====")
    value = input("Enter register marks (e.g. PPAPP): ")
    print("Attendance percent:", attendance_from_register(value))


if __name__ == "__main__":
    main()
