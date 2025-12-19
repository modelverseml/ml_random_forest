from xgboost import XGBClassifier,XGBRegressor


class XGBoostModels:

    def __init__(self,n_estimators = 100,learning_rate = 0.1):

        self.n_estimators = n_estimators

        self.learning_rate = learning_rate

    
    def get_regressor_model(self,train_df,test_df, parameters_dict = {}):

        if not parameters_dict:

            parameters_dict = {
                'n_estimators' : self.n_estimators,
                'learning_rate' : self.learning_rate

            }
            
        reg_model = XGBRegressor(**parameters_dict)


        reg_model.fit(train_df,test_df)

        return reg_model
    
    def get_classifier_model(self,train_df,test_df, parameters_dict = {}):

        if not parameters_dict:

            parameters_dict = {
                'n_estimators' : self.n_estimators,
                'learning_rate' : self.learning_rate

            }

        classifier_model = XGBClassifier(**parameters_dict)
        

        classifier_model.fit(train_df,test_df)

        return classifier_model