
#  BASE EEEEE Styling 1

import streamlit as st
import requests
import json
import logging

# Custom CSS for fixed header and input at the bottom with improved colors and fonts
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');
    
    /* Set background color for the entire page */
    .stApp {
        background-color: #FAFAFA; /* Light grey background */
        font-family: 'Poppins', sans-serif; /* Modern font */
        padding-bottom: 100px; /* Ensure there's room for the input at the bottom */
    }

    /* Custom header style with fixed position */
    .custom-header {
        font-size: 36px;
        font-weight: bold;
        color: #FFFFFF;
        text-align: center;
        padding: 20px;
        background-color: #333333;
        border-radius: 0px 0px 10px 10px;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000; /* Ensure it stays above other content */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Slight shadow */
    }

    /* Push the rest of the content below the fixed header */
    .stApp {
        padding-top: 120px;
    }
            

    .footer-input {
        position: fixed !important;
        bottom: 0 !important;
        width: 100% !important;
        background-color: #f1f1f1 !important;
        padding: 10px !important;
        box-shadow: 0 -1px 10px rgba(0, 0, 0, 0.1) !important;
    }
    .footer-input input {
        width: 100% !important;
        padding: 10px !important;
        font-size: 16px !important;
    }

    /* Chat bubbles for user and bot messages */
    .user-bubble {
        background-color: #e6f7ff;
        padding: 10px;
        border-radius: 10px;
        color: #333333;
        max-width: 80%;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        word-wrap: break-word;
    }
    
    .bot-bubble {
        background-color: #bf00ff;
        padding: 10px;
        border-radius: 10px;
        color: #ffffff;
        text-align: right;
        max-width: 80%;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        word-wrap: break-word;
    }

    /* Hide the Streamlit footer */
    footer {
        visibility: hidden;
    }

    /* Hide the Streamlit header */
    header {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

# Add a custom header
st.markdown("<div class='custom-header'>Food Recommendation System</div>", unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if "messages" not in st.session_state:
    st.session_state.messages = []  # List to store chat messages
if "user_input" not in st.session_state:
    st.session_state.user_input = ""  # To store user input text

# Create a container for the chat interface
chat_container = st.container()

def display_messages():
    with chat_container:
        for msg in st.session_state.messages:
            if msg["sender"] == "user":  # User messages
                col1, col2 = st.columns([4, 5])
                with col1:
                    st.markdown(f"""
                        <div class='user-bubble'>
                        {msg['message']}
                        </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.empty()
            else:  # Bot messages
                col1, col2 = st.columns([5, 3])
                with col2:
                    st.markdown(f"""
                        <div class='bot-bubble'>
                        {msg['message']}
                        </div>
                    """, unsafe_allow_html=True)
                with col1:
                    st.empty()

def call_api(user_input):
    api_url = "http://172.29.8.241:7071/api/tomato"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "user_message": user_input
    }

    try:
        # Make the POST request
        response = requests.post(api_url, headers=headers, json=payload)
        res = response.json()
        print(res['response'])
        # Check if the response is successful
        if response.status_code == 200:
            return res['response']
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error occurred while calling the API: {e}"

# Function to handle user input and display new messages
def handle_user_input():
    user_input = st.session_state.user_input_text  # Get the user input
    if user_input:  # If there's input
        st.session_state.messages.append({"sender": "user", "message": user_input})  # Add user message

        # Call the API and get the bot response
        bot_response = call_api(user_input)

        # Append bot response to the message list
        st.session_state.messages.append({"sender": "bot", "message": bot_response})
        
        st.session_state.user_input_text = ""  # Clear the user inputs

# Input field and button for the user to type messages
input_placeholder = st.empty()

# Place the input at the footer
st.markdown('<div class="footer-input">', unsafe_allow_html=True)
user_input = input_placeholder.text_input("Type your message here...", value=st.session_state.user_input, key="user_input_text", on_change=handle_user_input)
st.markdown('</div>', unsafe_allow_html=True)

# Display the messages in the chat container
display_messages()































####################################################












# Styling 1

import streamlit as st
import requests
import json
import logging

# Custom CSS for fixed header and input at the bottom with improved colors and fonts
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');
    
    /* Set background color for the entire page */
    .stApp {
        background-color: #FAFAFA; /* Light grey background */
        font-family: 'Poppins', sans-serif; /* Modern font */
        padding-bottom: 100px; /* Ensure there's room for the input at the bottom */
    }

    /* Custom header style with fixed position */
    .custom-header {
        font-size: 36px;
        font-weight: bold;
        color: #FFFFFF;
        text-align: center;
        padding: 20px;
        background-color: #333333;
        border-radius: 0px 0px 10px 10px;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000; /* Ensure it stays above other content */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Slight shadow */
    }

    /* Push the rest of the content below the fixed header */
    .stApp {
        padding-top: 120px;
    }
    
    .footer-input input {
    width: 100% !important;
    padding: 12px !important; /* Slightly larger padding for comfort */
    font-size: 16px !important;
    border: 1px solid #ccc !important; /* Light gray border */
    border-radius: 8px !important; /* Rounded corners for a modern look */
    outline: none !important;
    background-color: #f8f8f8 !important; /* Softer background color */
}

            

    .footer-input {
        position: fixed !important;
        bottom: 0 !important;
        width: 100% !important;
        background-color: #f1f1f1 !important;
        padding: 10px !important;
        box-shadow: 0 -1px 10px rgba(0, 0, 0, 0.1) !important;
    }
    # .footer-input input {
    #     width: 100% !important;
    #     padding: 10px !important;
    #     font-size: 16px !important;
    # }

    /* Chat bubbles for user and bot messages */
    .user-bubble {
        background-color: #e6f7ff;
        padding: 10px;
        border-radius: 10px;
        color: #333333;
        max-width: 80%;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        word-wrap: break-word;
    }
    
    .bot-bubble {
        background-color: #bf00ff;
        padding: 10px;
        border-radius: 10px;
        color: #ffffff;
        text-align: right;
        max-width: 80%;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        word-wrap: break-word;
    }

    /* Hide the Streamlit footer */
    footer {
        visibility: hidden;
    }

    /* Hide the Streamlit header */
    header {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

# Add a custom header
st.markdown("<div class='custom-header'>Food Recommendation System</div>", unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if "messages" not in st.session_state:
    st.session_state.messages = []  # List to store chat messages
if "user_input" not in st.session_state:
    st.session_state.user_input = ""  # To store user input text

# Create a container for the chat interface
chat_container = st.container()

def display_messages():
    with chat_container:
        for msg in st.session_state.messages:
            if msg["sender"] == "user":  # User messages
                col1, col2 = st.columns([4, 5])
                with col1:
                    st.markdown(f"""
                        <div class='user-bubble'>
                        {msg['message']}
                        </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.empty()
            else:  # Bot messages
                col1, col2 = st.columns([5, 3])
                with col2:
                    st.markdown(f"""
                        <div class='bot-bubble'>
                        {msg['message']}
                        </div>
                    """, unsafe_allow_html=True)
                with col1:
                    st.empty()

def call_api(user_input):
    api_url = "http://172.29.8.241:7071/api/tomato"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "user_message": user_input
    }

    try:
        # Make the POST request
        response = requests.post(api_url, headers=headers, json=payload)
        res = response.json()
        print(res['response'])
        # Check if the response is successful
        if response.status_code == 200:
            return res['response']
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error occurred while calling the API: {e}"

# Function to handle user input and display new messages
def handle_user_input():
    user_input = st.session_state.user_input_text  # Get the user input
    if user_input:  # If there's input
        st.session_state.messages.append({"sender": "user", "message": user_input})  # Add user message

        # Call the API and get the bot response
        bot_response = call_api(user_input)

        # Append bot response to the message list
        st.session_state.messages.append({"sender": "bot", "message": bot_response})
        
        st.session_state.user_input_text = ""  # Clear the user inputs

# Input field and button for the user to type messages
input_placeholder = st.empty()

# Place the input at the footer
st.markdown('<div class="footer-input">', unsafe_allow_html=True)
user_input = input_placeholder.text_input("Type your message here...", value=st.session_state.user_input, key="user_input_text", on_change=handle_user_input)
st.markdown('</div>', unsafe_allow_html=True)

# Display the messages in the chat container
display_messages()

















# # API
# import streamlit as st
# import requests
# import json

# # Set up the title of the app
# st.title("Food Recommendation System")

# # Initialize session state variables if they don't exist
# if "messages" not in st.session_state:
#     st.session_state.messages = []  # List to store chat messages
# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""  # To store user input text

# # Create a container for the chat interface
# chat_container = st.container()


# #####
# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":  # User messages
#                 col1, col2 = st.columns([4, 5])
#                 with col1:
#                     st.markdown(f"""
#                         <div style='background-color: #e6f7ff; padding: 10px; border-radius: 10px; width: fit-content; max-width: 80%; word-wrap: break-word;'>
#                         <span style='color: #bf00ff;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()
#             else:  # Bot messages
#                 col1, col2 = st.columns([5, 1])
#                 with col2:
#                     st.markdown(f"""
#                         <div style='background-color: #bf00ff; padding: 10px; border-radius: 10px; text-align: right; width: fit-content; max-width: 80%; word-wrap: break-word;'>
#                         <span style='color: white;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()
# #####


# ###
# def call_api(user_input):
#     api_url = "http://172.29.8.241:7071/api/tomato"
#     headers = {
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "user_message": user_input
#     }

#     try:
#         # Make the POST request
#         response = requests.post(api_url, headers=headers, data=json.dumps(payload))

#         # Check if the response is successful
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return f"Error: {response.status_code}"
#     except Exception as e:
#         return f"Error occurred while calling the API: {e}"

# ###


# # Function to handle user input and display new messages
# def handle_user_input():
#     user_input = st.session_state.user_input_text  # Get the user input
#     if user_input:  # If there's input
#         st.session_state.messages.append({"sender": "user", "message": user_input})  # Add user message

#         # Call the API and get the bot response
#         bot_response = call_api(user_input)

#         # Append bot response to the message list
#         st.session_state.messages.append({"sender": "bot", "message": bot_response})
        
#         st.session_state.user_input_text = ""  # Clear the user inputs

# # Input field and button for the user to type messages
# input_placeholder = st.empty()
# user_input = input_placeholder.text_input("Type your message here...", value=st.session_state.user_input, key="user_input_text", on_change=handle_user_input)

# # Display the messages in the chat container
# display_messages()

















# display_messages



# Function to display the messages in the chat container
# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":  # User messages
#                 col1, col2 = st.columns([5, 1])
#                 with col1:
#                     st.markdown(f"""
#                         <div style='background-color: #e6f7ff; padding: 10px; border-radius: 10px; width: fit-content; max-width: 80%;'>
#                         <span style='color: #bf00ff;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()
#             else:  # Bot messages
#                 col1, col2 = st.columns([1, 5])
#                 with col2:
#                     st.markdown(f"""
#                         <div style='background-color: #bf00ff; padding: 10px; border-radius: 10px; text-align: right; width: fit-content; max-width: 80%; float: right;'>
#                         <span style='color: white;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()




#call_api

# # Function to make the POST request (equivalent to the curl command)
# def call_api(user_input):
#     # Define the API URL (same as in the curl command)
#     api_url = "http://172.29.8.241:7071/api/tomato"
    
#     # Define the headers and payload to match the curl command
#     headers = {
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "user_message": user_input  # Sending the user's message as 'user_message' in the request body
#     }
    
#     try:
#         # Make the POST request
#         response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        
#         # Log response status and text to debug if necessary
#         st.write(f"Response Status Code: {response.status_code}")
#         st.write(f"Response Content: {response.text}")

#         # Check if the response is successful (status code 200)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return f"Error: {response.status_code}, {response.text}"
#     except Exception as e:
#         return f"Error occurred while calling the API: {e}"



























# import streamlit as st

# # Set the page title
# st.title("Restaurants Recomendation System")

# # Initialize the session state to keep track of conversation and input
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""

# # Container for displaying the conversation history
# chat_container = st.container()

# # Function to display messages in the chat
# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":
#                 col1, col2 = st.columns([5, 1])
#                 with col2:
#                     st.markdown(f"""
#                         <div style='background-color: #e6f7ff; padding: 5px; border-radius: 5px; text-align: right;'>
#                         <span style='color: #bf00ff;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()
#             else:
#                 col1, col2 = st.columns([1, 5])
#                 with col1:
#                     st.markdown(f"""
#                         <div style='background-color: #bf00ff; padding: 5px; border-radius: 5px;'>
#                         <span>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()

# # Display existing messages
# display_messages()

# # Create a placeholder for the input field so we can re-render it dynamically
# input_placeholder = st.empty()

# # Text input box for user input (re-rendered by placeholder)
# user_input = input_placeholder.text_input("Type your message here...", value=st.session_state.user_input, key="user_input_text")

# # Button to send the message
# if st.button("Send"):
#     if user_input:
#         # Add user's message to the conversation
#         st.session_state.messages.append({"sender": "user", "message": user_input})

#         # Add bot's response (placeholder for now)
#         bot_response = "This is a bot response."
#         st.session_state.messages.append({"sender": "bot", "message": bot_response})

#         # Clear the input field by re-rendering the input widget (no key needed here)
#         st.session_state.user_input = ""
#         input_placeholder.text_input("Type your message here...", value="")

#     # Re-display the updated conversation
#     display_messages()























# # MAINNNNN
# import streamlit as st

# # Set up the title of the app
# st.title("Food Recommendation System")

# # Initialize session state variables if they don't exist
# if "messages" not in st.session_state:
#     st.session_state.messages = []  # List to store chat messages
# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""  # To store user input text

# # Create a container for the chat interface
# chat_container = st.container()

# # Function to display the messages in the chat container
# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":  # User messages
#                 col1, col2 = st.columns([5, 1])
#                 with col1:
#                     st.markdown(f"""
#                         <div style='background-color: #e6f7ff; padding: 10px; border-radius: 10px; width: fit-content; max-width: 80%;'>
#                         <span style='color: #bf00ff;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()
#             else:  # Bot messages
#                 col1, col2 = st.columns([1, 5])
#                 with col2:
#                     st.markdown(f"""
#                         <div style='background-color: #bf00ff; padding: 10px; border-radius: 10px; text-align: right; width: fit-content; max-width: 80%; float: right;'>
#                         <span style='color: white;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()

# # Function to handle user input and display new messages
# def handle_user_input():
#     user_input = st.session_state.user_input_text  # Get the user input
#     if user_input:  # If there's input
#         st.session_state.messages.append({"sender": "user", "message": user_input})  # Add user message
#         bot_response = "This is a Test response."  # Simulated bot response
#         st.session_state.messages.append({"sender": "bot", "message": bot_response})  # Add bot response
#         st.session_state.user_input_text = ""  # Clear the user inputs

# # Input field and button for the user to type messages
# input_placeholder = st.empty()
# user_input = input_placeholder.text_input("Type your message here...", value=st.session_state.user_input, key="user_input_text", on_change=handle_user_input)

# # Display the messages in the chat container
# display_messages()























# # MAIN
# import streamlit as st
# st.title("Food Recommendation System")
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""
# chat_container = st.container()

# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":
#                 col1, col2 = st.columns([5, 1])
#                 with col1:
#                     st.markdown(f"""
#                         <div style='background-color: #e6f7ff; padding: 10px; border-radius: 10px; width: fit-content; max-width: 80%;'>
#                         <span style='color: #bf00ff;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()
#             else:
#                 col1, col2 = st.columns([1, 5])
#                 with col2:
#                     st.markdown(f"""
#                         <div style='background-color: #bf00ff; padding: 10px; border-radius: 10px; text-align: right; width: fit-content; max-width: 80%;float: right;'>
#                         <span style='color: white;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()

# display_messages()

# input_placeholder = st.empty()

# user_input = input_placeholder.text_input("Type your message here...", value=st.session_state.user_input, key="user_input_text")

# if st.button("Send"):
#     if user_input:
#         st.session_state.messages.append({"sender": "user", "message": user_input})

#         bot_response = "This is a Test response."
#         st.session_state.messages.append({"sender": "bot", "message": bot_response})

#         st.session_state.user_input = ""
#         input_placeholder.text_input("Type your message here...", value="")

#     display_messages()



















# V2
# import streamlit as st

# # Set the page title
# st.title("Food Recommendation System")

# # Initialize session state for storing messages and user input
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""

# # Function to display messages in the chat
# def display_messages():
#     for msg in st.session_state.messages:
#         if msg["sender"] == "user":
#             col1, col2 = st.columns([5, 1])
#             with col1:
#                 st.markdown(f"""
#                     <div style='background-color: #e6f7ff; padding: 10px; border-radius: 10px; width: fit-content; max-width: 80%;'>
#                     <span style='color: #bf00ff;'>{msg['message']}</span>
#                     </div>
#                 """, unsafe_allow_html=True)
#             with col2:
#                 st.empty()
#         else:
#             col1, col2 = st.columns([1, 5])
#             with col2:
#                 st.markdown(f"""
#                     <div style='background-color: #bf00ff; padding: 10px; border-radius: 10px; text-align: right; width: fit-content; max-width: 80%; float: right;'>
#                     <span style='color: white;'>{msg['message']}</span>
#                     </div>
#                 """, unsafe_allow_html=True)
#             with col1:
#                 st.empty()

# # Input box for user message
# user_input = st.text_input("Type your message here...", key="user_input_text")

# # Button to send the message
# if st.button("Send"):
#     if user_input.strip() != "":  # Check if the input is not empty
#         # Append user's message
#         st.session_state.messages.append({"sender": "user", "message": user_input})

#         # Simulate bot's response (you can replace this with actual logic)
#         bot_response = "This is a Test response."
#         st.session_state.messages.append({"sender": "bot", "message": bot_response})

#         # Clear the input after sending the message
#         st.session_state.user_input = ""  # Ensure input box is cleared

# # After processing the button click, redisplay the messages
# display_messages()







# V1
# import streamlit as st

# # Set the page title
# st.title("Food Recommendation System")

# # Initialize session state for storing messages and user input
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""

# # Container for displaying chat messages
# chat_container = st.container()

# # Function to display messages in the chat
# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":
#                 col1, col2 = st.columns([5, 1])
#                 with col1:
#                     st.markdown(f"""
#                         <div style='background-color: #e6f7ff; padding: 10px; border-radius: 10px; width: fit-content; max-width: 80%;'>
#                         <span style='color: #bf00ff;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()
#             else:
#                 col1, col2 = st.columns([1, 5])
#                 with col2:
#                     st.markdown(f"""
#                         <div style='background-color: #bf00ff; padding: 10px; border-radius: 10px; text-align: right; width: fit-content; max-width: 80%; float: right;'>
#                         <span style='color: white;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()

# # Display existing messages
# display_messages()

# # Input box for user message
# user_input = st.text_input("Type your message here...", value=st.session_state.user_input, key="user_input_text")

# # Send button functionality
# if st.button("Send"):
#     if user_input.strip() != "":  # Check if the input is not empty
#         # Append user's message
#         st.session_state.messages.append({"sender": "user", "message": user_input})

#         # Simulate bot's response (you can replace this with actual logic)
#         bot_response = "This is a Test response."
#         st.session_state.messages.append({"sender": "bot", "message": bot_response})

#         # Clear the input after sending the message
#         st.session_state.user_input = ""
#     else:
#         st.warning("Please enter a message before sending!")

# # After the message is processed, redisplay messages
# display_messages()









# import streamlit as st

# # Custom CSS to fix the input box at the bottom and make the chat scrollable
# st.markdown("""
#     <style>
#     .chat-container {
#         height: calc(100vh - 150px); /* Adjust to make space for the input box */
#         overflow-y: auto;
#         padding-bottom: 60px;
#         padding-top: 20px;
#     }
#     .chat-input-container {
#         position: fixed;
#         bottom: 0;
#         width: 100%;
#         background-color: white;
#         padding: 10px;
#         border-top: 1px solid #ccc;
#     }
#     .stTextInput {
#         width: 80% !important;
#         display: inline-block;
#     }
#     .stButton {
#         display: inline-block;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Set the page title
# st.title("Food Recommendation System")

# # Initialize the session state to keep track of conversation and input
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""

# # Scrollable container for chat messages
# st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
# chat_container = st.container()

# # Function to display chat messages
# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":
#                 col1, col2 = st.columns([5, 1])
#                 with col1:
#                     st.markdown(f"""
#                         <div style='background-color: #e6f7ff; padding: 10px; border-radius: 10px; width: fit-content; max-width: 80%;'>
#                         <span style='color: #bf00ff;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()
#             else:
#                 col1, col2 = st.columns([1, 5])
#                 with col2:
#                     st.markdown(f"""
#                         <div style='background-color: #bf00ff; padding: 10px; border-radius: 10px; text-align: right; width: fit-content; max-width: 80%; float: right;'>
#                         <span style='color: white;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()

# # Display chat messages initially
# display_messages()
# st.markdown("</div>", unsafe_allow_html=True)

# # Fix the input box at the bottom
# st.markdown("<div class='chat-input-container'>", unsafe_allow_html=True)
# with st.form(key='input_form', clear_on_submit=True):
#     user_input = st.text_input("Type your message here...", value="", key="user_input_text")
#     submit_button = st.form_submit_button(label="Send")
# st.markdown("</div>", unsafe_allow_html=True)

# # Handle the form submission
# if submit_button and user_input:
#     # Add user's message to the conversation
#     st.session_state.messages.append({"sender": "user", "message": user_input})

#     # Add bot's response (placeholder for now)
#     bot_response = "This is a Test response."
#     st.session_state.messages.append({"sender": "bot", "message": bot_response})

#     # Re-display updated conversation
#     display_messages()









# import streamlit as st

# st.title("Food Recommendation System")

# # Initialize the session state
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""

# chat_container = st.container()

# # Function to display chat messages
# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":
#                 col1, col2 = st.columns([5, 1])
#                 with col1:
#                     st.markdown(f"""
#                         <div style='background-color: #e6f7ff; padding: 10px; border-radius: 10px; width: fit-content; max-width: 80%;'>
#                         <span style='color: #bf00ff;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()
#             else:
#                 col1, col2 = st.columns([1, 5])
#                 with col2:
#                     st.markdown(f"""
#                         <div style='background-color: #bf00ff; padding: 10px; border-radius: 10px; text-align: right; width: fit-content; max-width: 80%;float: right;'>
#                         <span style='color: white;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()

# display_messages()

# # Aligning input box and button side by side
# col_input, col_button = st.columns([4, 1])

# with col_input:
#     # Text input box
#     user_input = st.text_input("", value=st.session_state.user_input, key="user_input_text", placeholder="Type your message here...")

# with col_button:
#     # Button to send the message
#     if st.button("Send"):
#         if user_input:
#             # Add user's message
#             st.session_state.messages.append({"sender": "user", "message": user_input})

#             # Bot's response
#             bot_response = "This is a bot response."
#             st.session_state.messages.append({"sender": "bot", "message": bot_response})

#             # Clear the input field after sending
#             st.session_state.user_input = ""

#         # Re-display updated conversation
#         display_messages()


