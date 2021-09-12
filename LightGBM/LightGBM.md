## **Table of Contents**

- **Parameters Tuning**
  - **Tune Parameters for the Leaf-wise (Best-first) Tree**
- **Data Structure API**
  - **lightgbm.Dataset**
- **Training API**
  - **lightgbm.cv**
- **ploting**
  - **lightgbm.plot_importance**

- - - 

## **Parameters Tuning**

https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html

### **Tune Parameters for the Leaf-wise (Best-first) Tree**

LightGBM は、リーフワイズ木成長アルゴリズムを使用していますが、他の多くの一般的なツールは、深度ワイズ木成長を使用しています。深さ方向の木の成長に比べて、葉の方向のアルゴリズムははるかに速く収束することができます。しかし、適切なパラメータを使用しないと、葉の成長はオーバーフィッティングになる可能性があります。

リーフワイズツリーを使って良い結果を得るために、以下の重要なパラメータがあります。

1. **num_leaves. num_leaves** これは木のモデルの複雑さをコントロールするための主要なパラメータです。理論的には、**num_leaves = 2^(max_depth)** と設定すれば、深さ方向の木と同じ数の葉を得ることができます。しかし、この単純な変換は実際には良くない。その理由は、leaf-wise treeは通常、一定の葉の数に対してdepth-wise treeよりもはるかに深いからである。制約のない深さは、オーバーフィッティングを誘発する可能性があります。したがって、**num_leaves**を調整しようとするときには、**2^(max_depth)** よりも小さくなるようにするべきである。例えば、**max_depth=7**の場合、depth-wise木は良い精度を得ることができますが、**num_leaves**を**127**に設定するとオーバーフィッティングを引き起こす可能性があり、**70**または**80**に設定するとdepth-wiseよりも良い精度を得ることができます。

2. **min_data_in_leaf**。これは、リーフワイズツリーでのオーバーフィッティングを防ぐための非常に重要なパラメータです。その最適な値は、学習サンプルの数と **num_leaves** に依存します。大きな値を設定することで、深すぎる木の成長を避けることができますが、アンダーフィッティングを引き起こす可能性があります。実際には、大規模なデータセットでは数百から数千に設定すれば十分である。

3. **max_depth. max_depth**を使って、木の深さを明示的に制限することもできます。

### **For Faster Speed**

#### **Add More Computational Resources**

OpenMP が利用可能なシステムでは、LightGBM は多くの処理を並列化するために OpenMP を使用します。LightGBM が使用するスレッドの最大数は、パラメータ **num_threads** によって制御されます。デフォルトでは、OpenMP のデフォルトの動作（実際の CPU コアごとに 1 つのスレッド、または環境変数 **OMP_NUM_THREADS** が設定されている場合はその値）に従います。最高のパフォーマンスを得るためには、利用可能な実CPUコアの数を設定してください。

利用可能なCPUコア数が多いマシンに移行することで、より高速なトレーニングが可能になる場合があります。

また、分散型（マルチマシン）トレーニングを使用すると、トレーニング時間を短縮できる場合があります。詳細は「分散学習ガイド」を参照してください。

### **Use a GPU-enabled version of LightGBM**

You might find that training is faster using a GPU-enabled build of LightGBM. See the GPU Tutorial for details.

GPU 対応の LightGBM を使用すると、トレーニングが速くなる場合があります。詳細については、GPUチュートリアルを参照してください。

### **Grow Shallower Trees**

OpenMP が利用可能なシステムでは、LightGBM は多くの処理を並列化するために OpenMP を使用します。LightGBM が使用するスレッドの最大数は、パラメータ num_threads によって制御されます。デフォルトでは、OpenMP のデフォルトの動作（実際の CPU コアごとに 1 つのスレッド、または環境変数 OMP_NUM_THREADS が設定されている場合はその値）に従います。最高のパフォーマンスを得るためには、利用可能な実CPUコアの数を設定してください。

