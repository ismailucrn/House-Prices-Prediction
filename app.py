import pickle
import pandas as pd
import numpy as np
import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))
target_encoder=pickle.load(open("target_encoder.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

st.title("House Price Prediction")
st.write("Evin fiyatını tahmin etmek için öncelikle bazı bilgilere ihtiyacımız var.")

lotarea = st.number_input("Lütfen LotArea değerini giriniz: ")
grlivarea = st.number_input("Lütfen GrLivArea değerini giriniz: ")
bsmtunfsf = st.number_input("Lütfen BsmtUnfSF değerini giriniz: ")
totalbsmtsf = st.number_input("Lütfen TotalBsmtSF değerini giriniz: ")
garagearea = st.number_input("Lütfen GarageArea değerini giriniz: ")
firstflrsf = st.number_input("Lütfen 1stFlrSF değerini giriniz: ")
lotfrontage = st.number_input("Lütfen LotFrontage değerini giriniz: ")
yearbuilt = st.number_input("Lütfen YearBuilt değerini giriniz: ")
masvnrarea = st.number_input("Lütfen MasVnrArea değerini giriniz: ")
garageyrblt = st.number_input("Lütfen GarageYrBlt değerini giriniz: ")
neighborhood = st.selectbox("Lütfen Neighborhood değerini giriniz: ", df["Neighborhood"].unique())
secondndflrsf = st.number_input("Lütfen 2ndFlrSF değerini giriniz: ")
yearremodadd = st.number_input("Lütfen YearRemodAdd değerini giriniz: ")
openporchsf = st.number_input("Lütfen OpenPorchSF değerini giriniz: ")
mosold = st.number_input("Lütfen MoSold değerini giriniz: ")
overallqual = st.number_input("Lütfen OverallQual değerini giriniz: ")

#predict edilecek verileri bir dict'e atıyoruz (predict'e etkisi az olanları manuel olarak girdik)
data = {"MSSubClass": [50],
        "MSZoning": ["RL"],
        "LotFrontage": [lotfrontage],
        "LotArea": [lotarea],
        "LotShape": ["Reg"],
        "LandContour": ["Lvl"],
        "LotConfig": ["Inside"],
        "Neighborhood": [neighborhood],
        "Condition1": ["Norm"],
        "BldgType": ["1Fam"],
        "HouseStyle": ["1Story"],
        "OverallQual": [overallqual],
        "OverallCond": [5],
        "YearBuilt": [yearbuilt],
        "YearRemodAdd": [yearremodadd],
        "RoofStyle": ["Gable"],
        "Exterior1st": ["VinylSd"],
        "Exterior2nd": ["VinylSd"],
        "MasVnrType": ["None"],
        "MasVnrArea": [masvnrarea],
        "ExterQual": ["TA"],
        "ExterCond": ["TA"],
        "Foundation": ["PConc"],
        "BsmtQual": ["TA"],
        "BsmtExposure": ["No"],
        "BsmtFinType1": ["Unf"],
        "BsmtFinSF1": [383.5],
        "BsmtFinType2": ["Unf"],
        "BsmtUnfSF": [bsmtunfsf],
        "TotalBsmtSF": [totalbsmtsf],
        "HeatingQC": ["Ex"],
        "1stFlrSF": [firstflrsf],
        "2ndFlrSF": [secondndflrsf],
        "GrLivArea": [grlivarea],
        "BsmtFullBath": [0],
        "FullBath": [2.0],
        "HalfBath": [0],
        "BedroomAbvGr": [3],
        "KitchenQual": ["TA"],
        "TotRmsAbvGrd": [6],
        "Fireplaces": [1.0],
        "FireplaceQu": ["Gd"],
        "GarageType": ["Attchd"],
        "GarageYrBlt": [garageyrblt],
        "GarageFinish": ["Unf"],
        "GarageCars": [2.0],
        "GarageArea": [garagearea],
        "WoodDeckSF": [0],
        "OpenPorchSF": [openporchsf],
        "Fence": ["MnPrv"],
        "MoSold": [mosold],
        "YrSold": [2008],
        "SaleType": ["WD"],
        "SaleCondition": ["Normal"]}

# predict edilecek verileri dataframe'e çeviriyoruz
data = pd.DataFrame(data)

# tüm data'ya target encoding uyguluyoruz
data = target_encoder.transform(data)

# predict ediyoruz
pred = model.predict(data)

# predict butonuna basıldığında predict edilen değeri büyük puntolarla yazdırıyoruz ve ortalıyoruz
if st.button("Predict"):
    st.header("Tahmini ev fiyatı: ")
    st.title("$" + str(np.round(pred[0], 2)))


