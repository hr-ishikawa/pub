
## Hybrid 検索

Vector Search と Keyword Search を並行して行い、結果を統合する

#### **Vector Search** (Dense Vector)
文章単位でLLMモデルでベクター化

#### **Keyword Search** (Sparse Vector)
トークン(ほぼ単語・句)単位でベクター化  
・出現頻度x統計処理 TF-IDF (Term Frequency - Inverse Document Frequency), BM25(TF-IDFの確率モデルによる改良版)  
・学習済みモデル    BGE-M3 Sparse (多言語対応), SPLADE (Sparse Lexical and Expansion model, 日本語非対応, 日本語派生版もあり)  

**よくあるパターン**
```text
クエリは、VectorSearchとBM25Searchで並行して行い、RRFでランクを統合する  
Query [Vector検索] -+- embedding - VectorSearch[絞り込み] -+-> RRF[絞り込み] -> rerank[文章比較] -> 最終順位
             　　   +- Tokenize  - BM25Search[絞り込み]   -+   
```
