# LeetCode Note

我抽空写了个Chrome插件[LeetCode-Digest](https://github.com/tankgit/LeetCode-Digest-Chrome)，可以把需要的题目信息和代码一同转化为markdown，然后存成文件，我又在本地写了个脚本，可以自动归类这些保存的题目文件，然后创建索引，方便以后复习。

## 索引

- 所有题目：[main.md](main.md)

- 按照标签索引：[tags.md](tags.md)
- 按照难度索引：[levels.md](levels.md)

- 按照标记索引：[mark.md](mark.md)

- 预览图

  ![Screen Shot 2020-05-13 at 9.47.28 PM](assets/Screen%20Shot%202020-05-13%20at%209.47.28%20PM.png)

## 利用脚本创建自己的笔记

我已经在仓库的`scripts`目录下提供了我自动生成这些索引文件的脚本，你需要把`shell_func.sh`里的函数添加到你的终端环境里，并把`gleet.py`添加到你的环境变量`$PATH`下。

- 具体整个记笔记的流程为：

    1. 在leetcode-cn做题

    2. 做完以后，在**题目描述页面**使用[LeetCode-Digest](https://github.com/tankgit/LeetCode-Digest-Chrome)插件一键生成你所需要的markdown笔记，它会自动保存到系统粘贴板。

    3. 打开终端，使用`leet`命令（由`shell_func.sh`提供），它会根据系统粘贴板自动生成该题的笔记文件到`$LEETCODE_PATH/archive`目录下（终端里需要提前设置好`$LEETCODE_PATH`变量，archive目录可能需要手动创建，即你想保存笔记的目录位置）。具体使用命令如下（我用了macOS终端下的`open`命令，它会自动使用打开`.md`文件的软件，其他系统请替换为你markdown编辑器的可执行文件）。如果你已经保存过该题，想覆盖原笔记，重新生成，请使用`sf`选项。

	```shell
	## 指令教程，以下为几个用法的示例。
	# 保存粘贴板存的的笔记到你设定的leetcode archive目录
	$ leet -s [题目数字编号].md
	# 保存并打开笔记
	$ leet -so [题目数字编号].md
	# 强制覆盖原笔记，保存并打开
	$ leet -sof [题目数字编号].md
	```
	
	4. 此时笔记文件已经生成并且自动打开，同时`leet`命令自动调用`gleet.py`命令（需要你提前设置到环境变量里）在`$LEETCODE_PATH`路径下创建/更新了上述4个索引文件

### 常见问题

- **MacOS/Linux用户**请务必把`scripts`目录下的脚本添加到终端环境中，否则可能你得自行修改很多地方。
- shell脚本的环境为zsh中开发，一般来说其他shell环境也能用，如果不行请自行debug。python脚本为python3.x开发，python2请自行debug。
- **Windows用户**可能需要自行写一个类似`shell_func.sh`里的函数，我提供的并不能用。