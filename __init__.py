from .PMSnodes import LoadBase64Audio
from .PMSnodes import PMSSendAudio


NODE_CLASS_MAPPINGS = {
    "LoadBase64Audio": LoadBase64Audio,
    "PMSSendAudio": PMSSendAudio,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadBase64Audio": "Load Audio (Base64)",
    "PMSSendAudio": "Send Audio (Websocket)",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
