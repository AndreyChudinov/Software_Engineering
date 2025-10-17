def find_employee_entries(entries, employee_id):
    try:
        first_index = entries.index(employee_id)

        try:
            second_index = entries.index(employee_id, first_index + 1)
            return entries[first_index:second_index + 1]
        except ValueError:
            return entries[first_index:]

    except ValueError:
        return ()


print(find_employee_entries((1, 2, 3), 8))
print(find_employee_entries((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(find_employee_entries((1, 2, 8, 5, 1, 2, 9), 8))