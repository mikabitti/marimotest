import marimo

__generated_with = "0.17.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import os
    from pathlib import Path
    return Path, mo


@app.cell
def _(mo):
    folder_input = mo.ui.text(
        value=".",
        label="Folder path:",
        placeholder="Enter folder path (default: current directory)"
    )

    return (folder_input,)


@app.cell
def _(Path, folder_input, mo):
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
    return (file_checkboxes,)


@app.cell
def _(file_checkboxes, mo):
    mo.stop(file_checkboxes is None)
    return


@app.cell(hide_code=True)
def _(folder_input):
    folder_input
    return


@app.cell
def _(file_checkboxes):
    file_checkboxes
    return


@app.cell
def _(file_checkboxes, mo):
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
    return


if __name__ == "__main__":
    app.run()
