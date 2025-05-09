import os


class PromptPalette:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": (
                    "STRING",
                    {"default": "", "multiline": True},
                )
            },
            "optional": {"prefix": ("STRING", {"forceInput": True})},
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    CATEGORY = "utils"

    def process(self, text, prefix=None):
        lines = text.split("\n")
        filtered_lines = []
        for line in lines:
            # Skip empty lines
            if not line.strip():
                continue
            # Skip commented lines
            if line.strip().startswith("//"):
                continue
            # Remove inline comments
            if "//" in line:
                line = line.split("//")[0].rstrip()
            # Add comma
            if not line.strip().endswith(","):
                line = line + ", "
            filtered_lines.append(line)
        result = "\n".join(filtered_lines)

        if prefix:
            result = prefix + "\n" + result

        return (result,)


NODE_CLASS_MAPPINGS = {"PromptPalette": PromptPalette}
NODE_DISPLAY_NAME_MAPPINGS = {"PromptPalette": "Prompt Palette"}
WEB_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), "web")
