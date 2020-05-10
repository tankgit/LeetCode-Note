## LeetCode Notes - Medium

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

###  [3. Longest Substring Without Repeating Characters](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

- mine, 双指针，就俩情况，一是右边界遇到了重复元素，停止，算目前长度看是否最长，然后移动左边界，直至重复元素被排除在外，重新开始。

    ```python
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            p=q=max_len=0
            while q<len(s):
                while q<len(s) and s[q] not in s[p:q]:q+=1
                max_len=max(max_len,q-p)
                while q<len(s) and s[q] in s[p:q]:p+=1
            return max_len
    ```

### [5. Longest Palindromic Substring](https://leetcode-cn.com/problems/longest-palindromic-substring/)

- mine:

  ```python
  class Solution:
      def longestPalindrome(self, s: str) -> str:
          i=j=k=0
          pal=[i,j]
          for k in range(len(s)):
              i,j=k,k+1
              if j>=len(s):
                  break
  
              while i>=0 and j<len(s) and s[i]==s[j]:
                  if j-i>pal[1]-pal[0]:
                      pal=[i,j]
                  i-=1
                  j+=1
              i,j=k-1,k+1
              while i>=0 and j<len(s) and s[i]==s[j]:
                  if j-i>pal[1]-pal[0]:
                      pal=[i,j]
                  i-=1
                  j+=1
          return s[pal[0]:pal[1]+1]
  ```
  
- 注意一个常见的错误解法，就是反向string，然后求最大公共子串，这个解法很快，但是一旦，反向的string里有原string的逆向副本（非回文的），就会导致结果仅是最大公共子串但却不是回文。例如$S = \text{“abacdfgdcaba”}, S'=\textrm{“abacdgfdcaba”}$，结果是`abacd`，并非回文。

- 还有个算法就是Manacher算法，时间复杂度是$O(n)$，不过也是在我上面这个算法的基础上优化扩展的。

### [6. ZigZag Conversion](https://leetcode-cn.com/problems/zigzag-conversion/)

- mine, 就是找了个通式，找到了 原index$\rightarrow$每行的位置$\rightarrow$新index 这三者之间的关系。

  ```python
  class Solution:
      def convert(self, s: str, numRows: int) -> str:
          if numRows==1:
              return s
          r=[]
          k=2*(numRows-1)
          i=x=y=0
          while i < len(s):
              r.append(s[x*k+y])
              if y!=0 and y!=k/2 and x*k+k-y<len(s):
                  i+=1
                  r.append(s[x*k+k-y])
              x,i=x+1,i+1
              if x*k+y>=len(s):
                  x,y=0,y+1
          return ''.join(r)
  
  ```

- 有一个很妙的解法，很简洁，不是找通式，而是按照row来先拼出每一行的string，最后再把所有行的string按顺序拼起来

  ```python
  class Solution:
      def convert(self, s: str, numRows: int) -> str:
          if numRows < 2: return s
          res = ["" for _ in range(numRows)]
          i, flag = 0, -1
          for c in s:
              res[i] += c
              if i == 0 or i == numRows - 1: flag = -flag
              i += flag
          return "".join(res)
  ```


### [8. String to Integer (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/)

- mine:

  ```python
  class Solution:
      def myAtoi(self, str: str) -> int:
          i=0
          while i<len(str) and str[i]==' ':
              i+=1
          j=i
          if i==len(str): return 0
          if ord(str[i])<48 or ord(str[i])>57:
              if str[i] in ['-','+']:
                  j+=1
              else:
                  return 0
          while j<len(str) and 48<=ord(str[j])<=57:
              j+=1
          if str[i:j] in ['-','+']: return 0
          r=int(str[i:j])
          if r<=-2**31:
              return -2**31
          elif r>=2**31-1:
              return 2**31-1
          else:
              return r
  ```


### [11. Container With Most Water](https://leetcode-cn.com/problems/container-with-most-water/) 👁‍🗨

- 暴力解法不可取，使用首位双指针，每次只移动小的那个（移动大的，体积只可能比原来小）：

  ```python
  class Solution:
      def maxArea(self, height: List[int]) -> int:
          max_vol=0
          i,j=0,len(height)-1
          while i<=j:
              vol=(j-i)*min(height[i],height[j])
              max_vol=max(vol,max_vol)
              if height[i]<height[j]:
                  i+=1
              else:
                  j-=1
          return max_vol
  ```

### [12. Integer to Roman](https://leetcode-cn.com/problems/integer-to-roman/)

