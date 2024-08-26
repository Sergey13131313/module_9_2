first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)
second_result = [(x1, x2) for x1 in first_strings for x2 in second_strings if len(x1) == len(x2)]
print(second_result)

third_result = {x: len(x) for x in first_strings + second_strings}
print(third_result)
