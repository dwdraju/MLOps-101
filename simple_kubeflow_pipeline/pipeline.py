import kfp
from kfp import dsl, local, compiler
from kfp.dsl import InputPath, OutputPath, Input, Output, Artifact
from pprint import pprint


local.init(runner=local.DockerRunner())

# Define the preprocess component with a Docker image
@dsl.component(
    base_image='dwdraju/mlops:kubeflow-pipeline-v12'
)
def preprocess_component(output_data: Output[Artifact]):
    import subprocess
    import os
    output_data_path = output_data.path
    # Ensure the output directory exists
    # os.makedirs(os.path.dirname(output_data_path), exist_ok=True)

    # Run the preprocess.py script, passing the output path
    result = subprocess.run(['python', 'preprocess.py', '--output', output_data_path])
    
    # Check if the script executed correctly
    if result.returncode != 0:
        raise RuntimeError(f"Preprocessing failed with error: {result.stderr}")
    
    print(f"Preprocessing completed. Output saved to {output_data_path}")

# Define the train component with a Docker image
@dsl.component(
    base_image='dwdraju/mlops:kubeflow-pipeline-v12'
)
def train_component(input_data_path: Input[Artifact], model_output: Output[Artifact]):
    input_data_path=input_data_path.path
    model_output_path = model_output.path
    import subprocess
    subprocess.run(['python', 'train.py', '--input', input_data_path, '--output', model_output_path])

# Define the evaluate component with a Docker image
@dsl.component(
    base_image='dwdraju/mlops:kubeflow-pipeline-v12'
)
def evaluate_component(model_path: Input[Artifact], metrics_output: Output[Artifact]):
    import subprocess
    model_path = model_path.path
    metrics_output_path = metrics_output.path
    subprocess.run(['python', 'evaluate.py', '--model', model_path, '--metrics', metrics_output_path])

# Define the deploy component with a Docker image
@dsl.component(
    base_image='dwdraju/mlops:kubeflow-pipeline-v12'
)
def deploy_component(model_path: Input[Artifact]):
    import subprocess
    model_path=model_path.path
    subprocess.run(['python', 'deploy.py', '--model', model_path])

# # Define the pipeline
# @dsl.pipeline(
#     name="HF NLP Pipeline",
#     description="Pipeline for fine-tuning a Hugging Face model."
# )
# def pipeline():
#     # Create the preprocess step
#     preprocess_task = preprocess_component()
#         # Create the train step that depends on the preprocess step
#     print("abccc: ", preprocess_task.outputs['output_data'])
#     sdfsfsa = preprocess_task.outputs['output_data']
#     train_task = train_component(
#         input_data_path = sdfsfsa
#     )
#     # sdfsa=str(train_task.outputs['model_output'])
#     evaluate_task = evaluate_component(
#         model_path=(train_task.outputs['model_output'])
#     )

#     deploy_task = deploy_component(
#         model_path=(train_task.outputs['model_output'])
#     )

# # Compile the pipeline
# if __name__ == '__main__':
#     kfp.compiler.Compiler().compile(pipeline, 'pipeline.yaml')

preprocess_task = preprocess_component()
#     # Create the train step that depends on the preprocess step
# train_task = train_component(
#     input_data_path = (preprocess_task.outputs['output_data'].uri)
# )
# evaluate_task = evaluate_component(
#     model_path=train_task.outputs['model_output'].uri
# )

# deploy_task = deploy_component(
#     model_path=train_task.outputs['model_output'].uri
# )
# preprocess_component1 = preprocess_component()
# print("here is output:",preprocess_component1.outputs['output_data'].uri)
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

