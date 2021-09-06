## **lightgbm.Dataset**
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

## **lightgbm.train**

## **lightgbm.cv**

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
|feature_name (list of str, or 'auto', optional (default="auto"))|Feature names. If ‘auto’ and data is pandas DataFrame, data columns names are used.|特徴名。auto'でデータがpandas DataFrameの場合は、データのカラム名が使用されます。 |
|categorical_feature (list of str or int, or 'auto', optional (default="auto"))|Categorical features. If list of int, interpreted as indices. If list of str, interpreted as feature names (need to specify feature_name as well). If ‘auto’ and data is pandas DataFrame, pandas unordered categorical columns are used. All values in categorical features should be less than int32 max value (2147483647). Large values could be memory consuming. Consider using consecutive integers starting from zero. All negative values in categorical features will be treated as missing values. The output cannot be monotonically constrained with respect to a categorical feature.|カテゴリ機能。intのリストの場合、インデックスとして解釈されます。strのリストの場合、フィーチャー名として解釈されます（feature_nameも指定する必要があります）。auto」でデータがpandas DataFrameの場合、pandas unordered categorical columnsが使用されます。カテゴリカルフィーチャーのすべての値は、int32の最大値（2147483647）未満でなければなりません。大きな値はメモリを消費する可能性があります。ゼロから始まる連続した整数の使用を検討してください。カテゴリー機能の負の値はすべて欠損値として扱われます。カテゴリ特徴量に対して出力を単調に拘束することはできません。 |早期停止を有効にします。CVスコアを継続するには，少なくともearly_stopping_roundsラウンドごとに改善する必要があります．少なくとも1つの指標が必要です。複数の指標がある場合は、すべての指標をチェックします。最初の指標だけをチェックするには、paramsのfirst_metric_onlyパラメータをTrueに設定します。評価履歴の最後のエントリは、最良の反復からのものです。|
|fpreproc (callable or None, optional (default=None))|Preprocessing function that takes (dtrain, dtest, params) and returns transformed versions of those.|(dtrain, dtest, params)を受け取り，それらを変換したものを返す前処理関数。|
|verbose_eval (bool, int, or None, optional (default=None))|Whether to display the progress. If None, progress will be displayed when np.ndarray is returned. If True, progress will be displayed at every boosting stage. If int, progress will be displayed at every given verbose_eval boosting stage.|進捗状況を表示するかどうかを指定します。Noneの場合、np.ndarrayが返されたときに進捗状況が表示される。Trueの場合は、ブーストステージごとに進捗状況が表示されます。intの場合は、与えられたverbose_evalのブーストステージごとにプログレスが表示されます。 |
|show_stdv (bool, optional (default=True))|Whether to display the standard deviation in progress. Results are not affected by this parameter, and always contain std.|進捗状況に標準偏差を表示するかどうか。結果はこのパラメータの影響を受けず、常にstdを含みます。 |
|seed (int, optional (default=0))|Seed used to generate the folds (passed to numpy.random.seed).|フォールドの生成に使用するシード（numpy.random.seedに渡す）。 |
|callbacks (list of callable, or None, optional (default=None))|List of callback functions that are applied at each iteration. See Callbacks in Python API for more information.|各イテレーションで適用されるコールバック関数のリスト。詳細はPython APIのコールバックを参照してください。 |
|eval_train_metric (bool, optional (default=False))|Whether to display the train metric in progress. The score of the metric is calculated again after each training step, so there is some impact on performance.|進行中の列車のメトリックを表示するかどうかを指定します。メトリックのスコアは各トレーニングステップの後に再度計算されるため、パフォーマンスに多少の影響があります。 |
|return_cvbooster (bool, optional (default=False))|Whether to return Booster models trained on each fold through CVBooster.|CVBooster を通して各フォールドで学習された Booster モデルを返すかどうか． |
|Returns|eval_hist|Evaluation history. The dictionary has the following format: {‘metric1-mean’: [values], ‘metric1-stdv’: [values], ‘metric2-mean’: [values], ‘metric2-stdv’: [values], …}. If return_cvbooster=True, also returns trained boosters via cvbooster key.評価履歴. 辞書の形式は以下のとおりです．{'metric1-mean': [値], 'metric1-stdv': [値], 'metric2-mean': [値], 'metric2-stdv': [値], ...}. return_cvbooster=True の場合，cvbooster キーによって学習されたブースターも返されます．|
|Return type|dict|戻り値のタイプ: dict|



www.DeepL.com/Translator（無料版）で翻訳しました。
