# Task 2: Strings (15 points)
#
# The first five lines read the input for you. Do not change them.
# Then print exactly four lines. Example, if the input is:
#     "  juan "      (first name)
#     " CRUZ"        (last name)
#     " rice meal "  (item)
#     2              (quantity)
#     2024-1234      (student ID)
# the program prints:
#     Customer: Juan Cruz
#     Initials: J.C.
#     Item: Rice Meal x2
#     ID: ******234
#
# Hints: strip(), title(), upper(), indexing like name[0], slicing like text[-3:],
#        len(), "*" * 5, and f-strings.
#
# RULE: never put text inside input(). The grader types the answers for you.

first_name = input()
last_name = input()
item = input()
qty = input()
student_id = input()

clean_first = first_name.strip().title()
clean_last = last_name.strip().title()
clean_item = item.strip().title()
clean_id = student_id.strip()

customer_name = f"{clean_first} {clean_last}"
initials = f"{clean_first[0].upper()}.{clean_last[0].upper()}."
masked_id = "*" * (len(clean_id) - 3) + clean_id[-3:]

print(f"Customer: {customer_name}")
print(f"Initials: {initials}")
print(f"Item: {clean_item} x{qty.strip()}")
print(f"ID: {masked_id}")