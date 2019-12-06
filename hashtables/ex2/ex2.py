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

    """
    YOUR CODE HERE
    """
    #print(hashtable)
    #print("tickets", tickets)
    print("route is", route)
    for i in tickets:
        #print("INSERTION: source is ", i.source)
        #print("INSERTION: destination is: ", i.destination)
        hash_table_insert(hashtable, i.source, i.destination)
        #print("retrieval: ", hash_table_retrieve(hashtable, i.source))
        
        if i.source is "NONE":
            print("First destination ", i.destination)
            
            route[0] = i.destination
            print("route 0 ", route[0])
    
    for i in range (length - 1):
        nextDestination = hash_table_retrieve(hashtable, route[i])
        print("Next destination is ", nextDestination)
        route[i+1] = nextDestination
        

        # if i.value == 
        #print("STORAGE hashtable key is ", i)
        #print("STORAGE hashtbale value is ", i.value)
        #route.append(i.value)
        
    print("route is ", route)
    #hash_table_insert(tickets.source, tickets.destination)
    #print(hashtable)
    # for i in hashtable:
    #     print(i)




    return route
