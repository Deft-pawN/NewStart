# -*- coding: utf-8 -*-

print 11,(soup.head.meta['content']),22  # 输出所得标签的‘’属性值
print 22,(soup.span.string);#？？查找到第一个span的标签返回值
print 33,(soup.span.text)  # 两个效果一样，返回标签的text

# name属性是‘’的标签的<ResultSet>类，是一个由<Tag>组成的list
print 44,(soup.find_all(attrs={'name': 'keywords'}))#find_all的作用,对应的属性
print 55,(soup.find_all(class_='logo'))  # class属性是‘’的<Tag>的list,即<ResultSet>
#print(soup.find_all(class_='site_name')[0])  # 这是一个<Tag>

print 66,(soup.find(attrs={'name': 'keywords'})) # name属性是‘’的标签的<Tag>类,find_all和find的区别
print 77,(soup.find('meta', attrs={'name': 'keywords'}))  # name属性是‘’的meta标签的<Tag>类
print 88,(soup.find('meta', attrs={'name': 'keywords'})['content'])  # <Tag类>可直接查属性值，相当于下面的一个content标签
# 配合re模块使用，可以忽略大小写
# 如下面例子，可以找到name属性为keywords，KEYWORDS,KeyWORds等的meta标签
print 99,(soup.find('meta', attrs={'name': re.compile('keywords', re.IGNORECASE)}))
#print 100,soup.prettify()输出所有的网页代码

'''-------------------------------------------------------------------------'''
'''----------------------------修改BeautifulSoup—----------------------------'''
'''-------------------------------------------------------------------------'''
soup.find(attrs={'name': 'keywords'}).extract  # 调用这个方法，可以删除这一个标签
print '名字',soup.title.name
soup.title.name = 'ppp'  # 可以把Tag的名字<title>改成<ppp>

# 可以使用append(),insert(),insert_after()或者insert_before()等方法来对新标签进行插入。
Tag1 = soup.new_tag('li', class_='123')
'''创造一个Tag'''
a.title.append(Tag1)  # 把Tag1添加为name是title的Tag的最后一个【子节点】，没有换行
# .insert(0,Tag1)----这里用insert的话，第一个参数可以控制所添加【子节点】的先后位置
# .insert_after(Tag1)---和insert_before一样，添加为Title的【兄弟节点】

soup.head.meta['content'] = '随便输入，可以添加（或更改）这个Tag的content属性（值）'
del soup.head.meta['content']  # 这个语法可以直接删除这个Tag的content属性

soup.li.clear  # 调用方法会清除所有li标签的text
soup.title.string = '用这个方法可以修改title标签的内容'  # 慎用，只用于最子孙最小的节点，用于父节点会清空子节点
soup.div.append('放在div子节点位置的 最后append最后，是标签内容')
soup.div.insert(0, '放在div子节点位置的 最前insert【0】最前，是标签内容')