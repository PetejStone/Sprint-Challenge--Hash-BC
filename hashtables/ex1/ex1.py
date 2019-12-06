#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
     
    
    for i in range(len(weights)):
        #create a hash table of all weights
        hash_table_insert(ht, weights[i], i) #inserting weight into hashtable with it's key and value
    
    for i in range(len(weights)):
        new_value = limit - weights[i] #subtracting limit from the given weight for each weight in weights
        checker = None #checker default to None
       
        if hash_table_retrieve(ht, new_value): #if any of the weights === the difference, then these two add up to the limit
            checker = i  #set checker equal to the current weight
            new_value = hash_table_retrieve(ht, new_value) #new value is now equal to that value in the hashtable
        
            #put greater item first
            if checker > new_value: #if weight is greater
                return (checker, new_value)
            else:
                return (new_value, checker)
    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
