import streamlit as st
from google.cloud import language_v1

# Set page title and favicon
st.set_page_config(
    page_title="🔍 Python Code Debugger",
    page_icon="🔍",
)

# Authenticate with Google Cloud Natural Language API using API key
API_KEY = "AIzaSyBgSCbRuJmV0DIyvfiaXaTjZTsI6LjsOb4"  # Replace with your actual API key
client = language_v1.LanguageServiceClient(credentials=API_KEY)

# Set title and subtitle
st.title("Python Code Debugger")
st.sidebar.subheader("Instructions")
st.sidebar.write("Enter your Python code in the text area below, then click 'Generate' to debug it.")

# Create an input box
label = "Enter your Python code"
prompt = st.text_area(label, height=300)

# If the button is clicked, generate the output
if st.button("Generate"):
    # Split Python code into lines
    lines = prompt.split('\n')

    # Initialize debugged code
    debugged_code = ""

    # Analyze each line of Python code
    for line in lines:
        document = language_v1.Document(content=line, type_=language_v1.Document.Type.PLAIN_TEXT)
        response = client.analyze_syntax(request={'document': document})
        debugged_line = ' '.join([token.text.content for token in response.tokens])
        debugged_code += debugged_line + '\n'

    # Display the debugged Python code
    st.write("Debugged Python code:")
    st.code(debugged_code, language='python')
