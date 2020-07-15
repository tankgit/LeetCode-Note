# [面试题 10.01. 合并排序的数组](https://leetcode-cn.com/problems/sorted-merge-lcci/)

---

难度 `简单` | 标签 `数组` `双指针`  | 获赞 `55`

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
<p>给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。</p>
<p>初始化&nbsp;A 和 B 的元素数量分别为&nbsp;<em>m</em> 和 <em>n</em>。</p>
<p><strong>示例:</strong></p>
<pre><strong>输入:</strong>
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3
<strong>输出:</strong>&nbsp;[1,2,2,3,5,6]</pre>
<p><strong>说明:</strong></p>
<ul>
	<li><code>A.length == n + m</code></li>
</ul>
</section>

## My Solution

```cpp
class Solution {
public:
    void merge(vector<int>& A, int m, vector<int>& B, int n) {
        int k=m+n-1;
        m--;
        n--;
        while(k>=0){
            if(n<0 || m>=0 && A[m]>=B[n])A[k]=A[m--];
            else{A[k]=B[n--];}
            k--;
        }
    }
};
```

双指针需要额外m+n的空间，考虑到A的后面都是空的，我们可以直接用逆向双指针，从后往前插，在A基础上修改。

