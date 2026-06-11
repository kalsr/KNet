# IoT Sensor Data File Management Platform


import streamlit as st
from io import BytesIO
import json
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import shutil
from datetime import datetime
import random

# ---------------------------------------------------------
# Page config
# ---------------------------------------------------------
st.set_page_config(page_title="IoT Sensor Data File Management Platform", layout="wide")

# ---------------------------------------------------------
# Bold blue title bar + app explanation
# ---------------------------------------------------------
st.markdown(
    """
    <div style="background-color:#004aad;padding:15px;border-radius:5px;">
        <h1 style="color:white;text-align:center;margin-bottom:5px;">
            IoT Sensor Data File Management Application Platform
        </h1>
        <h4 style="color:white;text-align:center;margin-top:0;">
            Developed by Randy Singh, Technology Innovation Team (DISA/BDE5)
        </h4>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    This application manages **IoT sensor data files** used for machine learning and data mining with tools such as WEKA.  
    It provides capabilities to create new IoT files, create files in directories, read existing sensor data files, 
    delete duplicate files, determine file size for storage planning, copy files for record keeping, check last modified dates, 
    and append new records to existing files. Visual diagrams, synthetic file metadata, and exportable reports (PDF, Word, JSON) 
    make it suitable for training, documentation, and real‑world IoT data management workflows.
    """
)

st.markdown("---")

# ---------------------------------------------------------
# Operation definitions
# ---------------------------------------------------------
operations = {
    "Create new IoT file": {
        "id": 1,
        "description": (
            "Create a new IoT sensor data file and write a specified number of records into it. "
            "Useful for generating training datasets or test files for ML pipelines."
        ),
        "mermaid": """
flowchart TD
    User[User] --> UI[Create File Form]
    UI --> FileSys[File System]
    FileSys --> NewFile[New IoT Data File]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Create File Form";
    "Create File Form" -> "File System";
    "File System" -> "New IoT Data File";
}
""",
    },
    "Create IoT file in a directory": {
        "id": 2,
        "description": (
            "Create an IoT file inside a specified directory, ensuring folder structure exists. "
            "Supports organizing sensor data by project, device, or environment."
        ),
        "mermaid": """
flowchart TD
    User[User] --> DirInput[Directory + File Name]
    DirInput --> FS[File System]
    FS --> Folder[Create Directory]
    Folder --> File[Create IoT File]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Directory + File Name";
    "Directory + File Name" -> "File System";
    "File System" -> "Directory";
    "Directory" -> "IoT File";
}
""",
    },
    "Read existing IoT sensor data file": {
        "id": 3,
        "description": (
            "Open and read an existing IoT sensor data file to inspect its contents. "
            "Useful for validating datasets before feeding them into ML or analytics tools."
        ),
        "mermaid": """
flowchart TD
    User[User] --> SelectFile[Select IoT File]
    SelectFile --> FS[File System]
    FS --> Content[Read File Contents]
    Content --> Display[Display in UI]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Select IoT File";
    "Select IoT File" -> "File System";
    "File System" -> "File Contents";
    "File Contents" -> "UI Display";
}
""",
    },
    "Delete duplicate IoT file": {
        "id": 4,
        "description": (
            "Delete unnecessary or duplicate IoT sensor data files to reduce clutter and storage usage. "
            "Supports hygiene of data repositories and compliance with retention policies."
        ),
        "mermaid": """
flowchart TD
    User[User] --> SelectDup[Select Duplicate File]
    SelectDup --> FS[File System]
    FS --> Delete[Delete File]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Select Duplicate File";
    "Select Duplicate File" -> "File System";
    "File System" -> "Delete Operation";
}
""",
    },
    "Determine IoT data file size": {
        "id": 5,
        "description": (
            "Calculate the size of an IoT sensor data file in bytes, KB, MB, and higher units. "
            "Helps with storage planning and capacity management for large datasets."
        ),
        "mermaid": """
flowchart TD
    User[User] --> SelectFile[Select File]
    SelectFile --> FS[File System]
    FS --> SizeCalc[Calculate Size]
    SizeCalc --> Display[Show Size Metrics]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Select File";
    "Select File" -> "File System";
    "File System" -> "Size Calculator";
    "Size Calculator" -> "Size Metrics Display";
}
""",
    },
    "Copy IoT data file to another file": {
        "id": 6,
        "description": (
            "Copy an IoT sensor data file to a new file name for backup, record keeping, or experimentation. "
            "Supports versioning and safe duplication of datasets."
        ),
        "mermaid": """
flowchart TD
    User[User] --> Src[Select Source File]
    User --> Dest[Enter Destination Name]
    Src --> FS[File System]
    Dest --> FS
    FS --> Copy[Copy Operation]
    Copy --> NewFile[New File Created]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Source File";
    User -> "Destination Name";
    "Source File" -> "File System";
    "Destination Name" -> "File System";
    "File System" -> "Copy Operation";
    "Copy Operation" -> "New File";
}
""",
    },
    "Check when IoT file was last modified": {
        "id": 7,
        "description": (
            "Retrieve the last modified timestamp of an IoT sensor data file. "
            "Useful for audit trails, data freshness checks, and lifecycle management."
        ),
        "mermaid": """
flowchart TD
    User[User] --> SelectFile[Select File]
    SelectFile --> FS[File System]
    FS --> Meta[Read Metadata]
    Meta --> Display[Show Last Modified Date]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Select File";
    "Select File" -> "File System";
    "File System" -> "File Metadata";
    "File Metadata" -> "Last Modified Display";
}
""",
    },
    "Add new records to existing IoT data file": {
        "id": 8,
        "description": (
            "Append new sensor records to an existing IoT data file. "
            "Supports incremental data collection and continuous logging."
        ),
        "mermaid": """
flowchart TD
    User[User] --> SelectFile[Select Existing File]
    User --> NewRec[Enter New Records]
    SelectFile --> FS[File System]
    NewRec --> FS
    FS --> Append[Append Records]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Existing File";
    User -> "New Records";
    "Existing File" -> "File System";
    "New Records" -> "File System";
    "File System" -> "Append Operation";
}
""",
    },
}

