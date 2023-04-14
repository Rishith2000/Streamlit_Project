import lazypredict
from lazypredict.Supervised import LazyClassifier
from lazypredict.Supervised import LazyRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error
import streamlit as st 

st.subheader("Automation")

if 'data' not in st.session_state:
    st.warning('Upload a CSV file in Upload Data page')
else:
    @st.cache
    def classifier(X_train, X_test, y_train, y_test):
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        clf = LazyClassifier(verbose=1, ignore_warnings=True, custom_metric = None)
        models,predictions = clf.fit(X_train_scaled, X_test_scaled, y_train, y_test)
        return models,predictions

    @st.cache
    def regressor(X_train, X_test, y_train, y_test):
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        reg = LazyRegressor(verbose=1, ignore_warnings=False, custom_metric = None)
        models,predictions = reg.fit(X_train_scaled, X_test_scaled, y_train, y_test)
        return models,predictions


    data=st.session_state['data']
    c=st.selectbox('Select the weather the data set comes under Classification or Regression',[' ','Classification','Regression'],key="<uniquevalueofsomesort>")
    if(c=='Classification'):
        
        X=data.copy()
        l=[" "]
        l.extend(data.columns)
        v=st.selectbox('Please select the target column',l,key = "156")
        if(v!=" "):
            y=X[v]
    #st.write(y)
            X.drop(v,axis=1,inplace=True)
        #st.write(X)

            ratio=st.slider(label='Select the split ratio',min_value=0.0,max_value=1.0,step=0.1,value=0.8)

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1-ratio)

        

        ### fitting data in LazyClassifier
        
            models,predictions=classifier(X_train, X_test, y_train, y_test)
            st.write(models)

            # model evaluation
            if len(models) > 0:
                best_model = models.iloc[0]
                st.write("Best Model: ", best_model[0])
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)
                y_pred = best_model[1].predict(X_test_scaled)
                score = accuracy_score(y_test, y_pred)
                st.write("Accuracy: ", score)

    if(c=='Regression'):
        X=data.copy()
        l=[" "]
        l.extend(data.columns)
        v=st.selectbox('Please select the target column',l)
        if(v!=" "):

            y=X[v]

            X.drop(v,axis=1,inplace=True)
    

            ratio=st.slider(label='Select the split ratio',min_value=0.0,max_value=1.0,step=0.1,value=0.8)

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=ratio)
        
            models,predictions=regressor(X_train, X_test, y_train, y_test)
            st.write(models)

            # model evaluation
            if len(models) > 0:
                best_model = models.iloc[0]
                st.write("Best Model: ", best_model[0])
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)
                y_pred = best_model[1].predict(X_test_scaled)
                score = r2_score(y_test, y_pred)
                st.write("R2 Score: ", score)
                mse = mean_squared_error(y_test, y_pred)
                st.write("Mean Squared Error: ", mse)



    

    
    
   
