#User function Template for python3

class Solution: 
    def select(self, arr, i):
        m = i
        for j in range(i,len(arr)):
            if arr[j]< arr[m]:
                m = j
        return m
        # code here 
    
    def selectionSort(self, arr,n): 
        for i in range(n):
            idx = self.select(arr,i)
            temp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = temp
        return arr
        #code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
