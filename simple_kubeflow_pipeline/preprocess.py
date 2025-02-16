import argparse
from datasets import load_dataset

def preprocess(output_path: str):
    # Load a small open-source dataset from Hugging Face
    dataset = load_dataset('davidadamczyk/ag_news-100', split='train[:1%]')  # Fetch a small subset of the dataset

    # Write the dataset to the file at output_path
    with open(output_path, 'w', encoding='utf-8') as f:
        for item in dataset:
            f.write(f"{item['text']}\t{item['label']}\n")  # Format: text tab label

def main():
    parser = argparse.ArgumentParser(description="Preprocess data.")
    parser.add_argument('--output', type=str, required=True, help="Path to save the preprocessed data")  # Expect the path
    args = parser.parse_args()
    print("args is this:", args)
    # Call preprocess with the correct path
    preprocess(args.output)

if __name__ == "__main__":
    main()
