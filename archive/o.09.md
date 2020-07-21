# [剑指 Offer 09. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)

---

难度 `简单` | 标签 `栈` `设计`  | 获赞 `90`

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
<p>用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 <code>appendTail</code> 和 <code>deleteHead</code> ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，<code>deleteHead</code>&nbsp;操作返回 -1 )</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
<strong>输出：</strong>[null,null,3,-1]
</pre>
<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
<strong>输出：</strong>[null,-1,null,null,5,2]
</pre>
<p><strong>提示：</strong></p>
<ul>
	<li><code>1 &lt;= values &lt;= 10000</code></li>
	<li><code>最多会对&nbsp;appendTail、deleteHead 进行&nbsp;10000&nbsp;次调用</code></li>
</ul>
</section>

## My Solution

```python
class CQueue:
 
    def __init__(self):
        self.s1=[]
        self.s2=[]
        self.N=0
 
    def appendTail(self, value: int) -> None:
        self.s1.append(value)
        self.N+=1
 
    def deleteHead(self) -> int:
        if self.N==0:return -1
        while self.s1: self.s2.append(self.s1.pop())
        res=self.s2.pop()
        while self.s2: self.s1.append(self.s2.pop())
        self.s2=[]
        self.N-=1
        return res
 
 
# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

