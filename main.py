
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










# import streamlit as st
# import requests
# import json

# # Set up the title of the app
# st.title("Food Recommendation System")

# # Custom CSS for background color and other styles
# st.markdown("""
#     <style>
#     /* Set background color for the entire page */
#     .stApp {
#         background-color: #FF5733;
#     }

#     /* Style the input text box */
#     input[type="text"] {
#         background-color: #e6f7ff;
#         color: #bf00ff;
#         border: none;
#         border-radius: 10px;
#         padding: 10px;
#         width: 100%;
#     }

#     /* Hide the Streamlit footer */
#     footer {
#         visibility: hidden;
#     }

#     /* Hide the Streamlit header */
#     header {
#         visibility: hidden;
#     }
#     </style>
#     """, unsafe_allow_html=True)

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





#CSS
# # Custom CSS for background color and other styles including the header
# st.markdown("""
#     <style>
#     /* Set background color for the entire page */
#     .stApp {
#         background-color: #FF5733;
#     }

#     /* Custom header style */
#     .custom-header {
#         font-size: 36px;
#         font-weight: bold;
#         color: #FFFFFF;
#         text-align: center;
#         padding: 20px;
#         background-color: #333333;
#         border-radius: 0px 0px 10px 10px;
#     }

#     /* Style the input text box */
#     input[type="text"] {
#         background-color: #e6f7ff;
#         color: #bf00ff;
#         border: none;
#         border-radius: 10px;
#         padding: 10px;
#         width: 100%;
#     }

#     /* Hide the Streamlit footer */
#     footer {
#         visibility: hidden;
#     }

#     /* Hide the Streamlit header */
#     header {
#         visibility: hidden;
#     }
#     /* Push content below header */
#     .main-content {
#         padding-top: 100px;  /* Adjust this to account for the header's height */
#     }
#     </style>
#     """, unsafe_allow_html=True)











### Working

# import streamlit as st
# import requests
# import json


# st.markdown("""
#     <style>
#     /* Set background color for the entire page */
#     .stApp {
#         background-color: #FF5733;
#     }

#     /* Custom header style with fixed position */
#     .custom-header {
#         font-size: 36px;
#         font-weight: bold;
#         color: #FFFFFF;
#         text-align: center;
#         padding: 20px;
#         background-color: #333333;
#         border-radius: 0px 0px 10px 10px;
#         position: fixed;
#         top: 0;
#         left: 0;
#         width: 100%;
#         z-index: 1000; /* Ensure it stays above other content */
#     }

#     /* Push the rest of the content below the fixed header */
#     .stApp {
#         padding-top: 100px;
#     }

#     /* Style the input text box */
#     input[type="text"] {
#         background-color: #e6f7ff;
#         color: #bf00ff;
#         border: none;
#         border-radius: 10px;
#         padding: 10px;
#         width: 100%;
#     }

#     /* Hide the Streamlit footer */
#     footer {
#         visibility: hidden;
#     }

#     /* Hide the Streamlit header */
#     header {
#         visibility: hidden;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Add a custom header
# st.markdown("<div class='custom-header'>Food Recommendation System</div>", unsafe_allow_html=True)

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
#                 col1, col2 = st.columns([5, 3])
#                 with col2:
#                     st.markdown(f"""
#                         <div style='background-color: #bf00ff; padding: 10px; border-radius: 10px; text-align: right; width: fit-content; max-width: 80%; word-wrap: break-word;'>
#                         <span style='color: white;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()

# #####

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









# # proper working main

# import streamlit as st
# import requests
# import json
# import logging

# # Custom CSS for fixed header and input at the bottom
# st.markdown("""
#     <style>
#     /* Set background color for the entire page */
#     .stApp {
#         background-color: #FF5733;
#         padding-bottom: 100px; /* Ensure there's room for the input at the bottom */
#     }

#     /* Custom header style with fixed position */
#     .custom-header {
#         font-size: 36px;
#         font-weight: bold;
#         color: #FFFFFF;
#         text-align: center;
#         padding: 20px;
#         background-color: #333333;
#         border-radius: 0px 0px 10px 10px;
#         position: fixed;
#         top: 0;
#         left: 0;
#         width: 100%;
#         z-index: 1000; /* Ensure it stays above other content */
#     }

#     /* Push the rest of the content below the fixed header */
#     .stApp {
#         padding-top: 100px;
#     }

