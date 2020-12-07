import streamlit as st
import pandas as pd
import pickle

st.header("""
My Application!
""")

st.sidebar.header('User Input')
st.sidebar.subheader('Please enter your data:')
#st.header('Application of MEAW')
st.markdown(
    """
<style>
.reportview-container .markdown-text-container {
    font-family: Lucida Console;
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#d7bde2, #aed6f1 );
    color: white;
}
.Widget>label {
    color: white;
    font-family: "Lucida Sans;
}
[class^="st-b"]  {
    color: black;
    font-family: cursive;
}
.st-bb {
    background-color:#a3e4d7;
}
.st-at {
    background-color:  none;
}
footer {
    font-family: Lucida Sans;
}
.reportview-container .main footer, .reportview-container .main footer a {
    color:  none;
}
header .decoration {
    background-image: none;
}

</style>
""",
    unsafe_allow_html=True,
)


def get_input():
    #widgets
    v_AcademicYear = st.sidebar.selectbox('AcademicYear', ['2562'])

    v_AcademicSemester = st.sidebar.checkbox('AcademicSemester: 1')
    
    v_Sex = st.sidebar.radio('Sex', ['Male','Female'])
    v_FacultyName = st.sidebar.selectbox('FacultyName', ['School of Liberal Arts',
        'School of Management',
        'School of Information Technology',
        'School of Law',
        'School of Cosmetic Science',
        'School of Health Science',
        'School of Nursing',
        'School of Medicine',
        'School of Sinology',
        'School of Integrative Medicine',
        'School of Agro-industry',
        'School of Science',
        'School of Social Innovation',
        'School of Dentistry'])
    v_EntryTypeName = st.sidebar.selectbox('EntryTypeName', [
        'QUOTA 17 NORTHERN PROVINCES', 
        'DIRECT ADMISSION BY SCHOOL',
        'DISABLE STUDENT',
        'EP-MEP PROGRAM',
        'QUOTA BY SCHOOL',
        'SPECIAL TALENT',
        'GOOD BEHAVE STUDENTS',
        'INTERNATIONAL SCHOOL',
        'CHIANG RAI DEVELOPMENT SCHOLARSHIP',
        'QUOTA BY COMMUNITY HOSPITAL',
        'SPECIAL FOR GOOD STUDENT'])

    v_TCAS = st.sidebar.radio('TCAS',['1','2'])
 
    v_GPAX = st.sidebar.slider('GPAX', 1.31, 4.00, 3.26)
    
    v_GPA_Eng = st.sidebar.slider('GPA_Eng', 0.91, 4.00, 3.31)
   
    v_GPA_Math = st.sidebar.slider('GPA_Math', 0.45, 4.00, 2.83)
   
    v_GPA_Sci = st.sidebar.slider('GPA_Sci', 0.62, 4.00, 3.01)
    
    v_GPA_Sco = st.sidebar.slider('GPA_Sco', 0.70, 4.00, 3.47)

# --- checkbox---
   
    st.sidebar.subheader('Expectation for studying in MFU:')
    v_Q2 = st.sidebar.checkbox('Quality of life')
    v_Q3 = st.sidebar.checkbox('Campus and facilities')

    st.sidebar.subheader('Source of information for this application:')
    v_Q4 = st.sidebar.checkbox('modern and ready-to-use learning support and facilities')
    v_Q8 = st.sidebar.checkbox('Facebook Admission@MFU')
    v_Q9 = st.sidebar.checkbox('Facebook MFU')
    v_Q13 = st.sidebar.checkbox('school teachers')
    v_Q14 = st.sidebar.checkbox('education exhibitions')
    v_Q18 = st.sidebar.checkbox('other sources')
    v_Q19 = st.sidebar.checkbox('https://admission.mfu.ac.th')
    v_Q20 = st.sidebar.checkbox('https://www.mfu.ac.th')
    v_Q21 = st.sidebar.checkbox('other educational websites')

    st.sidebar.subheader('Factor to apply for MFU :')
    v_Q23 = st.sidebar.checkbox('easy/convenient transportation')
    v_Q24 = st.sidebar.checkbox('suitable cost')
    v_Q26 = st.sidebar.checkbox('learning in English')
    v_Q28 = st.sidebar.checkbox('excellence in learning support and facilities')
    v_Q29 = st.sidebar.checkbox('provision of preferred major')
    v_Q30 = st.sidebar.checkbox('environment and setting motivate learning')
    v_Q31 = st.sidebar.checkbox('experienced and high-quality instructors')

    st.sidebar.subheader('IF your application fails, will you try again?:')
    v_Q34 = st.sidebar.checkbox('try the same major')
    v_Q35 = st.sidebar.checkbox('try a different major')

    st.sidebar.subheader('Reason for apply for the major:')
    v_Q37 = st.sidebar.checkbox('suggestion by school teacher')
    v_Q38 = st.sidebar.checkbox('suggestion by family')
    v_Q40 = st.sidebar.checkbox('chance of getting a job after graduation')
    v_Q41 = st.sidebar.checkbox('less competitive than other universities')

    #dictionary
    data = {'AcademicYear': v_AcademicYear,
            'AcademicSemester': v_AcademicSemester,
            'Sex': v_Sex,
            'FacultyName': v_FacultyName,
            'EntryTypeName': v_EntryTypeName,
            'TCAS': v_TCAS,
            'GPAX': v_GPAX,
            'GPA_Eng': v_GPA_Eng,
            'GPA_Math': v_GPA_Math,
            'GPA_Sci' : v_GPA_Sci,
            'GPA_Sco' : v_GPA_Sco,
            'Q2': v_Q2,'Q3': v_Q3,'Q4': v_Q4,'Q8': v_Q8,'Q9': v_Q9,'Q13': v_Q13,
            'Q14': v_Q14,'Q18': v_Q18,'Q19': v_Q19,'Q20': v_Q20,'Q21': v_Q21,'Q23': v_Q23,
            'Q24': v_Q24,'Q26': v_Q26,'Q28': v_Q28,'Q29': v_Q29,'Q30': v_Q30,'Q31': v_Q31,
            'Q34': v_Q34,'Q35': v_Q35,'Q37': v_Q37,'Q38': v_Q38,'Q40': v_Q40,'Q41': v_Q41,
            }

    #create data frame
    data_df = pd.DataFrame(data, index=[0])
    return data_df

df = get_input()
st.write(df)

data_sample = pd.read_excel('tcas_new_sample1.xlsx')
df = pd.concat([df, data_sample],axis=0)

cat_data = pd.get_dummies(df[['Sex','FacultyName','EntryTypeName']])

#Combine all transformed features together
X_new = pd.concat([cat_data, df], axis=1)
X_new = X_new[:1] # Select only the first row (the user input data)
#Drop un-used feature
X_new = X_new.drop(columns=['Sex','FacultyName','EntryTypeName'])


# -- Reads the saved normalization model
load_nor = pickle.load(open('normalization.pkl', 'rb'))
#Apply the normalization model to new data
X_new = load_nor.transform(X_new)
st.write(X_new)

# -- Reads the saved classification model
load_knn = pickle.load(open('best_knn.pkl', 'rb'))
# Apply model for prediction
prediction = load_knn.predict(X_new)
st.write(prediction)