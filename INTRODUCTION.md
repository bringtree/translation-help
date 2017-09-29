Spoken language understanding (SLU) aims to extract the meaning
of the speech utterances. While understanding language is still considered
an unsolved problem, in the last decade, a variety of practical
goal-oriented conversational understanding systems have been built
for limited domains. These systems aim to automatically identify the
intent of the user as expressed in natural language, extract associated
arguments or slots, and take actions accordingly to satisfy the user’s
requests. In such systems, the speaker’s utterance is typically recognized
using an automatic speech recognizer (ASR).  Then the intent
of the speaker is identified from the recognized word sequence using
an SLU component. Finally, a dialog or task manager (DM) interacts
with the user (not necessarily in natural language) and helps the
user achieve the task that the system is designed to support.

****
Spoken language understanding (SLU) aims to extract the meaning
of the speech utterances.
```diff
+ SLU的目的是提取出语音的意思。
```

****
While understanding language is still considered
an unsolved problem, in the last decade, a variety of practical
goal-oriented conversational understanding systems have been built
for limited domains.
```diff
+ 虽然理解语言仍然是被当作一个未解决的问题，但是在过去十年里，
各种实用的面向用户交流和理解的系统在一些的领域已经被建立
```

****
These systems aim to automatically identify the
intent of the user as expressed in natural language, extract associated
arguments or slots, and take actions accordingly to satisfy the user’s
requests.
```diff
+ 这些系统旨在自动地辨认当用户表达自然语言的意图，获取语句间或者槽位间的联系，
同时采取行动来满足用户的请求。
```

****
In such systems, the speaker’s utterance is typically recognized
using an automatic speech recognizer (ASR).
```diff
+ 在这样的系统里，通常使用一个自动语音识别器（ASR）来识别说话者的言语。
```

****
Then the intent of the speaker is identified from the recognized word sequence using
an SLU component.
```diff
+ 获取语句的联系或者槽位的联系，同时根据用户请求的满意度采取行动
```

****
In such systems, the speaker’s utterance is typically recognized
using an automatic speech recognizer (ASR).

```diff
+ 在这样的系统里，通常使用一个自动语音识别器（ASR）来识别说话者的语言
```

****
Then the intent of the speaker is identified
from the recognized word sequence using an SLU component.
```diff
+ 然后使用SLU的组件根据已经认识的单词序列来识别说话者的意图
```

****
Finally, a dialog or task manager (DM) interacts with
the user (not necessarily in natural language)
and helps the user achieve the task that the system is designed to support.
```diff
+ 最后，对话框或者任务管理（DM）与用户(不一定是自然语言) 交互，
并帮助用户实现这个系统被设计支持好的任务。
```

In the early 90s, DARPA (Defense Advanced Research Program
Agency) initiated the Airline Travel Information System (ATIS) project.
The ATIS task consisted of spoken queries on flight-related information.
An example utterance is I want to fly to Boston from New
York next week. Understanding was reduced to the problem of extracting
task-specific arguments, such as Destination and Departure
Date. Participating systems employed either a data-driven statistical
approach [1, 2] or a knowledge-based approach [3, 4, 5].

****
In the early 90s, DARPA (Defense Advanced Research Program Agency)
initiated the Airline Travel Information System (ATIS) project.
```diff
+ 在90年代的早期，DARPA（国防高级研究计划署）开始ATIS（航空旅行信息系统）的项目。
```

****
The ATIS task consisted of spoken queries on flight-related information.
```diff
+ ATIS任务由与飞机相关的信息口语询问组成。
```

****
An example utterance is I want to fly to Boston from New York next week.
```diff
+ 下个星期，我想坐飞机从波斯顿到纽约。就是一个典型的口语询问例子。
```

****
Understanding was reduced to the problem of extracting task-specific arguments,
such as Destination and Departure Date.
```diff
+ 理解从问题中筛选出的与特定任务有关的参数，例如:目的地和出发时间、
```

****
Participating systems employed either a data-driven statistical approach [1, 2]
or a knowledge-based approach [3, 4, 5].
```diff
+ 参与的系统采用以数据驱动的统计方法方法[1,2] 或者 是基于知识库的方法[3,4,5]
```

Almost simultaneously with the semantic frame filling-based
SLU approaches, a new task emerged motivated by the success of
the early commercial interactive voice response (IVR) applications
used in call centers. The SLU was framed as classifying users’ utterances
into predefined categories (called as intents or call-types) [6].

****
```diff
+ 大多数的
```