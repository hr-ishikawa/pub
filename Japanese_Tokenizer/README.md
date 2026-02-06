## 日本語Tokenizer / 形態素解析

### 1. Janome
```pyton
# pip install janome
from janome.tokenizer import Tokenizer
from pprint import pprint

# Janomeのインスタンス化
tokenizer = Tokenizer()

text = '今日は、良い天気です。'
tokens = tokenizer.tokenize(text)
pprint([(t.surface, t.part_of_speech) for t in tokens])
```
### 2. Sudachi
```pyton
# pip install SudachiPy sudachidict_core
from sudachipy import Dictionary
from pprint import pprint

# Sudachiのインスタンス化
tokenizer = Dictionary().create()

text = '今日は、良い天気です。'
tokens = tokenizer.tokenize(text)
pprint([(t.surface(), t.part_of_speech()) for t in tokens])
```
