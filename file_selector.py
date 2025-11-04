import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import os
    from pathlib import Path
    return Path, mo, os


@app.cell
def __(mo):
    folder_input = mo.ui.text(
        value=".",
        label="Folder path:",
        placeholder="Enter folder path (default: current directory)"
    )
    folder_input
    return (folder_input,)


@app.cell
def __(Path, folder_input, mo, os):
    def get_recent_files(folder_path, n=5):
        """Get the n most recently modified files in a folder."""
        try:
            path = Path(folder_path)
            if not path.exists():
                return []

            # Get all files (not directories) with their modification times
            files = []
            for item in path.iterdir():
                if item.is_file():
                    files.append((item, item.stat().st_mtime))

            # Sort by modification time (most recent first)
            files.sort(key=lambda x: x[1], reverse=True)

            # Return top n files
            return [str(f[0]) for f in files[:n]]
        except Exception as e:
            return []

    recent_files = get_recent_files(folder_input.value)

    if recent_files:
        file_checkboxes = mo.ui.multiselect(
            options={path: Path(path).name for path in recent_files},
            label="Select files:"
        )
        mo.md(
            f"**Top 5 most recently modified files in:** `{folder_input.value}`")
    else:
        file_checkboxes = None
        mo.md(f"No files found in `{folder_input.value}`")
    return file_checkboxes, get_recent_files, recent_files


@app.cell
def __(file_checkboxes, mo):
    mo.stop(file_checkboxes is None)
    file_checkboxes
    return


@app.cell
def __(file_checkboxes, mo):
    selected_paths = file_checkboxes.value

    mo.md(
        f"""
        **Selected file paths:**
        
        ```python
        {selected_paths}
        ```
        
        Number of selected files: {len(selected_paths)}
        """
    )
    return (selected_paths,)


if __name__ == "__main__":
    app.run()
