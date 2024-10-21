from kfp import local
from kfp import dsl

local.init(runner=local.SubprocessRunner())

@dsl.component
def add(a: int, b: int) -> int:
    return a + b

# run a single component
task = add(a=1, b=2)
assert task.output == 3

# or run it in a pipeline
@dsl.pipeline
def math_pipeline(x: int, y: int, z: int) -> int:
    t1 = add(a=x, b=y)
    t2 = add(a=t1.output, b=z)
    return t2.output

pipeline_task = math_pipeline(x=1, y=2, z=3)
assert pipeline_task.output == 6