利用可能なCPUコア数が多いマシンに移行することで、より高速なトレーニングが可能になる場合があります。

また、分散型（マルチマシン）トレーニングを使用すると、トレーニング時間を短縮できる場合があります。詳細は「分散学習ガイド」を参照してください。

#### **GPU対応のLightGBMを使用する**。

GPU 対応の LightGBM を使用すると、トレーニングが速くなる場合があります。詳細については、GPUチュートリアルを参照してください。


#### **Grow Shallower Trees**（浅い木を育てる）。

LightGBM の合計トレーニング時間は、追加されるツリーノードの総数に応じて増加します。LightGBM には、ツリーのノード数を制御するために使用できるいくつかのパラメータがあります。

以下の提案は、トレーニングを高速化しますが、トレーニングの精度が低下する可能性があります。

#### **max_depth**を減少させる

このパラメータは、各ツリーのルートノードとリーフノードの間の最大距離を制御する整数です。学習時間を短縮するには**max_depth**を小さくする。

#### **num_leaves**を減少させる

LightGBM は、深さに関係なく、ノードを追加することで得られる利益に基づいてツリーにノードを追加します。機能説明書の図は、このプロセスを示しています。
決定木の連続した3つの画像で、それぞれが2つのリーフノードを追加した木を示しています。リーフ単位での成長により、他よりも長いブランチを持つツリーができることを示しています。

このような成長戦略のため、木の複雑さを制限するために **max_depth** だけを使用するのは簡単ではありません。**num_leaves** パラメータは、木の最大ノード数を設定します。**num_leaves**を小さくすると、トレーニング時間が短縮されます。

#### **min_gain_to_split**を増やします

新しいツリーノードを追加する際、LightGBM は最大のゲインを持つ分割ポイントを選択します。ゲインとは、基本的に、分割点を追加したことによるトレーニング損失の減少のことです。デフォルトでは、LightGBM は **min_gain_to_split** を 0.0 に設定しており、これは「小さすぎる改善はない」ことを意味します。しかし、実際には、学習損失の非常に小さな改善がモデルの汎化誤差に意味のある影響を与えないことがあるかもしれません。学習時間を短縮するために、**min_gain_to_split**を増やす。

#### **min_data_in_leaf**と**min_sum_hessian_in_leaf**を増やします 

トレーニングデータのサイズや特徴の分布によっては、LightGBM が少数のオブザベーションしか記述していないツリーノードを追加する可能性があります。最も極端な例として、トレーニングデータから1つのオブザベーションのみが該当するツリーノードを追加することを考えてみましょう。これはうまく一般化できない可能性が高く、おそらくオーバーフィッティングの兆候です。

これは、**max_depth** や **num_leaves** などのパラメータで間接的に防ぐことができますが、LightGBM には、このような過度に特定されたツリーノードの追加を直接防ぐためのパラメータもあります。

- **min_data_in_leaf**（ミニデータ・イン・リーフ）。ツリーノードを追加するために、ツリーノードに入る必要のあるオブザベーションの最小数。

- **min_sum_hessian_in_leaf**: min_sum_hessian_in_leaf: 葉の中のオブザベーションのヘシアン（各オブザベーションについて評価された目的関数の2次導関数）の最小和。いくつかの回帰目的では、これは単に各ノードに入らなければならないレコードの最小数です。分類目的の場合、これは確率の分布の合計を表します。このパラメータの値をどのように推論するかについては、Stack Overflowの回答を参照してください。

### **Grow Less Trees**

#### **num_iterations**の減少

**num_iterations** パラメータは、実行されるブースティング ラウンドの数を制御します。LightGBM は学習者として決定木を使用するため、これは「木の数」と考えることもできます。

**num_iterations** を変更する場合は、**learning_rate** も変更してください。**learning_rate** は、学習時間には影響しませんが、学習精度には影響します。一般的なルールとして、**num_iterations**を減らした場合、**learning_rate**を増やすべきです。

