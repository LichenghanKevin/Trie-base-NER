# Trie_base_NER
基於中文字典構建trie tree， 加速 Dictionary-based NER

# 使用方法

```python
from NER_Tree import *

# Load dictionary data and construct trie tree
Trie_tree = LoadData("./dictionary.txt")


sentence = "顏面部撕裂傷，騎車汽車發生車禍致鼻樑撕裂傷"
NER_output = tokenize(Trie_tree, sentence)
print(NER_output)
```
