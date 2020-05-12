## LeetCode Notes - Hard

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

###[4.  Median of Two Sorted Arrays](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

- Main Steps

    1. 把两个list分别进行分割，从某处一刀两断![Screen Shot 2020-04-25 at 11.39.26 AM](assets/Screen%20Shot%202020-04-25%20at%2011.39.26%20AM.png)
    2. 确认两件事，我们就可以得到答案
       1. $\text{len}(\text{left_part})=\text{len}(\text{right_part})$
       2. $\max(\text{left_part})\leq \min(\text{right_part})$

    3. 我们先确定（先任选） $i$ ，然后根据 $i$ 计算 $j$ 
    4. 然后比较$A[i-1]$ 和$B[j]$以及$B[j-1]$和$A[i]$，根据结果调整 $i$ 的位置
    5. 调整位置我们采用二分搜索，具体见代码
    6. 最后分情况讨论临界边界的几种情况即可

    ```python
    class Solution:
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            m,n=len(nums1),len(nums2)
            if m>n:
                nums1,nums2=nums2,nums1
                m,n=n,m
            imin,imax,h_len=0,m,(m+n+1)//2
            while imin<=imax:
                i=(imin+imax)//2
                j=h_len-i
                if i<m and nums2[j-1] > nums1[i]:
                    imin=i+1
                elif i>0 and nums1[i-1] > nums2[j]:
                    imax=i-1
                else:
                    if i==0: max_left=nums2[j-1]
                    elif j==0:  max_left=nums1[i-1]
                    else: max_left=max(nums1[i-1],nums2[j-1])
                    if (m+n) % 2 == 1:
                        return max_left

                    if i==m: min_right=nums2[j]
                    elif j==n: min_right=nums1[i]
                    else: min_right=min(nums1[i],nums2[j])
                    return (max_left+min_right)/2.0
    ```

### [10. Regular Expression Matching](https://leetcode-cn.com/problems/regular-expression-matching/)

- 此题耗时很久未做出，原思路为从前往后遍历pattern，依次按照规则寻找所有matched子串，然后把子串（在s中最靠后的匹配位置）记录下来，然后每次读一个pattern（或一对，因为含“\*”）依次更新，matched的最后匹配位置，一旦遇到不可匹配，将其从matched中删除。但是实际实现时，这个思路需要考虑太多情况，还要借助很多额外储存空间，遂放弃。

- 官方解法一：递归回溯，每次只看最前的一个匹配（或包含“*”的一对），两种主要情况：

  - 如果第一个字符匹配上了，且第二位为"\*"，那么忽略原串匹配上的这个字符，从s[1:]开始，重新套用该函数搜索，pattern不变。或者没匹配上（因为带有"\*"，所以就算字符没匹配上也没关系，直接忽略），也可以直接重新递归匹配，只不过忽略现在这个匹配，从p[2:]开始。
  - 如果第一个字符匹配上了，且第二不位“\*”，那么很简单，直接pass这个字符，s和p都从下一位开始重新匹配。
  - 其他情况就是，没匹配上第一个字符，结合上两种情况一起输出，看最终是否是true or false。

  ```python
  class Solution:
      def isMatch(self, s: str, p: str) -> bool:
          if not p:
              return not s
  
          first_match = (s != '') and p[0] in [s[0],'.']
  
          if len(p)>=2 and p[1]=='*':
              return self.isMatch(s,p[2:]) or first_match and self.isMatch(s[1:],p)
          else:
              return first_match and self.isMatch(s[1:],p[1:])
  ```

- 官方解法而：动态规划，类似第一个，但是引入了一个标记数组，节省了计算和储存开销，详情见[leetcode官方解法](https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode/]

### [23. Merge k Sorted Lists](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

- 其实这题竟然暴力也能解，先把所有list的所有值输出到数组，然后排序，在创建新的list返回，最终复杂度取决于排序。