num_iterationsとlearning_rateの適切な値の選択は、データと目的に大きく依存するため、これらのパラメータはハイパーパラメータ・チューニングによって、可能な値のセットから選択されることが多いです。

**num_iterations**を小さくすると、トレーニング時間を短縮できます。

#### **Use Early Stopping**

早期停止を有効にした場合、各ブーストラウンドの後、モデルの学習精度は、学習プロセスで利用できなかったデータを含む検証セットに対して評価されます。その精度は、前回のブースティングラウンドの精度と比較されます。モデルの精度が一定の回数連続して向上しない場合、LightGBM はトレーニングプロセスを停止します。

この「連続したラウンド数」は、パラメータ **early_stopping_rounds** によって制御されます。たとえば、**early_stopping_rounds=1** の場合、「検証セットの精度が初めて向上しなかった場合、トレーニングを停止する」となります。

early_stopping_roundsを設定し、検証セットを用意することで、トレーニング時間を短縮できる可能性があります。

#### **Consider Fewer Splits**

前のセクションで説明したパラメータは、何本の木を構築するか、木ごとに何個のノードを構築するかを制御します。木のノードをモデルに追加するのに必要な時間を短縮することで、トレーニング時間をさらに短縮することができます。

以下の提案は、トレーニングを高速化しますが、トレーニングの精度を損なう可能性があります。

#### **Enable Feature Pre-Filtering When Creating Dataset**

デフォルトでは、LightGBM **Dataset** オブジェクトが構築されると、**min_data_in_leaf** の値に基づいて、一部のフィーチャーがフィルタリングされます。

簡単な例として、1000 件の観測データセットに feature_1 という特徴があるとします。feature_1 には、25.0（995 件）と 50.0（5 件）の 2 つの値しかありません。min_data_in_leaf = 10の場合、この特徴に対する分割はなく、少なくとも1つのリーフノードが5つのオブザベーションしか持たない有効な分割になります。

LightGBM は、この特徴を再検討して反復ごとに無視するのではなく、トレーニング前に **Dataset** を構築する際にこの特徴をフィルタリングします。

**feature_pre_filter=False** を設定してこのデフォルトの動作をオーバーライドしている場合は、**feature_pre_filter=True** を設定してトレーニング時間を短縮します。

#### データセットの作成時に**max_bin**または**max_bin_by_feature**を減らす

