import numpy as np
import pickle

modelFilename = 'binary_tree_model.sav'
scalerFilename = 'scaler_model.sav'


def model_prediction(radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, points_worst, symmetry_worst, fractal_dimension_worst):
    
    ModelosTree = pickle.load(open(modelFilename, 'rb'))
    scaler = pickle.load(open(scalerFilename, 'rb'))
    
    X_test = np.array([radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se,
                      compactness_se, concavity_se, points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, points_worst, symmetry_worst, fractal_dimension_worst])
    X_test = X_test.reshape((1, -1))

    X_norm = scaler.transform(X_test)

    return ModelosTree.predict(X_norm)[0]

