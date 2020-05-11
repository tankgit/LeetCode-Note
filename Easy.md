## LeetCode Notes - Easy

---

> 🔹: Not figure out on my own
>
> 🔸: Spent lot of time on coding
>
> 👁‍🗨: May come from a interview
>
> ㊙️: Important knowledge or method need to be reviewed

---

[TOC]

---


### [1. Two Sum](https://leetcode.com/problems/two-sum/description/)
- try to use dictionary to save time, when you get a problem with two elements connected, distribute them into key and value to bind them without time consumption.
- O(n) solution:

  ```python
class Solution:
      def twoSum(self, nums, target):
          """
          :type nums: List[int]
          :type target: int
          :rtype: List[int]
          """
          dict={}
          for i in range(len(nums)):
              if nums[i] in dict:
                  return [dict[nums[i]],i]
              else:
                  dict[target-nums[i]]=i
  ```

### [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/description/)
- python3 solution:

  ```python
class Solution:
      def reverse(self, x: int) -> int:
          sign=(x>0)-(x<0)
          rev=int(str(sign*x)[::-1])
          return sign*rev*(rev<2**31)
  ```
  


### [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)
- my solution, consider all negative numbers are not palindrome.

  ```python
class Solution:
  	def isPalindrome(self, x):
  		"""
          :type x: int
          :rtype: bool
          """
          if x<0:
              return False
          return str(x)==str(x)[::-1]
  ```


### [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/description/)

- mine:

  ```python
  class Solution:
      def romanToInt(self, s: str) -> int:
          table1={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
          table2={'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}
          num=i=0
          while i<len(s):
              if s[i:i+2] in table2:
                  num+=table2[s[i:i+2]]
                  i+=2
              else:
                  num+=table1[s[i]]
                  i+=1
          return num
  ```


### [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)

- mine:

  ```python
  class Solution:
      def longestCommonPrefix(self, strs: List[str]) -> str:
          if strs==[]: return ''
          prefix=''
          for i in range(len(min(strs,key=lambda x:len(x)))):
              ch=strs[0][i]
              if not all([ch == x[i] for x in strs]):
                  break
              prefix+=ch
          return prefix
  ```


- a useful tool, just one line:

  ```python
  return os.path.commonprefix(strs)
  ```

### [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)

- mine:

  ```python
  class Solution:
      def isValid(self, s: str) -> bool:
          stack=[]
          for c in s:
              if stack and stack[-1]+c in ['()','[]','{}']: stack=stack[:-1]
              else:stack.append(c)
          return not stack
  ```

### [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)

- mine, updated:

  ```python
  class Solution:
      def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
          z=new=ListNode(0)
          while l1 and l2:
              z.next=ListNode(0)
              z=z.next
              l1,l2=(l1,l2) if l1.val<l2.val else (l2,l1)
              z.val,l1=l1.val,l1.next
          l1=l1 if l1 else l2
          z.next=l1
          return new.next
  ```

- super great solution, exchange two lists, each time get a smallest one in the lists:

  ```python
  def mergeTwoLists(self, a, b):
      if not a or b and a.val > b.val:
          a, b = b, a
      if a:
          a.next = self.mergeTwoLists(a.next, b)
      return a
  ```

### [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

- mine:

  ```python
  class Solution:
      def removeDuplicates(self, nums: List[int]) -> int:
          p=q=0
          while p<len(nums):
              if nums[p]!=nums[q]:
                  q+=1
                  nums[q]=nums[p]
              p+=1
          return q+1
  ```
  

### [27. Remove Element](https://leetcode.com/problems/remove-element/description/)

- mine:

  ```python
  class Solution:
      def removeElement(self, nums: List[int], val: int) -> int:
          p=q=0
          while p<len(nums):
              if nums[p]!=val:
                  nums[q]=nums[p]
                  q+=1
              p+=1
          return q
  ```
  
- 一个更简洁的解法，这个解法可能会变动nums里元素的顺序，但是好像官方后台解法就是这个（可以从测试输出样例看出）

  ```python
    def removeElement(self, nums, val):
      start, end = 0, len(nums) - 1
      while start <= end:
          if nums[start] == val:
              nums[start], end = nums[end], end - 1
          else:
              start +=1
      return start
  ```

### [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/description/)

- 原先我用的python的一个函数方便地解决这个问题，不过感觉不是这道题要考察的

  ```python
  class Solution(object):
      def strStr(self, haystack, needle):
          if needle=="": return 0
          l=len(haystack.split(needle)[0])
          if l==len(haystack):return -1
          else: return l
  ```

- 使用一般的指针搜索，像C语言一样naive一点的解法

  ```python
  class Solution:
      def strStr(self, haystack: str, needle: str) -> int:
          p=q=0
          while p<len(haystack) and needle:
              if haystack[p]==needle[q]: q+=1
              elif q!=0:
                  p=p-q+1
                  q=0
                  continue
              if q==len(needle): return p-q+1
              p+=1
          return -1 if needle else 0
  ```

- 稍微不那么naive一点

  ```python
  class Solution:
      def strStr(self, haystack: str, needle: str) -> int:
          p=0
          for p in range(len(haystack)-len(needle)+1):
              if haystack[p:p+len(needle)]==needle: return p
          return -1 if needle else 0
  ```

### [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)

- mine:

  ```python
  class Solution:
      def searchInsert(self, nums: List[int], target: int) -> int:
          idx=0
          while idx<len(nums):
              if nums[idx]>=target:return idx
              idx+=1
          return idx
  ```
  
- one line solution:

  ```python
  return len([x for x in nums if x<target])
  ```

### [38. Count and Say](https://leetcode.com/problems/count-and-say/description/)

- mine:

  ```python
  class Solution:
      def countAndSay(self, n: int) -> str:
          s='1'
          while n>1:
              dic=[]
              pre='#'
              for i in range(len(s)):
                  if s[i]!=pre: 
                      dic.append([s[i],1])
                      pre=s[i]
                  else: dic[-1][1]+=1
              s=''.join([str(x[1])+x[0] for x in dic])
              n-=1
          return s
  ```
  
- 借助python的库可以这样写，但这样做不好。

  ```python
  def countAndSay(self, n):
      s = '1'
      for _ in range(n - 1):
          s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
      return s
  ```


### [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)🔹