LightGBM のトレーニングでは、トレーニングの速度を向上させ、トレーニングに必要なメモリを削減するために、連続的な特徴を離散的なビンにバケットします。このビン分けは、**Dataset**の構築時に一度だけ行われます。ノードを追加する際に考慮される分割数は **O(#feature * #bin)** であるため、特徴ごとのビンの数を減らすことで、評価が必要な分割数を減らすことができます。

**max_bin** は、フィーチャーがバケット化されるビンの最大数を制御します。**max_bin_by_feature**を渡すことで、フィーチャーごとにこの最大数を設定することも可能です。

**max_bin**または**max_bin_by_feature**を減らすことで、トレーニング時間を短縮することができます

#### データセット作成時に**min_data_in_bin**を増やす

いくつかのビンは、少数のオブザベーションを含むかもしれません。それは、可能な分割ポイントとしてそのビンの境界を評価する努力が、最終的なモデルをあまり変えないことを意味するかもしれません。**min_data_in_bin**を設定することで、ビンの粒度をコントロールすることができます。

**min_data_in_bin** を大きくすると、トレーニング時間が短縮されます。

#### **feature_fraction の減少**

デフォルトでは、LightGBM はトレーニング プロセス中に **Dataset** のすべてのフィーチャを考慮します。この動作は、**feature_fraction** を **0 以上かつ 1.0 未満の値**に設定することで変更できます。たとえば、**feature_fraction** を **0.5** に設定すると、LightGBM は各ツリーを構築する最初の段階で、50% のフィーチャーをランダムに選択します。これにより、各ツリーノードを追加するために評価しなければならないスプリットの合計数が減少します。

トレーニング時間を短縮するには、**feature_fraction** を減らします。

#### **max_cat_threshold** を減らす。

LightGBM は、カテゴリ特徴の最適な分割を見つけるために、カスタム アプローチを使用します。このプロセスでは、LightGBM はカテゴリ特徴を 2 つのグループに分ける分割を検討します。このような分割は、「k-vs.-rest」分割と呼ばれることがあります。max_cat_threshold の値が大きいほど、分割ポイントが多くなり、探索するグループのサイズが大きくなります。

max_cat_thresholdを小さくすると、トレーニング時間が短縮されます。

### Use Less Data

#### Use Bagging

デフォルトでは、LightGBM は各反復においてトレーニングデータのすべてのオブザベーションを使用します。その代わりに、LightGBM にトレーニングデータをランダムにサンプリングするように指示することができます。このように、複数のランダムなサンプルを交換せずに学習するプロセスを「バギング」と呼びます。

デフォルトでは、LightGBM は各反復においてトレーニングデータのすべてのオブザベーションを使用します。その代わりに、LightGBM にトレーニングデータをランダムにサンプリングするように指示することができます。このように、複数のランダムなサンプルを交換せずに学習するプロセスを「バギング」と呼びます。

**bagging_freq** を 0 より大きい整数に設定して、新しいサンプルを抽出する頻度を制御します。**bagging_fraction**に**0.0以上1.0未満**の値を設定して、サンプルの大きさを制御します。例えば、**{"bagging_freq": 5, "bagging_fraction": 0.75}**は、LightGBMに「5回の反復ごとに置き換えなしで再サンプルし、トレーニングデータの75%のサンプルを抽出する」と指示します。

学習時間を短縮するには、**bagging_fraction** を小さくします。

#### 構築したデータセットを**save_binary** で保存します。

これは、LightGBM CLI にのみ適用されます。パラメータ **save_binary** を渡すと、トレーニングデータセットとすべての検証セットが、LightGBM が理解できるバイナリ形式で保存されます。これにより、データセットの構築時に行われたビン化やその他の作業を再度行う必要がないため、次回のトレーニングを高速化できます。

#### 精度向上のために

- 大きな **max_bin** を使用する（速度が低下する可能性があります）。
- 小さなl**earning_rate**と大きな**num_iterations**を使用する。
- **num_leaves**を大きくする(オーバーフィッティングを起こす可能性がある)
- 大きな学習データを使う
- dartを試す

#### オーバーフィッティングへの対処

- 小さな**max_bin**を使う
- 小さな**num_leaves**を使う
- **min_data_in_leaf** と **min_sum_hessian_in_leaf** を使う。
- **bagging_fraction** と **bagging_freq** を設定して bagging を使用する。
- **feature_fraction** を設定して、特徴のサブサンプリングを行う。
- 大きな学習データを使う
- 正則化に**lambda_l1**, **lambda_l2**, **min_gain_to_split**を使う。
- 深層木の成長を避けるために**max_depth**を試す
- **extra_trees**を試す
- **path_smooth**を増やしてみる

<br>

## **Data Structure API**

### **lightgbm.Dataset**

https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.Dataset.html#lightgbm.Dataset

lightgbm.Dataset (data, label=None, reference=None, weight=None, group=None, init_score=None, silent='warn', feature_name='auto', categorical_feature='auto', params=None, free_raw_data=True)


|Param|Desc|説明|
|-----|----|----|
|data<br> (str, pathlib.Path, numpy array, pandas DataFrame, H2O DataTable's Frame, scipy.sparse, Sequence, list of Sequence or list of numpy array)|Data source of Dataset. If str or pathlib.Path, it represents the path to a text file (CSV, TSV, or LibSVM) or a LightGBM Dataset binary file.|データセットのデータソースです。str または pathlib.Path の場合，テキストファイル（CSV, TSV, LibSVM）または LightGBM Dataset のバイナリファイルへのパスを表します．|
|label<br> (list, numpy 1-D array, pandas Series / one-column DataFrame or None, optional (default=None))|Label of the data.|データのラベルを指定します。|
|reference<br> (Dataset or None, optional (default=None))|If this is Dataset for validation, training data should be used as reference.|これが検証用のDatasetであれば、トレーニングデータを参照として使用する必要があります。|
|weight<br> (list, numpy 1-D array, pandas Series or None, optional (default=None))|Weight for each instance.|各インスタンスの重みです。|
|group<br> (list, numpy 1-D array, pandas Series or None, optional (default=None))|Group/query data. Only used in the learning-to-rank task. sum(group) = n_samples. For example, if you have a 100-document dataset with group = [10, 20, 40, 10, 10, 10], that means that you have 6 groups, where the first 10 records are in the first group, records 11-30 are in the second group, records 31-70 are in the third group, etc.|グループ/クエリデータ。sum(group) = n_samples となります。例えば、100文書のデータセットでgroup = [10, 20, 40, 10, 10, 10]の場合、6つのグループがあり、最初の10レコードが第1グループ、11～30レコードが第2グループ、31～70レコードが第3グループ、ということになります。|
|init_score<br> (list, numpy 1-D array, pandas Series or None, optional (default=None))|Init score for Dataset.)|Datasetの初期スコアです。|
|silent<br> (bool, optional (default=False))|Whether to print messages during construction.|作業中にメッセージを表示するかどうか。|
|feature_name<br> (list of str, or 'auto', optional (default="auto"))|Feature names. If ‘auto’ and data is pandas DataFrame, data columns names are used.|フィーチャー名。auto'でデータがpandas DataFrameの場合は、データのカラム名が使われます。|
|categorical_feature<br> (list of str or int, or 'auto', optional (default="auto"))|Categorical features. If list of int, interpreted as indices. If list of str, interpreted as feature names (need to specify feature_name as well). If ‘auto’ and data is pandas DataFrame, pandas unordered categorical columns are used. All values in categorical features should be less than int32 max value (2147483647). Large values could be memory consuming. Consider using consecutive integers starting from zero. All negative values in categorical features will be treated as missing values. The output cannot be monotonically constrained with respect to a categorical feature.|カテゴリー的特徴です。intのリストの場合、インデックスとして解釈されます。str のリストの場合、フィーチャー名として解釈されます（feature_name も指定する必要があります）。auto」でデータがpandas DataFrameの場合、pandas unordered categorical columnsが使用されます。カテゴリカルフィーチャーのすべての値は、int32の最大値（2147483647）未満でなければなりません。大きな値はメモリを消費する可能性があります。ゼロから始まる連続した整数の使用を検討してください。カテゴリー機能の負の値はすべて欠損値として扱われます。出力は、カテゴリー特徴に対して単調に制約されることはありません。|
|params<br> (dict or None, optional (default=None))|Other parameters for Dataset.)|Datasetのその他のパラメータ。|
|free_raw_data<br> (bool, optional (default=True))|If True, raw data is freed after constructing inner Dataset.|Trueの場合、内部のDatasetを構築した後に生データを解放します。|

