#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
     
    
    for i in range(len(weights)):
        # print(weights[i])
        #print(limit)
        hash_table_insert(ht, weights[i], i)
    
    for i in range(len(weights)):
        new_value = limit - weights[i]
        checker = None
        # print(new_value)
        # {
        #     4: 0,
        #     6: 1,
        #     15: 3

        # }
        # linked_pair = hash_table_retrieve(ht, 4)
        # print(f'LINKED PAIR {linked_pair}')
        if hash_table_retrieve(ht, new_value):
            checker = i
            new_value = hash_table_retrieve(ht, new_value)
            # print(checker)
            # print(hash_table_retrieve(ht, new_value))
            if checker > new_value:
                return (checker, new_value)
            else:
                return (new_value, checker)
        # print(checker)
        # print(new_value)
        
        # if checker > new_value:
        #     return (checker,new_value)
        # else:
        #     return (new_value, checker)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