- 动态规划

  ```python
  class Solution:
      def maxSubArray(self, nums: List[int]) -> int:
          max_i=[nums[0]]
          for i in range(1,len(nums)):
              max_i.append(max(max_i[i-1]+nums[i],nums[i]))
          return max(max_i)
  ```

  

- 这个是一样的解法，不过更省空间

  ```python
  class Solution(object):
      def maxSubArray(self, nums):
          """
          :type nums: List[int]
          :rtype: int
          """
          if not nums:
              return 0
          s=m=nums[0]
          for i in nums[1:]:
              s=max(i,s+i)
              m=max(m,s)
          return m   
  ```

- *分治法，[参考官方](https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/)，值得注意的是虽然该方法时间复杂度也为$O(n)$，甚至因为递归而效率更低，但是该方法在实际应用中更加有用，它可以算出对于array的每一个子串的最大子序列和。

### [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/description/)

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])
```

### [66. Plus One](https://leetcode.com/problems/plus-one/description/)

- mine

  ```python
  class Solution(object):
      def plusOne(self, digits):
          """
          :type digits: List[int]
          :rtype: List[int]
          """
          s=''
          for i in digits:
              s+=str(i)
          p1=str(int(s)+1)
          return [int(x) for x in p1]
  ```

### [67. Add Binary](https://leetcode.com/problems/add-binary/description/)

- mine

  ```python
  class Solution(object):
      def addBinary(self, a, b):
          """
          :type a: str
          :type b: str
          :rtype: str
          """
          r=0
          c=''
          a=int(a)
          b=int(b)
          while a+b!=0:
              ia=a-int(a/10)*10
              ib=b-int(b/10)*10
              n=ia^ib^r
              r= ( (ia^ib) & r ) | (ia&ib) 
              c=str(n)+c
              a=a/10
              b=b/10
          if r==1:
              c='1'+c
          if c=='':
              c='0'
          return c
  ```

- recursive solution:

  ```python
     class Solution:
          def addBinary(self, a, b):
              if len(a)==0: return b
              if len(b)==0: return a
              if a[-1] == '1' and b[-1] == '1':
                  return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
              if a[-1] == '0' and b[-1] == '0':
                  return self.addBinary(a[0:-1],b[0:-1])+'0'
              else:
                  return self.addBinary(a[0:-1],b[0:-1])+'1'
  ```

### [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/description/)


- mine:

  ```python
  class Solution(object):
      def mySqrt(self, x):
          """
          :type x: int
          :rtype: int
          """
          l,r=0,x
          while l<=r:
              mid=(r-l)//2+l
              smid=mid**2
              if smid <= x <(mid+1)**2:
                  return mid
              elif smid>x:
                  r=mid
              else:
                  l=mid+1
  ```


### [*70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)

- mine, but TLE, use recursion:

  ```python
  class Solution(object):
      def climbStairs(self, n):
          """
          :type n: int
          :rtype: int
          """
          if n<2:
              return 1
          return self.climbStairs(n-1)+self.climbStairs(n-2)
  ```


- Equally, if use a loop that is equivalent(theoretically) with recursion, it runs faster:

  ```python
  class Solution(object):
      def climbStairs(self, n):
          a=b=1
          for _ in range(n):
              a,b= b, a+b
          return a
  ```


- Think about it, how to convert recursion to an equivalent loop.

### [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)

- mine

  ```python
  class Solution(object):
      def deleteDuplicates(self, head):
          """
          :type head: ListNode
          :rtype: ListNode
          """
          p=head
          while p and p.next:
              if p.next.val==p.val:
                  p.next=p.next.next
              else:
                  p=p.next
          return head
  ```


### [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)

- mine:

  ```python
  class Solution(object):
      def merge(self, nums1, m, nums2, n):
          """
          :type nums1: List[int]
          :type m: int
          :type nums2: List[int]
          :type n: int
          :rtype: void Do not return anything, modify nums1 in-place instead.
          """
          p=0
          for i in range(n):
              while nums2[i]>nums1[p] and p<m+i:
                  p+=1
              for j in reversed(range(p,m+i)):
                  nums1[j+1]=nums1[j]
              nums1[p]=nums2[i]
  ```
```

### [100. Same Tree](https://leetcode.com/problems/same-tree/description/)

- mine:

  ```python
  # Definition for a binary tree node.
  # class TreeNode(object):
  #     def __init__(self, x):
  #         self.val = x
  #         self.left = None
  #         self.right = None
  
  class Solution(object):
      def isSameTree(self, p, q):
          """
          :type p: TreeNode
          :type q: TreeNode
          :rtype: bool
          """
          return self.run(p)==self.run(q)
          
      def run(self,t):
          if not t:
              return [t]
          l=self.run(t.left)
          r=self.run(t.right)
          a=[]
          a.append(t.val)
          a.extend(l)
          a.extend(r)
          return a
```

- the simplest way:

  ```python
  def isSameTree(self, p, q):
      def t(n):
          return n and (n.val, t(n.left), t(n.right))
      return t(p) == t(q)
  ```

### [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/description/)

