# Metrics to evaluate the models
from lightfm import evaluation
import numpy as np

def evaluation_lfm(model, test_interactions, user_features, item_features):
    # Calculate precision and recall@k
    k = 10
    precision = evaluation.precision_at_k(model, test_interactions, k=k, user_features=user_features, item_features=item_features).mean()
    recall = evaluation.recall_at_k(model, test_interactions, k=k, user_features=user_features, item_features=item_features).mean()

    # Calculate AUC-ROC score
    auc_roc = evaluation.auc_score(model, test_interactions, user_features=user_features, item_features=item_features).mean()


    print('Precision: ', precision)
    print('Recall: ', recall)
    print('AUC-ROC: ', auc_roc)