import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+ '\n')
    functions.write_todos(todos)


st.title('My todo App')
st.subheader('This is my todo app.')
st.write('This app is to increase your productivity')


for index, todo in enumerate (todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._experimental_rerun()


st.text_input(label='Add here', placeholder='Add new todo',key='new_todo',
              on_change=add_todo)

st.session_state