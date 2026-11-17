import streamlit as st
import pandas as pd

st.title("Student Record Management System")

# Store student records
if "students" not in st.session_state:
    st.session_state.students = pd.DataFrame(
        columns=["Roll No", "Name", "Age", "Course"]
    )

# Menu
menu = st.sidebar.selectbox(
    "Select Operation",
    ["Add Student", "View Students", "Update Student", "Delete Student"]
)

# CREATE
if menu == "Add Student":
    st.header("Add Student")

    roll = st.number_input("Roll Number", min_value=1, step=1)
    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1, step=1)
    course = st.text_input("Course")

    if st.button("Add Student"):
        if name and course:
            if roll not in st.session_state.students["Roll No"].values:
                new_student = pd.DataFrame([{
                    "Roll No": roll,
                    "Name": name,
                    "Age": age,
                    "Course": course
                }])

                st.session_state.students = pd.concat(
                    [st.session_state.students, new_student],
                    ignore_index=True
                )

                st.success("Student added successfully!")
            else:
                st.error("Roll number already exists!")
        else:
            st.warning("Please enter all details.")

# READ
elif menu == "View Students":
    st.header("View Student Records")

    st.dataframe(
        st.session_state.students,
        use_container_width=True
    )

# UPDATE
elif menu == "Update Student":
    st.header("Update Student")

    students = st.session_state.students

    if not students.empty:
        roll = st.selectbox("Select Roll Number", students["Roll No"])

        student = students[students["Roll No"] == roll].iloc[0]

        name = st.text_input("Name", value=student["Name"])
        age = st.number_input("Age", min_value=1, value=int(student["Age"]))
        course = st.text_input("Course", value=student["Course"])

        if st.button("Update Student"):
            index = students[students["Roll No"] == roll].index[0]

            st.session_state.students.loc[index, "Name"] = name
            st.session_state.students.loc[index, "Age"] = age
            st.session_state.students.loc[index, "Course"] = course

            st.success("Student updated successfully!")
    else:
        st.warning("No student records available.")

# DELETE
elif menu == "Delete Student":
    st.header("Delete Student")

    students = st.session_state.students

    if not students.empty:
        roll = st.selectbox("Select Roll Number", students["Roll No"])

        if st.button("Delete Student"):
            st.session_state.students = students[
                students["Roll No"] != roll
            ].reset_index(drop=True)

            st.success("Student deleted successfully!")
    else:
        st.warning("No student records available.")