# **AutoGluon Predictors**
https://auto.gluon.ai/stable/api/autogluon.predictor.html
```
# データセット
#   df_test   学習に使用
#   df_valid  検証に使用(Label付)
#   df_test   予測に使用(Labelなし)
# 目的変数: target_colname
# 評価関数: metric
# 試行方法(モデルセット)のプリセット: presets

# インストール
!pip install -U "mxnet_cu101<2.0.0"   # for GPU: CUDA 10.1 for goolge colaboratory (Aug. 2021)
!pip install autogluon

# ライブラリ
import autogluon as ag
from autogluon.tabular import TabularPredictor

# 学習
predictor = TabularPredictor(label=target_colname, eval_metric=metric, path=save_path)\
                        .fit(df_train, presets=presets)

# 学習結果
results = predictor.fit_summary()

# 検証予測
y_pred = predictor.predict(df_valid.drop(columns=[target_colname]))   # 目的変数列を除いておく

# 検証結果の確認
perf = predictor.evaluate_predictions(y_true=df_valid[target_colname], y_pred=y_pred, auxiliary_metrics=True)

# 予測
y_pred = predictor.predict(df_test))


# 保存モデルの読込
predictor = TabularPredictor.load(save_path)
```

## **TabularPredictor**
https://auto.gluon.ai/stable/api/autogluon.predictor.html#autogluon.tabular.TabularPredictor
```
class autogluon.tabular.TabularPredictor（
    label、
    problem_type = None、 # Default=None = Auto  'binary', 'multiclass', 'regression', 'quantile'
    eval_metric = None、  # Default=None = Auto 
        # Classification: ['accuracy', 'balanced_accuracy', 
        #     'f1', 'f1_macro', 'f1_micro', 'f1_weighted', 'roc_auc', 'roc_auc_ovo_macro7, 
        #     'average_precision', 'precision', 'precision_macro', 'precision_micro', ' Precision_weighted', 
        #     'recall', 'recall_macro', 'recall_micro', 'recall_weighted', 
        #     'log_loss', 'pac_score']                          
        # Regression:  ['root_mean_squared_error', 'mean_squared_error', 'mean_absolute_error', 
        #     'median_absolute_error', 'r2']             
    path = None、
    verbosity = 2、
    sample_weight = None、
    weight_evaluation = False、
    groups = None、** kwargs
）
```

## **fit**
https://auto.gluon.ai/stable/api/autogluon.predictor.html#autogluon.tabular.TabularPredictor.fit

```
fit(
    train_data, 
    tuning_data = None, 
    time_limit = None, # recommend: None
    presets = None,   # default = ['medium_quality_faster_train'] 
        # best_quality
        # high_quality_fast_inference_only_refi
        # good_quality_faster_inference_only_refit
        # medium_quality_faster_train
        # optimize_for_deployment
        # ignore_text
    hyperparameters = None, #  ['default', 'light', 'very_light', 'toy', 'multimodal']
    feature_metadata = 'infer', 
    **kwargs
)
```

