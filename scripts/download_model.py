#!/usr/bin/env python3
"""
Script to download the Mistral-7B-Instruct model locally.
"""

from transformers import AutoTokenizer, AutoModelForCausalLM
import os


def download_model():
    model_dir = "./models/phi2"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    print("Downloading Phi-2...")
    tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2")
    model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2")

    tokenizer.save_pretrained(model_dir)
    model.save_pretrained(model_dir)
    print("Download complete.")


if __name__ == "__main__":
    download_model()