#     /* Style the input text box and position it at the bottom */
#     .footer-input {
#         position: fixed;
#         bottom: 0;
#         left: 0;
#         width: 100%;
#         background-color: #333333;
#         padding: 10px;
#         z-index: 1000;  /* Ensure input stays above other content */
#         display: flex;
#         justify-content: center;
#     }

#     .footer-input input[type="text"] {
#         width: 90%; /* Adjust this to change the input width */
#         padding: 10px;
#         font-size: 16px;
#         border-radius: 10px;
#         border: none;
#         color: #bf00ff;
#     }

#     /* Hide the Streamlit footer */
#     footer {
#         visibility: hidden;
#     }

#     /* Hide the Streamlit header */
#     header {
#         visibility: hidden;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Add a custom header
# st.markdown("<div class='custom-header'>Food Recommendation System</div>", unsafe_allow_html=True)

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
#                 col1, col2 = st.columns([5, 3])
#                 with col2:
#                     st.markdown(f"""
#                         <div style='background-color: #bf00ff; padding: 10px; border-radius: 10px; text-align: right; width: fit-content; max-width: 80%; word-wrap: break-word;'>
#                         <span style='color: white;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()

# #####

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
#         response = requests.post(api_url, headers=headers, json=payload)
#         res = response.json()
#         print(res['response'])
#         # Check if the response is successful
#         if response.status_code == 200:
#             return res['response']
#         else:
#             return f"Error: {response.status_code}"
#     except Exception as e:
#         return f"Error occurred while calling the API: {e}"

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

# # Place the input at the footer
# st.markdown('<div class="footer-input">', unsafe_allow_html=True)
# user_input = input_placeholder.text_input("Type your message here...", value=st.session_state.user_input, key="user_input_text", on_change=handle_user_input)
# st.markdown('</div>', unsafe_allow_html=True)

# # Display the messages in the chat container
# display_messages()



#############################################





# Styling 1

import streamlit as st
import requests
import json
import logging
import base64

# # Custom CSS for fixed header and input at the bottom with improved colors and fonts
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');
    
#     /* Set background color for the entire page */
#     .stApp {
#         background-color: #FAFAFA; /* Light grey background */
#         font-family: 'Poppins', sans-serif; /* Modern font */
#         padding-bottom: 100px; /* Ensure there's room for the input at the bottom */
#     }

#     /* Custom header style with fixed position */
#     .custom-header {
#         font-size: 36px;
#         font-weight: bold;
#         color: #FFFFFF;
#         text-align: center;
#         padding: 20px;
#         background-color: #333333;
#         border-radius: 0px 0px 10px 10px;
#         position: fixed;
#         top: 0;
#         left: 0;
#         width: 100%;
#         z-index: 1000; /* Ensure it stays above other content */
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Slight shadow */
#     }

#     /* Push the rest of the content below the fixed header */
#     .stApp {
#         padding-top: 120px;
#     }
            

#     .footer-input {
#         position: fixed !important;
#         bottom: 0 !important;
#         width: 100% !important;
#         background-color: #f1f1f1 !important;
#         padding: 10px !important;
#         box-shadow: 0 -1px 10px rgba(0, 0, 0, 0.1) !important;
#     }
#     .footer-input input {
#         width: 100% !important;
#         padding: 10px !important;
#         font-size: 16px !important;
#     }

#     /* Chat bubbles for user and bot messages */
#     .user-bubble {
#         background-color: #e6f7ff;
#         padding: 10px;
#         border-radius: 10px;
#         color: #333333;
#         max-width: 80%;
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
#         word-wrap: break-word;
#     }
    
#     .bot-bubble {
#         background-color: #bf00ff;
#         padding: 10px;
#         border-radius: 10px;
#         color: #ffffff;
#         text-align: right;
#         max-width: 80%;
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
#         word-wrap: break-word;
#     }

#     /* Hide the Streamlit footer */
#     footer {
#         visibility: hidden;
#     }

#     /* Hide the Streamlit header */
#     header {
#         visibility: hidden;
#     }
#     </style>
#     """, unsafe_allow_html=True)


# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');
#     @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&display=swap');
    