# ---------------------------------------------------------
# Sidebar: operation selection + synthetic data
# ---------------------------------------------------------
if "record_count" not in st.session_state:
    st.session_state.record_count = 0

st.sidebar.header("IoT File Operations & Synthetic Data")

operation_name = st.sidebar.selectbox(
    "Select file management operation",
    options=list(operations.keys()),
)

record_count = st.sidebar.slider(
    "Number of synthetic file metadata records",
    min_value=0,
    max_value=500,
    value=st.session_state.record_count,
    step=10,
)

reset = st.sidebar.button("Reset synthetic data")

if reset:
    st.session_state.record_count = 0
    record_count = 0

st.session_state.record_count = record_count

st.sidebar.markdown(f"**Current synthetic records:** {st.session_state.record_count}")

# ---------------------------------------------------------
# Synthetic data generation (file metadata)
# ---------------------------------------------------------
def generate_synthetic_data(n):
    filenames = [
        "diabetes.arff",
        "breast-cancer.arff",
        "Gas_Consumption_Building_74.txt",
        "Electric_Consumption_Building_74.txt",
        "CCTV_Camera_Dataset.txt",
        "Thermal_Solar_Plant_Recordings.csv",
        "Household_Power_Consumption.txt",
        "Smart_Cars.csv",
        "TimeBasedFeatures-Dataset-120s-NO-VPN.arff",
        "Corona_Virus_Global_Data.csv",
    ]
    data = []
    for i in range(n):
        fname = random.choice(filenames)
        size_bytes = random.randint(10_000, 50_000_000)
        data.append(
            {
                "record_id": i + 1,
                "file_name": fname,
                "size_bytes": size_bytes,
                "size_mb": round(size_bytes / (1024 * 1024), 3),
                "status": random.choice(["Active", "Archived", "To Delete", "Under Review"]),
            }
        )
    return data

synthetic_data = generate_synthetic_data(record_count)

# ---------------------------------------------------------
# Main layout
# ---------------------------------------------------------
selected_op = operations[operation_name]

col_left, col_right = st.columns([1, 1])

