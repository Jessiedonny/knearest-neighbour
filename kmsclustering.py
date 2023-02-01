import csv
import sys
import os
import random
import math

#take command line argument
try:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <please use wine as an argument>")

k=int(arg2)
outputlines=[]

file_dir=os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
data_dir=file_dir+'/data/'

##################################
#Load wine data
##################################
data_instances=[]   
with open(data_dir+str(arg1),newline='') as data_csv:
    csvreader=csv.reader(data_csv,delimiter=' ')
    header=next(csvreader)
    for row in csvreader:
        data_instances.append(row)
    

data_rows=len(data_instances)
number_of_features=len(header)-1

########################################################
#Calculating the range of each feature, store them in r
########################################################
r=[]
for n in range(number_of_features):
    b_max=float(data_instances[0][n])
    b_min=float(data_instances[0][n])
    for i in range(data_rows):
        if b_max<float(data_instances[i][n]):
           b_max=float(data_instances[i][n])
        if b_min>float(data_instances[i][n]):
           b_min=float(data_instances[i][n])
    r.append((b_max-b_min)**2)  ###this is the range of each feature

##Pick K random instances
means=random.sample(data_instances, k)


############################################################
## Create k clusters by assigning every instance to the nearest cluster:
## based on the nearest mean according to the distance measure
############################################################
#start the loop here
centroid=means  #store the old means
print(centroid)
outputlines.append(str(centroid))
loop_counter=0
while True:
    print('Loop run no.',loop_counter)
    outputlines.append('Loop run no.'+ str(loop_counter))
    #create K clusters, store in clusters[]
    clusters=[]
    for i in range(k):
        clusters.append([]) 
    
    #calculate distances row by row
    for n in range(data_rows):  #calculate distances row by row
        distances=[]
        for m in range(k):
            d=0
            for i in range(number_of_features): #Calculate the mean of each feature
                d=d+(float(data_instances[n][i])-float(centroid[m][i]))**2/r[i]  ##caculate the distance - sum all
            distances.append(math.sqrt(d)) ##calculate the distance - square root the d caculated above
        cluster_label=distances.index(min(distances)) #find the index of the minimum distance, use it as the cluster number
        clusters[cluster_label].append(data_instances[n])  #assign the instance to the nearest cluster


    ########################################################
    #Calculating new means, store in new_means[]
    ########################################################
    new_means=[]
    for m in range(len(clusters)): 
        new_means.append([]) 
        number_of_instances=len(clusters[m])
        mean=[]
        for n in range(number_of_features):  
            sum=0 
            for i in range(number_of_instances):
                sum=sum+float(clusters[m][i][n])
            mean.append(round(sum/number_of_instances,2))        #assign new mean to a list   
        new_means[m]=mean #add the list of new mean to new_means
    
    s=0 #use s as a signal indicating when to stop the loop - time to break the loop if the old mean equals the new mean
    for i in range(len(centroid)):
        for n in range(number_of_features):
            print('new means:',new_means[i][n],'old means:',centroid[i][n])
            outputlines.append('new means:'+ str(new_means[i][n])+'old means:'+str(centroid[i][n]))
            if float(new_means[i][n])!=float(centroid[i][n]): 
                s=s+1
            
    print('New centroid:',new_means)
    outputlines.append('New centroid:'+str(new_means))
    print('Old centroid:',centroid)
    outputlines.append('Old centroid:'+str(centroid))
    
    if s>0:
        centroid=new_means #assign new means to centroid
        loop_counter+=1
        continue
    else:
        break


for n in range(len(clusters)):
    z=0
    for i in range(len(clusters[n])):
        clusters[n][i].append(n)  #add the predicted cluster at the end of each instance
        z=z+1
    print(z,' instance(s) belong to cluster ',n+1)
    outputlines.append(str(z)+' instance(s) belong to cluster '+str(n+1))
    

#output to sampleoutput.txt
with open(file_dir+'/kmeanssampleoutput.txt','w')  as f:
    f.write('\n'.join(outputlines))    




