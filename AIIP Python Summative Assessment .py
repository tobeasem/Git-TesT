#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem 1: Generating Sensor Data
import random as rand 
SensorData = []
SensorCluster = []
import datetime as datetime

# Generating a cluster of 32 lists with each list containg 16 random floats
i = 0
while i < 32:
    i = i + 1
    for j in range(16): 
        SensorDataNumbers = rand.random()
        SensorData.append(SensorDataNumbers)
        
    SensorCluster.append(SensorData)
    SensorData= []
    print (SensorCluster)
    
    
# Problem 2: Date and Time stamping data and storing to a file  

import random as rand 
SensorData = []
SensorCluster = []
import datetime as datetime
#create datetime object
now = datetime.datetime.now()
#convert datetime to string
now = now.strftime("%Y-%m-%d %H-%M-%S-%f")
# Generating a cluster of 32 lists with each list containg 16 random floats
i = 0
while i < 32:
    i = i + 1
    for j in range(16): 
        SensorDataNumbers = rand.random()
        SensorData.append(SensorDataNumbers)
        
    SensorCluster.append(SensorData)
    SensorData= []
    sensorDataWithTime = {now:SensorCluster}
    print (sensorDataWithTime)
#Storing and saving data generated; writing data to a file 
stringdata = str(sensorDataWithTime )
saveFile = open("SensorData.py", "w")
saveFile.write (stringdata)
saveFile.close()

# Problem 3: Create dummy data set with "err" and create function to check for this error
import random as rand 
SensorData = []

for j in range(5): 
    SensorDataNumbers = rand.random()
    SensorData.append(SensorDataNumbers)
    


SensorData[1] = "err"
    

def testForError(SensorData):
    #Check for string in dataset, 
    if SensorData.str.contains('err'):
        #Make the program repalce error with 0000
        d = {'err':0000}
        SensorData = SensorData.replace(d)
        #Creating log for the error
        logging.basicConfig(filename='errors.log',level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s',level=logging.INFO,
                            datefmt='%Y-%m-%d %H:%M:%S')
        logging.info("A String was detected")
        return SensorData

