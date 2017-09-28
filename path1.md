#### WHAT IS LEFT TO BE UNDERSTOOD IN ATIS?
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


****
One of the main data resources used in many studies over the
past two decades for spoken language understanding (SLU) research
in spoken dialog systems is the airline travel information system
(ATIS) corpus

```diff
+ airline travel information system(简称ATIS)这个数据集是过去20年里被用来做口语识别(简称SLU)研究的
主要数据资源库之一。
```
```diff
+
```
****
Two primary tasks in SLU are intent determination
(ID) and slot filling (SF). Recent studies reported error rates below
5% for both of these tasks employing discriminative machine learning
techniques with the ATIS test set.
```diff
+ SLU的2个重要任务是意图推测(简称ID) 和 槽位填充(简称SF)。
最近的研究表明通过采用机器学习判别技术，能使得机器在测试ATIS这个数据集时错误率低于5%
```
```diff
+
```

****
While these low error rates
may suggest that this task is close to being solved, further analysis
reveals the continued utility of ATIS as a research corpus.
```diff
+ 然而这样的低错误率似乎在表明这个任务将要被解决了，进一步分析揭示ATIS作为一个研究的数据集是持续有效的。
```
```diff
+
```
****
In this paper,
our goal is not experimenting with domain specific techniques or
features which can help with the remaining SLU errors, but instead
exploring methods to realize this utility via extensive error analysis
```diff
+ 在这篇论文里，我们的目标不是去尝试特定领域的技术或者用剩下的SLU错误的特征(不知道怎么翻译),而是坚持去探索方法通过对错误的广泛分析来意识到功用。
```
```diff
+
```
****
We conclude that even with such low error rates, ATIS test set still
includes many unseen example categories and sequences, hence requires
more data.
```diff
+ 我们得出了这样的结论。即使在如此低的错误率下，ATIS测试集仍然包含了许多不常见的类别和序列的例子，
为此要求我们去获取更多的数据。
```
```diff
+
```
****
Better yet, new annotated larger data sets from
more complex tasks with realistic utterances can avoid over-tuning
in terms of modeling and feature design.
```diff
+ 不过好在，从现实中的复杂的对话任务得到的新的拥有注释的数据集能够避免对模型和特征进行过度调整
```
```diff
+
```
****
We believe that advancements
in SLU can be achieved by having more naturally spoken data
sets and employing more linguistically motivated features while preserving
robustness due to speech recognition noise and variance due
to natural language.
```diff
+ 我们相信SLU的发展能通过拥有更多自然的口语数据集和运用更多的情感语言特征来实现，
同时保留由语音识别噪音的稳定性和由不同原生语言导致的差异。
```
```diff
+
```