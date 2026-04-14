# ============================================================
# HỆ THỐNG QUẢN LÝ ĐIỂM SINH VIÊN
# Học phần: Lập trình Python (FIT4018)
# Sinh viên: Nguyễn Hữu Hoàng - MSSV: 0379101031
# Lớp: D0625HNCNA4
# ============================================================


def initialize_students():
    """Khởi tạo danh sách sinh viên trống trong bộ nhớ."""
    return []


def display_menu():
    """Hiển thị menu chức năng."""
    print("\n--- HỆ THỐNG QUẢN LÝ ĐIỂM SINH VIÊN ---")
    print("1. Thêm Sinh viên Mới")
    print("2. Xem Danh sách Sinh viên")
    print("3. Tìm kiếm Sinh viên")
    print("4. Xóa Sinh viên")
    print("5. Thống kê Điểm")
    print("6. Thoát chương trình")
    print("-" * 42)


def classify_grade(gpa):
    """Xếp loại học lực dựa trên điểm trung bình."""
    if gpa >= 9.0:
        return "Xuất sắc"
    elif gpa >= 8.0:
        return "Giỏi"
    elif gpa >= 6.5:
        return "Khá"
    elif gpa >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"


def validate_score(prompt):
    """Yêu cầu nhập điểm và kiểm tra tính hợp lệ (0-10)."""
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 10:
                return score
            else:
                print("Lỗi: Điểm phải nằm trong khoảng 0 đến 10.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ.")


def add_student(students):
    """Thêm một sinh viên mới vào danh sách."""
    print("\n--- THÊM SINH VIÊN MỚI ---")
    name = input("Nhập Họ và Tên: ").strip()
    mssv = input("Nhập MSSV: ").strip()

    if not name or not mssv:
        print("Lỗi: Họ tên và MSSV không được để trống.")
        return

    for student in students:
        if student['mssv'] == mssv:
            print(f"Lỗi: MSSV '{mssv}' đã tồn tại trong danh sách.")
            return

    midterm = validate_score("Nhập Điểm giữa kỳ (0-10): ")
    final = validate_score("Nhập Điểm cuối kỳ (0-10): ")

    gpa = round(midterm * 0.4 + final * 0.6, 2)
    grade = classify_grade(gpa)

    new_student = {
        "name": name,
        "mssv": mssv,
        "midterm": midterm,
        "final": final,
        "gpa": gpa,
        "grade": grade
    }
    students.append(new_student)
    print(f"Đã thêm sinh viên '{name}' (ĐTB: {gpa} - {grade}) thành công.")


def view_students(students):
    """Hiển thị toàn bộ danh sách sinh viên."""
    if not students:
        print("\nDanh sách sinh viên hiện đang trống.")
        return

    print("\n--- DANH SÁCH SINH VIÊN ---")
    print(f"{'STT':<5}{'HỌ TÊN':<22}{'MSSV':<15}{'GIỮA KỲ':<10}{'CUỐI KỲ':<10}{'ĐTB':<8}{'XẾP LOẠI':<12}")
    print("-" * 82)

    for i, s in enumerate(students, 1):
        print(f"{i:<5}{s['name'][:20]:<22}{s['mssv'][:13]:<15}{s['midterm']:<10}{s['final']:<10}{s['gpa']:<8}{s['grade']:<12}")

    print("-" * 82)
    print(f"Tổng cộng: {len(students)} sinh viên")


def search_student(students):
    """Tìm kiếm sinh viên theo họ tên hoặc MSSV."""
    if not students:
        print("\nDanh sách trống, không thể tìm kiếm.")
        return

    keyword = input("\nNhập Họ tên hoặc MSSV cần tìm: ").strip().lower()
    if not keyword:
        print("Vui lòng nhập từ khóa tìm kiếm.")
        return

    results = []
    for s in students:
        if keyword in s['name'].lower() or keyword in s['mssv'].lower():
            results.append(s)

    if results:
        print(f"\n--- KẾT QUẢ TÌM KIẾM ({len(results)} sinh viên) ---")
        for i, s in enumerate(results, 1):
            print(f"{i}. {s['name']} | MSSV: {s['mssv']} | "
                  f"Giữa kỳ: {s['midterm']} | Cuối kỳ: {s['final']} | "
                  f"ĐTB: {s['gpa']} | Xếp loại: {s['grade']}")
    else:
        print(f"Không tìm thấy sinh viên nào khớp với '{keyword}'.")


def delete_student(students):
    """Xóa một sinh viên dựa trên MSSV."""
    if not students:
        print("\nDanh sách trống, không thể xóa.")
        return

    view_students(students)

    mssv_to_delete = input("\nNhập MSSV của sinh viên cần xóa (hoặc 'huy' để hủy): ").strip()

    if mssv_to_delete.lower() == 'huy':
        print("Đã hủy thao tác xóa.")
        return

    found_index = -1
    for i, s in enumerate(students):
        if s['mssv'] == mssv_to_delete:
            found_index = i
            break

    if found_index == -1:
        print(f"Không tìm thấy sinh viên có MSSV '{mssv_to_delete}'.")
    else:
        student_name = students[found_index]['name']
        confirm = input(f"Bạn có chắc muốn xóa '{student_name}' (MSSV: {mssv_to_delete})? (c/k): ").strip().lower()

        if confirm == 'c':
            removed = students.pop(found_index)
            print(f"Đã xóa sinh viên '{removed['name']}' thành công.")
        else:
            print("Đã hủy thao tác xóa.")


def show_statistics(students):
    """Thống kê tổng quan về điểm số sinh viên."""
    if not students:
        print("\nDanh sách trống, không có dữ liệu để thống kê.")
        return

    total = len(students)
    gpa_list = [s['gpa'] for s in students]
    highest = max(gpa_list)
    lowest = min(gpa_list)
    average = round(sum(gpa_list) / total, 2)

    grade_count = {}
    for s in students:
        grade = s['grade']
        grade_count[grade] = grade_count.get(grade, 0) + 1

    print(f"\n--- THỐNG KÊ ĐIỂM ---")
    print(f"Tổng số sinh viên : {total}")
    print(f"ĐTB cao nhất      : {highest:.2f}")
    print(f"ĐTB thấp nhất     : {lowest:.2f}")
    print(f"ĐTB trung bình lớp: {average:.2f}")
    print(f"\nPhân loại học lực:")

    for grade_name in ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Yếu"]:
        count = grade_count.get(grade_name, 0)
        print(f"  - {grade_name}: {count} sinh viên")


def main():
    """Hàm chính của chương trình."""
    students = initialize_students()

    print("=" * 42)
    print("  CHÀO MỪNG ĐẾN VỚI HỆ THỐNG")
    print("  QUẢN LÝ ĐIỂM SINH VIÊN")
    print("=" * 42)

    while True:
        display_menu()

        try:
            choice = input("Nhập lựa chọn của bạn (1-6): ").strip()
        except EOFError:
            choice = '6'

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            show_statistics(students)
        elif choice == '6':
            print("\nCảm ơn đã sử dụng Hệ thống Quản lý Điểm Sinh viên.")
            print("Lưu ý: Dữ liệu chỉ lưu trong bộ nhớ và sẽ mất khi thoát.")
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 6.")


if __name__ == "__main__":
    main()
