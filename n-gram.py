def reform(sentence):
  if sentence.endswith('.'):
    sentence = sentence[:-1]

  sentence_modify1 = sentence.replace[:1]
  sentence_modify2 = "BOS" + sentence_modify1 + "EOS"
  return sentence_modify2


def compareList(ori_list, test_list):
  count_list = [0] * (len(test_list))
  for i in range(0, len(test_list) - 1):
    for j in range(0, len(ori_list) - 2):
      if test_list[i] == ori_list[j]:
        if test_list[i+1] == ori_list[j+1]:
          count_list[i]+=1
  return count_list
import numpy as np

np.linspace()