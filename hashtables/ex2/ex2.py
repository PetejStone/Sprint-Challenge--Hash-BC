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
    
    start = None  ## starting destination
    route = [] #route list to be returned
    source = None  # source of the next destination
    #next source === current destination
    for i in range(length): #for every instance of ticket
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination) #add to hash table with source as key, and destination as value
        if tickets[i].source == "NONE": # if the source is NONE, this is the first tripe
            start = tickets[i] #set this ticket to the starting point
            source = start.destination #set the source of this ticket (destination)
            route.append(source) #append the destination of the starting point to the route

   
    
    while len(route) < length and source: #while the length of route is < length and source is not none
        next_dest = hash_table_retrieve(hashtable, source) # access next dest by using source, which is the starting point for new destination
        route.append(next_dest) #append new destination
        source = next_dest #set source to next destination
    
    
        

    return route
