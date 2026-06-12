# -----------------------------
# Operation 3: Read file (PATCHED)
# -----------------------------
elif selected_op["id"] == 3:
    st.markdown("### Read IoT Sensor Data File")

    st.markdown("You can read:")
    st.markdown("- A file from **workspace/files**")
    st.markdown("- A file from **workspace/uploads**")
    st.markdown("- A file uploaded via the uploader")

    # Workspace file list
    workspace_files = sorted(os.listdir(FILES_DIR))
    upload_files = sorted(os.listdir(UPLOADS_DIR))

    read_mode = st.radio(
        "Choose file source:",
        ["Workspace Files", "Uploaded Files", "File Uploader"],
        index=0
    )

    # -----------------------------
    # READ FROM WORKSPACE
    # -----------------------------
    if read_mode == "Workspace Files":
        if len(workspace_files) == 0:
            st.warning("No files found in workspace/files.")
        else:
            file_to_read = st.selectbox("Select a workspace file", workspace_files)

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

    # -----------------------------
    # READ FROM UPLOADS DIRECTORY
    # -----------------------------
    if read_mode == "Uploaded Files":
        if len(upload_files) == 0:
            st.warning("No uploaded files found in workspace/uploads.")
        else:
            file_to_read = st.selectbox("Select an uploaded file", upload_files)

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

    # -----------------------------
    # READ DIRECTLY FROM FILE UPLOADER
    # -----------------------------
    if read_mode == "File Uploader":
        uploaded = st.file_uploader("Upload a file to read")

        if uploaded:
            try:
                content = uploaded.read().decode("utf-8", errors="ignore")
                st.text_area("Uploaded File Contents", content, height=300)
            except Exception as e:
                st.error(f"Error reading uploaded file: {e}")
