#所有的模块要经历的两个步骤
	#要操作的概念本身： 正则表达式   时间
	#使用模块去操作它：   re        time

#学习 正则表达式  本身
	#什么是正则表达式
		#一种匹配字符串的规则
		#input 一串数据
			#是不是qq号码： 全数字 5位以上  12位以下，第一位不是零
			#是不是身份证号：18位/15位 第一位不是零  18位的最后一位可能是x或数字
		#有一个文件
			#要你把这个文件中所有的手机号都摘取出来
	#正则表达式能做作什么
		#可以定制一个规则，
			#1.来确认某一个字符串是否符合规则
			#2 从大段的字符串中找到符合规则的内容
		#程序领域
			#1.登陆注册页的表单验证  web开发 要求简单语法
			#2.爬虫
				#爬虫 把这个网页下载下来，从里面提取一些信息，找到我要的所有信息，做数据分析
			#3.自动化开发  日志分析
# 什么是正则表达式 : 一种匹配字符串的规则

# 明确一件事:
    # 正则表达式是一种独立的语法
    # 和python没关系

# 要先学习正则的语法
# 再学习使用python来操作正则

# 帮助学习的工具 http://tool.chinaz.com/regex/

# 元字符
    # [] [^]  个性化的定制,
        # [1-9]下面这一组无法描述的一般用上面字符组的形式
        # [\d\s]一个特殊元字符无法描述一个字符内出现的内容了
    # \d \D \w \W \s \S \t \n
		# \d == [0-9] 也表示匹配一个字符,匹配的是一个数字
		# \w == [0-9a-zA-Z_] 也表示匹配一个数字字母下划线
		# \s == [\n \t]  包括回车 空格 和 制表符tab
			# \n  匹配回车
			# \t  匹配制表符
		# \D  匹配非数字
		# \W  匹配非数字字母下滑线
		# \S  匹配非空白

		# [\d\D] [\w\W] [\s\S] 匹配所有
    # .  匹配除了换行符之外的所有字符 爬虫容易用,表单不容易用
    # ^  匹配字符串的开始
		#[^x] 匹配除了x以外的任意字符
		#[^aeiou] 匹配除了aeiou这几个字母以外的任意字符
	# $  匹配字符串的结束
    # |  或 A | B
	# () 分组

# 量词
    # *  0-n
    # +  1-n
    # ?  0-1
    #{n} 重复n次
	# {n,} 重复n次或更多次 贪婪匹配
	# {n,m} 重复n到m次  贪婪匹配
	# 特殊的用法和现象
	# ?的使用
	# 1. 在量词的后面跟了一个 ? 取消贪婪匹配 非贪婪(惰性)模式
	# ?? \ *? \+? \ {n}?
	# 李.{1,3}?和 李莲英和  惰性匹配 回溯算法
	# 最常用  .*?x 匹配任意字符直到找到一个x
	#身份证号：[1-9]\d{14}(\d{2}[1-9X])?
	#email： \w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}
	#小数或整数  \d+(\.\d+)?
# 其他知识 :
    # 贪婪匹配 - 回溯算法
    # 量词? - 惰性匹配
"""
贪婪匹配 :  默认向更多次匹配 (回溯算法)
非贪婪匹配: 默认向更少次匹配 (语法在量词的后面加?号)

. 代表除了\n,可以匹配任意字符
.? .+ .* .{m,n}

回溯算法:从左到右进行匹配,直到再也匹配不到了,回头,拿离右边最近的一个值.

非贪婪匹配语法: (语法在量词的后面加?号)
.??  .+? .*? .{m,n}?
"""

# 总结
    # 元字符
    # 元字符量词   默认贪婪匹配
    # 元字符量词?  表示惰性匹配


# 在python中使用正则表达式
    # 转义符 : 在正则中的转义符 \ 在python中的转义符
    # re模块
        # findall search match
        # sub subn split
        # compile finditer
    # python中的正则表达式
        # findall 会优先显示分组中的内容,要想取消分组优先,(?:正则表达式)
        # split 遇到分组 会保留分组内被切掉的内容
        # search 如果search中有分组的话,通过group(n)就能够拿到group中的匹配的内容
# 正则表达式进阶
    # 分组命名
        # (?P<name>正则表达式) 表示给分组起名字
        # (?P=name)表示使用这个分组,这里匹配到的内容应该和分组中的内容完全相同
    # 通过索引使用分组
        # \1 表示使用第一组,匹配到的内容必须和第一个组中的内容完全相同




















