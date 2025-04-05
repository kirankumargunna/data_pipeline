import pandas as pd
from process_data import process_csv


def test_process_csv():
    # Create a sample CSV for testing
    df = pd.DataFrame({"A": [1, None, 3], "B": [4, 5, 6]})
    df.to_csv("test_input.csv", index=False)
    
    # Run the function
    rows, cols = process_csv("test_input.csv", "test_output.csv")
    
    # Check results
    result_df = pd.read_csv("test_output.csv")
    assert rows == 2, "Should drop one row with NaN"
    assert cols == 2, "Should have 2 columns"
    assert len(result_df) == 2, "Output should have 2 rows"
