# LangChainとLangGraphによるRAG・AIエージェント[実践]入門

https://gihyo.jp/book/2024/978-4-297-14530-9  
https://github.com/GenerativeAgents/agent-book  

## 目次

### 第1章　LLMアプリケーション開発の基礎

#### 1.1　活用され始めた生成AI

#### 1.2　Copilot vs AIエージェント

#### 1.3　すべてはAIエージェントになる

#### 1.4　AIエージェントの知識地図

#### 1.5　まとめ

### 第2章　OpenAIのチャットAPIの基礎

#### 2.1　OpenAIのチャットモデル

- ChatGPTにおける「モデル」
- OpenAIのAPIで使えるチャットモデル
- モデルのスナップショット

#### 2.2　OpenAIのチャットAPIの基本

- Chat Completions API
- Chat Completions APIの料金
- 発生した料金の確認
- COLUMN　GPT-4とGPT-4　Turbo
- COLUMN　Batch API

#### 2.3　入出力の長さの制限や料金に影響する「トークン」

- トークン
- Tokenizerとtiktokenの紹介
- 日本語のトークン数について

#### 2.4　Chat Completions APIを試す環境の準備

- Google Colabとは
- Google Colabのノートブック作成
- OpenAIのAPIを使用するための登録
- OpenAIのAPIキーの準備

#### 2.5　Chat Completions APIのハンズオン

- OpenAIのライブラリ
- Chat Completions APIの呼び出し
- 会話履歴を踏まえた応答を得る
- ストリーミングで応答を得る
- 基本的なパラメータ
- JSONモード
- Vision（画像入力）
- COLUMN　Completions API

#### 2.6　Function calling

- Function callingの概要
- Function callingのサンプルコード
- パラメータ「tool_choice」
- COLUMN　Function callingを応用したJSONの生成
- COLUMN　Structured Outputs

#### 2.7　まとめ

- COLUMN　Assistants API

### 第3章　プロンプトエンジニアリング

#### 3.1　プロンプトエンジニアリングの必要性

- COLUMN　プロンプトエンジニアリングとファインチューニング

#### 3.2　プロンプトエンジニアリングとは

#### 3.3　プロンプトの構成要素の基本

- 題材：レシピ生成AIアプリ..
- プロンプトのテンプレート化
- 命令と入力データの分離
- 文脈を与える
- 出力形式を指定する
- プロンプトの構成要素のまとめ

#### 3.4　プロンプトエンジニアリングの定番の手法

- Zero-shotプロンプティング
- Few-shotプロンプティング
- COLUMN　Few-shotプロンプティングのその他の形式
- Zero-shot Chain of Thoughtプロンプティング

#### 3.5　まとめ.

- COLUMN　マルチモーダルモデルのプロンプトエンジニアリング

### 第4章　LangChainの基礎

#### 4.1　LangChainの概要

- なぜLangChainを学ぶのか
- LangChainの全体像
- LangChainの各種コンポーネントを提供するパッケージ群
- LangChainのインストール
- COLUMN　LangChain v0.1からの安定性の方針
- LangSmithのセットアップ
- LangChainの主要なコンポーネント

#### 4.2　LLM/Chat model

- LLM
- Chat model
- ストリーミング
- LLMとChat modelの継承関係
- LLM/Chat modelのまとめ

#### 4.3　Prompt template

- PromptTemplate
- ChatPromptTemplate
- MessagesPlaceholder
- LangSmithのPrompts
- COLUMN　マルチモーダルモデルの入力の扱い
- Prompt templateのまとめ

#### 4.4　Output parser

- Output parserの概要
- PydanticOutputParserを使ったPythonオブジェクトへの変換
- StrOutputParser
- Output parserのまとめ

#### 4.5　Chain―LangChain Expression Language（LCEL）の概要

- LangChain Expression Language（LCEL）とは
- promptとmodelの連鎖
- StrOutputParserを連鎖に追加
- PydanticOutputParserを使う連鎖
- Chainのまとめ
- COLUMN　with_structured_output

#### 4.6　LangChainのRAGに関するコンポーネント

- RAG（Retrieval-Augmented Generation）
- LangChainのRAGに関するコンポーネントの概要
- Document loader
- Document transformer
- Embedding model
- Vector store..
- COLUMN　4次元以上のベクトルの距離
- LCELを使ったRAGのChainの実装
- LangChainのRAGに関するコンポーネントのまとめ
- COLUMN　Indexing API

#### 4.7　まとめ

- COLUMN　Agent

### 第5章　LangChain Expression Language（LCEL）徹底解説

#### 5.1　RunnableとRunnableSequence―LCELの最も基本的な構成要素

- Runnableの実行方法―invoke・stream・batch
- COLUMN　LCELはどのように実現されているのか
- LCELの「|」でさまざまなRunnableを連鎖させる
- LangSmithでのChainの内部動作の確認.
- COLUMN　なぜLCELが提供されているのか

