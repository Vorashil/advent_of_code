import csv

with open('input_day1.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)



def convert(input_list):
	result = []
	for entry in input_list:
		result.append(int(entry[0]))
	return result

res = convert(data)
# print(res)


def find_triples(expense_report):
	for i in expense_report:
		for j in expense_report:
			for k in expense_report:
				if i+j+k == 2020:
					return (i, j, k)

def find_triples_two(expense_report):
	for i in expense_report:
		for j in expense_report:
			if (2020-i-j) in expense_report:
				return (i, j, 2020-i-j)


# triple = find_trixles(res)
triple2 = find_triples_two(res)

print(triple2)

print(triple2[0]*triple2[1]*triple2[2])