import pandas as pd
import json
import sys


def convert_csv_to_jsonl(csv_file, jsonl_file):
    try:
        # Read CSV file
        df = pd.read_csv(csv_file)

        # Verify required columns
        required_columns = ["System", "User", "Assistant"]
        if not all(col in df.columns for col in required_columns):
            missing = [col for col in required_columns if col not in df.columns]
            raise ValueError(f"Missing required columns: {', '.join(missing)}")

        # Check for empty or invalid entries
        for col in required_columns:
            if df[col].isnull().any():
                raise ValueError(f"Empty values found in column: {col}")

        # Convert to JSONL
        with open(jsonl_file, "w", encoding="utf-8") as f:
            for _, row in df.iterrows():
                messages = [
                    {"role": "system", "content": str(row["System"]).strip()},
                    {"role": "user", "content": str(row["User"]).strip()},
                    {"role": "assistant", "content": str(row["Assistant"]).strip()},
                ]
                json.dump({"messages": messages}, f, ensure_ascii=False)
                f.write("\n")

        print(f"Successfully converted {csv_file} to {jsonl_file}")
        print(f"Generated {len(df)} JSONL entries")

    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    input_csv = "data.csv"  # Replace with your CSV file path
    output_jsonl = "data.jsonl"  # Desired output JSONL file
    convert_csv_to_jsonl(input_csv, output_jsonl)