- mine, based on by [100. Same Tree](https://leetcode.com/problems/same-tree/description/) 

  ```python
  class Solution(object):
      def isSymmetric(self, root):
          """
          :type root: TreeNode
          :rtype: bool
          """
          def lrun(t):
              return t and (lrun(t.left), t.val, lrun(t.right))
          def rrun(t):
              return t and (rrun(t.right), t.val, rrun(t.left))
          return lrun(root)==rrun(root)
  ```

### [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

- mine

  ```python
  class Solution(object):
      def maxDepth(self, root):
          """
          :type root: TreeNode
          :rtype: int
          """
          def run(d,t):
              if not t:
                  return d
              return max(run(d+1,t.left),run(d+1,t.right))
          return run(0,root)
  ```

### [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/)

- mine:

  ```python
  class Solution(object):
      def levelOrderBottom(self, root):
          """
          :type root: TreeNode
          :rtype: List[List[int]]
          """
          a={}
          def run(a,d,t):
              if not t:
                  return
              run(a,d+1,t.left)
              run(a,d+1,t.right)
              if d not in a:
                  a[d]=[]
              a[d].append(t.val)
          run(a,0,root)
          return [a[x] for x in sorted(a,reverse=True)]
  ```

### [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)

- mine:

  ```python
  class Solution(object):
      def sortedArrayToBST(self, nums):
          """
          :type nums: List[int]
          :rtype: TreeNode
          """
          def build(n,l,r):
              if l==r:
                  return None
              mid=(r-l)//2+l
              root=TreeNode(n[mid])
              root.left=build(n,l,mid)
              root.right=build(n,mid+1,r)
              return root
          
          return build(nums,0,len(nums))
  ```

### [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)

- mine:

  ```python
  class Solution(object):
      def isBalanced(self, root):
          """
          :type root: TreeNode
          :rtype: bool
          """
          def deep(d,root):
              if not root:
                  return True,d
              l,ld=deep(d+1,root.left)
              r,rd=deep(d+1,root.right)
              return l and r and abs(ld-rd)<2,max(ld,rd)
          j,d=deep(0,root)
          return j
  ```

- Optimized with `min(...) or max(...)`:

  ```python
  class Solution(object):
    def minDepth(self, root):
        """
                :type root: TreeNode
                :rtype: int
                """
        if not root:
            return 0
        def deep(d,root):
            if not root:
                return None
            if not root.left and not root.right:
                return d
            ds=[deep(d+1,root.left),deep(d+1,root.right)]
            return min(ds) or max(ds)
        return deep(1,root)
  ```


### [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)

- mine:

  ```python
  class Solution(object):
      def minDepth(self, root):
          """
          :type root: TreeNode
          :rtype: int
          """
          def deep(d,root):
              if not root:
                  return d-1
              ld=deep(d+1,root.left)
              rd=deep(d+1,root.right)
              if not root.left:
                  return rd
              elif not root.right:
                  return ld
              else:
                  return min(ld,rd)
          return deep(1,root)
  ```


- brilliant:

  ```python
  def minDepth(self, root):
      if not root: return 0
      d = map(self.minDepth, (root.left, root.right))
      return 1 + (min(d) or max(d))
  
  def minDepth(self, root):
      if not root: return 0
      d, D = sorted(map(self.minDepth, (root.left, root.right)))
      return 1 + (d or D)
  ```


### [112. Path Sum](https://leetcode.com/problems/path-sum/description/)

- mine, pursuit of speed, sacrificed simplicity:

  ```python
  class Solution(object):
      def hasPathSum(self, root, sum):
          """
          :type root: TreeNode
          :type sum: int
          :rtype: bool
          """
          def deep(sum,root,goal):
              sv=sum+root.val
              if not root.left and not root.right:
                  return sv == goal
              jl=jr=False
              if root.left:
                  jl=deep(sv,root.left,goal)
                  if jl:
                      return True
              if root.right:
                  jr=deep(sv,root.right,goal)
                  if jr:
                      return True
              return False
          if not root:
              return False
          return deep(0,root,sum)
  ```


### [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)

- mine:

  ```python
  class Solution(object):
      def generate(self, numRows):
          """
          :type numRows: int
          :rtype: List[List[int]]
          """
          if numRows==0:
              return []
          p=[[1]]
          for i in range(1,numRows):
              k=[]
              for j in range(i+1):
                  if j==0 or j==i:
                      k.append(1)
                  else:
                      k.append(p[i-1][j-1]+p[i-1][j])
              p.append(k)
          return p
  ```


- my simple but slower:

  ```python
  class Solution(object):
      def generate(self, numRows):
          if numRows==0:
              return []
          p=[[1]]
          for i in range(1,numRows):
              k=[0]+p[i-1]+[0]
              p.append([k[x-1]+k[x] for x in range(1,i+2)])
          return p
  ```


- great solution using map:

  ```python
  def generate(self, numRows):
          res = [[1]]
          for i in range(1, numRows):
              res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
          return res[:numRows]
	```

  ```python
      1 3 3 1 0 
   +  0 1 3 3 1
   =  1 4 6 4 1
  ```

### [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/description/)

- my thought is using Combination Equation, but it's far more slow and inelegant

- a simple solution:

  ```python
  class Solution(object):
      def getRow(self, rowIndex):
          """
          :type rowIndex: int
          :rtype: List[int]
          """
          row=[1]
          for i in range(rowIndex):
              row=[x+y for x,y in zip([0]+row,row+[0])]
          return row
  ```

### [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

- mine:

  ```python
  class Solution(object):
      def maxProfit(self, prices):
          """
          :type prices: List[int]
          :rtype: int
          """
          m=0
          buy=0
          for i in range(len(prices)):
              if prices[i]<prices[buy]:
                  buy=i
              elif prices[i]-prices[buy]>m:
                  m=prices[i]-prices[buy]
          return m
  ```

- another equivalent (but slower?) solution:

  ```python
  def maxProfit(prices):
      max_profit, min_price = 0, float('inf')
      for price in prices:
          min_price = min(min_price, price)
          profit = price - min_price
          max_profit = max(max_profit, profit)
      return max_profit
  ```

- the most elegant so far and different solution(In Java):

  ```java
  public int maxProfit(int[] prices) {
      int maxCur = 0, maxSoFar = 0;
      for(int i = 1; i < prices.length; i++) {
          maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);
          maxSoFar = Math.max(maxCur, maxSoFar);
      }
      return maxSoFar;
  }
  ```

### [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)

- my one line solution:

  ```python
  class Solution(object):
      def maxProfit(self, prices):
          """
          :type prices: List[int]
          :rtype: int
          """
          return sum([max(0,prices[i]-prices[i-1]) for i in range(1,len(prices))])
  ```

### [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

- my stupid solution:

  ```python
  class Solution(object):
      def isPalindrome(self, s):
          """
          :type s: str
          :rtype: bool
          """
          i=j=0
          l=len(s)
          while i<l and j<l:
              while i<l and not s[i].isalnum():
                  i+=1
              while j<l and not s[-(j+1)].isalnum():
                  j+=1
              if i<l and j<l and s[i].lower()!=s[-(j+1)].lower():
                  return False
              else:
                  i+=1
                  j+=1
          while i<l:
              if s[i].isalnum():
                  return False
              i+=1
          while j<l:
              if s[-(j+1)].isalnum():
                  return False
              j+=1
          return True
  ```

- remove invalid characters first:

  ```python
  class Solution:
      def isPalindrome(self, s):
          s = ''.join(e for e in s if e.isalnum()).lower()
          return s==s[::-1]
  ```

### [136. Single Number](https://leetcode.com/problems/single-number/description/)

- the classic one line solution:

  ```python
  class Solution(object):
      def singleNumber(self, nums):
          """
          :type nums: List[int]
          :rtype: int
          """
          return reduce(lambda x,y:x^y,nums)
  ```

  - `lambda x,y: x^y` can be replaced by:

    ```python
    import operator
    func = operator.xor
    ```

### [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/#/description)

- Wiki reference: [Cycle detection](https://en.wikipedia.org/wiki/Cycle_detection)

- Using **a fast point and a slow point** to detect cycle in a list.

  - if no cycle, it'll finally end up with `None` node.
  - if has cycle, fast point will eventually catch up with slow point.

    ```python
    class Solution(object):
        def hasCycle(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            if not head:
                return False
            slow=head
            fast=head.next
            while slow is not fast:
                if not fast or not fast.next:
                    return False
                else:
                    slow=slow.next
                    fast=fast.next.next
            return True
    ```

- python tips: `try - exception` usage.
    ```python
    class Solution(object):
        def hasCycle(self, head):
            """
            :type head: ListNode
            :rtype: bool
            """
            if not head:
                return False
            s=head
            f=s.next
            try:
                while s is not f:
                    s=s.next
                    f=f.next.next
                return True
            except:
                return False
    ```

### [155. Min Stack](https://leetcode.com/problems/min-stack/#/description)

- my first time solution, it can be simpler but this one is faster on `getMin()`:

  ```python
  import sys
  
  class MinStack(object):
  
      def __init__(self):
          """
          initialize your data structure here.
          """
          self.stack=[]
          self.minn=[]
          
          
  
      def push(self, x):
          """
          :type x: int
          :rtype: void
          """
          self.stack.append(x)
          if self.minn==[] or x<self.minn[-1][0]:
              self.minn.append([x,len(self.stack)])
          
  
      def pop(self):
          """
          :rtype: void
          """
          if len(self.stack)==self.minn[-1][1]:
              self.minn.pop()
          x=self.stack.pop()
          
          
  
      def top(self):
          """
          :rtype: int
          """
          if len(self.stack)==0:
              return None  
          else:
              return self.stack[-1]
  
      def getMin(self):
          """
          :rtype: int
          """
          return self.minn[-1][0]
  ```


### [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/#/description)
- Finding a common in two different situations can be considered to exchange each other's status.
- my solution:
- ```python
  class Solution(object):
      def getIntersectionNode(self, headA, headB):
          """
          :type head1, head1: ListNode
          :rtype: ListNode
          """
          p=headA
          q=headB
          k=0
          while p and q and p is not q:
              p=p.next
              q=q.next
              if not p:
                  p=headB
                  k+=1
              if not q:
                  q=headA
                  k+=1
              if k>2:
                  break
          return p if p is q else None
  ```

  refined solution, more concise:

  ```python
  class Solution(object):
      def getIntersectionNode(self, headA, headB):
          if not headA or not headB:
              return None
          p=headA
          q=headB
          while p is not q:
              p=p.next if p else headB
              q=q.next if q else headA
          return p
  ```

### [167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description)

- mine, stupid, very first try:

  ```python
  class Solution(object):
      def twoSum(self, numbers, target):
          """
          :type numbers: List[int]
          :type target: int
          :rtype: List[int]
          """
          def biSearch(val,left,right):
              if right-left==0:
                  if numbers[left]==val:
                      return left
                  else:
                      return None
              mid=left+(right-left)/2
              if numbers[mid]>val:
                  return biSearch(val,left,mid)
              elif numbers[mid]<val:
                  return biSearch(val,mid+1,right)
              else:
                  return mid
                  
          if len(numbers)<2:
              return None
          i=0
          midval=target/2.0
          while numbers[i]<midval and i<len(numbers):
              i+=1
          for j in range(0,i+1):    
              k=biSearch(target-numbers[j],j+1,len(numbers)-1)
              if k!=None:
                  return [j+1,k+1]
          return None
  ```

- a simple `O(n)` solution:

  ```python
  def twoSum(self, numbers, target):
      i,j=0,len(numbers)-1
      while i<j:
          s=numbers[i]+numbers[j]
          if s==target:
              return i+1,j+1
          if s<target:
              i+=1
              else:
                  j-=1
  ```

- a smart solution using dictionary:

  ```python
  def twoSum2(self, numbers, target):
      dic = {}
      for i, num in enumerate(numbers):
          if target-num in dic:
              return [dic[target-num]+1, i+1]
          dic[num] = i
  ```

### [168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/#/description)

- It seems that you can treat it as a 26-system but not exactly in details.

  ```python
  class Solution(object):
      def convertToTitle(self, n):
          """
          :type n: int
          :rtype: str
          """
          r=''
          while n>0:
              m,n=(n-1)%26,(n-1)//26
              r=chr(65+m)+r
          return r
  ```

### [169. Majority Element](https://leetcode.com/problems/majority-element/#/description)
- Sometimes, if you have no better algorithms, perhaps you can run a sort algorithm in advance

  ```python
  class Solution(object):
      def majorityElement(self, nums):
          """
          :type nums: List[int]
          :rtype: int
          """
          return sorted(nums)[len(nums)/2]
  ```
### [171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/#/description)

- mine:

  ```python
  class Solution(object):
      def titleToNumber(self, s):
          """
          :type s: str
          :rtype: int
          """
          return reduce(lambda i,j: i*26+ord(j)-64, [0]+[x for x in s])
  ```


### [172. Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/#/description)
- my solution:

  ```python
  class Solution(object):
      def trailingZeroes(self, n):
          """
          :type n: int
          :rtype: int
          """
          s=0
          k=5
          while n//k!=0:
              s+=n//k
              k*=5
          return s
  ```
- equivalent, but a little bit different:

  ```python
  class Solution(object):
      def trailingZeroes(self, n):
          """
          :type n: int
          :rtype: int
          """
          r=0
          while n>0:
              n/=5
              r+=n
          return r
  ```
### [189. Rotate Array](https://leetcode.com/problems/rotate-array/#/description)

- my latest solution:

  ```python
  class Solution(object):
      def rotate(self, nums, k):
          """
          :type nums: List[int]
          :type k: int
          :rtype: void Do not return anything, modify nums in-place instead.
          """
          r=k if len(nums)>k else k-len(nums)
          for i in range(len(nums)-r):
              nums.append(nums[0])
              nums.pop(0)
  ```


- Solution 1: regular solution with `O(n)` space complexity and `O(n)` time complexity

  ```python
  class Solution(object):
      def rotate(self, nums, k):
          n=len(nums)
          k%=n
          a=[]
          for i in range(0,k):
              a.append(nums[i])
              nums[i]=nums[-k+i]
          for i in range(k,n):
              a.append(nums[i])
              nums[i]=a[i-k]
  ```

- Solution 2: reverse function with `O(1)` space complexity and `O(n)` time complexity

  ```python
  public void rotate(int[] nums, int k) {
      if(nums == null || nums.length < 2){
          return;
      }
      k = k % nums.length;
      reverse(nums, 0, nums.length - k - 1);
      reverse(nums, nums.length - k, nums.length - 1);
      reverse(nums, 0, nums.length - 1);
  }
  
  private void reverse(int[] nums, int i, int j){
      int tmp = 0;       
      while(i < j){
          tmp = nums[i];
          nums[i] = nums[j];
          nums[j] = tmp;
          i++;
          j--;
      }
  }
  ```

- Solution 3: 

  ```python
  def rotate(self, nums, k):
      n = len(nums)
      k = k % n
      nums[:] = nums[n-k:] + nums[:n-k]
  ```

### [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/#/description)
- mine:
```python
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r=0
        for i in range(0,32):
            r+=(n&1)*(2**(31-i))
            n>>=1
        return r
```
- In python, we can transform binary and  string like:

  ```python
  >>> '{0:04b}'.format(3)
  0011
  >>> int('0011',2)
  3
  ```

  - `b` stand for binary, `o` stand for octonary,  `d` stand for decimal, `x` stand for hexadecimal
  - `int(string,n)`, `n` stand for different number systems.

- in this case, here is a simple solution:

  ```python
  class Solution:
      def reverseBits(self, n):
          b='{0:032b}'.format(n)
          return int(b[::-1],2)
  ```

### [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/#/description)

- my one line solution:

  ```python
  class Solution(object):
      def hammingWeight(self, n):
          """
          :type n: int
          :rtype: int
          """
          return sum([ord(x)-48 for x in '{0:032b}'.format(n)])
  ```

- legacy:

  ```python
  class Solution(object):
      def hammingWeight(self, n):
          """
          :type n: int
          :rtype: int
          """
          r=0
          for _ in range(0,32):
              r+=n&1
              n>>=1
          return r
  ```

- A brilliant `C` solution:  for any integer `n`, each time we do `n&(n-1)`, the answer is eliminated a `1` digit compared with the original `n`.
```cpp
int hammingWeight(uint32_t n) {
    int count = n ? 1 : 0;
    while(n &= (n-1)) count++;
    return count;
}
```

- With the python build-in function:
```python
return bin(n).count('1')
```

### [*198. House Robber](https://leetcode.com/problems/house-robber/#/description)
- the recursion way: 
  - case 1: choose $i^{th}$ house and $1^{th}$$ to $ $(i-2)^{th}$ houses' best plan
  - case 2: do not choose $i^{th}$ house, only choose  $1^{th}$$ to $ $(i-1)^{th}$ houses' best plan
- attention with the python expression:

  ```python
  class Solution(object):
      def rob(self, nums):
          """
          :type nums: List[int]
          :rtype: int
          """
          f1=f2=0
          for i in nums:
              f1,f2=f2,max(f1+i,f2)
          return f2
  ```

### [202. Happy Number](https://leetcode.com/problems/happy-number/#/description)

- mine:

  ```python
  class Solution(object):
      def isHappy(self, n):
          """
          :type n: int
          :rtype: bool
          """
          s=[]
          while n!=1:
              n=sum([int(i)**2 for i in str(n)])
              if n in s:
                  return False
              else:
                  s.append(n)
          return True
  ```

- Consider that the crux of the problem is to figure out whether it has a loop, we can use a use similar way in [141. Linked List Cycle](#141-linked-list-cycle), it will be a O(1) space solution.

### [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/#/description)

- remember the formation of this sort of problem.

- define a previous pointer.

  ```python
  # Definition for singly-linked list.
  # class ListNode(object):
  #     def __init__(self, x):
  #         self.val = x
  #         self.next = None
  
  class Solution(object):
      def removeElements(self, head, val):
          """
          :type head: ListNode
          :type val: int
          :rtype: ListNode
          """
          s=p=ListNode(0)
          s.next=head
          while p and p.next:
              if p.next.val==val:
                  p.next=p.next.next
              else:
                  p=p.next
          return s.next
  ```
### [*204. Count Primes](https://leetcode.com/problems/count-primes/#/description)
- The ordinary solution, but **time limit exceeded**:

  ```python
  class Solution(object):
      def countPrimes(self, n):
          """
          :type n: int
          :rtype: int
          """
          def isPrime(n):
              k=int(math.sqrt(n))+1
              for i in range(2,k):
                  if n%i==0:
                      return False
              return True
              
          s=0
          for i in range(2,n):
              if isPrime(i):
                  s+=1
          return s
  ```
- determine a part of prime numbers(actually just `2` is enough) and multiply them and mark them as composite number.

  ```python
  class Solution(object):
      def countPrimes(self, n):
          """
          :type n: int
          :rtype: int
          """
          if n<=2:
              return 0
          k=[True]*n
          k[0]=k[1]=False
          for i in range(2,(n-1)/2+1):
              if k[i]:
                  for j in range(i,(n-1)//i+1):
                      k[i*j]=False
          return sum(k)
  ```
### [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/#/description)

- too slow but passed:

  ```python
  class Solution(object):
      def isIsomorphic(self, s, t):
          """
          :type s: str
          :type t: str
          :rtype: bool
          """
          d=[]
          for i,j in zip(s,t):
              if (i,j) not in d:
                  if i not in [x[0] for x in d] and j not in [x[1] for x in d]:
                      d.append((i,j))
                  else:
                      return False
          return True
  ```
- more different solutions: [Python different solutions (dictionary, etc).](https://discuss.leetcode.com/topic/19993/python-different-solutions-dictionary-etc), for example:

  ```python
  def isIsomorphic(self, s, t):
      return len(set(zip(s, t))) == len(set(s)) == len(set(t))
  ```


### [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/#/description)

- normal:

  ```python
  # Definition for singly-linked list.
  # class ListNode(object):
  #     def __init__(self, x):
  #         self.val = x
  #         self.next = None
  
  class Solution(object):
      def reverseList(self, head):
          """
          :type head: ListNode
          :rtype: ListNode
          """
          k=head
          p=None
          while k:
              k.next,p=p,k.next
              k,p=p,k
          return p
  ```


### [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/#/description)
- use the property of set in python:
```python
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums)!=len(set(nums))
```

### [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/#/description)
- TLE:
```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in xrange(1,k+1):
            for j in xrange(len(nums)-i):
                tem=nums[j:j+i+1]
                if len(tem)!=len(set(tem)):
                    return True
        return False
```
-use dictionary:
```python
def containsNearbyDuplicate(self, nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False
```

### [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/#/description)

- mine:

  ```python
  class MyStack(object):
  
      def __init__(self):
          """
          Initialize your data structure here.
          """
          self.stack=[]
          self.t=None
          
  
      def push(self, x):
          """
          Push element x onto stack.
          :type x: int
          :rtype: void
          """
          self.stack.append(x)
          self.t=x
          
  
      def pop(self):
          """
          Removes the element on top of the stack and returns that element.
          :rtype: int
          """
          for i in range(len(self.stack)-1):
              self.push(self.stack[0])
              self.stack=self.stack[1:]
          t=self.stack[0]
          self.stack=self.stack[1:]
          return t
          
          
  
      def top(self):
          """
          Get the top element.
          :rtype: int
          """
          print 'Top', self.t
          return self.t
          
  
      def empty(self):
          """
          Returns whether the stack is empty.
          :rtype: bool
          """
          print 'Empty',len(self.stack)==0
          return len(self.stack)==0
  ```

### [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/#/description)

- mine:

  ```python
  # Definition for a binary tree node.
  # class TreeNode(object):
  #     def __init__(self, x):
  #         self.val = x
  #         self.left = None
  #         self.right = None
  
  class Solution(object):
      def invertTree(self, root):
          """
          :type root: TreeNode
          :rtype: TreeNode
          """
          if not root:
              return None
          root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
          return root
  ```

### [231. Power of Two](https://leetcode.com/problems/power-of-two/#/description)
- ordinary:

  ```python
  class Solution(object):
      def isPowerOfTwo(self, n):
          """
          :type n: int
          :rtype: bool
          """
          if n==1:
              return True
          elif n<2:
              return False
          while n>=2:
              r,n=n%2,n/2
              if r==1:
                  return False
          return True
  ```

- count amount of `1` in binary format:

  ```python
  def isPowerOfTwo(self, n):
      return bin(n).count('1')==1 and n>0
  ```

- actually, it can be simpler and faster:

  ```python
  def isPowerOfTwo(self, n):
      return n>0 and not (n & (n-1))
  ```
### [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/#/description)

- mine:

  ```python
  class MyQueue(object):
  
      def __init__(self):
          """
          Initialize your data structure here.
          """
          self.q=[]
          self.f=None
          
  
      def push(self, x):
          """
          Push element x to the back of queue.
          :type x: int
          :rtype: void
          """
          if not self.q:
              self.f=x
          self.q.append(x)
          
          
  
      def pop(self):
          """
          Removes the element from in front of queue and returns that element.
          :rtype: int
          """
          cache=[]
          for i in range(len(self.q)):
              cache.append(self.q.pop(-1))
          r=cache.pop(-1)
          for i in range(len(cache)):
              self.push(cache.pop(-1))
          return r
          
  
      def peek(self):
          """
          Get the front element.
          :rtype: int
          """
          return self.f
          
  
      def empty(self):
          """
          Returns whether the queue is empty.
          :rtype: bool
          """
          return len(self.q)==0
  ```

### [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/#/description)
- it can't be solved via $XOR$ operation, for example:`[1,3,0,2]`,$1\bigoplus 3\bigoplus 0\bigoplus 2=0$, but it's apparently not a palindrome.

- my solution, using `O(n)`space:

  ```python
  # Definition for singly-linked list.
  # class ListNode(object):
  #     def __init__(self, x):
  #         self.val = x
  #         self.next = None
  
  class Solution(object):
      def isPalindrome(self, head):
          """
          :type head: ListNode
          :rtype: bool
          """
          s=[]
          while head:
              s.append(head.val)
              head=head.next
          return s==s[::-1]
  ```

- inspire: find a mid-element by slow-fast pointers. `O(1)`space

  ```python
  class Solution(object):
      def isPalindrome(self, head):
          p=q=head
          while p and p.next:
              p=p.next.next
              q=q.next
          tail=None
          while q:
              tem=q.next
              q.next=tail
              tail=q
              q=tem
          while tail:
              if head.val!=tail.val:
                  return False
              head=head.next
              tail=tail.next
          return True
  ```
### [*235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

- smart recursion solution:

  ```python
  # Definition for a binary tree node.
  # class TreeNode(object):
  #     def __init__(self, x):
  #         self.val = x
  #         self.left = None
  #         self.right = None
  
  class Solution(object):
      def lowestCommonAncestor(self, root, p, q):
          """
          :type root: TreeNode
          :type p: TreeNode
          :type q: TreeNode
          :rtype: TreeNode
          """
          next= p.val<root.val>q.val and root.left or\
                p.val>root.val<q.val and root.right
          return self.lowestCommonAncestor(next,p,q) if next else root
  ```

- smart iterative solution, `O(1)` space:

  ```python
  def lowestCommonAncestor(self, root, p, q):
      while (root.val - p.val) * (root.val - q.val) > 0:
          root = (root.left, root.right)[p.val > root.val]
      return root
  ```

### [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/description/)

- simple solution:

  ```python
  # Definition for singly-linked list.
  # class ListNode(object):
  #     def __init__(self, x):
  #         self.val = x
  #         self.next = None
  
  class Solution(object):
      def deleteNode(self, node):
          """
          :type node: ListNode
          :rtype: void Do not return anything, modify node in-place instead.
          """
          node.val,node.next=node.next.val,node.next.next
  ```

### [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

- mine:

  ```python
  class Solution(object):
      def isAnagram(self, s, t):
          """
          :type s: str
          :type t: str
          :rtype: bool
          """
          if len(s)!=len(t):
              return False
          d={}
          for i,j in zip(s,t):
              d[i]=d[i]+1 if i in d else 1
              d[j]=d[j]-1 if j in d else -1
          return all(x==0 for x in d.values())
  ```

### [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/description/)

- mine:

  ```python
  # Definition for a binary tree node.
  # class TreeNode(object):
  #     def __init__(self, x):
  #         self.val = x
  #         self.left = None
  #         self.right = None
  
  class Solution(object):
      def binaryTreePaths(self, root):
          """
          :type root: TreeNode
          :rtype: List[str]
          """
          if not root:
              return []
          def run(root,path,a):
              if not root.left and not root.right:
                  a.append(path+str(root.val))
                  return
              if root.left:
                  run(root.left,path+str(root.val)+'->',a)
              if root.right:
                  run(root.right,path+str(root.val)+'->',a)
          a=[]
          run(root,'',a)
          return a
  ```

### [258. Add Digits](https://leetcode.com/problems/add-digits/discuss/)

- mine:

  ```python
  class Solution(object):
      def addDigits(self, num):
          """
          :type num: int
          :rtype: int
          """
          while num>9:
              num=sum([int(x) for x in str(num)])
          return num
  ```

- mathematically proved solution:
  $$
  N=a_1\times10^0+a_2\times10^1+a_3\times10^2+\dots+a_n\times10^n\ where\ a_i\in[0,9]
  \\
  \because 10^i\mod9=1
  \\
  \therefore N\mod9=\sum^n_{i=1}a_i\mod9
  $$

  ```python
  def addDigits(self, num):
      if num == 0 : return 0
      else:return (num - 1) % 9 + 1
  ```

### [263. Ugly Number](https://leetcode.com/problems/ugly-number/description/)

- mine:

  ```python
  class Solution(object):
      def isUgly(self, num):
          """
          :type num: int
          :rtype: bool
          """
          if num==0:
              return False
          while num not in [1,2,3,5]:
              if num%2==0:
                  num/=2
              elif num%3==0:
                  num/=3
              elif num%5==0:
                  num/=5
              else:
                  return False
          return True
  ```

### [268. Missing Number](https://leetcode.com/problems/missing-number/description/)

- mine, both time and space complexity are `O(1)`

  ```python
  class Solution(object):
      def missingNumber(self, nums):
          """
          :type nums: List[int]
          :rtype: int
          """
          l=len(nums)
          s=sum(nums)
          return l*(l+1)/2 -s
  ```

### [278. First Bad Version](https://leetcode.com/problems/first-bad-version/description/)

- mine:

  ```python
  # The isBadVersion API is already defined for you.
  # @param version, an integer
  # @return a bool
  # def isBadVersion(version):
  
  class Solution(object):
      def firstBadVersion(self, n):
          """
          :type n: int
          :rtype: int
          """
          def biSearch(l,r):
              if isBadVersion(l):
                  return l
              if l-r==2:
                  return r
              mid=(r-l)//2+l
              if isBadVersion(mid):
                  return biSearch(l,mid)
              else:
                  return biSearch(mid+1,r)
          return biSearch(1,n)
  ```

- python tool `bisect(func, val, left, right)` is convenient:

  - `func`: function which you need to test each element
  - `val`: the specific goal of what result you want from the function

  ```python
  def firstBadVersion(self, n):
      class Wrap:
          def __getitem__(self, i):
              return isBadVersion(i)
      return bisect.bisect(Wrap(), False, 0, n)
  ```

### [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/description/)

- mine

  ```python
  class Solution(object):
      def moveZeroes(self, nums):
          """
          :type nums: List[int]
          :rtype: void Do not return anything, modify nums in-place instead.
          """
          i=j=0
          l=len(nums)
          while i+1+j<l:
              if nums[i]==0:
                  nums.append(0)
                  nums.pop(i)
                  j+=1
              else:
                  i+=1
  ```

### [290. Word Pattern](https://leetcode.com/problems/word-pattern/description/)

- similar to [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/#/description)

- mine

  ```python
  class Solution(object):
      def wordPattern(self, pattern, str):
          """
          :type pattern: str
          :type str: str
          :rtype: bool
          """
          d={}
          word=str.split(' ')
          if len(word)!=len(pattern):
              return False
          for i,j in zip(pattern,word):
              if i not in d:
                  if j in d.values():
                      return False
                  d[i]=j
              elif d[i]!=j:
                  return False
          return True
  ```

### [292. Nim Game](https://leetcode.com/problems/nim-game/description/)

- mine:

  ```python
  class Solution(object):
      def canWinNim(self, n):
          """
          :type n: int
          :rtype: bool
          """
          return n%4!=0
  ```

### [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/description/)

- mine, 'cause it will be called for many times, so store it first:

  ```python
  class NumArray(object):
  
      def __init__(self, nums):
          """
          :type nums: List[int]
          """
          self.nums=nums
          self.d={}
          
  
      def sumRange(self, i, j):
          """
          :type i: int
          :type j: int
          :rtype: int
          """
          if (i,j) not in self.d:
              self.d[(i,j)]=sum(self.nums[i:j+1])
          return self.d[(i,j)]
  ```

- another smart solution, which stored  the accumulate sum for each position:

  ```python
  class NumArray(object):
      def __init__(self, nums):
          self.accu = [0]
          for num in nums: 
              self.accu += self.accu[-1] + num,
  
      def sumRange(self, i, j):
          return self.accu[j + 1] - self.accu[i]
  ```

### [326. Power of Three](https://leetcode.com/problems/power-of-three/description/)

- many tricky solutions, one of it:

  ```python
  class Solution(object):
      def isPowerOfThree(self, n):
          return n > 0 and 1162261467 % n == 0
  ```

### [342. Power of Four](https://leetcode.com/problems/power-of-four/description/)

- mine:

  ```python
  class Solution(object):
      def isPowerOfFour(self, num):
          """
          :type num: int
          :rtype: bool
          """
          zero=len(bin(num))-3
          return num>0 and zero%2==0 and num&(num-1)==0
  ```

### [344. Reverse String](https://leetcode.com/problems/reverse-string/description/)

- python one line:

  ```python
  class Solution(object):
      def reverseString(self, s):
          """
          :type s: str
          :rtype: str
          """
          return s[::-1]
  ```

- general solution with recursion:

  ```python
  class Solution(object):
      def reverseString(self, s):
          l = len(s)
          if l < 2:
              return s
          return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])
  ```

### [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/description/)

- mine:

  ```python
  class Solution(object):
      def reverseVowels(self, s):
          """
          :type s: str
          :rtype: str
          """
          i=0
          j=len(s)-1
          v=['a','e','i','o','u','A','E','I','O','U']
          s=list(s)
          while i<j:
              while s[i] not in v and i<j:
                  i+=1
              while s[j] not in v and i<j:
                  j-=1
              s[i],s[j]=s[j],s[i]
              i+=1
              j-=1
          return ''.join(s)
  ```

### [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/description/)

- mine:

  ```python
  class Solution(object):
      def intersection(self, nums1, nums2):
          """
          :type nums1: List[int]
          :type nums2: List[int]
          :rtype: List[int]
          """
          return [ x for x in set(nums2) if x in set(nums1) ]
  ```

- using `set` in python, `set` has operations of set in math:

  - `set(a) & set(b)`: $A\cap B$
  - `set(a) | set(b)`: $A\cup B$

  ```python
  class Solution(object):
      def intersection(self, nums1, nums2):
          return list(set(nums1) & set(nums2))
  ```

### [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/description/)

- mine:

  ```python
  class Solution(object):
      def intersect(self, nums1, nums2):
          """
          :type nums1: List[int]
          :type nums2: List[int]
          :rtype: List[int]
          """
          return [ nums1.remove(x)==None and x for x in nums2 if x in nums1 ]
  ```

- use `collections.Counter()`:

  ```python
  def intersect(self, nums1, nums2):
      C = collections.Counter
      return list((C(nums1) & C(nums2)).elements())
  ```

### [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/description/)

- using [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method)

  ```python
  class Solution(object):
      def isPerfectSquare(self, num):
          """
          :type num: int
          :rtype: bool
          """
          n=num
          while n*n > num:
              n=(n+num/n)/2
          return n*n == num
  ```

### [*371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/description/)

- This problem is far more difficult than other problems under easy category.

- here is a solution using and only using bit operation:(from [this discussion](https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22+-*%22-completely-bit-manipulation-guaranteed))

  ```python
  class Solution(object):
      def getSum(self, a, b):
          """
          :type a: int
          :type b: int
          :rtype: int
          """
          # 32 bits integer max
          MAX = 0x7FFFFFFF
          # 32 bits interger min
          MIN = 0x80000000
          # mask to get last 32 bits
          mask = 0xFFFFFFFF
          while b != 0:
              # ^ get different bits and & gets double 1s, << moves carry
              a, b = (a ^ b) & mask, ((a & b) << 1) & mask
          # if a is negative, get a's 32 bits complement positive first
          # then get 32-bit positive's Python complement negative
          return a if a <= MAX else ~(a ^ mask)
  ```

- explanation:

  - we know bit addition follows:
    $$
    C_{i}=A_{i}\oplus B_{i}\oplus R_{i}
    \\
    R_{i+1}=R_i(A_i\oplus B_i)+A_iB_i
    $$

  - `(a ^ b)`: do `xor` operation for all bits first, as the first equation, but without $R_i$, we can do it in next part.

  - `(a & b)`: simulate $R_i$, get which bit should have a carry for next bit

  - `<< 1`: send the carry to next bit.

  - each time $R_i$ may cause another carry, so we need do all steps above over and over again, till the carry is 0.

  - all the operations are based on complement(补码).

### [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/description/)

- mine:

  ```python
  # The guess API is already defined for you.
  # @param num, your guess
  # @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
  # def guess(num):
  
  class Solution(object):
      def guessNumber(self, n):
          """
          :type n: int
          :rtype: int
          """
          def find(l,r):
              mid=(r-l)//2+l
              g=guess(mid)
              print l,r,mid,g
              if g==0:
                  return mid
              if g==-1:
                  return find(l,mid)
              if g==1:
                  return find(mid+1,r)
          return find(1,n)
  ```

### [383. Ransom Note](https://leetcode.com/problems/ransom-note/description/)

- mine:

  ```python
  class Solution(object):
      def canConstruct(self, ransomNote, magazine):
          """
          :type ransomNote: str
          :type magazine: str
          :rtype: bool
          """
          m=list(magazine)
          for i in ransomNote:
              if i not in m:
                  return False
              m.remove(i)
          return True
  ```

### [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/description/)

- mine:

  ```python
  class Solution(object):
      def firstUniqChar(self, s):
          """
          :type s: str
          :rtype: int
          """
          a={}
          for i in range(len(s)):
              if s[i] not in a:
                  a[s[i]]=[i,1]
              else:
                  a[s[i]][1]+=1
          b=sorted(a.values(),key=lambda x: x[0])
          print b
          for i in b:
              if i[1]==1:
                  return i[0]
          return -1
  ```

### [389. Find the Difference](https://leetcode.com/problems/find-the-difference/description/)

- mine:

  ```python
  class Solution(object):
      def findTheDifference(self, s, t):
          """
          :type s: str
          :type t: str
          :rtype: str
          """
          C=collections.Counter
          return list(C(t)-C(s))[0]
  ```

### [572. Subtree of Another Tree](https://leetcode-cn.com/problems/subtree-of-another-tree/)

- 没有想象中的做的顺畅

  ```python
  class Solution:
      def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
          def isSameTree(root,t):
              if root.val!=t.val: return False
              l=r=False
              if root.left and t.left: l=isSameTree(root.left,t.left)
              elif not(root.left or t.left): l=True
              if root.right and t.right: r=isSameTree(root.right,t.right)
              elif not(root.right or t.right): r=True
              return l and r
  
          if not s: return False
          flag=False
          if s.val==t.val: flag=isSameTree(s,t)
              return flag or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
  ```
  
 - 其实我最开始的思路就是官方正解，但是少考虑了一点点没有做对，即求出该序列的先序遍历DFS（或后序遍历），看是否包含就行了，但这样仅仅是**必要非充分条件**。我少想了一步，应该对**<u>每个叶子结点处理一下，让他们的左右指向某个假空值（跟真的None值区分开），然后遍历时把这些假空值也遍历进去</u>**，这样就可以用上述便利比较包含关系来确定答案了。