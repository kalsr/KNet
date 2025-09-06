

## Synthetic_Data_Generator.py 

# THIS APPLICATION IS DEVELOPED BY RANDY SINGH FROM KNet CONSULTING GROUP.

# python
# EMASS-DITPR-MAPS-ESPS STREAMLIT APP with Search & Excel Export
# Developed by Randy Singh – KNet Consulting Group.

import json
import os
import random
import uuid
import io
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="DISA Data Emulators", layout="wide")
st.title("📡 EMASS · DITPR · MAPS · ESPS – Data Emulator & API Repository")
st.caption("Developed by Randy Singh – KNet Consulting Group")

# -------------------------------
# Random Generators
# -------------------------------
def random_name():
    return f"{random.choice(['John','Jane','Alice','Bob','Charlie'])} {random.choice(['Smith','Doe','Johnson','Williams','Brown'])}"

def random_email():
    domains = ["example.com","mail.com","test.org"]
    return f"{random_name().replace(' ','.').lower()}@{random.choice(domains)}"

def random_address():
    return f"{random.randint(100,999)} {random.choice(['Main St','High St','Maple Ave','Oak St'])}, {random.choice(['Springfield','Riverside','Greenville','Fairview'])}, USA"

def random_phone():
    return f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"

def random_company():
    return random.choice(["TechCorp","BizSolutions","Innovate LLC","Alpha Inc","Global Ventures"])

def random_url():
    return random.choice(["https://example.com","https://mysite.com","https://website.org"])

def random_lat():
    return round(random.uniform(-90,90),6)

def random_lon():
    return round(random.uniform(-180,180),6)

def random_city():
    return random.choice(["New York","Los Angeles","Chicago","Houston","Phoenix"])

def random_product():
    return random.choice(["Widget","Gadget","Doodad","Thingamajig","Contraption"])

def random_price():
    return round(random.uniform(10,1000),2)

def random_word():
    return random.choice(["alpha","beta","gamma","delta","epsilon"])

# -------------------------------
# Generators for each Emulator
# -------------------------------
def generate_emass_record():
    return {
        "id": str(uuid.uuid4()),
        "name": random_name(),
        "email": random_email(),
        "address": random_address(),
        "phone_number": random_phone(),
        "company": random_company(),
        "api_url": random_url(),
        "description": random_word(),
        "emass_specific_field": random_word()
    }

def generate_ditpr_record():
    return {
        "id": str(uuid.uuid4()),
        "company": random_company(),
        "phone_number": random_phone(),
        "website": random_url(),
        "contact_name": random_name(),
        "contact_email": random_email(),
        "service_description": random_word(),
        "api_endpoint": random_url(),
        "ditpr_specific_field": random_word()
    }

def generate_maps_record():
    return {
        "id": str(uuid.uuid4()),
        "latitude": random_lat(),
        "longitude": random_lon(),
        "location_name": random_city(),
        "map_url": random_url(),
        "api_key": str(uuid.uuid4()),
        "service_name": random_word(),
        "maps_specific_field": random_word()
    }

def generate_esps_record():
    return {
        "id": str(uuid.uuid4()),
        "product_name": random_product(),
        "price": random_price(),
        "category": random.choice(["Electronics","Furniture","Clothing","Books","Toys"]),
        "api_version": f"v{random.randint(1,3)}",
        "developer_name": random_name(),
        "developer_email": random_email(),
        "service_description": random_word(),
        "api_base_url": random_url(),
        "esps_specific_field": random_word()
    }

# -------------------------------
# Repository Management
# -------------------------------
API_REPO_FILE = "API-REPOSITORY.json"

def load_api_repository():
    if os.path.exists(API_REPO_FILE):
        with open(API_REPO_FILE, "r") as f:
            return json.load(f)
    return []

def save_api_repository(repo):
    with open(API_REPO_FILE, "w") as f:
        json.dump(repo, f, indent=4)

def dataframe_to_txt(df):
    return "\n".join([" | ".join([f"{col}: {row[col]}" for col in df.columns]) for _,row in df.iterrows()])

def dataframe_to_excel_bytes(df):
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Data")
    buffer.seek(0)
    return buffer

# -------------------------------
# Streamlit UI
# -------------------------------
st.sidebar.header("⚙️ Controls")
choice = st.sidebar.selectbox("Choose Operation", [
    "Generate Data","Discover APIs","Move to Repository",
    "Display Repository","Upload JSON Logs","Clear Repository"
])

repo = load_api_repository()