#     /* Set background color for the entire page */
#     # .stApp {
#     #     background-color: #f4f4f9; /* Soft background */
#     #     # font-family: 'Poppins', sans-serif; /* Modern font */
#     #     padding-bottom: 100px; /* Ensure there's room for the input at the bottom */
#     # }
            
#     .stApp {
#     background-image: url("https://img.freepik.com/free-photo/top-view-frame-nourishing-meal_23-2148484626.jpg?t=st=1726367065~exp=1726370665~hmac=498132237c58b0591c5611242d7530b4bb6af9a94a42979aefddd4a4222380c7&w=1380"); /* Replace with your image URL */
#     background-size: cover; /* Ensures the image covers the entire background */
#     background-position: center; /* Centers the background image */
#     background-repeat: no-repeat; /* Prevents repeating the image */
#     font-family: 'Poppins', sans-serif; /* Modern font */
#     padding-bottom: 100px; /* Ensure there's room for the input at the bottom */
# }


#     # /* Custom header style with fixed position and gradient background */
#     # .custom-header {
#     #     font-size: 36px;
#     #     font-weight: bold;
#     #     color: #FFFFFF;
#     #     text-align: center;
#     #     padding: 20px;
#     #     background: linear-gradient(90deg, rgba(63,94,251,1) 0%, rgba(252,70,107,1) 100%);
#     #     border-radius: 0px 0px 15px 15px;
#     #     position: fixed;
#     #     top: 0;
#     #     left: 0;
#     #     width: 100%;
#     #     z-index: 1000; /* Ensure it stays above other content */
#     #     box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2); /* Slight shadow */
#     #     font-family: 'Comic Neue', sans-serif;
#     # }
            
#     .custom-header {
#         font-size: 36px;
#         font-weight: bold;
#         color: #FFFFFF;
#         text-align: center;
#         padding: 20px;
#         # background: linear-gradient(90deg, rgba(255, 94, 98, 1) 0%, rgba(255, 165, 0, 1) 100%); /* Soft red to orange gradient */
#         # background: linear-gradient(90deg, rgba(255, 150, 98, 1) 0%, rgba(255, 195, 100, 1) 100%);
#         background: linear-gradient(90deg, rgba(255, 94, 98, 0.9) 0%, rgba(255, 165, 0, 0.9) 100%);

#         border-radius: 0px 0px 15px 15px;
#         position: fixed;
#         top: 0;
#         left: 0;
#         width: 100%;
#         z-index: 1000; /* Ensure it stays above other content */
#         box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2); /* Slight shadow */
#         font-family: 'Comic Neue', sans-serif;
#     }


#     /* Push the rest of the content below the fixed header */
#     .stApp {
#         padding-top: 120px;
#     }
            

#     .footer-input input {
#     width: 100% !important;
#     padding: 12px !important;
#     font-size: 16px !important;
#     border-radius: 10px;
#     border: 2px solid #ccc;
#     box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
#     background-color: #ffffff; /* Bright white background for visibility */
#     color: #333333; /* Darker text color */
#     transition: all 0.3s ease;
#     }

#     .footer-input input::placeholder {
#         color: #040404 !important; /* Light grey for placeholder */
#         opacity: 1 !important; /* Ensures placeholder is visible */
#     }

#     .footer-input input:focus {
#         border-color: rgba(63,94,251,1);
#         box-shadow: 0 0 5px rgba(63,94,251,0.5);
#     }

#     /* Chat bubbles for user and bot messages with improved shadow and color */
#     .user-bubble {
#         background-color: #e6f7ff;
#         padding: 12px;
#         border-radius: 20px;
#         color: #333333;
#         max-width: 80%;
#         box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
#         word-wrap: break-word;
#     }
    
#     .bot-bubble {
#         background-color: #6050dc;
#         padding: 12px;
#         border-radius: 20px;
#         color: #ffffff;
#         text-align: right;
#         max-width: 80%;
#         box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
#         word-wrap: break-word;
#         transition: background-color 0.3s ease-in-out;
#     }

#     .bot-bubble:hover {
#         background-color: #4a3cb6;
#     }

#     /* Hide the Streamlit footer */
#     footer {
#         visibility: hidden;
#     }

#     /* Hide the Streamlit header */
#     header {
#         visibility: hidden;
#     }
#     </style>
#     """, unsafe_allow_html=True)



# # Add a custom header
# st.markdown("<div class='custom-header'>Tomato Recommendation System</div>", unsafe_allow_html=True)

