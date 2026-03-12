## Hiroo Ishikawa's Repository
**Version 1.5.0**: https://auto.gluon.ai/stable/whats_new/v1.5.0.html  
**TabularPredictor.fit**: https://auto.gluon.ai/stable/api/autogluon.tabular.TabularPredictor.fit.html  

|ファイル名|説明|
|-----|-----|
|AutoGluon_Ref_Man.md|ドキュメント抜粋|
|AutoGluon_Regression_boston.ipynb<br>AutoGluon_Regression_diamonds.ipynb|AutoGluonサンプルコード(回帰版)|
|README.md|This File|

#### presets

Available Presets: [‘extreme_quality’, ‘best_quality’, ‘high_quality’, ‘good_quality’, ‘medium_quality’, ‘experimental_quality’, ‘optimize_for_deployment’, ‘interpretable’, ‘ignore_text’]  
- best_quality={‘auto_stack’: True, ‘dynamic_stacking’: ‘auto’, ‘hyperparameters’: ‘zeroshot’}  
- high_quality={‘auto_stack’: True, ‘dynamic_stacking’: ‘auto’, ‘hyperparameters’: ‘zeroshot’, ‘refit_full’: True, ‘set_best_to_refit_full’: True, ‘save_bag_folds’: False}  
- good_quality={‘auto_stack’: True, ‘dynamic_stacking’: ‘auto’, ‘hyperparameters’: ‘light’, ‘refit_full’: True, ‘set_best_to_refit_full’: True, ‘save_bag_folds’: False}  

#### hyperparameters
```
from autogluon.tabular.configs.hyperparameter_configs import get_hyperparameter_config
print(f"default: \t\t {get_hyperparameter_config('default').keys()}")
print(f"interpretable: \t\t {get_hyperparameter_config('interpretable').keys()}")
print(f"zeroshot: \t\t {get_hyperparameter_config('zeroshot').keys()}")
print(f"zeroshot_2025_tabfm:  \t {get_hyperparameter_config('zeroshot_2025_tabfm').keys()}")
print(f"zeroshot_2025_12_18_cpu: {get_hyperparameter_config('zeroshot_2025_12_18_cpu').keys()}")
print(f"zeroshot_2025_12_18_gpu: {get_hyperparameter_config('zeroshot_2025_12_18_gpu').keys()}")
print(f"experimental: \t\t {get_hyperparameter_config('experimental').keys()}")
default: 		 dict_keys(['NN_TORCH', 'GBM', 'CAT', 'XGB', 'FASTAI', 'RF', 'XT'])
interpretable: 		 dict_keys(['IM_RULEFIT', 'IM_FIGS'])
zeroshot: 		 dict_keys(['NN_TORCH', 'GBM', 'CAT', 'XGB', 'FASTAI', 'RF', 'XT'])
zeroshot_2025_tabfm:  	 dict_keys(['REALTABPFN-V2', 'GBM', 'CAT', 'TABM', 'TABICL', 'XGB', 'MITRA'])
zeroshot_2025_12_18_cpu: dict_keys(['CAT', 'GBM_PREP', 'GBM', 'NN_TORCH', 'FASTAI'])
zeroshot_2025_12_18_gpu: dict_keys(['TABDPT', 'TABICL', 'MITRA', 'TABM', 'GBM_PREP', 'CAT', 'GBM', 'REALTABPFN-V2'])
experimental: 		 dict_keys(['TABPFNMIX', 'NN_TORCH', 'GBM', 'CAT', 'XGB', 'FASTAI', 'RF', 'XT'])
```
```
pprint(get_hyperparameter_config('zeroshot_2025_12_18_gpu')['TABM'])
[{'ag_args': {'name_suffix': '_r99', 'priority': -13},
  'amp': False,
  'arch_type': 'tabm-mini',
  'batch_size': 'auto',
  'd_block': 880,
  'd_embedding': 24,
  'dropout': 0.10792355695428629,
  'gradient_clipping_norm': 1.0,
  'lr': 0.0013641856391615784,
  'n_blocks': 5,
  'num_emb_n_bins': 16,
  'num_emb_type': 'pwl',
  'patience': 16,
  'share_training_batches': False,
  'tabm_k': 32,
  'weight_decay': 0.0},
 {'ag_args': {'name_suffix': '_r124', 'priority': -17}, ...},
...}]
```

#### Model Informations

predictor.leaderboard(silent=True)
predictor.model_names()
predictor.info()

#### Install

pip install torch==2.9.1+cu128 torchvision==0.24.1+cu128 torchaudio==2.9.1+cu128 --index-url https://download.pytorch.org/whl/cu128  
pip install autogluon.tabular[tabarena] autogluon.multimodal  

