import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def eda(train_features, train_targets_scored):
    print("EDA of DATA")

    print("HEAD of scored targets {} ".format(train_targets_scored.head()))
    print("Size of scored targets dataframe {}".format(train_targets_scored.shape))

    # Adding the targets data to train data
    train_data = train_features  # train_features.join(train_targets_scored.set_index('sig_id'), on='sig_id')
    print("head of train data {} ".format(train_data.head()))
    print("Size of train data {} ".format(train_data.shape))
    print("CHECKING VALUES OF CATEGORICAL VARIABLES")
    obj_df = train_data.select_dtypes(include=['object']).copy()
    print(obj_df.head())
    print(obj_df[obj_df.isnull().any(axis=1)])
    print("NO NULL VALUES IN CATEGORICAL FEATURES")



    # Converting categorical variables to numerical
    train_data["cp_type"] = train_data["cp_type"].astype('category').cat.codes
    train_data["cp_dose"] = train_data["cp_dose"].astype('category').cat.codes

    print(train_data['cp_type'].unique())  # trt_cp = 1 and ctl_vehicle = 0;
    print(train_data['cp_dose'].unique())  # D1 = 0 and D2 = 1;

    # THE LABELS ARE THE TARGETS SCORED

    # checking data after conversion
    print(train_data.head())
    print("Correlation matrix: ")

    corr_df = train_data[['g-0', 'g-1', 'c-21', 'c-22', 'c-23']]
    corr_matrix = corr_df.corr()
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    # Set up the matplotlib figure
    plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr_matrix, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()
    print(corr_df.corr())

    # The correlation between variables is not significant, although the correlations is betweeb a given
    # gene-function and cell viability.

    corr_df.boxplot(column=['g-0', 'g-1', 'c-21', 'c-22'])
    plt.show()
    train_data.boxplot(column=['g-21', 'g-51', 'c-32', 'c-33'])
    plt.show()

    # The data containing gene functions and cell viability seems to be having a lot of outliers and they all seem
    # to be starting and ending at the same point for the gene function variables and cell viability variables

    corr_df.plot.kde()
    plt.show()

    # Looking at the graphs, the data doesn't seems to be skewed