# # Initialize session state variables if they don't exist
# if "messages" not in st.session_state:
#     st.session_state.messages = []  # List to store chat messages
# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""  # To store user input text

# # Create a container for the chat interface
# chat_container = st.container()

# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":  # User messages
#                 col1, col2 = st.columns([4, 5])
#                 with col1:
#                     st.markdown(f"""
#                         <div class='user-bubble'>
#                         {msg['message']}
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()
#             else:  # Bot messages
#                 col1, col2 = st.columns([5, 4])
#                 with col2:
#                     st.markdown(f"""
#                         <div class='bot-bubble'>
#                         {msg['message']}
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()

# def call_api(user_input):
#     api_url = "http://172.29.8.241:7071/api/yourtomato"
#     headers = {
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "user_message": user_input
#     }

#     try:
#         # Make the POST request
#         response = requests.post(api_url, headers=headers, json=payload)
#         res = response.json()
#         print(res['response'])
#         # Check if the response is successful
#         if response.status_code == 200:
#             return res['response']
#         else:
#             return f"Error: {response.status_code}"
#     except Exception as e:
#         return f"Error occurred while calling the API: {e}"

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

# # Place the input at the footer
# st.markdown('<div class="footer-input">', unsafe_allow_html=True)
# user_input = input_placeholder.text_input("Type your message here...", value=st.session_state.user_input, key="user_input_text", on_change=handle_user_input)
# st.markdown('</div>', unsafe_allow_html=True)

# # Display the messages in the chat container
# display_messages()










#######################################
# # Function to convert an image file to base64
# def get_base64_image(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode()

# # Step 1: Specify the path to your image
# image_path = "Back.jpg"  # Ensure the image is in the same folder as this script or provide a full path

# # Step 2: Convert the image to base64 format
# base64_image = get_base64_image(image_path)

# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');
#     @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&display=swap');
    
#     /* Set background color for the entire page */
#     # .stApp {
#     #     background-color: #f4f4f9; /* Soft background */
#     #     # font-family: 'Poppins', sans-serif; /* Modern font */
#     #     padding-bottom: 100px; /* Ensure there's room for the input at the bottom */
#     # }
            
#     .stApp {
#     # background-image: url("https://img.freepik.com/free-photo/top-view-frame-nourishing-meal_23-2148484626.jpg?t=st=1726367065~exp=1726370665~hmac=498132237c58b0591c5611242d7530b4bb6af9a94a42979aefddd4a4222380c7&w=1380"); /* Replace with your image URL */
#     background-image: url("data:image/png;base64,{base64_image}");
#     background-size: cover; /* Ensures the image covers the entire background */
#     background-position: center; /* Centers the background image */
#     background-repeat: no-repeat; /* Prevents repeating the image */
#     font-family: 'Poppins', sans-serif; /* Modern font */
#     padding-bottom: 100px; /* Ensure there's room for the input at the bottom */
# }


#     # /* Custom header style with fixed position and gradient background */
#     # .custom-header {
#     #     font-size: 36px;
#     #     font-weight: bold;
#     #     color: #FFFFFF;
#     #     text-align: center;
#     #     padding: 20px;
#     #     background: linear-gradient(90deg, rgba(63,94,251,1) 0%, rgba(252,70,107,1) 100%);
#     #     border-radius: 0px 0px 15px 15px;
#     #     position: fixed;
#     #     top: 0;
#     #     left: 0;
#     #     width: 100%;
#     #     z-index: 1000; /* Ensure it stays above other content */
#     #     box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2); /* Slight shadow */
#     #     font-family: 'Comic Neue', sans-serif;
#     # }
            
#     .custom-header {
#         font-size: 36px;
#         font-weight: bold;
#         color: #FFFFFF;
#         text-align: center;
#         padding: 20px;
#         # background: linear-gradient(90deg, rgba(255, 94, 98, 1) 0%, rgba(255, 165, 0, 1) 100%); /* Soft red to orange gradient */
#         # background: linear-gradient(90deg, rgba(255, 150, 98, 1) 0%, rgba(255, 195, 100, 1) 100%);
#         background: linear-gradient(90deg, rgba(255, 94, 98, 0.9) 0%, rgba(255, 165, 0, 0.9) 100%);

