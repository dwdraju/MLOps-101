import argparse

def train(input_path: str, output_path: str):
    with open(input_path, 'r', encoding='utf-8') as f:
        data = f.read()
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"model trained with {data}")

def main():
    parser = argparse.ArgumentParser(description="Train a model.")
    parser.add_argument('--input', type=str, required=True, help="Path to input data")
    parser.add_argument('--output', type=str, required=True, help="Path to save the model")
    args = parser.parse_args()
    train(args.input, args.output)

if __name__ == "__main__":
    main()
