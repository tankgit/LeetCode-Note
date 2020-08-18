# [面试题 08.03. 魔术索引](https://leetcode-cn.com/problems/magic-index-lcci/)

---

难度 `简单` | 标签 `数组` `二分查找`  | 获赞 `27`

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
<p>魔术索引。 在数组<code>A[0...n-1]</code>中，有所谓的魔术索引，满足条件<code>A[i] = i</code>。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。</p>
<p><strong>示例1:</strong></p>
<pre><strong> 输入</strong>：nums = [0, 2, 3, 4, 5]
<strong> 输出</strong>：0
<strong> 说明</strong>: 0下标的元素为0
</pre>
<p><strong>示例2:</strong></p>
<pre><strong> 输入</strong>：nums = [1, 1, 1]
<strong> 输出</strong>：1
</pre>
<p><strong>提示:</strong></p>
<ol>
	<li>nums长度在[1, 1000000]之间</li>
</ol>
</section>

## My Solution

```python
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i,x in enumerate(nums):
            if i==x: return x
        return -1
```

