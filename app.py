# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 01:03:50 2021

@author: kolhe
"""


import streamlit as st
import pickle
import numpy as np

model=pickle.load(open('model.pkl','rb'))


def predict_price(Year, Present_Price, Kms_Driven, Owner, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual):
    res=np.array([[Year, Present_Price, Kms_Driven, Owner, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]]).astype(np.float64)
    prediction=model.predict(res)
    
    return(prediction[0])
    #pred='{0:.{1}f}'.format(prediction[0][0], 2)
    #return float(pred)


def main():
    st.title("Streamlit Tutorial")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Car Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    Year = st.number_input("Year Of Purchase")
    Present_Price = st.number_input("Present Price")
    Kms_Driven = st.number_input("Kms Driven")
    Owner = st.number_input("Number of owners")
    
    fueltype = st.selectbox("Select the fuel type", ['Petrol', 'CNG', 'Diesel'])
    Fuel_Type_Diesel = 0
    Fuel_Type_Petrol = 0
    if(fueltype == 'CNG'):
        Fuel_Type_Diesel = 0
        Fuel_Type_Petrol = 0
    elif(fueltype == 'Petrol'):
        Fuel_Type_Diesel = 0
        Fuel_Type_Petrol = 1
    if(fueltype == 'Diesel'):
        Fuel_Type_Diesel = 1
        Fuel_Type_Petrol = 0
    
    
    Seller_Type_Individual = 0
    sellertype = st.selectbox("Select the seller type", ['Dealer', 'Individual'])
    if(sellertype == 'Dealer'):
        Seller_Type_Individual = 0
        
    elif(sellertype == 'Individual'):
        Seller_Type_Individual = 1
    
    
    Transmission_Manual = 0
    trans = st.selectbox("Select the transmission type", ['Manual', 'Automatic'])
    if(trans == 'Manual'):
        Transmission_Manual = 1
        
    elif(trans == 'Automatic'):
        Transmission_Manual = 0

    


    if st.button("Predict"):               
        output=predict_price(Year, Present_Price, Kms_Driven, Owner, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual)
        
        output = round(output, 2)
        st.success('The selling price is {} lacs'.format(str(output)))


if __name__=='__main__':
    main()