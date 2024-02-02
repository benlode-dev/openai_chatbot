import streamlit as st
import openai
import toml

# Load the configuration for OpenAI API key
#config = toml.load(".streamlit/config.toml")
config = toml.load("config.toml")
openai_api_key = config["openai"]["api_key"]

# Set the OpenAI key
openai.api_key = openai_api_key

# Set up the Streamlit interface for chat
st.title("Chat with AI")
user_input = st.text_input("Type your message here:")

# When the user sends a message
if st.button("Send"):
    # Ensure the user has typed something
    if user_input:
        try:
            # Send the message to OpenAI's API using the new method
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are a helpful assistant."},
                          {"role": "user", "content": user_input}]
            )

            # Display the response
            st.write(response.choices[0].message['content'])
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please type a message.")