#         border-radius: 0px 0px 15px 15px;
#         position: fixed;
#         top: 0;
#         left: 0;
#         width: 100%;
#         z-index: 1000; /* Ensure it stays above other content */
#         box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2); /* Slight shadow */
#         font-family: 'Comic Neue', sans-serif;
#     }


#     /* Push the rest of the content below the fixed header */
#     .stApp {
#         padding-top: 120px;
#     }
            

#     .footer-input input {
#     width: 100% !important;
#     padding: 12px !important;
#     font-size: 16px !important;
#     border-radius: 10px;
#     border: 2px solid #ccc;
#     box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
#     background-color: #ffffff; /* Bright white background for visibility */
#     color: #333333; /* Darker text color */
#     transition: all 0.3s ease;
#     }

#     .footer-input input::placeholder {
#         color: #040404 !important; /* Light grey for placeholder */
#         opacity: 1 !important; /* Ensures placeholder is visible */
#     }

#     .footer-input input:focus {
#         border-color: rgba(63,94,251,1);
#         box-shadow: 0 0 5px rgba(63,94,251,0.5);
#     }

#     /* Chat bubbles for user and bot messages with improved shadow and color */
#     .user-bubble {
#         background-color: #e6f7ff;
#         padding: 12px;
#         border-radius: 20px;
#         color: #333333;
#         max-width: 80%;
#         box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
#         word-wrap: break-word;
#     }
    
#     .bot-bubble {
#         background-color: #6050dc;
#         padding: 12px;
#         border-radius: 20px;
#         color: #ffffff;
#         text-align: right;
#         max-width: 80%;
#         box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
#         word-wrap: break-word;
#         transition: background-color 0.3s ease-in-out;
#     }

#     .bot-bubble:hover {
#         background-color: #4a3cb6;
#     }

#     /* Hide the Streamlit footer */
#     footer {
#         visibility: hidden;
#     }

#     /* Hide the Streamlit header */
#     header {
#         visibility: hidden;
#     }
#     </style>
#     """, unsafe_allow_html=True)


######################## After removing water mark.
import base64
import streamlit as st

# Function to convert an image file to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Step 1: Specify the path to your image
image_path = "Back.jpg"  # Ensure the image is in the same folder as this script or provide a full path

# Step 2: Convert the image to base64 format
base64_image = get_base64_image(image_path)