- mine:

  ```python
  class Solution:
      def intToRoman(self, num: int) -> str:
          ch={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
          cov_rules={'DCCCC':'CM','CCCC':'CD','LXXXX':'XC','XXXX':'XL','VIIII':'IX','IIII':'IV'}
  
          ## Step 1: convert number to naive roman number without considering 6 special cases.
          res=''
          for base in sorted(ch.keys(),reverse=True):
              count=num//base
              if count>0:
                  res+=count*ch[base]
                  num-=base*count
          ## Step 2: convert the naive string to the final required format.
          simplified_res=''
          i=0
          while i<len(res):
              if res[i:i+5] in cov_rules:
                  simplified_res+=cov_rules[res[i:i+5]]
                  i+=5
              elif res[i:i+4] in cov_rules:
                  simplified_res+=cov_rules[res[i:i+4]]
                  i+=4
              else:
                  simplified_res+=res[i]
                  i+=1
          return simplified_res
  ```

- 我这个算是半个Hash table解法，稍微复杂了一点，其实可以在Step 1就把所有可能的情况全部表示出来，像这样：

  | 1000 | 900  | 500  | 400  | 100  |  90  |  50  |  40  |  10  |  9   |  5   |  4   |  1   |
  | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
  |  M   |  CM  |  D   |  CD  |  C   |  XC  |  L   |  XL  |  X   |  IX  |  V   |  IV  |  I   |

  然后就可以全部在第一步就完成了。

### [15. 3Sum](https://leetcode-cn.com/problems/3sum/)

- 使用双指针，只不过加了一些限定条件，比如避免重复解。

  ```python
  class Solution:
      def threeSum(self, nums: List[int]) -> List[List[int]]:
          if not nums or len(nums)<3: return []
          ans=[]
          sort_nums=sorted(nums)
          for i in range(len(nums)):
              if sort_nums[i]>0: break
              if i>0 and sort_nums[i]==sort_nums[i-1]: continue
              L,R=i+1,len(nums)-1
              while L<R:
                  sum3=sort_nums[i]+sort_nums[L]+sort_nums[R]
                  if sum3==0:
                      ans.append([sort_nums[i],sort_nums[L],sort_nums[R]])
                      while L<R and sort_nums[L]==sort_nums[L+1]: L+=1
                      while L<R and sort_nums[R]==sort_nums[R-1]: R-=1
                      L+=1
                      R-=1
                  elif sum3<0: L+=1
                  else: R-=1
          return ans
  ```

### [16. 3Sum Closest](https://leetcode-cn.com/problems/3sum-closest/)

