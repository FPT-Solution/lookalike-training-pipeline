from sklearn import tree
from sklearn import neighbors
from sklearn import naive_bayes
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

class Experiment:
    def __init__(self, run):
        self.run = run
    # TODO Huy: triển khai bào toán lookalike sử dụng một số model lên trên này nhé.
    def execute(self, X, y):
        clf1 = tree.DecisionTreeClassifier()
        clf2 = LogisticRegression(solver='liblinear')
        clf3 = neighbors.KNeighborsClassifier()
        clf4 = naive_bayes.GaussianNB()

        clf1 = clf1.fit(X, y)
        clf2 = clf2.fit(X, y)
        clf3 = clf3.fit(X, y)
        clf4 = clf4.fit(X, y)

        # evalute for choice best socre:
        list_model = [clf1, clf2, clf3, clf4]
        list_model_name =  ['Decision Tree', 'Logistic Regression', 'K Nearest Neighbour', 'Naive Bayes']
        list_score = []
        # Accuracy on training set
        for clf, label in zip(list_model,list_model_name):
            scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
            print("Accuracy: %0.4f (+/- %0.4f) [%s]" % (scores.mean(), scores.std(), label))
            list_score.append(scores.mean())

        # choose best socre:
        max_score = max(list_score)
        best_model = list_model[-1]
        
        return best_model.predict(X)
