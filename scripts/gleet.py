#!/usr/bin/env python

import os
import numpy as np
import sys
from datetime import datetime
import re

leetDir=os.environ['LEETCODE_PATH']
noteDir=os.path.join(leetDir,"archive")
mainPage=os.path.join(leetDir,"main.md")
tagsPage=os.path.join(leetDir,"tags.md")
lvlsPage=os.path.join(leetDir,"levels.md")
markPage=os.path.join(leetDir,"mark.md")

main_f=open(mainPage,'w')
tags_f=open(tagsPage,'w')
lvls_f=open(lvlsPage,'w')
mark_f=open(markPage,'w')


time=datetime.today().strftime('%Y-%m-%d %H:%M')
main_head1="\
# LeetCode Notes\n\n\
Last update: "+time+"\n\n"
main_head2="\
## Navigation\n\n\
Index by: [Tags](tags.md) | [Levels](levels.md) | [Marks](mark.md)\n\n\
## All Problems\n\n\
|#|题目|&nbsp;难度&nbsp;|标签|标记&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|\n\
|:---:|---|:---:|---|---|\n"

tags_head="# LeetCode Notes - Tags\n\n\
## Tags Cloud\n\n"
lvls_head="# LeetCode Notes - Levels\n\n\
[TOC]\n\n"
mark_head="# LeetCode Notes - Marks\n\n\
[TOC]\n\n"

main_lines=""

main_f.writelines(main_head1)
tags_f.writelines(tags_head)
lvls_f.writelines(lvls_head)
mark_f.writelines(mark_head)

colors={
    "简单":"#019A75",
    "中等":"#EE7337",
    "困难":"#5c0e0a"
}

mark_dict={
    "❌":"没有独立做出来",
    "🌀":"消耗时间太久",
    "㊙️":"涉及知识很重要",
    "🔑":"面试很可能会出",
    "👎":"这道题出的不好"
}

tags_list={}
lvls_list={"简单":"","中等":"","困难":""}
mark_list={}

noteList=[x[:-3] for x in os.listdir(noteDir) if re.search(r"^[0-9]+\.md$",x)]
noteList=sorted(noteList,key=lambda x: int(x))

for num in noteList:
    filepath = os.path.join(noteDir,num+'.md')
    with open(filepath,'r') as note:
        lines=note.readlines()
        title=lines[0].split(']')[0].split('.')[1][1:]
        level=re.search(r"难度 \`([^|]*)\` *[\|\n]{0,1}",lines[4]).group(1)
        tags=re.search(r"标签 (\`[^|]*\`) *[\|\n]{0,1}",lines[4]).group(1)
        mark=re.search(r"个人标签 ([^| ]*) *[\|\n]{0,1}",lines[4])
        mark=mark.group(1) if mark else ''
        level_color="<span style='color:"+colors[level]+"'><b>"+level+"</b></span>"
        rel_link=os.path.join("archive",num+".md")
        line="|"+num+"|["+title+"]("+rel_link+")|"+level_color+"|"+tags+"|"+mark+"|\n"
        main_lines+=line

        if lvls_list[level]=="":
            lvls_list[level]='\
|#|题目|标签|标记&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|\n\
|:---:|---|---|---|\n'
        lvls_list[level]+="|"+num+"|["+title+"]("+rel_link+")|"+tags+"|"+mark+"|\n"

        tags=[x for x in tags.split("`") if x not in ['', ' ']]
        mark=[x for x in mark_dict if x in mark]

        for tag in tags:
            if tag not in tags_list: 
                tags_list[tag]='## '+tag+'\n\n\
|#|题目|&nbsp;难度&nbsp;|标签|标记&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|\n\
|:---:|---|:---:|---|---|\n'
            tags_list[tag]+=line
        

        for m in mark:
            if m not in mark_list:
                mark_list[m]='\
|#|题目|&nbsp;难度&nbsp;|标签|标记&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|\n\
|:---:|---|:---:|---|---|\n'
            mark_list[m]+=line
        
count=str(main_lines.count('\n'))

main_f.write("**Total Notes: `"+count+"`**\n\n---\n\n")
main_f.writelines(main_head2+main_lines)
main_f.close()

tags_count={tag:tags_list[tag].count('\n')-4 for tag in tags_list}

for tag in sorted(tags_list,key=lambda x: tags_count[x],reverse=True):
    count=str(tags_count[tag])
    tag.replace
    tags_f.write("[`"+tag+"("+count+")`](#"+tag.replace(" ","-")+") ")

tags_f.write('\n\n')

for tag in tags_list:
    tags_f.writelines(tags_list[tag])
tags_f.close()

for lvl in colors:
    if lvl not in lvls_list: continue
    count=str(lvls_list[lvl].count('\n')-2)
    lvls_f.write("## "+lvl+"("+count+")\n\n")
    lvls_f.writelines(lvls_list[lvl])
lvls_f.close()

for m in mark_dict:
    if m not in mark_list: continue
    count=str(mark_list[m].count('\n')-2)
    mark_f.write("## "+m+mark_dict[m]+"("+count+")\n\n")
    mark_f.writelines(mark_list[m])
mark_f.close()