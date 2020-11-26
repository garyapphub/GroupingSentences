
# 使用说明

该代码的实现思路完全来自于知乎君言的《如何在百万级的数据里找到别人正在赚钱的项目》，功能主要为

  - 将一组句子根据相似度分类并存放到xls文件 
  - 将一组句子按词根热度排序，提取出前N名的词根形成xmind文件

## 如何使用

下面我将介绍如何使用

### 获取和使用

可以通过pip来安装也可以通过fork或clone本github到本地安装

####通过pip来安装

```sh
$ pip install groupingsentences
```

词向量文本分类，只需两行代码即可

```Python
from groupingsentences import gs_grouping_sentences_to_xls
gs_grouping_sentences_to_xls('input.csv', 'output.xls')
```

如果需要更多设置，该函数可接受的参数说明如下

```
inputfile: 顾名思义，就是待分类的字符串，一行一个字符串，如果是逗号分隔的只取第一个逗号前的字符串
outputfile: 要生成的文件位置
max_items: 一个文件可能很大，可以设置只提取前面10000个，进行试验性运行，查看结果是否符合要求
encoding：文件的编码类型，默认为gb18030， 因为文件编码也有可能是utf8等
type_of_func：计算相似度所用的函数类型，
					0 为向量余弦距离计算
					1 edit_distance
					2 jaccard_similarity
					3 tf_similarity
					4 tfidf_similarity
					7 KMeans word2vec距离计算，速度快（默认值）
					
threshold： 相似度阈值，可以设置比如大于0.8还是0.55就认为两个句子是相似的，可以调整此值输出不同的分类效果
model_file_path： word2vec 模型文件


```

[word2vec模型下载](https://pan.baidu.com/s/1TZ8GII0CEX32ydjsfMc0zw)


关键词根提取法，也只需两行代码即可

```Python
from groupingsentences import gs_grouping_sentences_to_xmind
gs_grouping_sentences_to_xmind('input.csv', 'output.xmind')
```

如果需要更多设置，该函数可接受的参数说明如下

```
inputfile: 顾名思义，就是待分类的字符串，一行一个字符串，如果是逗号分隔的只取第一个逗号前的字符串
outputfile: 要生成的文件位置
max_items: 一个文件可能很大，可以设置只提取前面10000个，进行试验性运行，查看结果是否符合要求
encoding：文件的编码类型，默认为gb18030， 因为文件编码也有可能是utf8等
topwordscount： 选取TOP 几个做节点
topword ：需探查的词根，如不输入则使用topwordscount查找词频最高的几个词根
stop_file_path ：STOP词汇所在位置
max_level ：xmind展示几层 默认1

```


####通过clone本github安装

```sh
$ git clone https://github.com/garyapphub/GroupingSentences.git
$ cd GroupingSentences
$ python setup.py install
```

接下来就可以以下代码进行测试了
```sh
$ python firsttest.py -i ./input.csv -o ./output.xls
$ python secondtest.py -i ./input.csv -o ./output.xmind
```

词向量文本分类更详细的使用说明如下：

```
python firsttest.py -i <inputfile> -o <outputfile> -c <maxcount 1000 default> -e <encoding gb18030 default> -f <typeofcomparefunction 0 default> -t <threshold 0.55 default> -m <word2vec model file path>
```

参数说明

```
inputfile: 顾名思义，就是待分类的字符串，一行一个字符串，如果是逗号分隔的只取第一个逗号前的字符串
outputfile: 要生成的文件位置
maxcount: 一个文件可能很大，可以设置只提取前面10000个，进行试验性运行，查看结果是否符合要求
encoding：文件的编码类型，默认为gb18030， 因为文件编码也有可能是utf8等
typeofcomparefunction：计算相似度所用的函数类型，
					默认值0为向量余弦计算
					1 edit_distance
					2 jaccard_similarity
					3 tf_similarity
					4 tfidf_similarity
					
threshold： 相似度阈值，可以设置比如大于0.8还是0.55就认为两个句子是相似的，可以调整此值输出不同的分类效果
model_file_path： word2vec 模型文件
```

关键词根提取法更详细的使用说明如下：

```
python secondtest.py -i <inputfile> -o <outputfile> -c <maxcount 1000 default> -e <encoding gb18030 default> -t <topwordscount 8 default> -w <topword> -p <stop file path> -m <max level>
```

参数说明

```
inputfile: 顾名思义，就是待分类的字符串，一行一个字符串，如果是逗号分隔的只取第一个逗号前的字符串
outputfile: 要生成的文件位置
maxcount: 一个文件可能很大，可以设置只提取前面10000个，进行试验性运行，查看结果是否符合要求
encoding：文件的编码类型，默认为gb18030， 因为文件编码也有可能是utf8等
topwordscount： 选取TOP 几个做节点
topword ：需探查的词根，如不输入则使用topwordscount查找词频最高的几个词根
stop_file_path ：STOP词汇所在位置
max_level ：xmind展示几层 默认1
```
[STOPWORDS 下载链接](https://github.com/goto456/stopwords.git)

参考列表

[[1]](https://zhuanlan.zhihu.com/p/179046666)   学会这几点，就可以在百万数据里找到能赚钱的项目

[[2]](https://blog.csdn.net/sinat_26811377/article/details/107492381)   计算2个句子的文本相似度（Python实现）

[[3]](https://cuiqingcai.com/6101.html)   自然语言处理中句子相似度计算的几种方法
