import streamlit as its

its.title("Welcome TO ITS Academy")
its.header("Institute of Traditional Studies !")

its.markdown("Let's Start Coding~~~")
its.code("""for i in range(1,5,1)):
            print("Hello Students...!")
            """)
name=its.text_input("Enter Your Name: ")
fname=its.text_input("Enter Your Father Name: ")
adr=its.text_area("Enter your Residence: ")

classdata=its.selectbox("Enter Your Course: ",("BCA","B.Com","B.Tech", "MBA","MCA", "M.Com","B.Tech","B.A","M.A","BBA","B.Pharma"))
button=its.button("submit")

if button:
    its.markdown(f"""
    Name : {name}
    Father Name : {fname}
    Residence : {adr}
    class : {classdata}
    """)
