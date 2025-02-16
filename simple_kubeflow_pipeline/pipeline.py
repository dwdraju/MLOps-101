import kfp
from kfp import dsl
from kfp.dsl import Input, Output, Artifact

# Initialize local runner
# local.init(runner=local.DockerRunner())  # This is not needed unless running locally.

# Define the preprocess component
@dsl.component(base_image='dwdraju/mlops:kubeflow-pipeline-v12')
def preprocess_component(output_data: Output[Artifact]):
    import subprocess

    result = subprocess.run(['python', 'preprocess.py', '--output', output_data.path])

    if result.returncode != 0:
        raise RuntimeError(f"Preprocessing failed with error: {result.stderr}")

    print(f"Preprocessing completed. Output saved to {output_data.path}")

# Define the train component
@dsl.component(base_image='dwdraju/mlops:kubeflow-pipeline-v12')
def train_component(input_data: Input[Artifact], model_output: Output[Artifact]):
    import subprocess

    subprocess.run(['python', 'train.py', '--input', input_data.path, '--output', model_output.path])

# Define the evaluate component
@dsl.component(base_image='dwdraju/mlops:kubeflow-pipeline-v12')
def evaluate_component(model: Input[Artifact], metrics_output: Output[Artifact]):
    import subprocess

    subprocess.run(['python', 'evaluate.py', '--model', model.path, '--metrics', metrics_output.path])

# Define the deploy component
@dsl.component(base_image='dwdraju/mlops:kubeflow-pipeline-v12')
def deploy_component(model: Input[Artifact]):
    import subprocess

    subprocess.run(['python', 'deploy.py', '--model', model.path])

# Define the pipeline
@dsl.pipeline(
    name="HF NLP Pipeline",
    description="Pipeline for fine-tuning a Hugging Face model."
)
def hf_nlp_pipeline():
    # Preprocess step
    preprocess_task = preprocess_component()
    
    # Train step, dependent on preprocess output
    train_task = train_component(input_data=preprocess_task.outputs['output_data'])
    
    # Evaluate step, dependent on train output
    evaluate_task = evaluate_component(model=train_task.outputs['model_output'])
    
    # Deploy step, dependent on train output
    deploy_task = deploy_component(model=train_task.outputs['model_output'])

# Compile the pipeline
if __name__ == '__main__':
    kfp.compiler.Compiler().compile(hf_nlp_pipeline, 'pipeline.yaml')
