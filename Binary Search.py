theList = [1,3,4,54,21,26,346,457,235,235,457,235,236,456,3456,345,37,4568,679,679,679,456,234,234,234,2342,35,456,457,45342,4523,23,423,645,745,532,42,4212,2,3,4,5,6,7,7,5,32,23,345,45,56,67,796,67,36,23,234,236,568,68,3452,34,1244,756,73,523,656,85,756,8]

#Lists must be sorted! While this is expensive to do its a requisit of binary search.
theList.sort()

#let's implement binary search here:
#check if tar is in nums
def binary_search(tar,nums):

  #generate walls around all index's contained in the list
  floor_index = -1
  ceiling_index = len(nums)

#while loop logic that will iterate through only if the list has elements
  while floor_index + 1 < ceiling_index:
    #calculate distance from ceiling to floor
    distance = ceiling_index - floor_index
    #calculate the midpoint in the list
    half_distance = distance / 2
    #determing the guess index aka middle index:
    guess_index = int(floor_index + half_distance)
    #translate index into an numeric value held in the list
    guess_value = nums[guess_index]

    #logic portion - did we find it?
    if guess_value == tar:
      print("Found {} at index {}".format(tar,guess_index))
      return True
    #if not found and guess is greater we move the uppoer bound to the mid point
    elif guess_value > tar:
      ceiling_index = guess_index
    #otherwise we move the lower bound to the mid point and search upper half
    else:
      floor_index = guess_index
  #worst case scenario - we didn't find the value in our list
  print("Value not found")
  return False

#Lets test it out ... We know 7 is in the list!
print("First Lookup for 7")
binary_search(7,theList)

#We know 99999 isn't in the list .....
print("Next Lookup for 99999")
binary_search(99999,theList)
