import marimo

__generated_with = "0.17.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def _():
    data = {
        'cust': ["John", "John", "John", "Marjanna", "Marjanna", "Marjanna"],
        'prod': ['apple', 'apple', 'apple', 'banana', 'banana', 'banana'],
        'amount': [1, 1, 2, 3, 2, 4],
        'type': ['Vel', 'Vel', 'Hyv', 'Hyv', 'Vel', 'Vel']
    }
    return (data,)


@app.cell
def _(data, pd):
    df = pd.DataFrame(data)
    return (df,)


@app.cell
def _(mo):

    mo.md("""
    ## Boolean Masks in Pandas

    A **boolean mask** is a Series of True/False values used to filter data.
    When you write `df['type'] == 'Vel'`, you create a mask showing which rows match.

    **Two types of masks in pandas:**
    1. **Boolean masks** (True/False filters) - used with indexing like `df[mask]`
    2. **mask() function** - replaces values where condition is True

    Let's explore both!
    """)
    return


@app.cell
def _(mo):
    mo.md("""## Part 1: Boolean Masks (Filtering)""")
    return


@app.cell
def _(mo):
    mo.md("""### Example: Creating a boolean mask""")
    return


@app.cell
def _(df):
    # Create a boolean mask
    vel_mask = df['type'] == 'Vel'
    vel_mask
    return (vel_mask,)


@app.cell
def _(mo):
    mo.md("""### Example: Using the mask to filter rows""")
    return


@app.cell
def _(df, vel_mask):
    # Use the mask to select only 'Vel' rows
    df[vel_mask]
    return


@app.cell
def _(mo):
    mo.md("""### Example: Multiple boolean masks with AND (&)""")
    return


@app.cell
def _(df):
    # Create two masks and combine them
    vel_mask_2 = df['type'] == 'Vel'
    amount_mask = df['amount'] > 1

    # Both conditions must be True
    combined = df[vel_mask_2 & amount_mask]
    combined
    return


@app.cell
def _(mo):
    mo.md("""
    ### Example: Real-world use - Calculate adjusted amounts

    This uses boolean masks to separate 'Vel' and 'Hyv' types,
    then processes them differently (like your calculate_adjusted_amount function!)
    """)
    return


@app.cell
def _(df, pd):
    def calculate_adjusted_amount(group):
        # Boolean masks to separate types
        vel_mask = group['type'] == 'Vel'  # True for Vel rows
        hyv_mask = group['type'] == 'Hyv'  # True for Hyv rows

        # Initialize result with zeros
        result = pd.Series(0, index=group.index, dtype=int)

        # Sum of Hyv values (to subtract from Vel)
        hyv_total = group.loc[hyv_mask, 'amount'].sum()

        # Process Vel values - subtract hyv_total from them
        remaining = hyv_total

        for idx in group[vel_mask].index:
            vel_value = group.loc[idx, 'amount']
            subtraction = min(vel_value, remaining)
            result.loc[idx] = max(0, vel_value - subtraction)
            remaining -= subtraction

        # Hyv values become 0 (already initialized)
        return result

    # Apply to each customer-product group
    df_adjusted = df.copy()
    df_adjusted['adjusted_amount'] = df_adjusted.groupby(['cust', 'prod'], group_keys=False).apply(
        calculate_adjusted_amount)

    df_adjusted
    return


@app.cell
def _(mo):
    mo.md("""
    **How it works:**
    1. `vel_mask = group['type'] == 'Vel'` creates [True, True, False] for a group
    2. `group[vel_mask]` selects only rows where mask is True
    3. `group.loc[vel_mask, 'amount']` gets the 'amount' column for those rows
    4. We process Vel and Hyv rows separately using their masks!
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ---
    ## Part 2: The mask() Function
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    The `mask()` function replaces values where the condition is **True**.
    Think of it as: "mask out" (hide/replace) values where condition is True.

    **Syntax**: `df.mask(condition, replacement_value)`
    """)
    return


@app.cell
def _(mo):
    mo.md("### Example 1: Mask amounts greater than 2")
    return


@app.cell
def _(df):
    # Replace amounts > 2 with -1
    df.mask(df['amount'] > 2, -1)
    return


@app.cell
def _(mo):
    mo.md("### Example 2: Mask specific column only")
    return


@app.cell
def _(df):
    # Only mask the 'amount' column where it's greater than 2
    df_copy = df.copy()
    df_copy['amount'] = df_copy['amount'].mask(df_copy['amount'] > 2, 999)
    df_copy
    return


@app.cell
def _(mo):
    mo.md("### Example 3: Mask rows where type is 'Vel'")
    return


@app.cell
def _(df):
    # Replace entire rows with NaN where type is 'Vel'
    df.mask(df['type'] == 'Vel')
    return


@app.cell
def _(mo):
    mo.md("### Example 4: Mask using multiple conditions")
    return


@app.cell
def _(df):
    # Mask rows where cust is 'John' AND amount > 1
    df.mask((df['cust'] == 'John') & (df['amount'] > 1), 0)
    return


@app.cell
def _(mo):
    mo.md("### Example 5: Mask with another DataFrame (element-wise replacement)")
    return


@app.cell
def _(df, pd):
    # Create a replacement DataFrame
    replacement = pd.DataFrame({
        'cust': ['MASKED'] * 6,
        'prod': ['MASKED'] * 6,
        'amount': [0] * 6,
        'type': ['MASKED'] * 6
    })

    # Mask amounts less than 2 with values from replacement DataFrame
    df.mask(df['amount'] < 2, replacement)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Example 6: Practical use case - Mask negative adjustments

    Let's say we want to hide customer names for orders with amount >= 3 (for privacy)
    """)
    return


@app.cell
def _(df):
    df_privacy = df.copy()
    df_privacy['cust'] = df_privacy['cust'].mask(df_privacy['amount'] >= 3, '[REDACTED]')
    df_privacy
    return


@app.cell
def _(mo):
    mo.md("""
    ### Bonus: mask() vs where()

    - **mask()**: Replaces values where condition is **True**
    - **where()**: Replaces values where condition is **False**

    They are opposites of each other!
    """)
    return


@app.cell
def _(df, pd):
    # Compare mask() and where() with the same condition

    masked = df['amount'].mask(df['amount'] > 2, -1)
    where_result = df['amount'].where(df['amount'] > 2, -1)

    comparison = {
        'Original': df['amount'],
        'mask (amount > 2)': masked,
        'where (amount > 2)': where_result
    }

    pd.DataFrame(comparison)
    return


if __name__ == "__main__":
    app.run()
