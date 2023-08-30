import streamlit as st
from my_component import my_component
#from streamlit_camera_access import my_component

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`
st.subheader("Component with constant args")

# Create an instance of our component with a constant `name` arg, and
# print its output value.
cam_input = my_component()

