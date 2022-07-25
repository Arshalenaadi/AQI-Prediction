import streamlit as st
import pickle
import numpy as np



model=pickle.load(open('model.pkl','rb'))
data= pickle.load(open('data.pkl','rb'))

st.title('AQI Prediction')
opt = st.selectbox(
     'Enter the year',
     (2022,2023,2024,2025,2030,2035))

opt1= st.selectbox(
     'Enter the state',
     (data['State'].unique()))
opt1=data['State'].replace({'Gujarat':0, 'Mizoram':1, 'Andhra Pradesh':2, 'Punjab':3, 'Karnataka':4,\
                       'Madhya Pradesh':5, 'Odisha':6, 'Chandigarh':7, 'Tamilnadu':8, 'Delhi':9,\
                       'Kerala':10, 'Haryana':11, 'Assam':12, 'Telengana':13, 'Rajasthan':14,\
                       'Jharkhand':15, 'West Bengal':16, 'Uttar Pradesh':17,'Maharashtra':18,\
                       'Bihar':19, 'Meghalaya':20},inplace=True)
     
     


opt2 = st.selectbox(
     'Enter the City',
     (data['City'].unique()))
opt2=data['City'].replace({'Ahmedabad':0, 'Aizawl':1, 'Amaravati':2, 'Amritsar':3, 'Bengaluru':4,\
                      'Bhopal':5, 'Brajrajnagar':6, 'Chandigarh':7, 'Chennai':8, 'Coimbatore':9,\
                      'Delhi':10, 'Ernakulam':11, 'Gurugram':12, 'Guwahati':13, 'Hyderabad':14,\
                      'Jaipur':15, 'Jorapokhar':16, 'Kochi':17, 'Kolkata':18, 'Lucknow':19, 'Mumbai':20,\
                      'Patna':21, 'Shillong':22, 'Talcher':23,'Thiruvananthapuram':24,'Visakhapatnam':25},inplace=True)   

opt3 = st.selectbox(
     'Enter the PM value',
     (data['PM'].unique()))

opt4 = st.selectbox(
     'Enter the CO value',
     (data['CO_subindex'].unique()))                

opt5= st.selectbox(
     'Enter the O3 value',
     (data['O3_subindex'].unique())) 
opt6= st.selectbox(
     'Enter the Ni value',
     (data['Ni'].unique()))
opt7= st.selectbox(
     'Enter the SO value',
     (data['SO2_subindex'].unique()))     
         




def forecasting():
     from lightgbm import LGBMRegressor
     
     x_predict = [opt,opt1,opt2,opt3,opt4,opt5,opt6,opt7]
     import numpy as np
     x_predict = np.array(x_predict).reshape(1,-1)
     predicted_value = model.predict(x_predict)    
     return predicted_value    


if st.button('Forecast'):
     pred= forecasting()
     st.write('Forecasted air quality index',pred)


    

    
