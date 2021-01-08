import csv
a=[]
with open('Data2.csv','r') as csvfile:
        datareader=csv.reader(csvfile)
        for row in datareader:
            a.append(row)
            print(row)
num_att=len(a[0])-1
print(num_att)
print("The initial Value of specific and general hypo")
S=['0']*num_att 
G=['?']*num_att
print(S)
print(G)  
#print('The most Specific hypo S0:[0,0,0,0,0,0]\n')
#print('The most General Hypo G0:[?,?,?,?,?,?]')
#comparing the 1st hypo
#negative sample ----> only G changes,which move we should not make
#positive sample---> Both S and G can change
#comparing 1st Training examples
for j in range(0,num_att):#row=0 and all value of j
    S[j]=a[0][j];
    #print(S) 
#comparing with Reamining Training examples of the data set
#Version Space computation
temp=[]
for i in range(0,len(a)):
    if (a[i][num_att]=='P'):
        print(".................................")
        for j in range(0,num_att):
            if(a[i][j]!=S[j]):
                S[j]='?'
        #print(S)            
        #this for loop only for negative sample like to eliminate some hypo from G        
        for j in range(0,num_att):
            for k in range(1,len(temp)):
                if temp[k][j]!='?' and temp[k][j]!=S[j]:
                    del temp[k]              
        print("For Training Example S{0}".format(i+1),S)
        if len(temp)==0:
                print("For Training Example G{0}".format(i+1),G)
        else:
                print("For Training Example G{0}".format(i+1),temp)
    #as we know for neg sample we dont change S but we refer S
    #and this data sample and S should Differ 
    if a[i][num_att]=='N':
        print(".................................")
        for j in range(0,num_att):
            if S[j]!=a[i][j] and S[j]!='?':
                G[j]=S[j]
                temp.append(G)
                G=['?']* num_att              
        print("For Training Example S{0}".format(i+1),S)
        print("For Training Example G{0}".format(i+1),temp)
