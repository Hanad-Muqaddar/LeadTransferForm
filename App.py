import streamlit as st
import requests

st.markdown(
    """
    <style>
    div.stButton > button {
        display: flex;
        justify-content: center;
        background-color: #0000FF;
        color:#ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    st.title('Lead :blue[Transfer] :orange[Form]')

    with st.form(key="my_form", clear_on_submit=True):
        col1, col2 = st.columns(2, gap="medium")
        with col1:
            first_name = st.text_input("First Name", value="")
        with col2:
            last_name = st.text_input("Last Name", value="")
        

        col3, col4 = st.columns(2, gap="medium")
        with col3:
            phone_number = st.text_input("Phone Number", value="")
        with col4:
            email_address = st.text_input("Email Address", value="")
        

        col5, col6 = st.columns(2, gap="medium")
        with col5:
            Address = st.text_input("Address", value="")
        with col6:
            city = st.text_input("City", value="")


        col7, col8 = st.columns(2, gap="medium")
        with col7:
            State = st.text_input("State", value="")
        with col8:
            Zip = st.text_input("Zip", value="")
        
        col9, col10 = st.columns(2, gap="medium")
        with col9:
            DOB = st.text_input("D.O.B", value="")
        with col10:
            Gender = st.text_input("Gender", value="")
        
        
        source_url = st.text_input("Source Url", value="")
        

        submit_button = st.form_submit_button("SUBMIT")

    if submit_button:
        url = f"""https://global-digital-media.trackdrive.com/api/v1/leads?caller_id={phone_number}
                &lead_token=f1be4fda3aa5488eb2a1684f3d1090b5&source_url={source_url}&zip={Zip}
                &first_name={first_name}&last_name={last_name}&email={email_address}&address={Address}
                &city={city}&state={State}&dob={DOB}&gender={Gender}"""
        headers= {}
        payload = {}
        try:
            r = requests.request("POST", url, headers=headers, data=payload)
            st.success('Submitted Successfully', icon="✅")
        except:
            st.error("There is some error Occured.")


if __name__ == "__main__":
    main()