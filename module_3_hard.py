def calculate_structure_sum(data_structure):
    counter = 0
    if isinstance(data_structure, (tuple,list,set)):
        for i in data_structure:
            counter += calculate_structure_sum(i)
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            counter += calculate_structure_sum(key)
            counter += calculate_structure_sum(value)
    elif isinstance(data_structure, (int,float)):
        counter += data_structure
    elif isinstance(data_structure, str):
        counter += len(data_structure)
    return counter

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))