- 然后是我想到的思路，就是挨个对比每个list目前第一个元素（各自最小的），然后把最小的那个输出成新list的下一个元素，最终时间复杂度是$O(kN)$，$k$是list数目，$N$是所有所有元素数量。

- 最后就是利用优先队列去优化第二个思路了，用优先队列去完成比较大小这一步

  ```python
  import heapq
  
  class Solution:
      def mergeKLists(self, lists: List[ListNode]) -> ListNode:
          head=p=ListNode(0)
          h=[]
          for l in lists:
              while l:
                  heapq.heappush(h,l.val)
                  l=l.next
          while h:
              p.next=ListNode(heapq.heappop(h))
              p=p.next
          return head.next
  ```

- 还有个分治的解法，参见[这里](https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/fen-zhi-gui-bing-pai-xu-by-fe-lucifer/)，（据说是leetcode目前最难链表题？？？可能是我没理解精髓

###  [25. Reverse Nodes in k-Group](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)

- 24题(medium)的升级版，同样思路上没啥难度，就是写起来需要注意不要弄混了。

  ```python
  class Solution:
      def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
          headhead=hh=ListNode(0)
          headhead.next=p=head
          while p:
              run=p
              for i in range(k):
                  if not run:
                      hh.next=p
                      return headhead.next
                  run=run.next
              pre=None
              tail=p
              for i in range(k):
                  tmp=p.next
                  p.next=pre
                  pre=p
                  p=tmp
              hh.next=pre
              hh=tail
          return headhead.next
  ```

### [30. Substring with Concatenation of All Words](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/)

- 我的暴力解法😅，时间上个空间上都打败了百分之个位数的网友🥴

  ```python
  class Solution:
      def findSubstring(self, s: str, words: List[str]) -> List[int]:
          if not s or not words: return []
          res=[]
          lw=len(words[0])
          ll=len(words)
          for i in range(len(s)):
              sub=s[i:i+lw*ll]
              if sorted([sub[x*lw:(x+1)*lw] for x in range(ll)])==sorted(words):
                  res.append(i)
  
          return res
  ```

- 其实答题思路就是我的方法，不过细节实现上过于粗糙，暴力使用各种python低效率方法，以下解法做了一些优化。

  - 首先考虑，每个词只有m长度，那么我们搜索只有m种初始情况，就是从s的第0...m-1个元素开始，向后搜索，每次跳m个长度。所以一开始第一层循环是遍历一个词的长度。
  - 生成一个Counter记录原words每个词的次数，在s上滑动，每次记录左端点保持不动，往右一个单词一个单词滑动，遇到一个词，就加一个这个词的count，如果超过了words里的count，就把左端点往右移动，直到count不超过words原本的count，这时候比较找到的词总数是否与words长度向度，就可以决定是否记录左端点了。最里层循环条件刚好可以帮助我们把非搜索词跳过，同时排出多余的重复词。

  ```python
  class Solution:
      def findSubstring(self, s: str, words: List[str]) -> List[int]:
          from collections import Counter
          if not s or not words:return []
          one_word = len(words[0])
          word_num = len(words)
          n = len(s)
          words = Counter(words)
          res = []
          for i in range(0, one_word):
              cur_cnt = 0
              left = i
              right = i
              cur_Counter = Counter()
              while right + one_word <= n:
                  w = s[right:right + one_word]
                  right += one_word
                  cur_Counter[w] += 1
                  cur_cnt += 1
                  while cur_Counter[w] > words[w]:
                      left_w = s[left:left+one_word]
                      left += one_word
                      cur_Counter[left_w] -= 1
                      cur_cnt -= 1
                  if cur_cnt == word_num :
                      res.append(left)
          return res
  ```

### [32. Longest Valid Parentheses](https://leetcode-cn.com/problems/longest-valid-parentheses/)

