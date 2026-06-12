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
# Create cloud-safe workspace
# ---------------------------------------------------------
WORKSPACE = "workspace"
FILES_DIR = os.path.join(WORKSPACE, "files")
UPLOADS_DIR = os.path.join(WORKSPACE, "uploads")

os.makedirs(FILES_DIR, exist_ok=True)
os.makedirs(UPLOADS_DIR, exist_ok=True)

# ---------------------------------------------------------
# Bold blue title bar + explanation
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
    This upgraded version uses a **cloud‑safe virtual filesystem** inside a dedicated `workspace/` folder.  
    All file operations (create, read, delete, copy, append, size, metadata) occur inside this workspace,  
    ensuring full compatibility with **Streamlit Cloud**, Windows, Linux, and macOS.  
    Uploaded files are stored in `workspace/uploads/`, and created files are stored in `workspace/files/`.
    """
)

st.markdown("---")

# ---------------------------------------------------------
# Operation definitions
# ---------------------------------------------------------
operations = {
    "Create new IoT file": {
        "id": 1,
        "description": "Create a new IoT sensor data file and write records into it.",
        "mermaid": """
flowchart TD
    User --> UI[Create File Form]
    UI --> FS[Workspace File System]
    FS --> NewFile[New IoT File]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Create File Form";
    "Create File Form" -> "Workspace File System";
    "Workspace File System" -> "New IoT File";
}
""",
    },
    "Create IoT file in a directory": {
        "id": 2,
        "description": "Create an IoT file inside a subdirectory of the workspace.",
        "mermaid": """
flowchart TD
    User --> DirInput[Directory + File Name]
    DirInput --> FS[Workspace]
    FS --> Folder[Create Directory]
    Folder --> File[Create IoT File]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Directory + File Name";
    "Directory + File Name" -> Workspace;
    Workspace -> "Directory";
    "Directory" -> "IoT File";
}
""",
    },
    "Read existing IoT sensor data file": {
        "id": 3,
        "description": "Read a file from workspace/files or from uploaded files.",
        "mermaid": """
flowchart TD
    User --> SelectFile[Select File]
    SelectFile --> FS[Workspace]
    FS --> Content[Read Contents]
    Content --> Display[Show in UI]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Select File";
    "Select File" -> Workspace;
    Workspace -> "File Contents";
    "File Contents" -> UI;
}
""",
    },
    "Delete duplicate IoT file": {
        "id": 4,
        "description": "Delete a file from workspace/files.",
        "mermaid": """
flowchart TD
    User --> SelectDup[Select File]
    SelectDup --> FS[Workspace]
    FS --> Delete[Delete File]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Select File";
    "Select File" -> Workspace;
    Workspace -> "Delete Operation";
}
""",
    },
    "Determine IoT data file size": {
        "id": 5,
        "description": "Calculate file size in bytes, KB, MB, GB.",
        "mermaid": """
flowchart TD
    User --> SelectFile[Select File]
    SelectFile --> FS[Workspace]
    FS --> SizeCalc[Calculate Size]
    SizeCalc --> Display[Show Metrics]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Select File";
    "Select File" -> Workspace;
    Workspace -> "Size Calculator";
    "Size Calculator" -> "Size Metrics";
}
""",
    },
    "Copy IoT data file to another file": {
        "id": 6,
        "description": "Copy a file inside workspace/files.",
        "mermaid": """
flowchart TD
    User --> Src[Source File]
    User --> Dest[Destination Name]
    Src --> FS[Workspace]
    Dest --> FS
    FS --> Copy[Copy Operation]
    Copy --> NewFile[New File]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Source File";
    User -> "Destination Name";
    "Source File" -> Workspace;
    "Destination Name" -> Workspace;
    Workspace -> "Copy Operation";
    "Copy Operation" -> "New File";
}
""",
    },
    "Check when IoT file was last modified": {
        "id": 7,
        "description": "Show last modified timestamp of a workspace file.",
        "mermaid": """
