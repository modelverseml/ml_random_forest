from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor


class RandomForestModels:

    def __init__(self,n_estimators = 100):

        self.n_estimators = n_estimators

    
    def get_regressor_model(self,train_df,test_df, parameters_dict = {}):

        if not parameters_dict:

            parameters_dict = {
                'n_estimators' : self.n_estimators,

            }

        reg_model = RandomForestRegressor(**parameters_dict)

        reg_model.fit(train_df,test_df)

        return reg_model
    
    def get_classifier_model(self,train_df,test_df, parameters_dict = {}):

        if not parameters_dict:

            parameters_dict = {
                'n_estimators' : self.n_estimators,

            }

        classifier_model = RandomForestClassifier(**parameters_dict)

        classifier_model.fit(train_df,test_df)

        return classifier_model