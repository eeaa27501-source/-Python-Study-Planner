import streamlit as st
from datetime import date

st.set_page_config(page_title="Python Study Planner", page_icon="📚", layout="wide")
st.title("📚 Python Study Planner")
st.caption("A simple browser-based study planner")
st.info("Demo version: tasks are kept in this browser session. They are not permanently stored on a server.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

with st.form("add_task", clear_on_submit=True):
    st.subheader("Add a study task")
    title = st.text_input("Task title", placeholder="e.g. Review algebra chapter 2")
    subject = st.text_input("Subject", placeholder="e.g. Mathematics")
    due = st.date_input("Due date", value=date.today())
    submitted = st.form_submit_button("Add task", type="primary")
    if submitted:
        if title.strip() and subject.strip():
            st.session_state.tasks.append({"title": title.strip(), "subject": subject.strip(), "due": due.isoformat(), "done": False})
            st.success("Task added.")
        else:
            st.warning("Please enter both a task title and a subject.")

st.divider()
tasks = st.session_state.tasks
total = len(tasks)
done = sum(t["done"] for t in tasks)
c1, c2, c3 = st.columns(3)
c1.metric("Total tasks", total)
c2.metric("Completed", done)
c3.metric("Progress", f"{(done/total*100):.0f}%" if total else "0%")
st.progress(done / total if total else 0)

st.subheader("Your tasks")
if not tasks:
    st.write("No tasks yet. Add your first study task above.")
else:
    for i, task in enumerate(tasks):
        a, b, c, d = st.columns([4, 2, 2, 1])
        a.write(("✅ " if task["done"] else "📝 ") + task["title"])
        b.write(task["subject"])
        c.write(task["due"])
        if d.button("Undo" if task["done"] else "Done", key=f"toggle_{i}"):
            task["done"] = not task["done"]
            st.rerun()
    if st.button("Clear all tasks", type="secondary"):
        st.session_state.tasks = []
        st.rerun()

st.caption("Built with Python and Streamlit. Educational demonstration.")