flowchart TD
    User --> SelectFile[Select File]
    SelectFile --> FS[Workspace]
    FS --> Meta[Read Metadata]
    Meta --> Display[Show Timestamp]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Select File";
    "Select File" -> Workspace;
    Workspace -> "Metadata";
    "Metadata" -> "Timestamp Display";
}
""",
    },
    "Add new records to existing IoT data file": {
        "id": 8,
        "description": "Append new records to a file in workspace/files.",
        "mermaid": """
flowchart TD
    User --> SelectFile[Select File]
    User --> NewRec[Enter Records]
    SelectFile --> FS[Workspace]
    NewRec --> FS
    FS --> Append[Append Operation]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Existing File";
    User -> "New Records";
    "Existing File" -> Workspace;
    "New Records" -> Workspace;
    Workspace -> "Append Operation";
}
""",
    },
}

# ---------------------------------------------------------
# Sidebar: operation selection + synthetic data
# ---------------------------------------------------------
if "record_count" not in st.session_state:
    st.session_state.record_count = 0

st.sidebar.header("Operations & Synthetic Data")

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

# ---------------------------------------------------------
# Synthetic data generator
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
        "Corona_Virus_World_Wide_Data.txt",
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
# Sidebar: Workspace directory browser
# ---------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("Workspace Directory Browser")

workspace_files = sorted(os.listdir(FILES_DIR))
st.sidebar.write(f"Files in workspace/files ({len(workspace_files)}):")

for f in workspace_files[:20]:
    st.sidebar.write(f"- {f}")

st.sidebar.markdown("---")
st.sidebar.subheader("Upload IoT Sensor Data File")

uploaded_file = st.sidebar.file_uploader("Upload a file")

if uploaded_file:
    save_path = os.path.join(UPLOADS_DIR, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.read())
    st.sidebar.success(f"Uploaded to {save_path}")

# ---------------------------------------------------------
# Main layout
# ---------------------------------------------------------
selected_op = operations[operation_name]

col_left, col_right = st.columns([1, 1])

with col_left:
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

    # -----------------------------
    # Operation 1: Create new file
    # -----------------------------
    if selected_op["id"] == 1:
        new_file_name = st.text_input("Enter new IoT file name")
        num_records = st.number_input("Number of records", min_value=0, step=1)
        records = []
        for i in range(int(num_records)):
            rec = st.text_input(f"Record #{i+1}", key=f"rec_create_{i}")
            records.append(rec)

        if st.button("Create file"):
            full_path = os.path.join(FILES_DIR, new_file_name)
            with open(full_path, "w", encoding="utf-8") as f:
                for r in records:
                    f.write(r + "\n")
            st.success(f"Created file: {full_path}")

    # -----------------------------
    # Operation 2: Create file in directory
    # -----------------------------
    elif selected_op["id"] == 2:
        subdir = st.text_input("Subdirectory inside workspace/files")
        file_name = st.text_input("File name")
        if st.button("Create file"):
            full_dir = os.path.join(FILES_DIR, subdir)
            os.makedirs(full_dir, exist_ok=True)
            full_path = os.path.join(full_dir, file_name)
            open(full_path, "w").close()
            st.success(f"Created file: {full_path}")

    # -----------------------------
    # Operation 3: Read file
    # -----------------------------
    elif selected_op["id"] == 3:
        file_to_read = st.selectbox("Select file to read", workspace_files)
        if st.button("Read file"):
            full_path = os.path.join(FILES_DIR, file_to_read)
            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            st.text_area("File contents", content, height=300)

        if uploaded_file:
            st.markdown("**Uploaded file contents:**")
            content = uploaded_file.read().decode("utf-8", errors="ignore")
            st.text_area("Uploaded file", content, height=300)

    # -----------------------------
    # Operation 4: Delete file
    # -----------------------------
    elif selected_op["id"] == 4:
        file_to_delete = st.selectbox("Select file to delete", workspace_files)
        if st.button("Delete file"):
            os.remove(os.path.join(FILES_DIR, file_to_delete))
            st.success(f"Deleted: {file_to_delete}")

    # -----------------------------
    # Operation 5: File size
    # -----------------------------
    elif selected_op["id"] == 5:
        file_to_size = st.selectbox("Select file", workspace_files)
        if st.button("Calculate size"):
            full_path = os.path.join(FILES_DIR, file_to_size)
            size_bytes = os.path.getsize(full_path)
            st.write(f"Bytes: {size_bytes}")
            st.write(f"KB: {size_bytes/1024:.3f}")
            st.write(f"MB: {size_bytes/1024/1024:.3f}")
            st.write(f"GB: {size_bytes/1024/1024/1024:.6f}")

    # -----------------------------
    # Operation 6: Copy file
    # -----------------------------
    elif selected_op["id"] == 6:
        src = st.selectbox("Source file", workspace_files)
        dst = st.text_input("Destination file name")
        if st.button("Copy file"):
            shutil.copy2(os.path.join(FILES_DIR, src), os.path.join(FILES_DIR, dst))
            st.success(f"Copied to: {dst}")

    # -----------------------------
    # Operation 7: Last modified
    # -----------------------------
    elif selected_op["id"] == 7:
        file_to_check = st.selectbox("Select file", workspace_files)
        if st.button("Check timestamp"):
            full_path = os.path.join(FILES_DIR, file_to_check)
            ts = os.path.getmtime(full_path)
            dt = datetime.fromtimestamp(ts)
            st.write(f"Last modified: {dt}")

    # -----------------------------
    # Operation 8: Append records
    # -----------------------------
    elif selected_op["id"] == 8:
        file_to_append = st.selectbox("Select file", workspace_files)
        num_append = st.number_input("Number of records to append", min_value=0, step=1)
        append_records = []
        for i in range(int(num_append)):
            rec = st.text_input(f"New Record #{i+1}", key=f"rec_append_{i}")
            append_records.append(rec)

        if st.button("Append"):
            full_path = os.path.join(FILES_DIR, file_to_append)
            with open(full_path, "a", encoding="utf-8") as f:
                for r in append_records:
                    f.write(r + "\n")
            st.success(f"Appended {len(append_records)} records.")

    # -----------------------------
    # Diagrams
    # -----------------------------
    st.markdown("#### Diagrams & Flow Charts")

    tab_mermaid, tab_graphviz = st.tabs(["Mermaid", "Graphviz"])

    with tab_mermaid:
        st.markdown(f"```mermaid\n{selected_op['mermaid']}\n```")

    with tab_graphviz:
        st.graphviz_chart(selected_op["graphviz"])

# ---------------------------------------------------------
# Right column: Synthetic data
# ---------------------------------------------------------
with col_right:
    st.subheader("Synthetic IoT File Metadata Preview")
    st.dataframe(synthetic_data, use_container_width=True)

# ---------------------------------------------------------
# Export functions
# ---------------------------------------------------------
def build_text_report(operation_name, op, synthetic_data):
    lines = [
        "IoT Sensor Data File Management Report",
        "Developed by Randy Singh, Technology Innovation Team (DISA/BDE5)",
        "",
        f"Operation: {operation_name}",
        "",
        "Description:",
        op["description"],
        "",
        "Synthetic Data Records:",
        f"Total: {len(synthetic_data)}",
    ]
    for row in synthetic_data[:50]:
        lines.append(
            f"{row['record_id']}: {row['file_name']} ({row['size_mb']} MB, {row['status']})"
        )
    return "\n".join(lines)

def export_pdf(text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    y = 750
    for line in text.split("\n"):
        c.drawString(40, y, line[:100])
        y -= 15
        if y < 40:
            c.showPage()
            y = 750
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
        "operation": operation_name,
        "description": op["description"],
        "synthetic_data": synthetic_data,
    }
    buffer = BytesIO()
    buffer.write(json.dumps(payload, indent=2).encode())
    buffer.seek(0)
    return buffer

# ---------------------------------------------------------
# Export buttons
# ---------------------------------------------------------
st.markdown("---")
st.subheader("Export Report")

report_text = build_text_report(operation_name, selected_op, synthetic_data)

col1, col2, col3 = st.columns(3)

with col1:
    st.download_button("📄 PDF", export_pdf(report_text), "iot_report.pdf")

with col2:
    st.download_button("📝 Word", export_word(report_text), "iot_report.docx")

with col3:
    st.download_button("🧾 JSON", export_json(operation_name, selected_op, synthetic_data), "iot_report.json")
