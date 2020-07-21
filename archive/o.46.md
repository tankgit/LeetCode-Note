# [剑指 Offer 46. 把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)

---

难度 `中等` | 获赞 `108`

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
<p>给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。</p>
<p>&nbsp;</p>
<p><strong>示例 1:</strong></p>
<pre><strong>输入:</strong> 12258
<strong>输出:</strong> <code>5
</code><strong>解释:</strong> 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"</pre>
<p>&nbsp;</p>
<p><strong>提示：</strong></p>
<ul>
	<li><code>0 &lt;= num &lt; 2<sup>31</sup></code></li>
</ul>
</section>

## My Solution

```python
class Solution:
    def translateNum(self, num: int) -> int:
        n=0
        k='012345'
        def trans(s):
            if not s:
                nonlocal n
                n+=1
                return
            if len(s)==1: trans([])
            elif s[0]=='1' or (s[0]=='2' and s[1] in k):
                trans(s[1:])
                trans(s[2:])
            else: trans(s[1:])
        trans(str(num))
        return n
```
