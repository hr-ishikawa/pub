import pandas as pd
import numpy as np

# ====================
# 1. データフレームの作成
# ====================
# 例として、数値特徴量だけの状況を想定
# X_train, X_valid は (サンプル数, 特徴量数) の形状とする
# y_train, y_valid は (サンプル数,) の形状とする
# ------------------------------------------------
# ここではダミーデータで例示
num_features = 10
num_train = 1000
num_valid = 200

np.random.seed(42)
X_train = np.random.rand(num_train, num_features)
y_train = np.random.rand(num_train)
X_valid = np.random.rand(num_valid, num_features)
y_valid = np.random.rand(num_valid)

# pandas.DataFrame 形式に変換
train_df = pd.DataFrame(X_train, columns=[f"feat_{i}" for i in range(num_features)])
train_df["target"] = y_train

valid_df = pd.DataFrame(X_valid, columns=[f"feat_{i}" for i in range(num_features)])
valid_df["target"] = y_valid

# =====================
# 2. DataConfig の定義
# =====================
from pytorch_tabular.config import DataConfig

continuous_cols = [f"feat_{i}" for i in range(num_features)]  # 数値特徴量
# categorical_cols = [...]                                    # カテゴリ変数があればこちら

data_config = DataConfig(
    target=["target"],               # 目的変数
    continuous_cols=continuous_cols, # 数値特徴量
    # categorical_cols=categorical_cols,
    validation_split=None,           # 今回は自前で train/valid を指定
)

# =========================
# 3. TrainerConfig の定義
# =========================
from pytorch_tabular.config import TrainerConfig

trainer_config = TrainerConfig(
    auto_lr_find=False,
    batch_size=32,
    max_epochs=50,
    gpus=0,  # GPUを使用するなら 1 にする等
    early_stopping=True,             # Early stoppingを有効化
    early_stopping_patience=5,       # 例えば5エポック改善がなければストップ
    checkpoints="best",              # ベストモデルを保存 ("best" 指定)
)

###############################################################################
# ここから各モデルごとの設定を変更した例を順番に示します。
# TabNet, FT-Transformer, TabTransformer の3種類があります。
###############################################################################

############################################
# A. TabNet を用いた回帰
############################################
from pytorch_tabular.models import TabNetModel
from pytorch_tabular.models.tabnet.config import TabNetConfig
from pytorch_tabular.tabular_trainer import TabularTrainer

# ------------------------
# 4. ModelConfig の定義
# ------------------------
tabnet_config = TabNetConfig(
    task="regression",      # 回帰
    loss="MSELoss",         # 損失関数(回帰なのでMSEを例に)
    learning_rate=1e-3,
    # TabNet 特有のパラメータ調整例
    n_d=8,
    n_a=8,
    n_steps=3,
    gamma=1.3,
)

# ------------------------
# 5. モデルの生成 & 学習
# ------------------------
tabnet_model = TabNetModel(
    config=tabnet_config,
    data_config=data_config
)
tabnet_trainer = TabularTrainer(
    model=tabnet_model,
    config=trainer_config
)

tabnet_trainer.fit(
    train=train_df,
    validation=valid_df
)

# ============================
# 6. 推論(予測)の例
# ============================
pred_df_tabnet = tabnet_trainer.predict(valid_df)
print("TabNet prediction shape:", pred_df_tabnet.shape)
print(pred_df_tabnet.head())

# チェックポイントのパス(ベストモデル)を表示する
print("Best checkpoint path:", tabnet_trainer.best_checkpoint_path)

############################################
# B. FT-Transformer を用いた回帰
############################################
from pytorch_tabular.models.ft_transformer import FTTransformerModel
from pytorch_tabular.models.ft_transformer.config import FTTransformerConfig

fttransformer_config = FTTransformerConfig(
    task="regression",
    loss="MSELoss",
    learning_rate=1e-3,
    # FT-Transformer 特有のパラメータ例
    num_attention_blocks=2,
    embedding_dim=16,
    # etc...
)

fttransformer_model = FTTransformerModel(
    config=fttransformer_config,
    data_config=data_config
)

fttransformer_trainer = TabularTrainer(
    model=fttransformer_model,
    config=trainer_config
)

fttransformer_trainer.fit(
    train=train_df,
    validation=valid_df
)

pred_df_fttransformer = fttransformer_trainer.predict(valid_df)
print("FT-Transformer prediction shape:", pred_df_fttransformer.shape)
print(pred_df_fttransformer.head())
print("Best checkpoint path:", fttransformer_trainer.best_checkpoint_path)

############################################
# C. TabTransformer を用いた回帰
############################################
from pytorch_tabular.models.tab_transformer import TabTransformerModel
from pytorch_tabular.models.tab_transformer.config import TabTransformerConfig

tabtransformer_config = TabTransformerConfig(
    task="regression",
    loss="MSELoss",
    learning_rate=1e-3,
    # TabTransformer 特有のパラメータ例
    n_layers=3,
    n_heads=4,
    embed_dim=16,
    # etc...
)

tabtransformer_model = TabTransformerModel(
    config=tabtransformer_config,
    data_config=data_config
)

tabtransformer_trainer = TabularTrainer(
    model=tabtransformer_model,
    config=trainer_config
)

tabtransformer_trainer.fit(
    train=train_df,
    validation=valid_df
)

pred_df_tabtransformer = tabtransformer_trainer.predict(valid_df)
print("TabTransformer prediction shape:", pred_df_tabtransformer.shape)
print(pred_df_tabtransformer.head())
print("Best checkpoint path:", tabtransformer_trainer.best_checkpoint_path)
