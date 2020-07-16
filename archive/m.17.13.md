# [面试题 17.13. 恢复空格](https://leetcode-cn.com/problems/re-space-lcci/)

---

难度 `中等` | 标签 `记忆化` `字符串`  | 个人标签 ❌㊙️ | 获赞 `104`

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
<p>哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子<code>"I reset the computer. It still didn’t boot!"</code>已经变成了<code>"iresetthecomputeritstilldidntboot"</code>。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典<code>dictionary</code>，不过，有些词没在词典里。假设文章用<code>sentence</code>表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。</p>
<p><strong>注意：</strong>本题相对原题稍作改动，只需返回未识别的字符数</p>
<p>&nbsp;</p>
<p><strong>示例：</strong></p>
<pre><strong>输入：</strong>
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
<strong>输出：</strong> 7
<strong>解释：</strong> 断句后为"<strong>jess</strong> looked just like <strong>tim</strong> her brother"，共7个未识别字符。
</pre>
<p><strong>提示：</strong></p>
<ul>
	<li><code>0 &lt;= len(sentence) &lt;= 1000</code></li>
	<li><code>dictionary</code>中总字符数不超过 150000。</li>
	<li>你可以认为<code>dictionary</code>和<code>sentence</code>中只包含小写字母。</li>
</ul>
</section>

## My Solution

```python
class Trie:
    def __init__(self):
        self.root={}
        self.end=-1

    def insert(self,word):
        curr=self.root
        for w in word[::-1]:
            if w not in curr: curr[w]={}
            curr=curr[w]
        curr[self.end]=True

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        trie=Trie()
        for word in dictionary: trie.insert(word)

        dp=[0]*(len(sentence)+1)
        for i in range(1,len(sentence)+1):
            dp[i]=dp[i-1]+1
            tmp=trie.root
            for j in range(i,0,-1):
                if sentence[j-1] not in tmp: break
                elif trie.end in tmp[sentence[j-1]]: dp[i]=min(dp[i],dp[j-1])
                tmp=tmp[sentence[j-1]]
        return dp[-1]
```

这道题用朴素的字典查询好像也能过，不过，这道题应该学习的是字典树，可以最大化利用字符串相同前缀，并进行$O(n)$时间的查询，以下为一个简单例子：

```
["looked","just","like","her","brother"]
```



![Screen Shot 2020-07-09 at 11.38.18 PM](assets/Screen%20Shot%202020-07-09%20at%2011.38.18%20PM.png)

利用传统字典的套娃，可以轻松实现字典树，遇到词的结尾（其实是开头），可以轻松判断。