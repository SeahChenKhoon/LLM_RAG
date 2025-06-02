from dotenv import load_dotenv
import os

class cls_Env:
    def __init__(self) -> None:
        load_dotenv(override=True)

        self.yaml_config_path = os.getenv("YAML_CONFIG_PATH", "")
        self.open_api_key = os.getenv("OPENAI_API_KEY", "")
        self.openai_model_name = os.getenv("OPENAI_MODEL_NAME", "")
        self.llm_temperature = os.getenv("LLM_TEMPERATURE", "")
        
