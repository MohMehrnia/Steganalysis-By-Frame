import csv
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.metrics.classification import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score


def loaddata(filename,instanceCol):
    file_reader = csv.reader(open(filename,'r'),delimiter=',')
    x = []
    y = []
    for row in file_reader:
        x.append(row[0:instanceCol])
        y.append(row[-1])
    return np.array(x[1:]).astype((np.float32)), np.array(y[1:]).astype(np.int)


def fractal_modeldata(filename):
    scores = []
    print(filename)
    X, Y = loaddata(filename, 33)
    np.random.seed(13)
    indices = np.random.permutation(2038)
    test_size = int(0.2 * len(indices))
    X_train = X[indices[:-test_size]]
    Y_train = Y[indices[:-test_size]]
    X_test = X[indices[-test_size:]]
    Y_test = Y[indices[-test_size:]]
    # relu, sigmoid
    classifier = LinearDiscriminantAnalysis()

    classifier.fit(X_train, Y_train)
    Y_pred = classifier.predict(X_test)
    print(accuracy_score(Y_test, Y_pred)*100)
    print(classification_report(Y_test, Y_pred))
    print(roc_auc_score(Y_test, Y_pred))


if __name__ == '__main__':
    fractal_modeldata('D:\\Databases\\Steganalysis\\Dataset\\Fractal\\Fractal-Features-hide4pgp-100.csv')
    fractal_modeldata('D:\\Databases\\Steganalysis\\Dataset\\Fractal\\Fractal-Features-hide4pgp-71.csv')
    fractal_modeldata('D:\\Databases\\Steganalysis\\Dataset\\Fractal\\Fractal-Features-hide4pgp-42.csv')
    fractal_modeldata('D:\\Databases\\Steganalysis\\Dataset\\Fractal\\Fractal-Features-hide4pgp-21.csv')
    fractal_modeldata('D:\\Databases\\Steganalysis\\Dataset\\Fractal\\Fractal-Features-hide4pgp-7.csv')


