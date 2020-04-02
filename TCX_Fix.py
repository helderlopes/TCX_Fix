from datetime import datetime, timedelta

SUFFIX_SIZE = 8
LAP_SUFFIX_SIZE = 3
DATE_SIZE = 20

file = open("input.tcx", "rt")
output = open("output.tcx", "wt")

firstTime = True
deltaValue = timedelta(seconds=0)
for line in file:
    if "<Time>" in line:
        length = len(line)
        originalTimeText = line[(length-DATE_SIZE-SUFFIX_SIZE):(length-SUFFIX_SIZE)]
        if firstTime:
            previousTime = datetime.strptime(originalTimeText, "%Y-%m-%dT%H:%M:%SZ") 
            firstTime = False
        currentTime = datetime.strptime(originalTimeText, "%Y-%m-%dT%H:%M:%SZ") 
        currentTime = currentTime - deltaValue
        deltaTime = currentTime - previousTime
        if deltaTime > timedelta(seconds=1):
            currentTime = previousTime + timedelta(seconds=1)
            deltaValue = deltaValue + deltaTime
        line = line.replace(originalTimeText, currentTime.strftime("%Y-%m-%dT%H:%M:%SZ"))
        previousTime = currentTime
#    if "<Lap StartTime=" in line and deltaValue > timedelta(seconds=0) :
#        length = len(line)
#        originalTimeText = line[(length-DATE_SIZE-LAP_SUFFIX_SIZE):(length-LAP_SUFFIX_SIZE)]
#        lapTime = currentTime + timedelta(seconds=1)
#        line = line.replace(originalTimeText, lapTime.strftime("%Y-%m-%dT%H:%M:%SZ"))
    output.write(line)

file.close()
output.close()