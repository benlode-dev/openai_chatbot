import streamlit as st
from openai import OpenAI

# OpenAI API key stored in Streamlit secrets
openai_api_key = st.secrets["openai_api_key"]

# Set the OpenAI key
client = OpenAI(api_key=openai_api_key)

# Set up the Streamlit interface for chat
st.title("Chat with AI")
user_input = st.text_input("Type your message here:")

# When the user sends a message
if st.button("Send"):
    # Ensure the user has typed something
    if user_input:
        try:
            # Send the message to OpenAI's API using the new method
            response = client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": user_input}])

            # Display the response
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please type a message.")
