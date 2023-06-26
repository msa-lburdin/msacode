
def find_indexes(nums, target):
    #Create empty dictionary
    complements = {}

    #loop through the list of nums
    for index in range(0, len(nums)):

        #calculate the complement 
        complement = target - nums[index]
        #check if the complement exists in the complement dictionary 
        #if in complements dictionary return both indexes
        if complement in complements:
            return [complements[complement], index]

        #Add the current item and index to the complement dictionary 
        complements[nums[index]] = index
        #if no solution return empty list
    return []



def main():
    nums = [2, 7, 11, 15]
    target = 9 
    result = find_indexes(nums, target) 
    print(result)

main()