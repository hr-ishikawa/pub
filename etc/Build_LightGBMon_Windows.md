Perplexity: boostの入手・インストールを含めた、lightgbm をwindows, CUDA対応のビルド完全手順

LightGBMをWindows環境でCUDA対応でビルドする完全手順を以下に示します。Boostの入手とインストールも含めています。

## 必要な環境の準備

1. Visual Studio（C++開発環境）をインストール
2. CMakeをダウンロードしてインストール
3. Git for Windowsをインストール
4. CUDA Toolkitをインストール（NVIDIAの公式サイトから最新版を入手）

## Boostのインストール

1. Boostの公式サイトから最新版（例：boost_1_80_0.zip）をダウンロード
2. ダウンロードしたZIPファイルを`C:\local\`に展開（例：`C:\local\boost_1_80_0`）
3. コマンドプロンプトを管理者権限で開き、以下のコマンドを実行:
   ```
   cd C:\local\boost_1_80_0
   bootstrap.bat
   b2 --toolset=msvc-14.2 address-model=64 --build-type=complete stage
   ```

## LightGBMのビルド

1. ソースコードの取得:
   ```
   git clone --recursive https://github.com/microsoft/LightGBM
   cd LightGBM
   ```

2. ビルドディレクトリの作成と移動:
   ```
   mkdir build
   cd build
   ```

3. CMakeの実行:
   ```
   cmake -A x64 -DUSE_GPU=1 -DUSE_CUDA=1 -DBOOST_ROOT=C:/local/boost_1_80_0 -DBOOST_LIBRARYDIR=C:/local/boost_1_80_0/stage/lib ..
   ```

4. ビルドの実行:
   ```
   cmake --build . --target ALL_BUILD --config Release
   ```

5. Pythonパッケージのインストール:
   ```
   cd ../python-package
   python setup.py install --precompile
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