# Step 3: Correctly interpolate the base64 string into the markdown
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&display=swap');
    
    .stApp {{
        background-image: url("data:image/png;base64,{base64_image}");
        background-size: cover; /* Ensures the image covers the entire background */
        background-position: center; /* Centers the background image */
        background-repeat: no-repeat; /* Prevents repeating the image */
        font-family: 'Poppins', sans-serif; /* Modern font */
        padding-bottom: 100px; /* Ensure there's room for the input at the bottom */
        opacity: 1;
    }}

    .custom-header {{
        font-size: 36px;
        font-weight: bold;
        color: #FFFFFF;
        text-align: center;
        padding: 20px;
        background: linear-gradient(90deg, rgba(255, 94, 98, 1) 0%, rgba(255, 165, 0, 1) 100%);
        border-radius: 0px 0px 15px 15px;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000; /* Ensure it stays above other content */
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2); /* Slight shadow */
        font-family: 'Comic Neue', sans-serif;
    }}

    .stApp {{
        padding-top: 120px;
    }}

    .footer-input input {{
        width: 100% !important;
        padding: 12px !important;
        font-size: 16px !important;
        border-radius: 10px;
        border: 2px solid #ccc;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
        background-color: #ffffff;
        color: #333333;
        transition: all 0.3s ease;
    }}

    .footer-input input::placeholder {{
        color: #040404 !important;
        opacity: 1 !important;
    }}

    .footer-input input:focus {{
        border-color: rgba(63,94,251,1);
        box-shadow: 0 0 5px rgba(63,94,251,0.5);
    }}

    .user-bubble {{
        background-color: #e6f7ff;
        padding: 12px;
        border-radius: 20px;
        color: #333333;
        max-width: 80%;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        word-wrap: break-word;
        opacity: 1;
    }}

    .bot-bubble {{
        background-color: #6050dc;
        padding: 12px;
        border-radius: 20px;
        color: #ffffff;
        text-align: left;
        max-width: 80%;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        word-wrap: break-word;
        transition: background-color 0.3s ease-in-out;
        opacity: 1;
    }}

    .bot-bubble:hover {{
        background-color: #4a3cb6;
    }}

    footer {{
        visibility: hidden;
    }}

    header {{
        visibility: hidden;
    }}
    </style>
    """, unsafe_allow_html=True)



# Add a custom header
st.markdown("<div class='custom-header'>Tomato Recommendation System</div>", unsafe_allow_html=True)

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
                col1, col2 = st.columns([5, 4])
                with col2:
                    st.markdown(f"""
                        <div class='bot-bubble'>
                        {msg['message']}
                        </div>
                    """, unsafe_allow_html=True)
                with col1:
                    st.empty()

def call_api(user_input):
    api_url = "http://172.29.8.241:7071/api/yourtomato"
    headers = {
        "Content-Type": "application/json"
    }
    
    # Prepare the chat history
    chat_history = [{"sender": msg["sender"], "message": msg["message"]} for msg in st.session_state.messages]
    
    payload = {
        "user_message": user_input,
        "chat_history": chat_history  # Include the chat history in the payload
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





















































































############################################# NOT WORKING DESIGNING
# import streamlit as st
# import streamlit.components.v1 as components

# # Custom CSS for fixed header and input at the bottom with improved colors and fonts
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');
    
#     /* Set background color for the entire page */
#     .stApp {
#         background-color: #FAFAFA; /* Light grey background */
#         font-family: 'Poppins', sans-serif; /* Modern font */
#         padding-bottom: 100px; /* Ensure there's room for the input at the bottom */
#     }

#     /* Custom header style with fixed position */
#     .custom-header {
#         font-size: 36px;
#         font-weight: bold;
#         color: #FFFFFF;
#         text-align: center;
#         padding: 20px;
#         background-color: #333333;
#         border-radius: 0px 0px 10px 10px;
#         position: fixed;
#         top: 0;
#         left: 0;
#         width: 100%;
#         z-index: 1000; /* Ensure it stays above other content */
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Slight shadow */
#     }

#     /* Push the rest of the content below the fixed header */
#     .stApp {
#         padding-top: 120px;
#     }

#     .footer-input {
#         position: fixed !important;
#         bottom: 0 !important;
#         width: 100% !important;
#         background-color: #f1f1f1 !important;
#         padding: 10px !important;
#         box-shadow: 0 -1px 10px rgba(0, 0, 0, 0.1) !important;
#     }
#     .footer-input input {
#         width: 100% !important;
#         padding: 10px !important;
#         font-size: 16px !important;
#     }

#     /* Chat bubbles for user and bot messages */
#     .user-bubble {
#         background-color: #e6f7ff;
#         padding: 10px;
#         border-radius: 10px;
#         color: #333333;
#         max-width: 80%;
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
#         word-wrap: break-word;
#     }

#     .bot-bubble {
#         background-color: #bf00ff;
#         padding: 10px;
#         border-radius: 10px;
#         color: #ffffff;
#         text-align: right;
#         max-width: 80%;
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
#         word-wrap: break-word;
#     }

#     /* Hide the Streamlit footer */
#     footer {
#         visibility: hidden;
#     }

#     /* Hide the Streamlit header */
#     header {
#         visibility: hidden;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Add a custom header
# st.markdown("<div class='custom-header'>Food Recommendation System</div>", unsafe_allow_html=True)

# # Initialize session state variables if they don't exist
# if "messages" not in st.session_state:
#     st.session_state.messages = []  # List to store chat messages

# # Create a container for the chat interface
# chat_container = st.container()

# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":  # User messages
#                 col1, col2 = st.columns([4, 5])
#                 with col1:
#                     st.markdown(f"""
#                         <div class='user-bubble'>
#                         {msg['message']}
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()
#             else:  # Bot messages
#                 col1, col2 = st.columns([5, 3])
#                 with col2:
#                     st.markdown(f"""
#                         <div class='bot-bubble'>
#                         {msg['message']}
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()

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
#         response = requests.post(api_url, headers=headers, json=payload)
#         res = response.json()
#         print(res['response'])
#         # Check if the response is successful
#         if response.status_code == 200:
#             return res['response']
#         else:
#             return f"Error: {response.status_code}"
#     except Exception as e:
#         return f"Error occurred while calling the API: {e}"