# -------------------------------
# Generate Data
# -------------------------------
if choice == "Generate Data":
    st.subheader("📑 Generate Emulator Records")
    emulator = st.selectbox("Select Emulator", ["EMASS","DITPR","MAPS","ESPS"])
    num = st.slider("Number of Records", 5, 100, 10, 5)
    if st.button("Generate"):
        if emulator == "EMASS":
            data = [generate_emass_record() for _ in range(num)]
        elif emulator == "DITPR":
            data = [generate_ditpr_record() for _ in range(num)]
        elif emulator == "MAPS":
            data = [generate_maps_record() for _ in range(num)]
        else:
            data = [generate_esps_record() for _ in range(num)]

        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        file_name = f"{emulator}-Output.json"
        with open(file_name,"w") as f: json.dump(data,f,indent=4)

        # Downloads
        st.download_button("Download JSON", data=json.dumps(data,indent=2), file_name=file_name, mime="application/json")
        st.download_button("Download CSV", data=df.to_csv(index=False), file_name=file_name.replace(".json",".csv"), mime="text/csv")
        st.download_button("Download TXT", data=dataframe_to_txt(df), file_name=file_name.replace(".json",".txt"), mime="text/plain")
        st.download_button("Download Excel", data=dataframe_to_excel_bytes(df), file_name=file_name.replace(".json",".xlsx"), mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# -------------------------------
# Discover APIs
# -------------------------------
elif choice == "Discover APIs":
    st.subheader("🔍 Discover APIs from Emulator Outputs")
    files = [f for f in os.listdir(".") if f.endswith(".json") and "Output" in f]
    if not files:
        st.warning("No JSON emulator outputs found.")
    else:
        file = st.selectbox("Select JSON File", files)
        if st.button("Discover"):
            with open(file,"r") as f: data=json.load(f)
            discovered = [rec for rec in data if any(k in rec for k in ["api_url","api_endpoint","map_url","api_base_url"])]
            if discovered:
                out_file=file.replace(".json","-Discovered-APIs.json")
                with open(out_file,"w") as f: json.dump(discovered,f,indent=4)
                st.success(f"✅ Discovered APIs saved to {out_file}")
                st.dataframe(pd.DataFrame(discovered))
            else:
                st.info("No APIs discovered in this file.")

# -------------------------------
# Move to Repository
# -------------------------------
elif choice == "Move to Repository":
    st.subheader("📦 Move Discovered APIs to Repository")
    files=[f for f in os.listdir(".") if f.endswith("Discovered-APIs.json")]
    if not files:
        st.warning("No discovered API files found.")
    else:
        file=st.selectbox("Select File to Move",files+["Move All"])
        if st.button("Move"):
            if file=="Move All":
                for f in files:
                    with open(f,"r") as fp: repo.extend(json.load(fp))
            else:
                with open(file,"r") as fp: repo.extend(json.load(fp))
            save_api_repository(repo)
            st.success("✅ APIs moved to repository.")

# -------------------------------
# Display Repository (with Search)
# -------------------------------
elif choice == "Display Repository":
    st.subheader("📚 API Repository")
    if not repo:
        st.info("Repository is empty.")
    else:
        df=pd.DataFrame(repo)

        # Search bar
        search_term = st.text_input("🔎 Search (name, company, email, URL):").lower()
        if search_term:
            mask = df.apply(lambda row: row.astype(str).str.lower().str.contains(search_term).any(), axis=1)
            df = df[mask]

        st.dataframe(df,use_container_width=True)

        # Chart
        st.subheader("📊 API Counts by Source")
        type_counts=df.apply(
            lambda row: "EMASS" if "emass_specific_field" in row else
                        "DITPR" if "ditpr_specific_field" in row else
                        "MAPS" if "maps_specific_field" in row else "ESPS",
            axis=1
        ).value_counts().reset_index()
        type_counts.columns=["Emulator","Count"]
        st.plotly_chart(px.bar(type_counts,x="Emulator",y="Count",color="Emulator",text="Count"),use_container_width=True)

        # Downloads
        st.download_button("Download JSON",data=json.dumps(df.to_dict(orient="records"),indent=2),file_name="API-REPOSITORY.json",mime="application/json")
        st.download_button("Download CSV",data=df.to_csv(index=False),file_name="API-REPOSITORY.csv",mime="text/csv")
        st.download_button("Download TXT",data=dataframe_to_txt(df),file_name="API-REPOSITORY.txt",mime="text/plain")
        st.download_button("Download Excel",data=dataframe_to_excel_bytes(df),file_name="API-REPOSITORY.xlsx",mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# -------------------------------
# Upload JSON Logs
# -------------------------------
elif choice == "Upload JSON Logs":
    st.subheader("📤 Upload JSON Log")
    uploaded=st.file_uploader("Upload JSON File",type=["json"])
    if uploaded:
        data=json.load(uploaded)
        repo.extend(data)
        save_api_repository(repo)
        st.success(f"✅ Uploaded {len(data)} records to repository.")

# -------------------------------
# Clear Repository
# -------------------------------
elif choice == "Clear Repository":
    if st.button("🗑️ Clear Repository"):
        repo=[]
        save_api_repository(repo)
        st.success("✅ Repository cleared.")


