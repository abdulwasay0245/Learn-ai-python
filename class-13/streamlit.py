import streamlit as st

from PIL import Image
# icon = Image.open("favicon.png")

# st.image(icon , width = 200)
# st.title("wasay")
# st.error("this is error")
# st.success("success")
# st.warning("warning")
# exp = ZeroDivisionError("zero division error")
# st.exception(exp)

chat_input = st.chat_input("Type Here")

if chat_input:
  st.chat_message("user").write(chat_input)
  st.chat_message("assistant").write("Hello how can i help you today!")


btn = st.button("Increment")

if "count" not in st.session_state:
  st.session_state.count = 0

if btn:
  st.session_state.count += 1
  st.write(f"The Button Click {st.session_state.count} Times")
