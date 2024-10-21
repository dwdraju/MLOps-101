import argparse

def deploy(model_path: str):
    with open(model_path, 'r') as f:
        model_info = f.read()
    print(f"Deploying model: {model_info}")

def main():
    parser = argparse.ArgumentParser(description="Deploy a model.")
    parser.add_argument('--model', type=str, required=True, help="Path to the model")
    args = parser.parse_args()
    deploy(args.model)

if __name__ == "__main__":
    main()
