import csv
import sys
import os
from genericpath import exists
import math
#################
#input arguments
#################
#take command line argument
try:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <argument missing - check readme.txt>")


k=int(arg3)
file_dir=os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
data_dir=file_dir+'/data/'


outputlines=[]
##################################
#use a list to store training data
##################################
training_instances=[]   
with open(data_dir+str(arg1),newline='') as training_data_csv:
    csvreader=csv.reader(training_data_csv,delimiter=' ')
    header=next(csvreader)
    #print(header)
    for row in csvreader:
        training_instances.append(row)

training_rows=len(training_instances)
number_of_features=len(header)-1

#######################################
#read test data 
#######################################
test_instances=[]
with open (data_dir+str(arg2),newline='') as test_data_csv:
    csvreader=csv.reader(test_data_csv,delimiter=' ')
    header=[]
    header=next(csvreader)
    #print(header)
    for row in csvreader:
        test_instances.append(row)
test_rows=len(test_instances)
########################################################
#Calculating the range of each feature, store them in r
########################################################
r=[]
for n in range(number_of_features):
    b_max=float(training_instances[0][n])
    b_min=float(training_instances[0][n])
    for i in range(training_rows):
        if b_max<float(training_instances[i][n]):
           b_max=float(training_instances[i][n])
        if b_min>float(training_instances[i][n]):
           b_min=float(training_instances[i][n])
    r.append((b_max-b_min)**2)  ###this is the range of each feature




#######################################
#Caculating the distances -  main algorithm of k-Nearest Neighbour!!!!
#######################################
corrected_prediction=0
for n in range(test_rows):
    distances=[]
    for m in range(training_rows):
        d=0
        for i in range(number_of_features):
            d=d+(float(test_instances[n][i])-float(training_instances[m][i]))**2/r[i]  ##caculate the distance - sum all
        distances.append(math.sqrt(d)) ##caculate the distance - square root the d caculated above
    #get k nearest neighbours
    selected_distance=[]
    selected_row_index=[]
    predicted_class=[]
    tempdistances=distances
    #find the smallest k distances and the index of the instances
    for i in range(k): 
        min_d=min(tempdistances)
        min_d_index=tempdistances.index(min_d)
        tempdistances[min_d_index]=min_d+max(tempdistances) ##once the min has been found, add the max value to it so it won't be selected next time in the loop
        selected_distance.append(min_d)
        selected_row_index.append(min_d_index)
        predicted_class.append(training_instances[min_d_index][number_of_features]) ##get the labelled class from training dataset
    
    #Vote for the class
    voter = {i:predicted_class.count(i) for i in predicted_class} ##count each predicted class
    result=max(voter)
   
    #caculating accuracy
    
    if (test_instances[n][number_of_features]==result):
        corrected_prediction=corrected_prediction+1

    print("Test instance",n+1 ," labelled class: ", test_instances[n][number_of_features], ", predicted class: ",result)
    outputlines.append('Test instance'+str(n+1)+ ' labelled class: '+str(test_instances[n][number_of_features]) +'predicted class: ' + str(result))
    #print(test_instances[n],"predicted class: ",result)
    
print("The accuracy of the prediction is: ",round(corrected_prediction/test_rows*100,2),"%")
outputlines.append("The accuracy of the prediction is: "+str(round(corrected_prediction/test_rows*100,2))+"%")    
    
#output to sampleoutput.txt
with open(file_dir+'/knnsampleoutput.txt','w')  as f:
    f.write('\n'.join(outputlines))

