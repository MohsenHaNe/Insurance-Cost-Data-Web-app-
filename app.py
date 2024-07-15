import streamlit as st
import pickle

# import Model
model = pickle.load(open('model.pkl','rb'))


# create app
def main():
  st.sidebar.header('Insurance Cost prediction')
  st.sidebar.text('A linear regression model has been used to predict the cost of insurance')
  # inputs
  age = st.slider('input your Age',0,100)
  sex = st.slider('what is your gender',0,1)
  bmi = st.slider('Enter your BMI',0.0,100.0)
  children = st.slider('how many children do you have?',0,5)
  smoker = st.slider('do you smoke؟',0,1)
  region = st.slider('where is yor region',0,3)

  inputs = [[age,sex,bmi,children,smoker,region]]

  if st.button('Predict'):
    res = model.predict(inputs).astype(float)
    st.success(f'Your insurance cost will be:{res}')


# run app
if __name__ == "__main__": # --> streamlit run app.py
  main()