import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


from sklearn import tree

def Normalizar(X_prime):
    scaler=StandardScaler()
    scaler.fit(X_prime)
    X=scaler.transform(X_prime)
    return (X,scaler)

def model_prediction(radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, points_worst, symmetry_worst, fractal_dimension_worst):
    W_P = pd.read_csv('breast-cancer.csv')



    X_prime = W_P.iloc[:, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                           16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]].values
                        
    Y = W_P.iloc[:, 1].values

    (X,scaler)=Normalizar(X_prime)

    ModelosTree = tree.DecisionTreeClassifier(max_leaf_nodes=20)
    ModelosTree.fit(X, Y)

    X_test = np.array([radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se,
                      compactness_se, concavity_se, points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, points_worst, symmetry_worst, fractal_dimension_worst])
    X_test = X_test.reshape((1, -1))

    return ModelosTree.predict(X_test)[0]
