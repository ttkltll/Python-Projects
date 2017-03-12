## 谱聚类介绍：
这篇博客对于谱聚类的介绍包括公式推导挺到位的，当时上课的ppt也是截这个图，所以能看懂的话挺不错的。http://www.cnblogs.com/FengYan/archive/2012/06/21/2553999.html

## 算法python实现：
对于公式的推导什么的个人的理解并不是很深，下面直接说说这个算法的实现吧：

1. 首先，因为这个算法其实最先是叫做谱方法，用于社区挖掘或者图挖掘，所以要用在聚类上，你需要一种东西来对样本直接进行连接，实现一个类似于图一样的结构，这里使用knn，就是前k个近邻就有连通，其他就没有。这样我们就能得到矩阵W，不过，有一个小问题，点a的k近邻中有b，但是b的k近邻可能是没有a的，这个时候，为了让矩阵W是一个对称矩阵，我们采用一个或原则，将$W=(W+W^T)/2$ ，这个就能得到一个对称的相似性矩阵了。
![获得相似矩阵W](http://img.blog.csdn.net/20170312185213886?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcHA4ODE4/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

2. 第二步很简单，算出每个节点的度数，得到度矩阵D。
![获得度矩阵D](http://img.blog.csdn.net/20170312185334574?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcHA4ODE4/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

3. 得到拉普拉斯矩阵$L=D-W$，很简单，不贴代码了。

4. 获得拉普拉斯矩阵L的特征矩阵，这个用内置函数就好。
![](http://img.blog.csdn.net/20170312185517253?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcHA4ODE4/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

5. 获得特征矩阵之后，我们使用kmeans方法来对特征矩阵进行一个聚类，每个特征向量是特征矩阵的列，而每行当成一个聚类样本。这样一聚类就是最终的成果了。为了图方便，我这里直接使用sklearn中的KMeans函数来调用：
![这里写图片描述](http://img.blog.csdn.net/20170312190106920?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcHA4ODE4/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

好了，到这里基本就大功告成了，分类基本已经完成了，最后来一波可视化，看看我们的实验结果，因为谱聚类能对球形数据进行聚类，所以我们直接来试试球形数据集：
![这里写图片描述](http://img.blog.csdn.net/20170312190307390?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcHA4ODE4/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

Nice，看上去还不错。
好了好了，本次实验就到这里。
完整代码地址：[github/pp8818](https://github.com/PP8818/Unsplash_Crawling/tree/master/py2/data-mining/clustering/spectral_cluster)记得给star喔~~
