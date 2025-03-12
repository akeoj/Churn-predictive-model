import streamlit as st
from mode import *


def main():
    st.title("Expresso Telecommunication Churn Prediction")

    user_id = st.selectbox("Insert your ID", (cat_col["user_id"]))
    region = st.selectbox("Insert your Region", (cat_col["REGION"]))
    tenure = st.selectbox("Insert your Subscription", (cat_col["TENURE"]))
    montant = st.number_input("Enter your Number", value=None)
    frequent_rech = st.number_input("Insert the frequency of your recharge", value=None)
    revenue = st.number_input("Insert the revenue", value=None)
    arpu_segment = st.number_input("Insert the Segment", value=None)
    Frequency = st.number_input("Insert the Frequency Number", value=None)
    data_vol = st.number_input("Insert the data volume of your recharge", value=None)
    On_net = st.number_input("Insert the On Net Revenue", value=None)
    orange = st.number_input("Insert the Orange", value=None)
    tigo = st.number_input("Insert the Tigo", value=None)
    zone1 = st.number_input("Insert value for zone 1", value=None)
    zone2 = st.number_input("Insert value for zone 2", value=None)
    mrg = st.text_input("Insert the MRG") #value=None)
    regularity = st.number_input("Insert the regularity", value=None)
    top_pack = st.selectbox("Insert your subscription pack", (cat_col["TOP_PACK"]))
    freq_top_pack = st.number_input("Insert the frequency pack number", value= None)


    CHURN = ""

    if st.button("Predict"):
        CHURN = prediction([user_id, region, tenure, montant, frequent_rech, revenue, arpu_segment, Frequency, data_vol, On_net, 
                            orange, tigo, zone1, zone2, mrg, regularity, top_pack, freq_top_pack])
        
    st.success(CHURN)



if __name__ == "__main__":
    main()  