with col_left:
    # Colored operation header
    st.markdown(
        f"""
        <div style="background-color:#008080;padding:10px;border-radius:5px;margin-bottom:10px;">
            <h3 style="color:white;margin:0;">Operation: {operation_name}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(f"**What this operation does:** {selected_op['description']}")

    st.markdown("#### Operation Controls")

    # Operation-specific UI
    if selected_op["id"] == 1:
        st.markdown("**Create New IoT File**")
        new_file_name = st.text_input("Enter new IoT file name (e.g., `new_sensor_data.txt`)")
        num_records = st.number_input("Number of records to write", min_value=0, step=1, value=0)
        records = []
        if num_records > 0:
            st.markdown("Enter records (one per line):")
            for i in range(int(num_records)):
                rec = st.text_input(f"Record #{i+1}", key=f"rec_create_{i}")
                records.append(rec)
        create_btn = st.button("Create file")
        if create_btn and new_file_name:
            with open(new_file_name, "w", encoding="utf-8") as f:
                for r in records:
                    f.write(r + "\n")
            st.success(f"File `{new_file_name}` created with {len(records)} records.")

    elif selected_op["id"] == 2:
        st.markdown("**Create IoT File in a Directory**")
        dir_path = st.text_input("Directory path (e.g., `./iot_data`)")
        file_name = st.text_input("File name (e.g., `sensor_log.txt`)")
        create_dir_btn = st.button("Create file in directory")
        if create_dir_btn and dir_path and file_name:
            os.makedirs(dir_path, exist_ok=True)
            full_path = os.path.join(dir_path, file_name)
            if not os.path.exists(full_path):
                open(full_path, "w", encoding="utf-8").close()
                st.success(f"File `{full_path}` created.")
            else:
                st.warning(f"File `{full_path}` already exists.")

    elif selected_op["id"] == 3:
        st.markdown("**Read Existing IoT Sensor Data File**")
        file_to_read = st.text_input("Enter path to existing IoT file")
        read_btn = st.button("Read file")
        if read_btn and file_to_read:
            if os.path.exists(file_to_read):
                with open(file_to_read, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                st.text_area("File contents", content, height=300)
            else:
                st.error("File does not exist.")

    elif selected_op["id"] == 4:
        st.markdown("**Delete Duplicate IoT File**")
        file_to_delete = st.text_input("Enter path to file to delete")
        del_btn = st.button("Delete file")
        if del_btn and file_to_delete:
            if os.path.exists(file_to_delete):
                os.remove(file_to_delete)
                st.success(f"File `{file_to_delete}` deleted.")
            else:
                st.error("File does not exist.")

    elif selected_op["id"] == 5:
        st.markdown("**Determine IoT Data File Size**")
        file_to_size = st.text_input("Enter path to file")
        size_btn = st.button("Calculate size")
        if size_btn and file_to_size:
            if os.path.exists(file_to_size):
                size_bytes = os.path.getsize(file_to_size)
                kb = size_bytes / 1024
                mb = kb / 1024
                gb = mb / 1024
                st.markdown(f"- **Bytes:** {size_bytes}")
                st.markdown(f"- **Kilobytes:** {kb:.3f}")
                st.markdown(f"- **Megabytes:** {mb:.3f}")
                st.markdown(f"- **Gigabytes:** {gb:.6f}")
            else:
                st.error("File does not exist.")

    elif selected_op["id"] == 6:
        st.markdown("**Copy IoT Data File to Another File**")
        src_file = st.text_input("Source file path")
        dst_file = st.text_input("Destination file path")
        copy_btn = st.button("Copy file")
        if copy_btn and src_file and dst_file:
            if os.path.exists(src_file):
                shutil.copy2(src_file, dst_file)
                st.success(f"File copied from `{src_file}` to `{dst_file}`.")
            else:
                st.error("Source file does not exist.")

    elif selected_op["id"] == 7:
        st.markdown("**Check When IoT File Was Last Modified**")
        file_to_check = st.text_input("Enter path to file")
        check_btn = st.button("Check last modified date")
        if check_btn and file_to_check:
            if os.path.exists(file_to_check):
                ts = os.path.getmtime(file_to_check)
                dt = datetime.fromtimestamp(ts)
                st.markdown(f"**Last modified on:** {dt.strftime('%m/%d/%Y %H:%M:%S')}")
            else:
                st.error("File does not exist.")

    elif selected_op["id"] == 8:
        st.markdown("**Add New Records to Existing IoT Data File**")
        file_to_append = st.text_input("Enter path to existing file")
        num_append = st.number_input("Number of records to append", min_value=0, step=1, value=0)
        append_records = []
        if num_append > 0:
            st.markdown("Enter records to append:")
            for i in range(int(num_append)):
                rec = st.text_input(f"New Record #{i+1}", key=f"rec_append_{i}")
                append_records.append(rec)
        append_btn = st.button("Append records")
        if append_btn and file_to_append:
            if os.path.exists(file_to_append):
                with open(file_to_append, "a", encoding="utf-8") as f:
                    for r in append_records:
                        f.write(r + "\n")
                st.success(f"Appended {len(append_records)} records to `{file_to_append}`.")
            else:
                st.error("File does not exist.")

    st.markdown("#### Diagrams & Flow Charts")

    tab_mermaid, tab_graphviz = st.tabs(["Mermaid diagram", "Graphviz diagram"])

    with tab_mermaid:
        st.markdown("##### Logical flow (Mermaid)")
        st.markdown(
            f"```mermaid\n{selected_op['mermaid']}\n```",
            unsafe_allow_html=True,
        )

    with tab_graphviz:
        st.markdown("##### Data/Process flow (Graphviz)")
        st.graphviz_chart(selected_op["graphviz"])

with col_right:
    st.subheader("Synthetic IoT File Metadata Preview")
    if synthetic_data:
        st.dataframe(synthetic_data, use_container_width=True)
    else:
        st.info("No synthetic data generated. Use the slider in the sidebar to create records.")

# ---------------------------------------------------------
# Export functions
# ---------------------------------------------------------
def build_text_report(operation_name, op, synthetic_data):
    lines = []
    lines.append("IoT Sensor Data File Management Report")
    lines.append("Developed by Randy Singh, Technology Innovation Team (DISA/BDE5)")
    lines.append("")
    lines.append(f"Selected Operation: {operation_name}")
    lines.append("")
    lines.append("Operation Description:")
    lines.append(op["description"])
    lines.append("")
    lines.append("Synthetic File Metadata Records:")
    lines.append(f"Total records: {len(synthetic_data)}")
    for row in synthetic_data[:50]:
        lines.append(
            f"Record {row['record_id']}: {row['file_name']} "
            f"(Size MB: {row['size_mb']}, Status: {row['status']})"
        )
    return "\n".join(lines)

def export_pdf(text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    y = height - 50
    for line in text.split("\n"):
        c.drawString(50, y, line[:100])
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50
    c.save()
    buffer.seek(0)
    return buffer

def export_word(text):
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

def export_json(operation_name, op, synthetic_data):
    payload = {
        "application": "IoT Sensor Data File Management Application Platform",
        "developer": "Randy Singh, Technology Innovation Team (DISA/BDE5)",
        "operation": operation_name,
        "description": op["description"],
        "synthetic_data": synthetic_data,
    }
    buffer = BytesIO()
    buffer.write(json.dumps(payload, indent=2).encode("utf-8"))
    buffer.seek(0)
    return buffer

# ---------------------------------------------------------
# Export buttons
# ---------------------------------------------------------
st.markdown("---")
st.subheader("Export File Management Report")

report_text = build_text_report(operation_name, selected_op, synthetic_data)

pdf_buffer = export_pdf(report_text)
word_buffer = export_word(report_text)
json_buffer = export_json(operation_name, selected_op, synthetic_data)

col1, col2, col3 = st.columns(3)

with col1:
    st.download_button(
        label="📄 Export as PDF",
        data=pdf_buffer,
        file_name="iot_file_management_report.pdf",
        mime="application/pdf",
    )

with col2:
    st.download_button(
        label="📝 Export as Word",
        data=word_buffer,
        file_name="iot_file_management_report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

with col3:
    st.download_button(
        label="🧾 Export as JSON",
        data=json_buffer,
        file_name="iot_file_management_report.json",
        mime="application/json",
    )
