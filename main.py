import pandas as pd
import sys
sys.path.insert(0, './')

pd.set_option('display.max_columns', 15)

from EDA.eda import eda
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Applied Statistics Project')
    train_features = pd.read_csv("data/train_features.csv")
    train_targets_scored = pd.read_csv("data/train_targets_scored.csv")

    eda(train_features, train_targets_scored)
