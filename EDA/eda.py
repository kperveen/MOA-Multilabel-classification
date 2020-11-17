def eda(train_features, train_targets_scored):
    print("EDA of DATA")

    print("HEAD of scored targets {} ".format(train_targets_scored.head()))
    print("Size of scored targets dataframe {}".format(train_targets_scored.shape))

    ## Adding the targets data to train data
    train_data = train_features.join(train_targets_scored.set_index('sig_id'), on='sig_id')
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