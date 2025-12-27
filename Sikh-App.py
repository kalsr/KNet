#$$$$

###Sikh app

Home
To:  me
 · 
Fri, Dec 26 at 9:36 PM
Below is a complete, simple Streamlit app that lets users click buttons to get information from ChatGPT about: Sikh GurusGuru Granth SahibSikh History The app uses buttons (GUI) and calls the OpenAI API to generate responses dynamically. 1. Prerequisites Install required libraries: pip install streamlit openai Set your OpenAI API key (recommended via environment variable): macOS / Linux export OPENAI_API_KEY="your_api_key_here" Windows (PowerShell) setx OPENAI_API_KEY "your_api_key_here" 2. Streamlit App Code ( app.py ) import streamlit as st from openai import OpenAI # Initialize OpenAI client client = OpenAI() st.set_page_config( page_title="Sikh Knowledge Explorer", layout="centered" ) st.title("🕉️ Sikh Knowledge Explorer") st.write( "Click a button below to learn about Sikh Gurus, " "the Guru Granth Sahib, or Sikh history." ) # Sidebar options st.sidebar.header("Choose a Topic") topic = None if st.sidebar.button("Sikh Gurus"): topic = "Provide a clear and respectful overview of the Ten Sikh Gurus." if st.sidebar.button("Guru Granth Sahib"): topic = ( "Explain what the Guru Granth Sahib is, its significance in Sikhism, " "and its core teachings." ) if st.sidebar.button("Sikh History"): topic = ( "Give an overview of Sikh history, including its origins, " "key events, and values." ) def get_chatgpt_response(prompt): response = client.chat.completions.create( model="gpt-4o-mini", messages=[ {"role": "system", "content": "You are a knowledgeable and respectful expert on Sikhism."}, {"role": "user", "content": prompt} ], max_tokens=500 ) return response.choices[0].message.content # Display output if topic: with st.spinner("Fetching information..."): answer = get_chatgpt_response(topic) st.subheader("📘 Information") st.write(answer) else: st.info("Please select a topic from the sidebar to begin.") 3. How It Works Streamlit UI Sidebar buttons for each topicClean, user-friendly layout ChatGPT Integration Sends a topic-specific prompt to ChatGPTReturns concise, r

Home
To:  me
 · 
Fri, Dec 26 at 9:36 PM
Message Body

Below is a complete, simple Streamlit app that lets users click buttons to get information from ChatGPT about:



Sikh Gurus
Guru Granth Sahib
Sikh History




The app uses buttons (GUI) and calls the OpenAI API to generate responses dynamically.









1. Prerequisites





Install required libraries:

pip install streamlit openai

Set your OpenAI API key (recommended via environment variable):



macOS / Linux

export OPENAI_API_KEY="your_api_key_here"

Windows (PowerShell)

setx OPENAI_API_KEY "your_api_key_here"









2. Streamlit App Code (

app.py

)



import streamlit as st

from openai import OpenAI



# Initialize OpenAI client

client = OpenAI()



st.set_page_config(

    page_title="Sikh Knowledge Explorer",

    layout="centered"

)



st.title("🕉️ Sikh Knowledge Explorer")

st.write(

    "Click a button below to learn about Sikh Gurus, "

    "the Guru Granth Sahib, or Sikh history."

)



# Sidebar options

st.sidebar.header("Choose a Topic")



topic = None



if st.sidebar.button("Sikh Gurus"):

    topic = "Provide a clear and respectful overview of the Ten Sikh Gurus."



if st.sidebar.button("Guru Granth Sahib"):

    topic = (

        "Explain what the Guru Granth Sahib is, its significance in Sikhism, "

        "and its core teachings."

    )



if st.sidebar.button("Sikh History"):

    topic = (

        "Give an overview of Sikh history, including its origins, "

        "key events, and values."

    )



def get_chatgpt_response(prompt):

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {"role": "system", "content": "You are a knowledgeable and respectful expert on Sikhism."},

            {"role": "user", "content": prompt}

        ],

        max_tokens=500

    )

    return response.choices[0].message.content



# Display output

if topic:

    with st.spinner("Fetching information..."):

        answer = get_chatgpt_response(topic)



    st.subheader("📘 Information")

    st.write(answer)



else:

    st.info("Please select a topic from the sidebar to begin.")









3. How It Works





Streamlit UI
Sidebar buttons for each topic
Clean, user-friendly layout

ChatGPT Integration
Sends a topic-specific prompt to ChatGPT
Returns concise, respectful explanations

Expandable
You can easily add buttons like:
“Five Ks”
“Sikh Festivals”
“Khalsa Panth”
Individual Gurus (Guru Nanak Dev Ji, Guru Gobind Singh Ji, etc.)












4. Example Enhancements (Optional)





If you want, I can also help you add:



📚 Individual buttons for each Guru
🌍 Punjabi language support
🧠 Follow-up question box
🗂️ Dropdown menus instead of buttons
🔊 Text-to-speech for accessibility
