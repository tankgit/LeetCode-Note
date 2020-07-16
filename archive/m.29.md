# [面试题29. 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)

---

难度 `简单` | 标签 `数组`  | 获赞 `50`

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
<p>输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>输出：</strong>[1,2,3,6,9,8,7,4,5]
</pre>
<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>matrix =&nbsp;[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>输出：</strong>[1,2,3,4,8,12,11,10,9,5,6,7]
</pre>
<p>&nbsp;</p>
<p><strong>限制：</strong></p>
<ul>
	<li><code>0 &lt;= matrix.length &lt;= 100</code></li>
	<li><code>0 &lt;= matrix[i].length&nbsp;&lt;= 100</code></li>
</ul>
<p>注意：本题与主站 54 题相同：<a href="https://leetcode-cn.com/problems/spiral-matrix/">https://leetcode-cn.com/problems/spiral-matrix/</a></p>
</section>

## My Solution

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i,j=0,0
        k=[0,1,0,-1]
        M,N=len(matrix),len(matrix[0]) if matrix else 0
        total=M*N
        res=[]
        while total>0:
            res.append(matrix[i][j])
            total-=1
            matrix[i][j]='a'
            if not 0<=i+k[0]<M or not 0<=j+k[1]<N or matrix[i+k[0]][j+k[1]]=='a' : k=k[1:]+k[:1]
            i+=k[0]
            j+=k[1]
        return res
```