|Param|Desc|説明|
|-----|----|----|
|train_data:<br>str or TabularDataset or pd.DataFrame|Table of the training data, which is similar to a pandas DataFrame. If str is passed, train_data will be loaded using the str value as the file path.|トレーニングデータのテーブルで、pandasのDataFrameに似ています。strが渡された場合、train_dataはstrの値をファイルパスとしてロードされます。|
|tuning_data:<br>str or TabularDataset or pd.DataFrame,<br>default = None|Another dataset containing validation data reserved for tuning processes such as early stopping and hyperparameter tuning. This dataset should be in the same format as train_data. If str is passed, tuning_data will be loaded using the str value as the file path. Note: final model returned may be fit on tuning_data as well as train_data. Do not provide your evaluation test data here! In particular, when num_bag_folds > 0 or num_stack_levels > 0, models will be trained on both tuning_data and train_data. If tuning_data = None, fit() will automatically hold out some random validation examples from train_data.|早期停止やハイパーパラメータチューニングなどのチューニング処理のために確保された検証データを含む別のデータセットです。このデータセットはtrain_dataと同じフォーマットでなければなりません。strを渡すと、strの値をファイルパスとしてtuning_dataが読み込まれます。注意：最終的に返されるモデルは，train_dataだけでなく，tuning_dataにもフィットする可能性があります．評価用のテストデータをここで提供してはいけません 特に num_bag_folds > 0 や num_stack_levels > 0 の場合、モデルは tuning_data と train_data の両方で学習されます。tuning_data = Noneの場合、fit()は自動的にtrain_dataからランダムな検証例をいくつか取り出します。|
|time_limitint,<br>default = None|Approximately how long fit() should run for (wallclock time in seconds). If not specified, fit() will run until all models have completed training, but will not repeatedly bag models unless num_bag_sets is specified.|fit()が実行されるおよその時間(秒単位のウォールクロック時間)。指定されていない場合、fit() はすべてのモデルが学習を完了するまで実行しますが、num_bag_sets が指定されていない限り、バッグモデルを繰り返し実行することはありません|
|presets:<br>list or str or dict, default = [‘medium_quality_faster_train’]|List of preset configurations for various arguments in fit(). Can significantly impact predictive accuracy, memory-footprint, and inference latency of trained models, and various other properties of the returned predictor. It is recommended to specify presets and avoid specifying most other fit() arguments or model hyperparameters prior to becoming familiar with AutoGluon. As an example, to get the most accurate overall predictor (regardless of its efficiency), set presets=’best_quality’. To get good quality with minimal disk usage, set presets=[‘good_quality_faster_inference_only_refit’, ‘optimize_for_deployment’] Any user-specified arguments in fit() will override the values used by presets. If specifying a list of presets, later presets will override earlier presets if they alter the same argument. For precise definitions of the provided presets, see file: autogluon/tabular/configs/presets_configs.py. Users can specify custom presets by passing in a dictionary of argument values as an element to the list.<br>Available Presets: [‘best_quality’, ‘high_quality_fast_inference_only_refit’, ‘good_quality_faster_inference_only_refit’, ‘medium_quality_faster_train’, ‘optimize_for_deployment’, ‘ignore_text’] It is recommended to only use one quality based preset in a given call to fit() as they alter many of the same arguments and are not compatible with each-other.|fit()の様々な引数に対するプリセット設定のリストです。訓練されたモデルの予測精度、メモリフットプリント、推論レイテンシー、および返される予測器の様々な他の特性に大きな影響を与えることができます。AutoGluonを使いこなす前に、プリセットを指定し、他のほとんどのfit()引数やモデルのハイパーパラメータを指定しないことをお勧めします。例として、最も正確な全体の予測値を得るためには（その効率に関わらず）、presets='best_quality'を設定します。ディスク使用量を最小限に抑えて良い品質を得るには、presets=['good_quality_faster_inference_only_refit', 'optimize_for_deployment'] fit()でユーザーが指定した引数は、presets が使う値を上書きします。プリセットのリストを指定した場合、後から指定したプリセットが同じ引数を変更すると、前のプリセットを上書きします。用意されているプリセットの正確な定義については、ファイル：autogluon/tabular/configs/presets_configs.pyを参照してください。ユーザーは、引数の値の辞書をリストの要素として渡すことで、カスタムプリセットを指定することができます。<br>利用可能なプリセット [best_quality', 'high_quality_fast_inference_only_refit', 'good_quality_faster_inference_only_refit', 'medium_quality_faster_train', 'optimize_for_deployment', 'ignore_text'] fit()を呼び出す際には、品質ベースのプリセットを1つだけ使うことをお勧めします。なぜなら、これらのプリセットは同じ引数の多くを変更し、互いに互換性がないからです。|
|-&nbsp;best_quality = {‘auto_stack’: True}|Best predictive accuracy with little consideration to inference time or disk usage. Achieve even better results by specifying a large time_limit value. Recommended for applications that benefit from the best possible model accuracy.|推論時間やディスク使用量をほとんど考慮せずに、最高の予測精度を得ることができます。大きなtime_limit値を指定することで、さらに良い結果を得ることができます。可能な限り最高のモデル精度が必要なアプリケーションにお勧めします。|
|-&nbsp;high_quality_fast_inference_<br>only_refit = {‘auto_stack’: True, ‘refit_full’: True, ‘set_best_to_refit_full’: True, ‘_save_bag_folds’: False}|High predictive accuracy with fast inference. ~10x-200x faster inference and ~10x-200x lower disk usage than best_quality. Recommended for applications that require reasonable inference speed and/or model size.|高速な推論で高い予測精度を実現。~best_qualityと比較して、推論速度が10倍〜200倍、ディスク使用量が10倍〜200倍低くなります。適度な推論速度とモデルサイズを必要とするアプリケーションにお勧めします。|
|-&nbsp;good_quality_faster_inference_<br>only_refit = {‘auto_stack’: True, ‘refit_full’: True, ‘set_best_to_refit_full’: True, ‘_save_bag_folds’: False, ‘hyperparameters’: ‘light’}|Good predictive accuracy with very fast inference. ~4x faster inference and ~4x lower disk usage than high_quality_fast_inference_only_refit. Recommended for applications that require fast inference speed.|非常に高速な推論で良好な予測精度を実現。~high_quality_fast_inference_only_refitと比較して、推論速度は4倍、ディスク使用量は4倍となっています。速い推論速度を必要とするアプリケーションにお勧めです。|
|-&nbsp;medium_quality_faster_train = {‘auto_stack’: False}|Medium predictive accuracy with very fast inference and very fast training time. ~20x faster training than good_quality_faster_inference_only_refit. This is the default preset in AutoGluon, but should generally only be used for quick prototyping, as good_quality_faster_inference_only_refit results in significantly better predictive accuracy and faster inference time.|非常に高速な推論と非常に高速な学習時間で中程度の予測精度を実現します。~good_quality_faster_inference_only_refitに比べてトレーニングが20倍程度高速です。good_quality_faster_inference_only_refitは、予測精度が大幅に向上し、推論時間が短縮されるため、これはAutoGluonのデフォルトのプリセットですが、一般的には迅速なプロトタイピングにのみ使用してください。|
|-&nbsp;optimize_for_deployment = {‘keep_only_best’: True, ‘save_space’: True}|Optimizes result immediately for deployment by deleting unused models and removing training artifacts. Often can reduce disk usage by ~2-4x with no negatives to model accuracy or inference speed. This will disable numerous advanced functionality, but has no impact on inference. This will make certain functionality less informative, such as predictor.leaderboard() and predictor.fit_summary().<br>Because unused models will be deleted under this preset, methods like predictor.leaderboard() and predictor.fit_summary() will no longer show the full set of models that were trained during fit().<br>Recommended for applications where the inner details of AutoGluon’s training is not important and there is no intention of manually choosing between the final models. This preset pairs well with the other presets such as good_quality_faster_inference_only_refit to make a very compact final model. Identical to calling predictor.delete_models(models_to_keep=’best’, dry_run=False) and predictor.save_space() directly after fit().|未使用のモデルを削除し、トレーニングの成果物を削除することで、結果を即座にデプロイメント用に最適化します。多くの場合、モデルの精度や推論速度に悪影響を与えることなく、ディスク使用量を約2～4倍に減らすことができます。これにより、多くの高度な機能が無効になりますが、推論には影響しません。predictor.leaderboard()やpredictor.fit_summary()のような特定の機能は、情報が少なくなります。<br>このプリセットでは未使用のモデルが削除されるため、predictor.leaderboard()やpredictor.fit_summary()のようなメソッドでは、fit()の間に学習されたモデルの完全なセットが表示されなくなります。<br>AutoGluonのトレーニングの詳細が重要ではなく、最終的なモデルを手動で選択する意図がないアプリケーションにお勧めします。このプリセットは、good_quality_faster_inference_only_refitのような他のプリセットと相性がよく、非常にコンパクトな最終モデルを作成します。fit()の直後にpredictor.delete_models(models_to_keep='best', dry_run=False)とpredictor.save_space()を呼んだのと同じです。|
|-&nbsp;ignore_text = {‘_feature_generator_kwargs’: {‘enable_text_ngram_features’: False, ‘enable_text_special_features’: False, ‘enable_raw_text_features’: False}}|Disables automated feature generation when text features are detected. This is useful to determine how beneficial text features are to the end result, as well as to ensure features are not mistaken for text when they are not. Ignored if feature_generator was also specified.|テキストの特徴が検出されたときに、特徴の自動生成を無効にします。こ れは、 テ キ ス ト 機能が最終結果に対 し て ど の よ う な利点を も た ら すかを判断す る のに有用であ り 、 ま た、 機能がテ キ ス ト でない と き に誤認 さ れない よ う にす る のに有用です。feature_generator が指定されている場合は無視されます。|
|||
|||
