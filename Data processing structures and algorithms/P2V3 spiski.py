class DisciplineNode:
    def __init__(self, code, name, lecturer, group_code, num_students, num_lecture_hours, num_practical_hours,
                 final_control_type, start_date):
        self.code = code
        self.name = name
        self.lecturer = lecturer
        self.group_code = group_code
        self.num_students = num_students
        self.num_lecture_hours = num_lecture_hours
        self.num_practical_hours = num_practical_hours
        self.final_control_type = final_control_type
        self.start_date = start_date
        self.next = None


class Curriculum:
    def __init__(self):
        self.head = None

    def add_discipline(self, code, name, lecturer, group_code, num_students, num_lecture_hours, num_practical_hours,
                       final_control_type, start_date):
        new_discipline = DisciplineNode(code, name, lecturer, group_code, num_students, num_lecture_hours,
                                        num_practical_hours, final_control_type, start_date)
        if self.head is None:
            self.head = new_discipline
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_discipline

    def search_by_lecturer(self, lecturer):
        matches = []
        current = self.head
        while current is not None:
            if current.lecturer == lecturer:
                matches.append(current)
            current = current.next
        return matches

    def sort_by_lecturer_surname(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head
        while current is not None:
            next_node = current.next
            if sorted_head is None or current.lecturer.split()[-1] < sorted_head.lecturer.split()[-1]:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next is not None and current.lecturer.split()[-1] >= temp.next.lecturer.split()[-1]:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node

        self.head = sorted_head

    def sort_by_num_hours(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head
        while current is not None:
            next_node = current.next
            if sorted_head is None or (current.num_lecture_hours + current.num_practical_hours) < \
                    (sorted_head.num_lecture_hours + sorted_head.num_practical_hours):
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next is not None and (current.num_lecture_hours + current.num_practical_hours) >= \
                        (temp.next.num_lecture_hours + temp.next.num_practical_hours):
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node

        self.head = sorted_head

    def sort_by_start_date(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head
        while current is not None:
            next_node = current.next
            if sorted_head is None or current.start_date < sorted_head.start_date:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next is not None and current.start_date >= temp.next.start_date:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node

        self.head = sorted_head

    def print_curriculum(self):
        current = self.head
        while current is not None:
            print(f"Discipline: {current.name}\n"
                  f"Code: {current.code}\n"
                  f"Lecturer: {current.lecturer}\n"
                  f"Group Code: {current.group_code}\n"
                  f"Number of Students: {current.num_students}\n"
                  f"Number of Lecture Hours: {current.num_lecture_hours}\n"
                  f"Number of Practical Hours: {current.num_practical_hours}\n"
                  f"Final Control Type: {current.final_control_type}\n"
                  f"Start Date: {current.start_date}\n")
            current = current.next


# Example usage:
curriculum = Curriculum()

# Adding disciplines
curriculum.add_discipline("001", "Mathematics", "John Smith", "G01", 30, 60, 30, "exam", "2022-09-01")
curriculum.add_discipline("002", "Physics", "Emma Johnson", "G02", 25, 45, 15, "pass", "2022-09-05")
curriculum.add_discipline("003", "Chemistry", "David Williams", "G01", 30, 50, 20, "exam", "2022-09-03")
curriculum.add_discipline("004", "Biology", "Sophia Davis", "G03", 20, 40, 10, "pass", "2022-09-07")

# Searching by lecturer
lecturer = "John Smith"
matches = curriculum.search_by_lecturer(lecturer)
print(f"Disciplines taught by {lecturer}:")
for discipline in matches:
    discipline_details = {
        "Code": discipline.code,
        "Name": discipline.name,
        "Group Code": discipline.group_code,
        "Number of Students": discipline.num_students,
        "Number of Lecture Hours": discipline.num_lecture_hours,
        "Number of Practical Hours": discipline.num_practical_hours,
        "Final Control Type": discipline.final_control_type,
        "Start Date": discipline.start_date
    }
    print(discipline_details)

# Sorting by lecturer's surname
curriculum.sort_by_lecturer_surname()
print("\nDisciplines sorted by lecturer's surname:")
curriculum.print_curriculum()

# Sorting by number of hours
curriculum.sort_by_num_hours()
print("\nDisciplines sorted by number of hours:")
curriculum.print_curriculum()

# Sorting by start date
curriculum.sort_by_start_date()
print("\nDisciplines sorted by start date:")
curriculum.print_curriculum()
