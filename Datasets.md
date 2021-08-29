## **データセット**

### **scikit-learn**
[Dataset loading utilities](https://scikit-learn.org/stable/datasets.html)  
|Description|n|Reg/Cls|Clss|Feats|load|
|---|--:|---|--:|--:|---|
|Boston house prices dataset|506|regression|||13|load_boston(*[, return_X_y])|
|Iris plants dataset|150|classification|3|4|load_iris(*[, return_X_y, as_frame])|
|Diabetes dataset|442|regression||10|load_diabetes(*[, return_X_y, as_frame])|
|Optical recognition of handwritten digits dataset|1797|classification|10||load_digits(*[, n_class, return_X_y, as_frame])|
|Linnerrud dataset|20|||3|load_linnerud(*[, return_X_y, as_frame]) |
|Wine recognition dataset|178|classification|3|13|load_wine(*[, return_X_y, as_frame])|
|Breast cancer wisconsin (diagnostic) dataset|569|classification|2|30|load_breast_cancer(*[, return_X_y, as_frame])|
|California Housing dataset|20604|regression||8|fetch_california_housing(*[, data_home, …])|





### **seaborn**
```
sns.load_dataset(name, cache=True, data_home=None, **kws)
sns.get_dataset_names()  
['anagrams',
 'anscombe',
 'attention',
 'brain_networks',
 'car_crashes',
 'diamonds',
 'dots',
 'exercise',
 'flights',
 'fmri',
 'gammas',
 'geyser',
 'iris',
 'mpg',
 'penguins',
 'planets',
 'tips',
 'titanic']
```
