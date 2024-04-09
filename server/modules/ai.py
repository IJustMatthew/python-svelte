import replicate
import os
from services.validators import get_size_by_aspect_ratio


def get_generated_images(data):
    """Generate images using the Replicate API"""

    token = data["token"]
    prompt = data["prompt"]
    negative_prompt = data["exclude"]
    resolution = get_size_by_aspect_ratio(data["ratio"])
    num_outputs = int(data["count"])
    os.environ["REPLICATE_API_TOKEN"] = token

    try:
        result_images = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={
                "prompt": prompt,
                "width": resolution[0],
                "height": resolution[1],
                "negative_prompt": negative_prompt,
                "num_outputs": num_outputs,
            },
        )

        return result_images

    except Exception:
        return (
            {"error": "Your API token is not valid or expired!"},
            401,
            {"Content-Type": "application/json"},
        )
