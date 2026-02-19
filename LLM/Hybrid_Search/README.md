## Hybrid 検索

Dense retrieval（semantic）と Lexical retrieval（keyword）を並行して行い、結果を統合する

#### **Semantic Search (Dense Vector retrieval)**
文章単位でEmbeddingモデルでベクター化

#### **Keyword Search** (転置インデックス/Sparse Vector retrieval)
```text
トークン(ほぼ単語・句)単位でインデックス化  
  ├─ 出現頻度x統計処理 (転置インデックス)  
  │     TF-IDF (Term Frequency - Inverse Document Frequency)  
  │     BM25(TF-IDFへTF飽和＋文書長正規化を導入した改良版)  
  └─ 学習済みモデル (Sparse Vector)  
        BGE-M3 Sparse (多言語対応)  
        SPLADE (Sparse Lexical and Expansion model, 日本語非対応, 日本語派生版もあり)
```

**よくある実装パターン**
```text
クエリは、VectorSearchとBM25Searchで並行して行い、RRFでランクを統合する  
Query [Vector検索] -+- embedding - SemanticSearch[絞り込み] -+-> RRF[絞り込み] -> rerank[文章比較] -> 最終順位
             　　   +- Tokenize  - BM25Search[絞り込み]     -+   
```
