import pandas as pd


def process_csv(input_file, output_file):
    """Read a CSV, clean it, and save the result."""
    df = pd.read_csv(input_file)
    df.dropna(inplace=True)  # Simple cleaning: drop missing values
    df.to_csv(output_file, index=False)
    return df.shape


if __name__ == "__main__":
    input_path = "input.csv"
    output_path = "output.csv"
    rows, cols = process_csv(input_path, output_path)
    print(f"Processed {rows} rows and {cols} columns.")
