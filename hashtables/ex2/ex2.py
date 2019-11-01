#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    
    start = None 
    route = []
    source = None 
    #next source === current destination
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        if tickets[i].source == "NONE":
            start = tickets[i]
            source = start.destination
            route.append(source)

    new_dest = hash_table_retrieve(hashtable, source)
    print(source)
    print(new_dest)
    # print(new_dest)
    
    while len(route) < length and source:
        next_dest = hash_table_retrieve(hashtable, source)
        print('hello')
        route.append(next_dest)
        source = next_dest
        print(route)
    
        

    return route
