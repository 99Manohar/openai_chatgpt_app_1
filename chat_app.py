from openai import OpenAI
import streamlit as st

#Read the API Key and Setup an OpenAI Client

f = open(r"C:\Users\HP\3D Objects\Desktop\GENAI\genai_apps\keys\openai_key.txt")
key = f.read()
client = OpenAI(api_key=key)

###############################
st.title("🤖 AI MCQ GENERATOR")

###############################

# #Take User's input
prompt = st.text_input("enter a datascience topic")

# #If the button is clicked, generate responses
if st.button("Generate") == True:

    response = client.chat.completions.create(

                model="gpt-3.5-turbo",
                messages=[
                {"role": "system", "content": """You are a helpful AI Assistant. 
                                            
                                           Given a Data Science topic you always generate 3 MCQ questions and answers for the test."""},
                {"role": "user", "content": prompt}
                ]
    )            
#     #Print the reponse on the web app
    st.write(response.choices[0].message.content)