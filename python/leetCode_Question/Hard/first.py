# Median of two sorted Arrays

class Solution(object):
    def findMedianSortedArrays(self,list1,list2):
        list3 = []
        list3 = list1.copy()
        list3.extend(list2)
        list3.sort()
        print("Merge list :",list3)
        n = len(list3)
        if n % 2 == 0:
            return (list3[n//2] + list3[(n//2)-1])/2
        else:
            return list3[(n)//2]


s = Solution()
print(s.Median([1,2],[3,4]))
        