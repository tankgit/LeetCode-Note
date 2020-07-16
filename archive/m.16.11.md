# [面试题 16.11. 跳水板](https://leetcode-cn.com/problems/diving-board-lcci/)

---

难度 `简单` | 标签 `递归` `记忆化`  | 获赞 `21`

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
<p>你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为<code>shorter</code>，长度较长的木板长度为<code>longer</code>。你必须正好使用<code>k</code>块木板。编写一个方法，生成跳水板所有可能的长度。</p>
<p>返回的长度需要从小到大排列。</p>
<p><strong>示例：</strong></p>
<pre><strong>输入：</strong>
shorter = 1
longer = 2
k = 3
<strong>输出：</strong> {3,4,5,6}
</pre>
<p><strong>提示：</strong></p>
<ul>
<li>0 &lt; shorter &lt;= longer</li>
<li>0 &lt;= k &lt;= 100000</li>
</ul>
</section>

## My Solution

```python
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k==0:return []
        if shorter==longer: return [shorter*k]
        res=[shorter*k]
        for i in range(1,k+1):
            v=res[-1]-shorter+longer
            res.append(v)
        return res
```

