# 数据模型相关代码
from pydantic import BaseModel
from typing import Optional

class GenerateRequest(BaseModel):
    product_name: str
    product_features: str
    target_audience: Optional[str] = ""
    use_scenarios: Optional[str] = ""
    tone: Optional[str] = ""
    style: Optional[str] = ""
    platform: str = "通用"
    output_format: Optional[str] = "text"
    lang: Optional[str] = "zh"
    model: Optional[str] = None