#### 5.2　RunnableLambda―任意の関数をRunnableにする

- chainデコレーターを使ったRunnableLamdaの実装
- RunnableLambdaへの自動変換
- Runnableの入力の型と出力の型に注意
- COLUMN　独自の関数をstreamに対応させたい場合

#### 5.3　RunnableParallel―複数のRunnableを並列につなげる

- RunnableParallelの出力をRunnableの入力に連結する
- RunnableParallelへの自動変換
- RunnableLambdaとの組み合わせ―itemgetterを使う例

#### 5.4　RunnablePassthrough―入力をそのまま出力する

- assign―RunnableParallelの出力に値を追加する
- COLUMN　astream_events

#### 5.5　まとめ

- COLUMN　Chat historyとMemory
- COLUMN　LangServe

### 第6章　Advanced RAG

#### 6.1　Advanced RAGの概要

#### 6.2　ハンズオンの準備

- COLUMN　インデクシングの工夫

#### 6.3　検索クエリの工夫

- HyDE（Hypothetical Document Embeddings）
- 複数の検索クエリの生成
- 検索クエリの工夫のまとめ

#### 6.4　検索後の工夫

- RAG-Fusion.
- リランクモデルの概要
- Cohereのリランクモデルを使用する準備
- Cohereのリランクモデルの導入
- 検索後の工夫のまとめ

#### 6.5　複数のRetrieverを使う工夫

- LLMによるルーティング
- ハイブリッド検索の例
- ハイブリッド検索の実装
- 複数のRetrieverを使う工夫のまとめ
- COLUMN　生成後の工夫

#### 6.6　まとめ

- COLUMN　マルチモーダルRAG

### 第7章　LangSmithを使ったRAGアプリケーションの評価

#### 7.1　第7章で取り組む評価の概要

- オフライン評価とオンライン評価

#### 7.2　LangSmithの概要

- LangSmithの料金プラン
- LangSmithの機能の全体像

#### 7.3　LangSmithとRagasを使ったオフライン評価の構成例

- Ragasとは
- この章で構築するオフライン評価の構成

#### 7.4　Ragasによる合成テストデータの生成

- Ragasの合成テストデータ生成機能の概要
- パッケージのインストール.
- 検索対象のドキュメントのロード
- Ragasによる合成テストデータ生成の実装
- LangSmithのDatasetの作成
- 合成テストデータの保存
- COLUMN　評価用のデータセットのデータ数.

#### 7.5　LangSmithとRagasを使ったオフライン評価の実装

- LangSmithのオフライン評価の概要
- 利用可能なEvaluator（評価器）
- Ragasの評価メトリクス
- COLUMN　Ragas以外の検索の評価メトリクス
- カスタムEvaluatorの実装
- 推論の関数の実装
- オフライン評価の実装・実行
- オフライン評価の注意点

#### 7.6　LangSmithを使ったフィードバックの収集

- この節で実装するフィードバック機能の概要
- フィードバックボタンを表示する関数の実装
- フィードバックボタンを表示
- COLUMN　Online Evaluator

#### 7.7　フィードバックの活用のための自動処理

- Automation ruleによる処理
- 良い評価のトレースを自動でDatasetに追加する

#### 7.8　まとめ

### 第8章　AIエージェントとは

#### 8.1　AIエージェントのためのLLM活用の期待

#### 8.2　AIエージェントの起源とLLMを使ったAIエージェントの変遷

- LLMベースのAIエージェント
- WebGPT
- Chain-of-Thoughtプロンプティング
- LLMと外部の専門モジュールを組み合わせるMRKL Systems
- Reasoning and Acting（ReAct）
- Plan-and-Solveプロンプティング

#### 8.3　汎用LLMエージェントのフレームワーク

- AutoGPT
- BabyAGI
- AutoGen
- crewAI
- crewAIのユースケース

#### 8.4　マルチエージェント・アプローチ.

- マルチエージェントの定義
- マルチエージェントでText-to-SQLの精度を上げる
- マルチエージェントでソフトウェア開発を自動化する

#### 8.5　AIエージェントが安全に普及するために

#### 8.6　まとめ

### 第9章　LangGraphで作るAIエージェント実践入門

#### 9.1　LangGraphの概要

- LangGraphとは何か
- LangGraphにおけるグラフ構造アプローチ

#### 9.2　LangGraphの主要コンポーネント

- ステート：グラフの状態を表現
- ノード：グラフを構成する処理の単位
- エッジ：ノード間の接続
- コンパイル済みグラフ

#### 9.3　ハンズオン：Q&Aアプリケーション