# # Function to handle user input and display new messages
# def handle_user_input(user_input):
#     if user_input:  # If there's input
#         st.session_state.messages.append({"sender": "user", "message": user_input})  # Add user message

#         # Call the API and get the bot response
#         bot_response = call_api(user_input)

#         # Append bot response to the message list
#         st.session_state.messages.append({"sender": "bot", "message": bot_response})

# # HTML form for input with JavaScript to send the input to Streamlit
# components.html("""
#     <div class="footer-input">
#         <input type="text" id="message_input" placeholder="Type your message here..." onkeydown="if(event.key === 'Enter'){sendMessage()}">
#     </div>
#     <script>
#         function sendMessage() {
#             let inputField = document.getElementById('message_input');
#             let userInput = inputField.value;
#             if (userInput) {
#                 window.parent.postMessage(userInput, "*");
#                 inputField.value = '';  // Clear the input field after sending
#             }
#         }
#         window.addEventListener('message', function(event) {
#             const message = event.data;
#             Streamlit.setComponentValue(message);
#         });
#     </script>
# """, height=100)

# # Capture the message sent from the HTML/JS input
# user_input = st.experimental_get_component_value()

# if user_input:
#     handle_user_input(user_input)

# # Display the messages in the chat container
# display_messages()



################################









# import streamlit as st
# import requests

# # Custom CSS for fixed header and input at the bottom with improved colors and fonts
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');
    
#     /* Set background color for the entire page */
#     .stApp {
#         background-color: #FAFAFA; /* Light grey background */
#         font-family: 'Poppins', sans-serif; /* Modern font */
#         padding-bottom: 100px; /* Ensure there's room for the input at the bottom */
#     }

#     /* Custom header style with fixed position */
#     .custom-header {
#         font-size: 36px;
#         font-weight: bold;
#         color: #FFFFFF;
#         text-align: center;
#         padding: 20px;
#         background-color: #333333;
#         border-radius: 0px 0px 10px 10px;
#         position: fixed;
#         top: 0;
#         left: 0;
#         width: 100%;
#         z-index: 1000; /* Ensure it stays above other content */
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Slight shadow */
#     }

#     /* Push the rest of the content below the fixed header */
#     .stApp {
#         padding-top: 120px;
#     }

#     /* Chat bubbles for user and bot messages */
#     .user-bubble {
#         background-color: #e6f7ff;
#         padding: 10px;
#         border-radius: 10px;
#         color: #333333;
#         max-width: 80%;
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
#         word-wrap: break-word;
#     }
    
#     .bot-bubble {
#         background-color: #bf00ff;
#         padding: 10px;
#         border-radius: 10px;
#         color: #ffffff;
#         text-align: right;
#         max-width: 80%;
#         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
#         word-wrap: break-word;
#     }

#     /* Hide the Streamlit footer */
#     footer {
#         visibility: hidden;
#     }

#     /* Hide the Streamlit header */
#     header {
#         visibility: hidden;
#     }
    
#     /* Style the input container to fix it at the bottom */
#     .input-container {
#         position: fixed;
#         bottom: 0;
#         left: 0;
#         width: 100%;
#         background-color: #f1f1f1;
#         padding: 10px;
#         box-shadow: 0 -1px 10px rgba(0, 0, 0, 0.1);
#         z-index: 9999;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Add a custom header
# st.markdown("<div class='custom-header'>Food Recommendation System</div>", unsafe_allow_html=True)

# # Initialize session state variables if they don't exist
# if "messages" not in st.session_state:
#     st.session_state.messages = []  # List to store chat messages

# # Create a container for the chat interface
# chat_container = st.container()

# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":  # User messages
#                 col1, col2 = st.columns([4, 5])
#                 with col1:
#                     st.markdown(f"""
#                         <div class='user-bubble'>
#                         {msg['message']}
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()
#             else:  # Bot messages
#                 col1, col2 = st.columns([5, 3])
#                 with col2:
#                     st.markdown(f"""
#                         <div class='bot-bubble'>
#                         {msg['message']}
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()

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
#         response = requests.post(api_url, headers=headers, json=payload)
#         res = response.json()
        
#         # Check if the response is successful
#         if response.status_code == 200:
#             return res['response']
#         else:
#             return f"Error: {response.status_code}"
#     except Exception as e:
#         return f"Error occurred while calling the API: {e}"

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

# # Display the messages in the chat container
# display_messages()

