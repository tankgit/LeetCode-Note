# [面试题 01.06. 字符串压缩](https://leetcode-cn.com/problems/compress-string-lcci/)

---

难度 `简单` | 标签 `字符串`  | 获赞 `42`

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
<p>字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串<code>aabcccccaaa</code>会变为<code>a2b1c5a3</code>。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。</p>
<p> <strong>示例1:</strong></p>
<pre><strong> 输入</strong>："aabcccccaaa"
<strong> 输出</strong>："a2b1c5a3"
</pre>
<p> <strong>示例2:</strong></p>
<pre><strong> 输入</strong>："abbccd"
<strong> 输出</strong>："abbccd"
<strong> 解释</strong>："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
</pre>
<p><strong>提示：</strong></p>
<ol>
<li>字符串长度在[0, 50000]范围内。</li>
</ol>
</section>

## My Solution

```python
class Solution:
    def compressString(self, S: str) -> str:
        res=''
        for i,c in enumerate(S+' '):
            if i==0 or c!=S[i-1]:
                if i!=0:res+=S[i-1]+str(tmp)
                tmp=1
            else: tmp+=1
        return res if len(res)<len(S) else S
```
