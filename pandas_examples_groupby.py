import marimo

__generated_with = "0.17.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    data = {
        'cust': ["John", "John", "John", "Marjanna", "Marjanna", "Marjanna"],
        'prod': ['apple', 'apple', 'apple', 'banana', 'banana', 'banana'],
        'amount': [1, 1, 2, 3, 2, 4],
        'type': ['Vel', 'Vel', 'Hyv', 'Hyv', 'Vel', 'Vel']
    }
    df = pd.DataFrame(data)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.groupby(['prod', 'type'])['amount'].sum()
    return


if __name__ == "__main__":
    app.run()
