from datetime import datetime, timedelta

file = open("input.tcx", "rt")
output = open("output.tcx", "wt")

firstTime = True
deltaValue = timedelta(seconds=0)
for line in file:
    if "<Time>" in line:
        startIndex = line.find("<Time>") + len("<Time>")
        endIndex = line.find("</Time>")
        originalTimeText = line[startIndex:endIndex]
        if firstTime:
            previousTime = datetime.strptime(originalTimeText, "%Y-%m-%dT%H:%M:%S.000Z") 
            firstTime = False
        currentTime = datetime.strptime(originalTimeText, "%Y-%m-%dT%H:%M:%S.000Z") 
        currentTime = currentTime - deltaValue
        deltaTime = currentTime - previousTime
        if deltaTime > timedelta(seconds=1):
            currentTime = previousTime + timedelta(seconds=1)
            deltaValue = deltaValue + deltaTime - timedelta(seconds=1)
        line = line.replace(originalTimeText, currentTime.strftime("%Y-%m-%dT%H:%M:%S.000Z"))
        previousTime = currentTime
    output.write(line)

file.close()
output.close()