import csv
num_attribute = 6
print("The number of instances in data are:", num_attribute)
a=[]
with open('Data1_2.csv','r') as csvfile:
	for row in csv.reader(csvfile):
		a.append(row)
print(a)
print("\nThe initial hypothesis is")
hypothesis=['0'] * num_attribute
print(hypothesis)
for j in range(0,num_attribute):
	hypothesis[j] = a[0][j];
for i in range(0,len(a)):
	if a[i][num_attribute]=='P':
		for j in range(0,num_attribute):
			if a[i][j]!=hypothesis[j]:
				hypothesis[j]='?'
			else:
				hypothesis[j]=a[i][j]
	print("Training Example No :{0} The hypothesis is".format(i),hypothesis)
print("The maximally specific hypothesis is \n")
print(hypothesis)
