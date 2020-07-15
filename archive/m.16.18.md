# [面试题 16.18. 模式匹配](https://leetcode-cn.com/problems/pattern-matching-lcci/)

---

难度 `中等` | 标签 `字符串`  | 获赞 `66`

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
<p>你有两个字符串，即<code>pattern</code>和<code>value</code>。 <code>pattern</code>字符串由字母<code>"a"</code>和<code>"b"</code>组成，用于描述字符串中的模式。例如，字符串<code>"catcatgocatgo"</code>匹配模式<code>"aabab"</code>（其中<code>"cat"</code>是<code>"a"</code>，<code>"go"</code>是<code>"b"</code>），该字符串也匹配像<code>"a"</code>、<code>"ab"</code>和<code>"b"</code>这样的模式。但需注意<code>"a"</code>和<code>"b"</code>不能同时表示相同的字符串。编写一个方法判断<code>value</code>字符串是否匹配<code>pattern</code>字符串。</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong> pattern = "abba", value = "dogcatcatdog"
<strong>输出：</strong> true
</pre>
<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong> pattern = "abba", value = "dogcatcatfish"
<strong>输出：</strong> false
</pre>
<p><strong>示例 3：</strong></p>
<pre><strong>输入：</strong> pattern = "aaaa", value = "dogcatcatdog"
<strong>输出：</strong> false
</pre>
<p><strong>示例 4：</strong></p>
<pre><strong>输入：</strong> pattern = "abba", value = "dogdogdogdog"
<strong>输出：</strong> true
<strong>解释：</strong> "a"="dogdog",b=""，反之也符合规则
</pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>0 &lt;= len(pattern) &lt;= 1000</code></li>
<li><code>0 &lt;= len(value) &lt;= 1000</code></li>
<li>你可以假设<code>pattern</code>只包含字母<code>"a"</code>和<code>"b"</code>，<code>value</code>仅包含小写字母。</li>
</ul>
</section>

## My Solution

```python
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        M,N=len(pattern),len(value)
        if not value and not pattern: return True
        elif not value: return len(set(pattern))==1
        elif not pattern: return False
        if len(set(pattern))==1: return value[:N//M]*M==value
        na=pattern.count('a')
        nb=M-na
        mna=N//na
        fa,fb=pattern.index('a'),pattern.index('b')
        for i in range(mna+1):
            ia,ib=i,(N-i*na)//nb
            ca=value[:ia] if fa==0 else value[ib*fa:ib*fa+ia]
            cb=value[ia*fb:ia*fb+ib] if fa==0 else value[:ib]
            v=''
            for c in pattern: v+=ca if c=='a' else cb
            if v==value:return True
        return False
```

pattern只有两种字符需要匹配，这就好办，我们就分别让a和b分别能代表多长的段，然后按照长度在value里面截取他们第一次出现所代表的段，然后按照pattern进行重复拼接，只要拼接结果等于value就True，否则遍历完所有可能长度还没有找到，就False