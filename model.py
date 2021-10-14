import numpy as np
import pandas as pd


from sklearn import tree


def model_prediction(gre, gpa, ses, gender, ethnic, rank):
    W_P = pd.read_csv('Admission2.csv')
    X_prime = W_P.iloc[:, [1, 2, 3, 4, 5, 6]].values
    Y = W_P.iloc[:, 0].values

    ModelosTree = tree.DecisionTreeClassifier(max_leaf_nodes=20)
    ModelosTree.fit(X_prime, Y)

    X_test = np.array([gre, gpa, ses, gender, ethnic, rank])
    X_test = X_test.reshape((1, -1))

    return ModelosTree.predict(X_test)[0]
