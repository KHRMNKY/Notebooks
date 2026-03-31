import math
import pandas as pd

def load_data(path):
    dataset = pd.read_csv(path)
    return dataset



class DecisionTree:
    
    def __init__(self, path, target):
        self.path = path;
        self.data = load_data(path)
        self.target = target
        
    def calculate_entropy(self,column):
        unique_values = self.data[column].unique()
        each_unique_value_entropy = []
        for unique_category in unique_values:
            chunk = self.data[self.data[column]==unique_category][self.target]
            j = 0
            for i in chunk:
                if i == "yes":
                    j+=1
            prob = j/chunk.count()
            
            if prob == 0 or prob == 1:
                entropy = 0
                
            else :
                neg_prob = 1-prob
                entropy = -(prob*math.log2(prob))-(neg_prob*math.log2(neg_prob))
                
            
            each_unique_value_entropy.append(entropy)
        return each_unique_value_entropy, unique_values
            
                
        
    
    def calculate_before_branch_entropy(self):
        j=0
        for i in self.data[self.target]:
            if i == "yes":
                j+=1
        prob = j/self.data[self.target].count()
        
        if prob==0 or prob==1:
            entropy_before=0
        else:
            neg_prob = 1-prob
            entropy_before = -(prob*math.log2(prob))-(neg_prob*math.log2(neg_prob))
        
        return entropy_before
    
    
    
    def calculate_gain(self, column):
        entropies, unique_values = self.calculate_entropy(column=column)
        sum_entropies = []
        total_count=len(self.data[column])
        for i, value in enumerate(unique_values):
            count = len(self.data[self.data[column]==value])
            entropy = entropies[i]
            sum_entropies.append((count/total_count)*entropy)
                    
                
        gain = self.calculate_before_branch_entropy() - sum(sum_entropies)
        return gain
    
    
if __name__== "__main__":
    tree_object = DecisionTree(path="./tennis.csv",target="play")
    print(tree_object.calculate_gain("outlook"))
    
        
    
    
    
    
    
    