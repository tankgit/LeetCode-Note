# [面试题64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)

---

难度 `中等` | 标签 `无` | 个人标签 🔑 | 获赞 `133`

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
<p>求 <code>1+2+...+n</code> ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入:</strong> n = 3
<strong>输出:&nbsp;</strong>6
</pre>
<p><strong>示例 2：</strong></p>
<pre><strong>输入:</strong> n = 9
<strong>输出:&nbsp;</strong>45
</pre>
<p>&nbsp;</p>
<p><strong>限制：</strong></p>
<ul>
	<li><code>1 &lt;= n&nbsp;&lt;= 10000</code></li>
</ul>
</section>

## My Solution

```python
class Solution:
    def sumNums(self, n: int) -> int:
        if n==1: return 1
        else: return n+self.sumNums(n-1)
```

[官方题解](https://leetcode-cn.com/problems/qiu-12n-lcof/solution/qiu-12n-by-leetcode-solution/)给出了不用递归的做法，运用到了一些位运算，但是最后为了解决循环问题，感觉有点取巧，这题出的并不怎么好。

不过，位运算那里的思路还是挺重要的。

