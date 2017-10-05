With advances in machine learning over the last decade, especially in discriminative classification techniques, researchers have framed the ID problem as a sample classification task and SF as a sequence classification task. Typically, word n-grams are used as features after preprocessing with generic entities, such as dates, locations, or phone numbers. Because of the very large dimension of the input space, large margin classifiers such as SVMs [11] or Adaboost[12] were found to be very good candidates for ID and CRFs [13] for SF. To take into account context, the recent trend is to match n-grams (a substring of n words) rather than words.

As discovered, data driven approaches are very well-suited for processing spontaneous spoken utterances. The data driven approaches are typically more robust to sentences that are not well-formed grammatically, which occurs frequently in spontaneous speech. Even in broadcast conversations where participants are very well trained and prepared, a large percentage of the utterances have disfluencies: rep- etitions, false starts, and filler words (e.g., uh) [14]. Furthermore, speech recognition introduces significant “noise” to the SLU com- ponent caused by background noise, mismatched domains, incor- rect recognition of proper names (such as city or person names), and reduced accuracy due to sub-real time processing requirements. A typical call routing system operates at around 20%-30% word error rate; one out of every three to five words is wrong [15]. Given that the researchers in this study also determined that one third of the ID errors are due to speech recognition noise, robust methods for spontaneous speech recognition are critically important for successful ID and SF in SLU systems. To this end, researchers have proposed many methods ranging from N-best rescoring, exploiting word confusion networks, and leveraging dialog context as prior knowledge (e.g., [15]).

伴随着机器学习在过去十年的发展，特别是判别分类技术，研究人员把ID问题当作是一个样本分类任务和
把SF当作是一个序列分类任务。通常在对通用实体(如数据，地点和电话号码)进行预加工后，
使用n-grams作为特征。由于输入空间的维度非常大，所以发现像SVMs和adaboost这类的大型边缘分类器
在ID问题上能取得很好的效果，另外对于SF，CRFs也能如此。为了联系语境的上下文，最近的趋势是使用由n个单词组成的字符串的n-grams来匹配
而不是基于单词。
正如发现的那样，数据驱动方法非常适合处理自发性口语.数据驱动的方法通常在那些语法不完善的语句能表现出好的效果，
这种情况在自发性口语中经常发生。即使在广播对话中,参与者们都训练有素和做好足够的准备，但是仍然有大部分的话语
被不利的因素所影响。如重复，错误的开始和填词（像uh）。
此外，语音识别会把显著的噪音引入到SLU模块，这些噪音包括了背景噪音，错误的域，错误的专有名词（像城市，人名）。
还有语音识别会由于时间的要求而被导致识别的准确率下降。
一个普通的路由呼叫系统在运行时会有20%-30%的单词识别错误。每3到5个单词中会有1个是识别错误的。
在本研究中，研究人员还确定了三分之一的错误是由于识别噪音造成的。
鲁棒性强的自发性口语识别的方法对ID和SF在SLU系统中的成功识别发挥地重要的作用。
为止，研究者们已经提出了更多的方法，像N-best重打分算法，词混淆网络和利用对话框上下文作为先验知识的方法。