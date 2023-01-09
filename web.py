import streamlit as st
import functions
import time as tm

list = functions.get_list()

def add_task():
    task = st.session_state['new_task'] + "\n"
    list.append(task)

    functions.write_list(list)

now = tm.strftime("%b, %d %Y")


# display the title, sub-header, and write a new line
st.title("My Todo App")
st.subheader("Every little step will help your achieve the big goal.")
st.write("Today is "+ now)
st.write("<p>Create a plan, execute your plan to maximize your <b>productivity</b></p>",
         unsafe_allow_html=True)

st.text_input(label="What is your plan today?",
              placeholder="Add new task..",
              on_change=add_task, key='new_task')

# display each task as checkbox on the web page
# and label/name each checkbox with its name
for index, task in enumerate(list):
    checkbox = st.checkbox(task, key=task)

    # removing the task when checkbox is clicked
    if checkbox:
        list.pop(index)
        functions.write_list(list)
        del st.session_state[task]
        st.experimental_rerun()
