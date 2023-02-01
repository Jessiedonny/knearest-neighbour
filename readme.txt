#This program is implemented in python3. There are 2 python files: knnclassifier.py and kmsclustering.py

#To run the knnclassifier, just run knnclassifier.py with 3 argument [name of training set] [name of test set] [K] K is a integer

Copy the below command line for convinience:

python3 knnclassifier.py wine-training wine-test 1
python3 knnclassifier.py wine-training wine-test 3
python3 knnclassifier.py wine-training wine-test 5

#To run the k-meansclustering, just run kmsclustering.py with 2 argument [name of the file] [k] k is an integer

python3 kmsclustering.py wine 3
python3 kmsclustering.py wine 5


------------------------------------------
What does this program do
It use the training data to build a decision tree, then take each instance to go through the tree to find the predicted label.

----------------
Note: data file must be in the 'data' folder under the same directory with dessiontree.py