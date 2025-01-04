Perplexity: boostの入手・インストールを含めた、Anaconda環境での、lightgbm をwindows, CUDA対応のビルド手順

Anaconda環境が「アクティブ」な状態でのLightGBMの正確なビルドとインストール手順は以下の通りです：

1. Anaconda環境のアクティブ化:
   ```
   conda activate your_environment_name
   ```
   (your_environment_nameは作成した環境の名前に置き換えてください)

2. 必要な依存関係のインストール:
   ```
   conda install cmake
   conda install -c conda-forge boost
   ```

3. LightGBMのソースコードの取得:
   ```
   git clone --recursive https://github.com/microsoft/LightGBM
   cd LightGBM
   ```

4. ビルドディレクトリの作成とCMakeの実行:
   ```
   mkdir build
   cd build
   cmake -A x64 -DUSE_GPU=1 -DUSE_CUDA=1 ..
   ```

5. ビルドの実行:
   ```
   cmake --build . --target ALL_BUILD --config Release
   ```

6. Pythonパッケージのインストール:
   ```
   cd ../python-package
   python setup.py install
   ```

この手順を踏むことで、Anaconda環境内でLightGBMをビルドし、インストールすることができます。環境がアクティブな状態でこれらのコマンドを実行することで、LightGBMは自動的にその環境のサイトパッケージディレクトリにインストールされ、Pythonから直接インポートして使用できるようになります。

Citations:
[1] https://effegma.com/install-anaconda/
[2] https://freelance.shiftinc.jp/column/python-anaconda
[3] https://zenn.dev/makio/articles/69e38f5c90033e
[4] https://qiita.com/t2y/items/2a3eb58103e85d8064b6
[5] https://qiita.com/ozaki_physics/items/985188feb92570e5b82d
   ```

## 動作確認

以下のPythonスクリプトで動作確認を行います:

```python
import lightgbm as lgb
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)

dtrain = lgb.Dataset(X_train, label=y_train)

params = {
    'device': 'cuda',
    'objective': 'multiclass',
    'num_class': 3,
    'metric': 'multi_logloss'
}

clf = lgb.train(params, dtrain, num_boost_round=100)
preds = clf.predict(X_test)
print(preds)
```

このスクリプトを実行し、エラーなく予測結果が表示されれば、CUDA対応のLightGBMが正常に動作していることが確認できます[1][3][5]。

Citations:
[1] https://an-engineer-note.com/?p=996
[2] https://www.kkaneko.jp/tools/win/boost.html
[3] https://gist.github.com/tsutomu-n/8df651ab2c169935e60eec33943032cb
[4] https://qiita.com/exp/items/f9be7b4029476ce5b2fe
[5] https://www.genspark.ai/spark/wsl2%E3%81%A7lightgbm%E3%81%AEgpu%E3%83%88%E3%83%AC%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%E3%82%92%E6%9C%89%E5%8A%B9%E3%81%AB%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/a429f9c4-a013-402e-8ef9-9818fc4d4202
