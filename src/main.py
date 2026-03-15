from abc import ABC, abstractmethod
from typing import Dict, Any, List

class PipelineStep(ABC):
    \"\"\"Abstract Base Class for MLOps Pipeline Steps.\"\"\"
    @abstractmethod
    def execute(self, config: Dict[str, Any]) -> bool:
        \"\"\"Execute the pipeline step.\"\"\"
        pass

class TrainingStep(PipelineStep):
    \"\"\"Automated Training Step implementation.\"\"\"
    def execute(self, config: Dict[str, Any]) -> bool:
        print(f"Executing Training with config: {config}")
        return True

class DeploymentStep(PipelineStep):
    \"\"\"Automated Deployment Step implementation.\"\"\"
    def execute(self, config: Dict[str, Any]) -> bool:
        print(f"Deploying model to production...")
        return True

class StepFactory:
    \"\"\"Factory Pattern for Pipeline Steps.\"\"\"
    _steps: Dict[str, type] = {
        "training": TrainingStep,
        "deployment": DeploymentStep
    }

    @staticmethod
    def get_step(step_type: str) -> PipelineStep:
        step_class = StepFactory._steps.get(step_type.lower())
        if not step_class:
            raise ValueError(f"Unknown pipeline step: {step_type}")
        return step_class()

class PipelineManager:
    \"\"\"Manager for orchestrating MLOps pipelines.\"\"\"
    def __init__(self):
        self.steps: List[PipelineStep] = []

    def add_step(self, step_type: str):
        self.steps.append(StepFactory.get_step(step_type))

    def run_pipeline(self, config: Dict[str, Any]):
        for step in self.steps:
            if not step.execute(config):
                print("Pipeline Failed at step: ", step)
                break

if __name__ == \"__main__\":
    manager = PipelineManager()
    manager.add_step("training")
    manager.add_step("deployment")
    manager.run_pipeline({"batch_size": 32, "epochs": 10})