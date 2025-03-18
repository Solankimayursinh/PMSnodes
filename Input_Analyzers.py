import base64
import json
import mimetypes
import io
import torchaudio
import torch

class InputAnalyzer:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"input_data": ("STRING", {"multiline": True})}}
    
    CATEGORY = "PMSnodes"
    RETURN_TYPES = ("STRING", )
    FUNCTION = "analyze"
    
    def analyze(self, input_data):
        result = {"type": "unknown", "format": "unknown"}

        if isinstance(input_data, str):
            if input_data.strip().startswith("{") and input_data.strip().endswith("}"):
                try:
                    json.loads(input_data)
                    result["type"] = "JSON"
                except json.JSONDecodeError:
                    result["type"] = "Text"
            elif input_data.strip().startswith("data:"):
                result["type"] = "Base64"
                try:
                    metadata, encoded = input_data.split(",", 1)
                    mime_type = metadata.split(";")[0][5:]
                    result["format"] = mime_type
                except Exception:
                    result["format"] = "Invalid Base64"
            else:
                result["type"] = "Text"
        elif isinstance(input_data, bytes):
            result["type"] = "Binary"
        elif isinstance(input_data, dict):
            result["type"] = "JSON"
        elif isinstance(input_data, list):
            result["type"] = "List"
        
        if result["type"] == "Base64":
            try:
                decoded_data = base64.b64decode(encoded)
                mime_type = mimetypes.guess_type("dummy." + result["format"].split("/")[-1])[0]
                if mime_type:
                    result["format"] = mime_type
            except Exception:
                result["format"] = "Invalid Base64"
        
        return (json.dumps(result, indent=4), )

NODE_CLASS_MAPPINGS = {
    "InputAnalyzer": InputAnalyzer,
}
