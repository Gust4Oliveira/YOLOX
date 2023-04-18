import sys, csv

root_path = sys.argv[1]

file = open(root_path,'r')
text = file.read() 

csvFile = csv.writer(open(root_path.replace('.log','.csv'),'w'))
csvFile.writerow(['class','accuracy'])

lines = text.splitlines()
for line in lines:
    if 'yolox.utils.visualize:vis:28' in line:
        csvFile.writerow((line[len(line)-15:-1]).split(':'))