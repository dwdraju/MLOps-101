import kfp
from kfp import dsl, local
from kfp.dsl import InputPath, OutputPath
from pprint import pprint


local.init(runner=local.SubprocessRunner())

# Define the preprocess component with a Docker image
@dsl.component(
    base_image='dwdraju/mlops:kubeflow-pipeline-v10'
)
def preprocess_component(output_data_path: OutputPath(str)):
    import subprocess
    import os

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_data_path), exist_ok=True)

    # Run the preprocess.py script, passing the output path
    result = subprocess.run(['python', 'preprocess.py', '--output', output_data_path])
    
    # Check if the script executed correctly
    if result.returncode != 0:
        raise RuntimeError(f"Preprocessing failed with error: {result.stderr}")
    
    print(f"Preprocessing completed. Output saved to {output_data_path}")

# Define the train component with a Docker image
@dsl.component(
    base_image='dwdraju/mlops:kubeflow-pipeline-v10'
)
def train_component(input_data_path: InputPath(str), model_output_path: OutputPath(str)):
    import subprocess
    subprocess.run(['python', 'train.py', '--input', input_data_path, '--output', model_output_path])

# Define the evaluate component with a Docker image
@dsl.component(
    base_image='dwdraju/mlops:kubeflow-pipeline-v10'
)
def evaluate_component(model_path: InputPath(str), metrics_output_path: OutputPath(str)):
    import subprocess
    subprocess.run(['python', 'evaluate.py', '--model', model_path, '--metrics', metrics_output_path])

# Define the deploy component with a Docker image
@dsl.component(
    base_image='dwdraju/mlops:kubeflow-pipeline-v10'
)
def deploy_component(model_path: InputPath(str)):
    import subprocess
    subprocess.run(['python', 'deploy.py', '--model', model_path])

# Define the pipeline
@dsl.pipeline(
    name="HF NLP Pipeline",
    description="Pipeline for fine-tuning a Hugging Face model."
)
def huggingface_pipeline():
    # Create the preprocess step
    preprocess_task = preprocess_component()
    print(preprocess_task.outputs)
    output_data_path = preprocess_task.outputs['output_data_path']
    # Create the train step that depends on the preprocess step
    train_task = train_component(
        input_data_path=output_data_path
    )

    # Create the evaluate step that depends on the train step
    evaluate_task = evaluate_component(
        model_path=train_task.output
    )
    
    # Create the deploy step that depends on the evaluate step
    deploy_task = deploy_component(
        model_path=train_task.output
    )

# Compile the pipeline
# if __name__ == '__main__':
#     kfp.compiler.Compiler().compile(pipeline, 'pipeline.yaml')

preprocess_component1 = preprocess_component()
print("here is output:",preprocess_component1)
# if __name__ == "__main__":
#     # Initialize the Kubeflow client
#     client = kfp.Client()
    
#     # Run the pipeline locally
#     # client.create_run_from_pipeline_func(
#     #     preprocess_component,
#     #     arguments={}
#     #     # mode=PipelineExecutionMode.LOCAL  # Set local mode execution
#     # )
#     client.create_run_from_pipeline_func(preprocess_component, arguments=[], experiment_name="my-experiment", run_name="test-run-1", namespace="kubeflow-user-example-com")

