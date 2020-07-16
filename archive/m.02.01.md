# [面试题 02.01. 移除重复节点](https://leetcode-cn.com/problems/remove-duplicate-node-lcci/)

---

难度 `简单` | 标签 `链表`  | 获赞 `47`

---

## Description

<style>
section pre{
    background-color: #eee;
    border: 1px solid #ddd;
    padding:10px;
    border-radius: 5px;
}
</style>
<section>
<p>编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。</p>
<p> <strong>示例1:</strong></p>
<pre><strong> 输入</strong>：[1, 2, 3, 3, 2, 1]
<strong> 输出</strong>：[1, 2, 3]
</pre>
<p> <strong>示例2:</strong></p>
<pre><strong> 输入</strong>：[1, 1, 1, 1, 2]
<strong> 输出</strong>：[1, 2]
</pre>
<p><strong>提示：</strong></p>
<ol>
<li>链表长度在[0, 20000]范围内。</li>
<li>链表元素在[0, 20000]范围内。</li>
</ol>
<p> <strong>进阶：</strong></p>
<p>如果不得使用临时缓冲区，该怎么解决？</p>
</section>

## My Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        p=head
        pre=ListNode(0)
        pre.next=p
        dic={}
        while p:
            if p.val not in dic:
                dic[p.val]=1
                pre=p
            else: pre.next=p.next
            p=p.next
        return head
```

以上是借助哈希表，但是这道题说不要借助额外空间，那么，我们可以使用双重循环，第一层循环从头到尾遍历，第二层从第一层的位置到末尾，去除与第一层目前相同的原素。