- 感觉我写的太麻烦了，考虑了很久各种情况，但是思路是对的，时间复杂度也还行， $O(n)$ 

  ```python
  class Solution:
      def longestValidParentheses(self, s: str) -> int:
          sub=[0]
          mark=[]
          stack=[]
          submaxs=[]
          prePaired=False
          for p in s:
              if p=='(':
                  prePaired=False
                  if len(sub)>len(mark): mark.append(0)
                  mark[-1]+=1
                  stack.append(p)
              if p==')':
                  if stack==[]:
                      prePaired=False
                      submaxs.append(max(sub))
                      sub=[0]
                      mark=[]
                      stack=[]
                  if stack and stack[-1]=='(':
                      mark[-1]-=1
                      if prePaired: sub[-1]+=2
                      else: sub.append(2)
                      if mark[-1]==0:
                          sub[-2]+=sub[-1]
                          sub.pop()
                          mark.pop()
                      stack.pop()
                      prePaired=True
                  else:
                      prePaired=False
          submaxs.append(max(sub))
          return max(submaxs)
  ```

- 跟大佬的答案一比我这简直是垃圾，[官方解法](https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode/)

### [37. Sudoku Solver](https://leetcode-cn.com/problems/sudoku-solver/)🔹🔸

- 这道题哔了🐶了。心累。

  ```python
  class Solution:
      def solveSudoku(self, board: List[List[str]]) -> None:
          """
          Do not return anything, modify board in-place instead.
          """
          def placeHere(val, i,j):
              rows[i][val]=1
              cols[j][val]=1
              boxs[bx(i,j)][val]=1
              board[i][j]=str(val)
  
          def isValid(val, i,j):
              return not (val in rows[i] or val in cols[j] or val in boxs[bx(i,j)])
  
          def remove(val, i,j):
              del rows[i][val]
              del cols[j][val]
              del boxs[bx(i, j)][val]
              board[i][j] = '.'  
  
  
          def doNext(i,j):
              if i==8 and j==8: 
                  nonlocal isSolved
                  isSolved=True
              else:
                  if j==8: doSUDO(i+1,0)
                  else: doSUDO(i,j+1)
  
          def doSUDO(i=0,j=0):
              if board[i][j] =='.':
                  for v in range(1,10):
                      if isValid(v,i,j): 
                          placeHere(v,i,j)
                          doNext(i,j)
                          if not isSolved: remove(v,i,j)
              else:
                  doNext(i,j)
  
          rows=[{} for x in range(9)]
          cols=[{} for x in range(9)]
          boxs=[{} for x in range(9)]
  
          bx=lambda i,j:i//3*3+j//3
  
          for i in range(9):
              for j in range(9):
                  if board[i][j]!='.':
                      val=int(board[i][j])
                      placeHere(val,i,j)
          
          isSolved=False
          doSUDO()
  ```

### [41. First Missing Positive](https://leetcode-cn.com/problems/first-missing-positive/)🔹

- 时间复杂度和空间复杂度要求都很高，我们只能在原数组上操作，思路比较巧妙

  ```python
  class Solution:
      def firstMissingPositive(self, nums: List[int]) -> int:
          if 1 not in nums: return 1
          length=len(nums)
          for i in range(length):
              if nums[i]>length or nums[i]<=0: nums[i]=1
          for x in nums:
              x=abs(x)
              if nums[x-1]>0: nums[x-1]*=-1
          for i in range(length):
              if nums[i]>0: return i+1
          return length+1
  ```

  

### [45. Jump Game II](https://leetcode-cn.com/problems/jump-game-ii/)

- 感觉没多难，第一时间想到的就是正解，所以也没看其他方法解析，复习时希望看一下

  ```python
  class Solution:
      def jump(self, nums: List[int]) -> int:
          i=steps=jump=0
          while i<len(nums)-1:
              jump=i+nums[i]
              for j in range(i+1,nums[i]+i+1):
                  if jump>=len(nums)-1: break
                  if j+nums[j]>jump+nums[jump]: jump=j
              i=jump
              steps+=1
          return steps
  ```
