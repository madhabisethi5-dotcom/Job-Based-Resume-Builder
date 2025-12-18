from google import genai
import streamlit as st
st.title("🤖 Job-Based Resume Builder")
client = genai.Client(api_key="PASTE_YOUR_GOOGLE_GENAI_API_KEY_HERE")
job_name = st.text_input(
    "Enter Job Title",
    placeholder="e.g. Data Scientist, Backend Developer, AI Engineer"
)
if job_name: 
    def resume(name,email,Phone_number,job_title,experience_level,skills,Highest_Qualification,job_description):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""Your erpot in resume build profationally,
        Create a professional resume for the following candidate:
        Name: {name},Email:{email},Phone:{Phone_number},Target Role: {job_title},Experience Level: {experience_level}
        Skills: {skills},Highest Qualification: {Highest_Qualification}
        Generate:
        1. Dont add any extra line.
        2. 3-5 ATS-profationally do not icludede symbols.
        3. A clean skills section.
        4. At the end,short full short and profationally and atractful summary.
        Keep the tone professional and concise.
        """
            )
        return response
else:
    st.write('gives the job discreption first')
name = st.text_input("Enter_your_name")
email = st.text_input("Enter_your_email")
Phone_number= st.text_input("Enter_your_Phone_Number")
job_title = st.text_input("Target_Job_Role")
experience_level = st.selectbox("Experience Level",["Fresher", "1-3 Years", "3-5 Years", "5+ Years"])
skills = st.text_area("Enter your skills (comma separated)",placeholder="Python, Streamlit, SQL, Machine Learning"
)
Highest_Qualification=st.selectbox("Highest Qualification:",('Bsc','B.com','Iti','Btech','Diploma','Msc','BBA','MBA'))
job_description = st.text_area(
    "Paste the complete job description here",
    placeholder="Paste job responsibilities, required skills, qualifications, etc."
)
if st.button("✨ Generate Resume using AI"):
    if not name or not email or not Phone_number or not job_title or not experience_level or not skills or not Highest_Qualification or not job_description:
        st.warning("Please fill in all required fields.")
    else:
        with st.spinner("Generating resume with GenAI..."):
            result = resume(name,email,Phone_number,job_title,experience_level,skills,Highest_Qualification,job_description)      
            st.write(result.text)
       

    

  

   
    




