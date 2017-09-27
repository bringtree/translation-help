WHAT IS LEFT TO BE UNDERSTOOD IN ATIS?
第一部分：
One of the main data resources used in many studies over the
past two decades for spoken language understanding (SLU) research
in spoken dialog systems is the airline travel information system
(ATIS) corpus. Two primary tasks in SLU are intent determination
(ID) and slot filling (SF). Recent studies reported error rates below
5% for both of these tasks employing discriminative machine learning
techniques with the ATIS test set. While these low error rates
may suggest that this task is close to being solved, further analysis
reveals the continued utility of ATIS as a research corpus. In this paper,
our goal is not experimenting with domain specific techniques or
features which can help with the remaining SLU errors, but instead
exploring methods to realize this utility via extensive error analysis.
We conclude that even with such low error rates, ATIS test set still
includes many unseen example categories and sequences, hence requires
more data. Better yet, new annotated larger data sets from
more complex tasks with realistic utterances can avoid over-tuning
in terms of modeling and feature design. We believe that advancements
in SLU can be achieved by having more naturally spoken data
sets and employing more linguistically motivated features while preserving
robustness due to speech recognition noise and variance due
to natural language.Index Terms— spoken language understanding, ATIS, discriminative
training



One of the main data resources used in many studies over the
past two decades for spoken language understanding (SLU) research
in spoken dialog systems is the airline travel information system
(ATIS) corpus

airline travel information system(简称ATIS)这个数据集是过去20年里被用来做口语识别(简称SLU)研究的
主要数据资源库之一。


Two primary tasks in SLU are intent determination
(ID) and slot filling (SF). Recent studies reported error rates below
5% for both of these tasks employing discriminative machine learning
techniques with the ATIS test set.

SLU的2个重要任务是意图推测(简称ID) 和 槽位填充(简称SF)。
最近的研究表明通过采用机器学习判别技术，能使得机器在测试ATIS这个数据集时错误率低于5%


While these low error rates
may suggest that this task is close to being solved, further analysis
reveals the continued utility of ATIS as a research corpus.
然而这样的低错误率似乎在表明这个任务将要被解决了，进一步分析揭示ATIS作为一个研究的数据集是持续有效的。


In this paper,
our goal is not experimenting with domain specific techniques or
features which can help with the remaining SLU errors, but instead
exploring methods to realize this utility via extensive error analysis

在这篇论文里，我们的目标不是去尝试特定领域的技术或者用剩下的SLU错误的特征(不知道怎么翻译),而是坚持去探索方法通过对错误的广泛分析来意识到功用。