<br>

## **Training API**

### **lightgbm.train**

https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.train.html

### **lightgbm.cv**

https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.cv.html

lightgbm.cv (params, train_set, num_boost_round=100, folds=None, nfold=5, stratified=True, shuffle=True, metrics=None, fobj=None, feval=None, init_model=None, feature_name='auto', categorical_feature='auto', early_stopping_rounds=None, fpreproc=None, verbose_eval=None, show_stdv=True, seed=0, callbacks=None, eval_train_metric=False, return_cvbooster=False)

|Param|Desc|説明|
|-----|----|----|
|params (dict)|Parameters for Booster.|Boosterのパラメータ。|
|train_set (Dataset)|Data to be trained on.|学習対象のデータ。|
|num_boost_round (int, optional (default=100))|Number of boosting iterations.|ブースティングの反復回数。|
|folds (generator or iterator of (train_idx, test_idx) tuples, scikit-learn splitter object or None, optional (default=None))|If generator or iterator, it should yield the train and test indices for each fold. If object, it should be one of the scikit-learn splitter classes (https://scikit-learn.org/stable/modules/classes.html#splitter-classes) and have split method. This argument has highest priority over other data split arguments.|generator or iteratorの場合は、各foldのtrainとtestのインデックスを生成する必要があります。オブジェクトの場合は，scikit-learn splitter クラス (https://scikit-learn.org/stable/modules/classes.html#splitter-classes) の一つであり，split メソッドを持つ必要があります．この引数は，他のデータ分割引数よりも優先されます．|
|nfold (int, optional (default=5))|Number of folds in CV.|CV内のフォールドの数．|
|stratified (bool, optional (default=True))|Whether to perform stratified sampling.|層化サンプリングを行うかどうか。|
|shuffle (bool, optional (default=True))|Whether to shuffle before splitting data.|データを分割する前にシャッフルするかどうか。|
|metrics (str, list of str, or None, optional (default=None))|Evaluation metrics to be monitored while CV. If not None, the metric in params will be overridden.|CV中にモニターする評価指標。Noneでない場合は、params内のメトリックがオーバーライドされます。|
|fobj (callable or None, optional (default=None))|Customized objective function. Should accept two parameters: preds, train_data, and return (grad, hess).|カスタマイズされた目的関数。2つのパラメータ（preds, train_data）とリターン（grad, hess）を受け取る必要があります。|
|- preds: list or numpy 1-D array|The predicted values. Predicted values are returned before any transformation, e.g. they are raw margin instead of probability of positive class for binary task.|予測値は変換される前の値が返されます。例えば、バイナリタスクの正クラスの確率の代わりに生のマージンが返されます。|
|- train_data: Dataset|The training dataset.|トレーニングデータセット。|
|- grad: list or numpy 1-D array|The value of the first order derivative (gradient) of the loss with respect to the elements of preds for each sample point.|各サンプルポイントの preds の要素に対する損失の一階微分（グラディエント）の値。|
|- hess: list or numpy 1-D array|The value of the second order derivative (Hessian) of the loss with respect to the elements of preds for each sample point.|各サンプルポイントの preds の要素に対する損失の二階微分（ヘシアン）の値。|
||For multi-class task, the preds is group by class_id first, then group by row_id. If you want to get i-th row preds in j-th class, the access way is score[j * num_data + i] and you should group grad and hess in this way as well.|マルチクラスタスクの場合、predsはまずclass_idでグループ化され、次にrow_idでグループ化されます。j番目のクラスのi行目のpredsを取得したい場合、アクセス方法はscore[j * num_data + i]であり、gradとhessもこの方法でグループ化する必要があります。|
|feval (callable, list of callable, or None, optional (default=None))|Customized evaluation function. Each evaluation function should accept two parameters: preds, train_data, and return (eval_name, eval_result, is_higher_better) or list of such tuples.|カスタマイズされた評価関数。各評価関数は2つのパラメータ: preds, train_dataを受け取り，(eval_name, eval_result, is_higher_better)を返すか，そのようなタプルのリストを返さなければならない．|
|- preds: list or numpy 1-D array|The predicted values. If fobj is specified, predicted values are returned before any transformation, e.g. they are raw margin instead of probability of positive class for binary task in this case.|リストまたは numpy の 1-D 配列|予測される値．fobjが指定された場合、予測値は変換前の値が返されます。例えば、このケースでは、バイナリタスクの正クラスの確率の代わりに生のマージンが返されます。|
|- train_data: Dataset|The training dataset.|トレーニングデータセット．|
|- eval_name: str|The name of evaluation function (without whitespace).|評価関数の名前(ホワイトスペースを含まない)|
|- eval_result: float|The eval result.|評価結果.|
|- is_higher_better: bool|Is eval result higher better, e.g. AUC is is_higher_better.|評価結果が高い方が良いかどうか，例えば AUC は is_higher_better.|
||For multi-class task, the preds is group by class_id first, then group by row_id. If you want to get i-th row preds in j-th class, the access way is preds[j * num_data + i]. To ignore the default metric corresponding to the used objective, set metrics to the string "None".|マルチクラスタスクでは、まず class_id でグループ化し、次に row_id でグループ化することが推奨されます。j番目のクラスのi番目の行の preds を取得したい場合、 preds[j * num_data + i] というアクセス方法になります。使用している目的語に対応するデフォルト・メトリックを無視するには、メトリックを文字列 "None "に設定します。|
|init_model (str, pathlib.Path, Booster or None, optional (default=None))|Filename of LightGBM model or Booster instance used for continue training.|トレーニングの継続に使用されるLightGBMモデルまたはBoosterインスタンスのファイル名。 |
|feature_name (list of str, or 'auto', optional (default="auto"))|Feature names. If ‘auto’ and data is pandas DataFrame, data columns names are used.|特徴名。'auto'でデータがpandas DataFrameの場合は、データのカラム名が使用されます。 |
|categorical_feature (list of str or int, or 'auto', optional (default="auto"))|Categorical features. If list of int, interpreted as indices. If list of str, interpreted as feature names (need to specify feature_name as well). If ‘auto’ and data is pandas DataFrame, pandas unordered categorical columns are used. All values in categorical features should be less than int32 max value (2147483647). Large values could be memory consuming. Consider using consecutive integers starting from zero. All negative values in categorical features will be treated as missing values. The output cannot be monotonically constrained with respect to a categorical feature.|カテゴリ機能。intのリストの場合、インデックスとして解釈されます。strのリストの場合、フィーチャー名として解釈されます（feature_nameも指定する必要があります）。autoでデータがpandas DataFrameの場合、pandas unordered categorical columnsが使用されます。カテゴリカルフィーチャーのすべての値は、int32の最大値（2147483647）未満でなければなりません。大きな値はメモリを消費する可能性があります。ゼロから始まる連続した整数の使用を検討してください。カテゴリー機能の負の値はすべて欠損値として扱われます。カテゴリ特徴量に対して出力を単調に拘束することはできません。 |早期停止を有効にします。CVスコアを継続するには，少なくともearly_stopping_roundsラウンドごとに改善する必要があります．少なくとも1つの指標が必要です。複数の指標がある場合は、すべての指標をチェックします。最初の指標だけをチェックするには、paramsのfirst_metric_onlyパラメータをTrueに設定します。評価履歴の最後のエントリは、最良の反復からのものです。|
|fpreproc (callable or None, optional (default=None))|Preprocessing function that takes (dtrain, dtest, params) and returns transformed versions of those.|(dtrain, dtest, params)を受け取り，それらを変換したものを返す前処理関数。|
|verbose_eval (bool, int, or None, optional (default=None))|Whether to display the progress. If None, progress will be displayed when np.ndarray is returned. If True, progress will be displayed at every boosting stage. If int, progress will be displayed at every given verbose_eval boosting stage.|進捗状況を表示するかどうかを指定します。Noneの場合、np.ndarrayが返されたときに進捗状況が表示される。Trueの場合は、ブーストステージごとに進捗状況が表示されます。intの場合は、与えられたverbose_evalのブーストステージごとにプログレスが表示されます。 |
|show_stdv (bool, optional (default=True))|Whether to display the standard deviation in progress. Results are not affected by this parameter, and always contain std.|進捗状況に標準偏差を表示するかどうか。結果はこのパラメータの影響を受けず、常にstdを含みます。 |
|seed (int, optional (default=0))|Seed used to generate the folds (passed to numpy.random.seed).|フォールドの生成に使用するシード（numpy.random.seedに渡す）。 |
|callbacks (list of callable, or None, optional (default=None))|List of callback functions that are applied at each iteration. See Callbacks in Python API for more information.|各イテレーションで適用されるコールバック関数のリスト。詳細はPython APIのコールバックを参照してください。 |
|eval_train_metric (bool, optional (default=False))|Whether to display the train metric in progress. The score of the metric is calculated again after each training step, so there is some impact on performance.|進行中の列車のメトリックを表示するかどうかを指定します。メトリックのスコアは各トレーニングステップの後に再度計算されるため、パフォーマンスに多少の影響があります。 |
|return_cvbooster (bool, optional (default=False))|Whether to return Booster models trained on each fold through CVBooster.|CVBooster を通して各フォールドで学習された Booster モデルを返すかどうか． |
|Returns|eval_hist|Evaluation history. The dictionary has the following format: {‘metric1-mean’: [values], ‘metric1-stdv’: [values], ‘metric2-mean’: [values], ‘metric2-stdv’: [values], …}. If return_cvbooster=True, also returns trained boosters via cvbooster key.評価履歴. 辞書の形式は以下のとおりです．{'metric1-mean': [値], 'metric1-stdv': [値], 'metric2-mean': [値], 'metric2-stdv': [値], ...}. return_cvbooster=True の場合，cvbooster キーによって学習されたブースターも返されます．|
|Return type|dict|戻り値のタイプ: dict|

<br>

## **ploting**

### **lightgbm.plot_importance**

https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.plot_importance.html#lightgbm.plot_importance

lightgbm.plot_importance (booster, ax=None, height=0.2, xlim=None, ylim=None, title='Feature importance', xlabel='Feature importance', ylabel='Features', importance_type='auto', max_num_features=None, ignore_zero=True, figsize=None, dpi=None, grid=True, precision=3, **kwargs)

|項目|説明|
|---|---|
|booster<br>(Booster or LGBMModel)|各特徴重要性をプロットする対象のBooster または LGBMModel インスタンス|
|ax=None<br>(matplotlib.axes.Axes or None, optional (default=None))|対象となる軸のインスタンス。Noneの場合、新しい図と軸が作成される|
|height<br>(float, optional (default=0.2))|ax.barh() に渡される棒の高さ(幅|
|xlim, ylim<br>tuple of 2 elements or None, optional (default=None))|ax.xlim(), ax.ylim()に渡されるタプル|
|title<br>(str or None, optional (default="Feature importance")) |軸のタイトル．Noneの場合，タイトルは無効になる|
|xlabel, ylabel<br>(str or None, optional (default: x="Feature importance", y=Features")))| X 軸、Y 軸のタイトルラベル。Noneの場合、タイトルは無効になる|
|importance_type<br>(str, optional (default="auto"))|重要度の計算方法。"auto"の場合、boosterパラメータがLGBMModelであれば、booster.importance_type属性が使用され、そうでなければ "split" となる。"split" の場合、結果にはその特徴がモデル内で使用された回数が含まれる。"gain" の場合、その特徴を使用した分割の合計ゲインが結果に含まれる。|
|max_num_features<br>(int or None, optional (default=None))|プロットに表示される上位フィーチャーの最大数。None または <1 の場合、すべてのフィーチャーが表示さる|
|ignore_zero<br>(bool, optional (default=True))|重要度ゼロの特徴を無視するかどうか|
|figsize<br>(tuple of 2 elements or None, optional (default=None)|プロット領域サイズ|
|dpi<br>(bool, optional (default=True))|図形の解像度|
|grid<br>(bool, optional (default=True))|軸のグリッドを追加するかどうか|
|precision<br>(int or None, optional (default=3))|浮動小数点値の表示を特定の精度に制限するために使用する|
|\*\*kwargs|ax.barh()に渡されるその他のパラメータ|


www.DeepL.com/Translator（無料版）で翻訳しました。
