from pydantic import BaseModel
class SWEBenchEvalResult(BaseModel):
    instance_id: str
    apply_patch_output: str
    test_output: str
    resolved: bool


                timeout = 900  # 15 minutes