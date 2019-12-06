#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

# weights_3 = [4, 6, 10, 15, 16]
#         answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
#         self.assertTrue(answer_3[0] == 3)
#         self.assertTrue(answer_3[1] == 1)
# 21 - 4 = 17.  No 17, stop
# 21 - 6 = 15.  Is there a 15? Yes, we're done

# 21 = limit
# 4 = weight.  In ht, 4 = key
# # 21-4 = key for ht


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    if len(weights) < 2:
        return None

    for i in range(length - 1):
        print("This is the weight: ", weights[i])
        print("where in array is the weight: ", i)
        hash_table_insert(ht, weights[i], i)

    for i in weights:
        weightBeingTested = hash_table_retrieve(ht, i)
        firstNumber = limit - weightBeingTested
        secondNumber = hash_table_retrieve(ht, firstNumber)
        if secondNumber is not None:
            answer = (firstNumber, secondNumber)
            return answer
            
        

    #     print("This is in storage: ", i.key)
        # if i.source is "NONE":
        #     route[0] = i.destination
    
    #for i in range (length - 1):
        
    #     nextDestination = hash_table_retrieve(hashtable, route[i])
    #     route[i+1] = nextDestination
    print("answer is: ", answer)
    #return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
