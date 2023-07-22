import json
import joblib
import pandas as pd
import shap

import logging
logger = logging.getLogger(__name__)

model = joblib.load('./app/scripts/models/xgbmodel.joblib')
config = json.load(open('./app/scripts/models/config.json'))

def get_dict_pred(dt_):
    k1 = []
    k2 = []
    for k,v in dt_.items():
        k1.append(k)
        val = {0:v}
        k2.append(val)
    valid = dict(zip(k1,k2))
    return valid

def get_shap_features(test):
    train = pd.read_csv("./data/X_train.csv")
    sv = shap.TreeExplainer(model, train)
    res = sv.shap_values(test)
    return res



def get_inf(config):
    # config = json.load(open('./scripts/models/config.json'))
    # print(config)
    


    dt_ = config["dt_"]
    dt  = get_dict_pred(dt_)
    data = pd.DataFrame(dt)
    predictions = model.predict(data) 
    sh = get_shap_features(data)[0]
    # print(f"Shap Values {sh}")
    features = list(dt_.keys())
    import numpy as np
    avg_sh = np.mean(sh)
    shaps = (sh-min(sh))/max(sh)-min(sh)
    # print(f"normalized Shap {shaps}")
    # print(features)
    # for_plot = dict(zip(features, sh))
    # print(f"for plot dict {for_plot}")
    return predictions, features, shaps



if __name__=="__main__":
    print(get_inf(None))



