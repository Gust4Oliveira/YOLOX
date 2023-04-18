import sys

root_path = sys.argv[1]

file = open(root_path,'r')
text = file.read() 

lines = text.splitlines()
inferTimes = []
for line in lines:
    if 'Infer time:' in line:
        inferTimes.append(line[len(line)-7:len(line)-1])

inferTimes = [float(i) for i in inferTimes]
inferTimeSum = sum(inferTimes)
averageInfer = round(inferTimeSum/len(inferTimes),4)
print('Average infer time:'+str(averageInfer))
print('Average FPS:'+str(round(1/averageInfer,4)))