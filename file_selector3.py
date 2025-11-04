import marimo

__generated_with = "0.17.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import os
    from pathlib import Path
    import pandas as pd
    return Path, mo, pd


@app.cell
def _(folder_input):
    folder_input
    return


@app.cell
def _(file_checkboxes, mo):
    mo.stop(file_checkboxes is None)
    file_checkboxes
    return


@app.cell
def _(df, mo):
    mo.ui.dataframe(df)
    return


@app.cell
def _(file_checkboxes, mo):
    selected_path = file_checkboxes.value
    mo.md(
        f"""
        **Selected file path:**

        ```python
        {selected_path}
        ```
        """
    )
    return (selected_path,)


@app.cell
def _(pd, selected_path):
    df = pd.read_csv(selected_path)

    df['duration'] = df['duration'].str.replace(' min', '').str.split(' h')

    def to_minutes(x: list):
        if len(x) == 2:
            return x[0]*60 + x[1]
        else:
            return x[0]

    df['real_duration'] = df['duration'].apply(to_minutes)
    df['distance'] = df['distance'].str.replace(
        ' km', '').str.replace(',', '.').astype(float)

    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(mo):
    folder_input = mo.ui.text(
        value=".",
        label="Folder path:",
        placeholder="Enter folder path (default: current directory)"
    )
    folder_input
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
        file_checkboxes = mo.ui.radio(
            options={path: path for path in recent_files},
            label="Select a file:"
        )
        mo.md(
            f"**Top 5 most recently modified files in:** `{folder_input.value}`")
    else:
        file_checkboxes = None
        mo.md(f"No files found in `{folder_input.value}`")
    return (file_checkboxes,)


if __name__ == "__main__":
    app.run()
