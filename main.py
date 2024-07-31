import streamlit as st
from datetime import datetime
from xata.client import XataClient
import base64

# Initialize Xata client using Streamlit secrets
# xata = XataClient(api_key=st.secrets["XATA_API_KEY"], db_url=st.secrets["XATA_DB_URL"])

def encode_file(file):
    return base64.b64encode(file.getvalue()).decode()

def main():
    st.set_page_config(page_title="Oil Spill Incident Reporting", layout="wide")
    
    st.title("Oil Spill Incident Reporting Form")
    
    st.write("""
    This form is for reporting oil spill incidents in the Niger Delta region of Nigeria. 
    The report will enable stakeholders in oil spill incident response and management to activate the emergency response plan.
    """)
    
    with st.form("oil_spill_report"):
        col1, col2 = st.columns(2)
        
        with col1:
            email = st.text_input("Email")
            organization = st.text_input("Reporter's Organization")
            phone = st.text_input("Mobile Phone Number")
            address = st.text_area("Address")
            date_observed = st.date_input("Date Oil Spill was Observed")
            time_observed = st.time_input("Time of Incident")
            
        with col2:
            location = st.selectbox("Location of Incident", 
                                    ["Offshore", "Swamp", "Land/Onshore", "Shallow Water/River", "Other"])
            if location == "Other":
                location = st.text_input("Specify Location")
            
            incident_site = st.text_input("Incident Facility/Site")
            city_state = st.text_input("City/State")
            coordinates = st.text_input("Geographical Coordinates")
            source = st.text_input("Source of Oil Spill/Equipment/Facility")
            
        cause = st.selectbox("Possible Cause(s) of Oil Spill", 
                             ["Equipment Failure", "Operational Failure", "Sabotage", 
                              "Natural Factors", "Attack on Facility", "Other"])
        if cause == "Other":
            cause = st.text_input("Specify Cause")
        
        description = st.text_area("Description of Incident")
        
        uploaded_files = st.file_uploader("Upload Pictures of Oil Spill", accept_multiple_files=True)
        
        submitted = st.form_submit_button("Submit Report")
        
        # if submitted:
        #     # Prepare data for XATA
        #     report_data = {
        #         "email": email,
        #         "organization": organization,
        #         "phone": phone,
        #         "address": address,
        #         "date_observed": date_observed.isoformat(),
        #         "time_observed": time_observed.isoformat(),
        #         "location": location,
        #         "incident_site": incident_site,
        #         "city_state": city_state,
        #         "coordinates": coordinates,
        #         "source": source,
        #         "cause": cause,
        #         "description": description,
        #         "timestamp": datetime.now().isoformat(),
        #         "images": []
        #     }
            
        #     # Handle file uploads
        #     if uploaded_files:
        #         for file in uploaded_files:
        #             file_data = {
        #                 "name": file.name,
        #                 "mime": file.type,
        #                 "base64Content": encode_file(file)
        #             }
        #             report_data["images"].append(file_data)
            
        #     # Insert data into XATA
        #     try:
        #         xata.records().insert("oil_spill_reports", report_data)
        #         st.success("Report submitted successfully!")
        #         if uploaded_files:
        #             st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")
        #     except Exception as e:
        #         st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()