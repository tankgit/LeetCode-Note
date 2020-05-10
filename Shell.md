## LeetCode Notes - Shell

---

[TOC]

---

### [193. Valid Phone Numbers](https://leetcode.com/problems/valid-phone-numbers)

- Consider using Regular Expression
- `grep`, notic the difference between `BRE(Basic Regular Expression)` and `ERE(Extend Regular Expression)`
  - `BRE`:  `a{1,2}` just matches `a{1,2}` literally, `a\{1,2\}` matches `a` or `aa`.
  - [details here](https://www.regular-expressions.info/gnu.html)
- `grep`, notice that you must use single quotes `'` to contain your expression. [click for details](https://stackoverflow.com/questions/3008423/quotes-when-using-grep)
#### My answer
```bash
cat file.txt |grep '^[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}$\|^([0-9]\{3\}) [0-9]\{3\}-[0-9]\{4\}$'
```
#### Suggest Answer
- Using grep:
```bash
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
```
- Using sed:
```bash
sed -n -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt
```
- Using awk:
```bash
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt
```