- LangChainとLangGraphのインストール.
- OpenAI APIキーの設定
- ロールの定義
- ステートの定義
- Chat modelの初期化
- ノードの定義
- グラフの作成
- ノードの追加
- エッジの定義
- 条件付きエッジの定義
- グラフのコンパイル
- グラフの実行
- 結果の表示
- COLUMN　グラフ構造をビジュアライズして表示する
- COLUMN　LangSmithによるトレース結果

#### 9.4　チェックポイント機能：ステートの永続化と再開

- チェックポイントのデータ構造
- ハンズオン：チェックポイントの動作を確認する

#### 9.5　まとめ

### 第10章　要件定義書生成AIエージェントの開発

#### 10.1　要件定義書生成AIエージェントの概要

- 要件定義とは何か
- 先行研究のアプローチを参考にする
- LangGraphのワークフローとして設計する

#### 10.2　環境設定

#### 10.3　データ構造の定義

#### 10.4　主要コンポーネントの実装

- PersonaGenerator
- InterviewConductor
- InformationEvaluator
- RequirementsDocumentGenerator

#### 10.5　ワークフロー構築

#### 10.6　エージェントの実行と結果の確認

#### 10.7　全体のソースコード

#### 10.8　まとめ

### 第11章　エージェントデザインパターン

#### 11.1　エージェントデザインパターンの概要

- デザインパターンとは
- エージェントデザインパターンが解決する課題領域
- エージェントデザインパターンの位置付け

#### 11.2　18のエージェントデザインパターン

- エージェントデザインパターンの全体図
- 1. パッシブゴールクリエイター（Passive Goal Creator）
- 2. プロアクティブゴールクリエイター（Proactive Goal Creator）
- 3. プロンプト／レスポンス最適化（Prompt/Response Optimizer）
- 4. 検索拡張生成（Retrieval-Augmented Generation：RAG）
- 5. シングルパスプランジェネレーター（Single-Path Plan Generator）.
- 6. マルチパスプランジェネレーター（Multi-Path Plan Generator）
- 7. セルフリフレクション（Self-Reflection）
- 8. クロスリフレクション（Cross-Reflection）
- 9. ヒューマンリフレクション（Human-Reflection）
- 10. ワンショットモデルクエリ（One-Shot Model Querying）
- 11. インクリメンタルモデルクエリ（Incremental Model Querying）
- 12. 投票ベースの協調（Voting-Based Cooperation）
- 13. 役割ベースの協調（Role-Based Cooperation）
- 14. 議論ベースの協調（Debate-Based Cooperation）
- 15. マルチモーダルガードレール（Multimodal Guardrails）
- 16. ツール／エージェントレジストリ（Tool/Agent Registry）
- 17. エージェントアダプター（Agent Adapter）
- COLUMN　LangChainのTool機能
- 18. エージェント評価器（Agent Evaluator）

#### 11.3　まとめ

### 第12章　LangChain/LangGraphで実装するエージェントデザインパターン

#### 12.1　本章で扱うエージェントデザインパターン

#### 12.2　環境設定

- 各パターンの実装コードの掲載について

#### 12.3　パッシブゴールクリエイター（Passive Goal Creator）

- 実装内容の解説
- COLUMN　Settingsクラスについて
- 実行結果

#### 12.4　プロンプト／レスポンス最適化（Prompt/Response Optimizer）

- 実装内容の解説
- プロンプト最適化
- レスポンス最適化

#### 12.5　シングルパスプランジェネレーター（Single-Path Plan Generator）

- 実装内容の解説
- COLUMN　タスクの並列実行への対応方法
- COLUMN　LangGraphのcreate_react_agent関数の解説
- 実行結果

#### 12.6　マルチパスプランジェネレーター（Multi-Path Plan Generator）

- 実装内容の解説
- COLUMN　実装の発展
- 実行結果

#### 12.7　セルフリフレクション（Self-Reflection）

- 実装内容の解説
- COLUMN　Faissとは
- 実行結果

#### 12.8　クロスリフレクション（Cross-Reflection）

- 実装内容の解説
- 実行結果

#### 12.9　役割ベースの協調（Role-Based Cooperation）

- 実装内容の解説
- 実行結果

#### 12.10　まとめ

### 付録　各種サービスのサインアップと第12章の各パターンの実装コード

#### A.1　各種サービスのサインアップ

- LangSmithのサインアップ
- Cohereのサインアップ
- Anthropicのサインアップ

#### A.2　第12章の各パターンの実装コード

- 1. パッシブゴールクリエイター（Passive Goal Creator）
- 2. プロンプト／レスポンス最適化（Prompt/Response Optimizer）
- 3. シングルパスプランジェネレーター（Single-Path Plan Generator）
- 4. マルチパスプランジェネレーター（Multi-Path Plan Generator）
- 5. セルフリフレクション（Self-Reflection）
- 6. クロスリフレクション（Cross-Reflection）
- 7. 役割ベースの協調（Role-Based Cooperation）
