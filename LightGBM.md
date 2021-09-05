## **lightgbm.Dataset**
lightgbm.Dataset(data, label=None, reference=None, weight=None, group=None, init_score=None, silent='warn', feature_name='auto', categorical_feature='auto', params=None, free_raw_data=True)


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

