import csv

with open('input_day1.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

def convert(input_list):
	result = []
	for entry in input_list:
		result.append(int(entry[0]))
	return result

def find_pair(expense_report):
	for i in expense_report:
		if (2020-i) in expense_report:
			return (i, 2020-i)


res = convert(data)
# print(res)



pair = find_pair(res)

print(pair[0] * pair[1])