- 有了[15. 3Sum](https://leetcode-cn.com/problems/3sum/)的思路，其实这道题也很像，同样的指针，只是判定条件不同了，而且也不需要所有解，一旦找到target直接返回，否则就遍历寻找最近的。

- 第6行和15行我加了两个额外的判定条件，及时停止搜索，减少时间开销。

  ```python
  class Solution:
      def threeSumClosest(self, nums: List[int], target: int) -> int:
          sorted_nums=sorted(nums)
          i,close_sum=0, None
          for i in range(len(sorted_nums)):
              if target> 0 and sorted_nums[i]>=target: break
              L,R=i+1,len(sorted_nums)-1
              while L<R:
                  s=sorted_nums[i]+sorted_nums[L]+sorted_nums[R]
                  if close_sum==None: close_sum=s
                  if abs(close_sum-target)>abs(s-target): close_sum=s
                  if s>target: R-=1
                  elif s<target: L+=1
                  else: return s
                  if target<0 and R<=target: break
          return close_sum
  ```

### [17. Letter Combinations of a Phone Number](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

- 这竟然是一道中等题，官方解法用的回溯，差不多一个意思了。

- mine:

  ```python
  class Solution:
      def letterCombinations(self, digits: str) -> List[str]:
          d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
          res=['']
          for s in digits:
              new=[]
              for e in res:
                  new+=[e+x for x in d[s]]
              res=new
          return res if res!=[''] else []
  ```


### [18. 4Sum](https://leetcode-cn.com/problems/4sum/)

- 服了， 4sum都出来了。思路跟3sum一样，套了个娃，把大问题剥成小问题遍历。

  ```python
  class Solution:
      def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
          def threeSum(nums, target):
              ans=[]
              for i in range(len(nums)):
                  L,R=i+1,len(nums)-1
                  while L<R:
                      s=nums[i]+nums[L]+nums[R]
                      if s==target: 
                          lst=[nums[i],nums[L],nums[R]]
                          if lst not in ans:
                              ans.append(lst)
                          L+=1
                          R-=1
                      elif s<target: L+=1
                      else: R-=1
              return ans
          
          if not nums or len(nums)<4: return []
          ans=[]
          s_nums=sorted(nums)
          for i in range(len(s_nums)-3):
              if i>0 and s_nums[i]==s_nums[i-1]: continue
              ans+=[[s_nums[i]]+x for x in threeSum(s_nums[i+1:],target-s_nums[i])]
          return ans
  ```

### [19. Remove Nth Node From End of List](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

- mine，对于一般链表的问题，递归更容易解决，尤其是需要这种从后往前找的，回溯更合适

  ```python
  class Solution:
      def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
          def remove(link,n):
              if not link: return 0
              s=remove(link.next,n)
              if s==n: link.next=link.next.next
              return s+1
          start=ListNode(0)
          start.next=head
          remove(start,n)
          return start.next
  ```

### [22. Generate Parentheses](https://leetcode-cn.com/problems/generate-parentheses/)

- 感觉也不是很难，但是调试了很久而且写的好麻烦，应该还可以简化

  ```python
  class Solution:
      def generateParenthesis(self, n: int):
          def switch(s,res):
              res.append(''.join(s))
              i=0
              l=r=0
              while i<2*n-1:
                  if s[i]+s[i+1]=='()' and l>r:
                      k=s.copy()
                      k[i+1],k[i]=k[i],k[i+1]
                      if ''.join(k) not in res:
                          switch(k,res)
                      l,r=l+1,r+1
                      i+=2
                      continue
                  if s[i]=='(': l+=1
                  if s[i]==')': r+=1
                  i+=1
          res=[]
          s=list(n*'('+n*')')
          switch(s,res)
          return res
  ```

- 官方解法有个思路，已知我们要求的generate函数是根据输入n输出所有可能的括号匹配，我们知道所有的括号肯定都是`(sub1)sub2`构成的，其中`sub1` `sub2`分别是合法的子串，再算上本身带的一个`()`一共要有`n`对括号，那么就可以用函数递归求，`(generate(i))genrate(n-1-i)`，步骤就是遍历$i\in [0,n-1]$，然后每次拼接这几个串，就是答案了。

  ```python
  class Solution:
      @lru_cache(None)
      def generateParenthesis(self, n: int) -> List[str]:
          if n == 0:
              return ['']
          ans = []
          for c in range(n):
              for left in self.generateParenthesis(c):
                  for right in self.generateParenthesis(n-1-c):
                      ans.append('({}){}'.format(left, right))
          return ans
  ```

###  [24. Swap Nodes in Pairs](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

- 主要考察链表操作，交换时会不会弄乱，思想上没啥难度。

  ```python
  class Solution:
      def swapPairs(self, head: ListNode) -> ListNode:
          headhead=pre=ListNode(0)
          headhead.next=l=head
          while l:
              if not l.next:
                  break
              pre.next=l.next
              tmp=l.next.next
              l.next.next=l
              l.next=tmp
              pre=l
              l=l.next
          return headhead.next
  ```

###  [29. Divide Two Integers](https://leetcode-cn.com/problems/divide-two-integers/)

- ​	写的时候思路有点混乱。。。反正用位移*2来逼近，不大于被除数的剩余部分再用同样办法。

  ```python
  class Solution:
      def divide(self, dividend: int, divisor: int) -> int:
          if dividend==-2**31 and divisor==-1: return 2**31-1
          if dividend>0 and divisor>0 or dividend<0 and divisor<0: sign=1
          else: sign=-1
          dividend=abs(dividend)
          divisor=abs(divisor)
  
          def dd(dividend,divisor):
              if dividend<divisor: return 0
              k=divisor
              i=0
              while k<=dividend:
                  k<<=1
                  i+=1
              diff=dividend-(k>>1)
              more=self.divide(diff,divisor)
              
              return 2**(i-1)+more
  
          res=dd(dividend,divisor)
          return res if sign>0 else -res
  ```


### [31. Next Permutation](https://leetcode-cn.com/problems/next-permutation/)

- 这个题时间复杂度打败了99.2%的python3提交（当然leetcode这个比较是个玄学）。一开始思路想错了但是没意识到，改了老半天了，这题思路上的坑不少，要注意。

  ```python
  class Solution:
      def nextPermutation(self, nums: List[int]) -> None:
          """
          Do not return anything, modify nums in-place instead.
          """
          mark=0
          l=len(nums)
          for i in reversed(range(1,l)):
              if nums[i]>nums[i-1]: 
                  mark=j=i
                  while j<l and nums[j]>nums[i-1]: j+=1
                  nums[i-1],nums[j-1]=nums[j-1],nums[i-1]
                  break
          for k in range(mark,mark+(l-mark)//2):
              nums[k],nums[-(k+1-mark)]=nums[-(k+1-mark)],nums[k]
  ```

### [33. Search in Rotated Sorted Array](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)`二分查找`

- 要求时间复杂度 $O(\log n)$ ，首先想到二分法，第一次写代码写总不对。。。看了一点点提示，要判断左右序列是否有序就容易许多了，不过还是边界上调了很久。。

  ```python
  class Solution:
      def search(self, nums: List[int], target: int) -> int:
          l,r=0,len(nums)-1
          flag=0
          while l<=r:
              mid=(r-l)//2+l
              flag1=True if nums[mid]>=nums[l] else False
              flag2=True if nums[r]>=nums[mid] else False
              if nums[mid]>target:
                  if flag1:
                      if nums[l]<target:r=mid-1
                      elif nums[l]>target:l=mid+1
                      else: return l
                  else: r=mid-1
              elif nums[mid]<target:
                  if flag2:
                      if nums[r]>target: l=mid+1
                      elif nums[r]<target: r=mid-1
                      else: return r
                  else: l=mid+1
              else: return mid
          return -1
  ```

- 其实写麻烦了，判断条件可以重整更优化，这太啰嗦了。。

###  [98. Validate Binary Search Tree](https://leetcode-cn.com/problems/validate-binary-search-tree/)

- 就离谱，正解应该是从叶子往上逐层判断，应该会好做很多，最一开始想从上往下找，结果就写的很复杂，好在也能行得通。。。子树的所有左节点都得比它小，右节点比它大，所以从上往下，所有向左拐的节点值都得比它左子树的左右子树大，向右拐的节点值都得比它右子树的左右子树小。所以向左拐时存一个数组，向右拐时存一个数组。即可。

  ```python
  class Solution:
      def isValidBST(self, root: TreeNode) -> bool:
          def checkChild(root, thl,thr):
              if not root: return True
  
              if not root.left: jud_l=True
              elif root.left.val<root.val and (not thr or root.left.val>max(thr)) and (not thl or root.left.val<min(thl)): jud_l=checkChild(root.left,thl+[root.val],thr.copy())
              else: jud_l=False
  
              if not root.right: jud_r=True
              elif root.right.val>root.val and (not thr or root.right.val>max(thr)) and (not thl or root.right.val<min(thl)): jud_r=checkChild(root.right,thl.copy(),thr+[root.val])
              else: jud_r=False
              return jud_l and jud_r
  
          return checkChild(root,[],[])
  ```
  

### [221. Maximal Square](https://leetcode-cn.com/problems/maximal-square/)

- 暴力解法也可过，不过采用动态规划，以当前点 $(i,j)$ 为矩形右下角，看能组成变长多大的矩形，记为$ dp(i,j)$ ，那么决定这个值的情况有两种：

  - 该点本身的值为0，那么 $dp(i,j)=0$

  - 该点本身的值为1，那么 $dp(i,j)$ 的值由该点左边，上边，以及左上边的点的 $dp$ 值决定，即这些 $dp$ 值的最小值，再加上该点本身提供的1点边长，则
    $$
    dp(i,j)=\min[dp(i-i,j), dp(i,j-1), dp(i-1,j-1)]+1
    $$

  ```python
  class Solution:
      def maximalSquare(self, matrix: List[List[str]]) -> int:
          if matrix==[]: return 0
          import numpy as np
          dp=np.zeros((len(matrix),len(matrix[0])))
          for i in range(len(matrix)):
              for j in range(len(matrix[0])):
                  if matrix[i][j]=="1": 
                      if i==0 or j==0: dp[i,j]=1
                      else: dp[i,j]=min(dp[i-1,j],dp[i,j-1],dp[i-1,j-1])+1
          return int(np.max(dp))**2
  ```

- 上述解法时间和空间复杂度都是$O(mn)$，其中 $m,n$ 是数组长宽。我们创建了新的 $m\times n$ 矩阵来储存 $dp$ 值，但可以注意到实际上只需要把 $dp$ 值覆盖到原数组即可，不会冲突，空间复杂度变为 $O(1)$

### [983. Minimum Cost For Tickets🔹](https://leetcode-cn.com/problems/minimum-cost-for-tickets/)

- 没写出来，这个`lru_cache(None)`值得注意一下，不加会超时，具体介绍和练习见[这篇文章](https://www.interviewcake.com/concept/java/lru-cache)和LeetCode146题。

  ```python
  class Solution:
      def mincostTickets(self, days: List[int], costs: List[int]) -> int:
          N=len(days)
          day_list=[1,7,30]
          
          @lru_cache(None)
          def min_cost(i):
              if i>=N: return 0
              curr_min=365000
              j=i
              for d,c in zip(day_list,costs):
                  while j<N and days[j]-days[i]<d: j+=1
                  curr_min= min(curr_min,min_cost(j)+c)
              return curr_min
  
          return min_cost(0)
  
  ```

  