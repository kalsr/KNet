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
# Cloud-safe workspace
# ---------------------------------------------------------
WORKSPACE = "workspace"
FILES_DIR = os.path.join(WORKSPACE, "files")
UPLOADS_DIR = os.path.join(WORKSPACE, "uploads")

os.makedirs(FILES_DIR, exist_ok=True)
os.makedirs(UPLOADS_DIR, exist_ok=True)

# ---------------------------------------------------------
# Title bar + explanation
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
    This application manages IoT sensor data files inside a cloud‑safe `workspace/` folder.  
    All file operations (create, read, delete, copy, append, size, metadata) occur inside this workspace,  
    ensuring compatibility with Streamlit Cloud, Windows, Linux, and macOS.  
    Uploaded files are stored in `workspace/uploads/`, and created/copied files are stored in `workspace/files/`.
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
        "description": "Read a file from workspace/files, workspace/uploads, or directly from uploader.",
        "mermaid": """
flowchart TD
    User --> SelectSource[Select Source]
    SelectSource --> FS[Workspace]
    FS --> Content[Read Contents]
    Content --> Display[Show in UI]
    """,
        "graphviz": """
digraph {
    rankdir=LR;
    User -> "Select Source";
    "Select Source" -> Workspace;
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
# Sidebar: operation + synthetic data
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
# Sidebar: workspace browser + uploader (A, B, C, D)
# ---------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("Workspace Directory Browser")

files_in_files = sorted(os.listdir(FILES_DIR))
files_in_uploads = sorted(os.listdir(UPLOADS_DIR))

st.sidebar.write(f"Files in workspace/files ({len(files_in_files)}):")
for f in files_in_files[:20]:
    st.sidebar.write(f"- {f}")

st.sidebar.write(f"Files in workspace/uploads ({len(files_in_uploads)}):")
for f in files_in_uploads[:20]:
    st.sidebar.write(f"- {f}")

st.sidebar.markdown("---")
st.sidebar.subheader("Upload IoT Sensor Data File")

uploaded_file_sidebar = st.sidebar.file_uploader("Upload a file")
auto_move = st.sidebar.checkbox("Automatically copy uploaded files into workspace/files", value=True)

if uploaded_file_sidebar:
    upload_path = os.path.join(UPLOADS_DIR, uploaded_file_sidebar.name)
    with open(upload_path, "wb") as f:
        f.write(uploaded_file_sidebar.read())
    st.sidebar.success(f"Uploaded to {upload_path}")

    if auto_move:
        dest_path = os.path.join(FILES_DIR, uploaded_file_sidebar.name)
        try:
            shutil.copy2(upload_path, dest_path)
            st.sidebar.success(f"Copied to workspace/files as {uploaded_file_sidebar.name}")
        except Exception as e:
            st.sidebar.error(f"Error copying to workspace/files: {e}")

# Manual move button (B)
if len(files_in_uploads) > 0:
    st.sidebar.markdown("Move uploaded file into workspace/files")
    file_to_move = st.sidebar.selectbox("Select uploaded file", files_in_uploads)
    if st.sidebar.button("Move selected uploaded file to workspace/files"):
        src = os.path.join(UPLOADS_DIR, file_to_move)
        dst = os.path.join(FILES_DIR, file_to_move)
        try:
            shutil.copy2(src, dst)
            st.sidebar.success(f"Moved {file_to_move} to workspace/files")
        except Exception as e:
            st.sidebar.error(f"Error moving file: {e}")

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

    # 1. Create new file
    if selected_op["id"] == 1:
        new_file_name = st.text_input("Enter new IoT file name")
        num_records = st.number_input("Number of records", min_value=0, step=1)
        records = []
        for i in range(int(num_records)):
            rec = st.text_input(f"Record #{i+1}", key=f"rec_create_{i}")
            records.append(rec)
        if st.button("Create file"):
            if new_file_name:
                full_path = os.path.join(FILES_DIR, new_file_name)
                with open(full_path, "w", encoding="utf-8") as f:
                    for r in records:
                        f.write(r + "\n")
                st.success(f"Created file: {full_path}")
            else:
                st.error("Please enter a file name.")

    # 2. Create file in directory
    elif selected_op["id"] == 2:
        subdir = st.text_input("Subdirectory inside workspace/files")
        file_name = st.text_input("File name")
        if st.button("Create file"):
            if subdir and file_name:
                full_dir = os.path.join(FILES_DIR, subdir)
                os.makedirs(full_dir, exist_ok=True)
                full_path = os.path.join(full_dir, file_name)
                open(full_path, "w").close()
                st.success(f"Created file: {full_path}")
            else:
                st.error("Please enter both subdirectory and file name.")

    # 3. Read file (safe, with all sources)
    elif selected_op["id"] == 3:
        st.markdown("### Read IoT Sensor Data File")
        st.markdown("You can read:")
        st.markdown("- A file from **workspace/files**")
        st.markdown("- A file from **workspace/uploads**")
        st.markdown("- A file uploaded directly here")

        workspace_files_local = sorted(os.listdir(FILES_DIR))
        upload_files_local = sorted(os.listdir(UPLOADS_DIR))

        read_mode = st.radio(
            "Choose file source:",
            ["Workspace Files", "Uploaded Files (workspace/uploads)", "File Uploader"],
            index=0
        )

        # Workspace files
        if read_mode == "Workspace Files":
            if len(workspace_files_local) == 0:
                st.warning("No files found in workspace/files.")
            else:
                file_to_read = st.selectbox("Select a workspace file", workspace_files_local)
                if st.button("Read workspace file"):
                    if file_to_read:
                        full_path = os.path.join(FILES_DIR, file_to_read)
                        try:
                            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                                content = f.read()
                            st.text_area("File Contents", content, height=300)
                        except Exception as e:
                            st.error(f"Error reading file: {e}")
                    else:
                        st.error("No file selected.")

        # Uploaded files in workspace/uploads
        if read_mode == "Uploaded Files (workspace/uploads)":
            if len(upload_files_local) == 0:
                st.warning("No uploaded files found in workspace/uploads.")
            else:
                file_to_read = st.selectbox("Select an uploaded file", upload_files_local)
                if st.button("Read uploaded file"):
                    if file_to_read:
                        full_path = os.path.join(UPLOADS_DIR, file_to_read)
                        try:
                            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                                content = f.read()
                            st.text_area("Uploaded File Contents", content, height=300)
                        except Exception as e:
                            st.error(f"Error reading file: {e}")
                    else:
                        st.error("No file selected.")

        # Direct uploader
        if read_mode == "File Uploader":
            uploaded_direct = st.file_uploader("Upload a file to read")
            if uploaded_direct:
                try:
                    content = uploaded_direct.read().decode("utf-8", errors="ignore")
                    st.text_area("Uploaded File Contents", content, height=300)
                except Exception as e:
                    st.error(f"Error reading uploaded file: {e}")

    # 4. Delete file
    elif selected_op["id"] == 4:
        workspace_files_local = sorted(os.listdir(FILES_DIR))
        if len(workspace_files_local) == 0:
            st.warning("No files to delete in workspace/files.")
        else:
            file_to_delete = st.selectbox("Select file to delete", workspace_files_local)
            if st.button("Delete file"):
                full_path = os.path.join(FILES_DIR, file_to_delete)
                try:
                    os.remove(full_path)
                    st.success(f"Deleted: {file_to_delete}")
                except Exception as e:
                    st.error(f"Error deleting file: {e}")

    # 5. File size
    elif selected_op["id"] == 5:
        workspace_files_local = sorted(os.listdir(FILES_DIR))
        if len(workspace_files_local) == 0:
            st.warning("No files in workspace/files.")
        else:
            file_to_size = st.selectbox("Select file", workspace_files_local)
            if st.button("Calculate size"):
                full_path = os.path.join(FILES_DIR, file_to_size)
                try:
                    size_bytes = os.path.getsize(full_path)
                    st.write(f"Bytes: {size_bytes}")
                    st.write(f"KB: {size_bytes/1024:.3f}")
                    st.write(f"MB: {size_bytes/1024/1024:.3f}")
                    st.write(f"GB: {size_bytes/1024/1024/1024:.6f}")
                except Exception as e:
                    st.error(f"Error getting file size: {e}")

    # 6. Copy file
    elif selected_op["id"] == 6:
        workspace_files_local = sorted(os.listdir(FILES_DIR))
        if len(workspace_files_local) == 0:
            st.warning("No files in workspace/files.")
        else:
            src = st.selectbox("Source file", workspace_files_local)
            dst = st.text_input("Destination file name")
            if st.button("Copy file"):
                if src and dst:
                    try:
                        shutil.copy2(os.path.join(FILES_DIR, src), os.path.join(FILES_DIR, dst))
                        st.success(f"Copied {src} to {dst}")
                    except Exception as e:
                        st.error(f"Error copying file: {e}")
                else:
                    st.error("Please select source and enter destination name.")

    # 7. Last modified
    elif selected_op["id"] == 7:
        workspace_files_local = sorted(os.listdir(FILES_DIR))
        if len(workspace_files_local) == 0:
            st.warning("No files in workspace/files.")
        else:
            file_to_check = st.selectbox("Select file", workspace_files_local)
            if st.button("Check timestamp"):
                full_path = os.path.join(FILES_DIR, file_to_check)
                try:
                    ts = os.path.getmtime(full_path)
                    dt = datetime.fromtimestamp(ts)
                    st.write(f"Last modified: {dt.strftime('%m/%d/%Y %H:%M:%S')}")
                except Exception as e:
                    st.error(f"Error reading timestamp: {e}")

    # 8. Append records
    elif selected_op["id"] == 8:
        workspace_files_local = sorted(os.listdir(FILES_DIR))
        if len(workspace_files_local) == 0:
            st.warning("No files in workspace/files.")
        else:
            file_to_append = st.selectbox("Select file", workspace_files_local)
            num_append = st.number_input("Number of records to append", min_value=0, step=1)
            append_records = []
            for i in range(int(num_append)):
                rec = st.text_input(f"New Record #{i+1}", key=f"rec_append_{i}")
                append_records.append(rec)
            if st.button("Append"):
                if file_to_append:
                    full_path = os.path.join(FILES_DIR, file_to_append)
                    try:
                        with open(full_path, "a", encoding="utf-8") as f:
                            for r in append_records:
                                f.write(r + "\n")
                        st.success(f"Appended {len(append_records)} records to {file_to_append}.")
                    except Exception as e:
                        st.error(f"Error appending to file: {e}")
                else:
                    st.error("No file selected.")

    # Diagrams
    st.markdown("#### Diagrams & Flow Charts")
    tab_mermaid, tab_graphviz = st.tabs(["Mermaid", "Graphviz"])
    with tab_mermaid:
        st.markdown(f"```mermaid\n{selected_op['mermaid']}\n```")
    with tab_graphviz:
        st.graphviz_chart(selected_op["graphviz"])

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
