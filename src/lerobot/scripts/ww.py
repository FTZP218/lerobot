from transformers import AutoProcessor
processor = AutoProcessor.from_pretrained("/home/zhq2004/.cache/huggingface/hub/SmolVLM2-500M-Video-Instruct")
processor.save_pretrained("/home/zhq2004/.cache/huggingface/hub/SmolVLM2-500M-Video-Instruct")