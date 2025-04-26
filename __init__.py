from .PMSnodes import PMSSendImage
from .PMSnodes import LoadBase64Audio
from .PMSnodes import PMSSendAudio
from .PMSnodes import PMSLoadText
from .PMSnodes import LoadImageBase64
from .PMSnodes import LoadMaskBase64


NODE_CLASS_MAPPINGS = {
    "PMSSendImage" : PMSSendImage,
    "LoadBase64Audio": LoadBase64Audio,
    "PMSSendAudio": PMSSendAudio,
    "PMSLoadText": PMSLoadText,
    "LoadImageBase64" : LoadImageBase64,
    "LoadMaskBase64" : LoadMaskBase64,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PMSSendImage": "Send Image (Websocket)",
    "LoadImageBase64" : "Load Image (Base64)",
    "LoadMaskBase64" : "Load Mask (Base64)",
    "LoadBase64Audio": "Load Audio (Base64)",
    "PMSSendAudio": "Send Audio (Websocket)",
    "PMSLoadText": "PMS Load Text"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