# # Create the fixed input box at the bottom of the screen
# with st.container():
#     st.markdown('<div class="input-container">', unsafe_allow_html=True)
#     user_input = st.text_input("Type your message here...", key="user_input_text", label_visibility="collapsed")
#     send_button = st.button("Send", on_click=handle_user_input)
#     st.markdown('</div>', unsafe_allow_html=True)





















# import streamlit as st
# import requests
# import json

# # Set a custom background image for the whole page
# page_bg_img = '''
# <style>
# .stApp {
#     background-image: url("pic.jpeg");
#     background-size: cover;
#     background-position: center;
#     background-repeat: no-repeat;
# }

# .chat-container {
#     background-color: rgba(255, 255, 255, 0.8);  /* Add some opacity for readability */
#     border-radius: 10px;
#     padding: 10px;
#     margin-bottom: 10px;
#     width: fit-content;
#     max-width: 80%;
#     word-wrap: break-word;
# }
# </style>
# '''



# # Apply the custom background style
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Set up the title of the app
# st.markdown("<h1 style='text-align: center; color: white;'>Food Recommendation System</h1>", unsafe_allow_html=True)

# # Initialize session state variables if they don't exist
# if "messages" not in st.session_state:
#     st.session_state.messages = []  # List to store chat messages
# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""  # To store user input text

# # Create a container for the chat interface
# chat_container = st.container()

# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":  # User messages
#                 col1, col2 = st.columns([4, 5])
#                 with col1:
#                     st.markdown(f"""
#                         <div class='chat-container' style='background-color: #e6f7ff; padding: 10px; border-radius: 10px;'>
#                         <span style='color: #bf00ff;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()
#             else:  # Bot messages
#                 col1, col2 = st.columns([5, 1])
#                 with col2:
#                     st.markdown(f"""
#                         <div class='chat-container' style='background-color: #bf00ff; padding: 10px; border-radius: 10px; text-align: right;'>
#                         <span style='color: white;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()

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

# import streamlit as st

# # Set a custom background image for the whole page
# page_bg_img = '''
# <style>
# body {
#     background-image: url("pic.jpeg");
#     background-size: cover;
#     background-position: center;
#     background-repeat: no-repeat;
#     background-attachment: fixed; /* Ensures the background image stays fixed when scrolling */
# }

# .chat-container {
#     background-color: rgba(255, 255, 255, 0.8);  /* Semi-transparent background */
#     border-radius: 10px;
#     padding: 20px;
#     margin-bottom: 10px;
#     width: fit-content;
#     max-width: 80%;
#     word-wrap: break-word;
#     margin-left: auto;  /* Centering the message container */
#     margin-right: auto;
#     box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);  /* Adds a slight shadow for better readability */
# }
# </style>
# '''

# # Apply the custom background style
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Set up the title of the app
# st.markdown("<h1 style='text-align: center; color: white;'>Food Recommendation System</h1>", unsafe_allow_html=True)

# # Initialize session state variables if they don't exist
# if "messages" not in st.session_state:
#     st.session_state.messages = []  # List to store chat messages
# if "user_input" not in st.session_state:
#     st.session_state.user_input = ""  # To store user input text

# # Create a container for the chat interface
# chat_container = st.container()

# def display_messages():
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["sender"] == "user":  # User messages
#                 col1, col2 = st.columns([4, 5])
#                 with col1:
#                     st.markdown(f"""
#                         <div class='chat-container' style='background-color: #e6f7ff; padding: 10px; border-radius: 10px;'>
#                         <span style='color: #bf00ff;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col2:
#                     st.empty()
#             else:  # Bot messages
#                 col1, col2 = st.columns([5, 1])
#                 with col2:
#                     st.markdown(f"""
#                         <div class='chat-container' style='background-color: #bf00ff; padding: 10px; border-radius: 10px; text-align: right;'>
#                         <span style='color: white;'>{msg['message']}</span>
#                         </div>
#                     """, unsafe_allow_html=True)
#                 with col1:
#                     st.empty()

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

#         # Log response for debugging
#         st.write(f"Response: {response.status_code}, {response.text}")

#         # Check if the response is successful
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return f"Error: {response.status_code}"
#     except Exception as e:
#         st.error(f"Error occurred while calling the API: {e}")
#         return f"Error occurred while calling the API: {e}"

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


