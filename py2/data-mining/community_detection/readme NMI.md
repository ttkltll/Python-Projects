## 介绍
NMI是社区发现(community detection)在有标准ground-truth的情况下的重要衡量指标，基本可以比较客观地评价出一个社区划分与标准划分之间相比的准确度。NMI的值域是0到1，越高代表划分得越准。具体的原理和例子可以参考这篇博客：http://www.cnblogs.com/ziqiao/archive/2011/12/13/2286273.html

因为之前自己要用到，但是发现在网上现成的计算NMI的代码基本都是matlab的和java的，没找到用python写的。所以今天闲来无事，把上面博客中的matlab实现方法用python实现了一下。将来就可以直接用了。

## 代码
其实代码很简单，就是参考博客中直接从matlab翻译成python，不过有一些小坑而已。
![python代码](http://img.blog.csdn.net/20170314151620613?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcHA4ODE4/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

直接给代码，跟博客中的没什么区别啦，这里解释一下代码中的eps是一个很小的正数，为了防止log函数中参数为0而已。
为了方便大家使用python的话可以直接用，最后附有下载地址。

## 结果
使用代码中的用例，可以看到，如果输出的结果是0.36456，说明结果就是正确的。

## 下载地址
[CDNS下载](http://download.csdn.net/detail/pp8818/9780721)

没积分的也可以github下载：
[github下载链接](https://github.com/PP8818/Python-Projects/tree/master/py2/data-mining/community_detection)
记得给star喔~

