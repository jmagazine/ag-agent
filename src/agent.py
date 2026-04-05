from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
import os

MODEL_DIR = "./models/phi2"


def load_llm():
    if not os.path.exists(MODEL_DIR):
        raise FileNotFoundError(
            f"Model not found at {MODEL_DIR}. Run scripts/download_model.py first."
        )

    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        temperature=0.1,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )

    llm = HuggingFacePipeline(pipeline=pipe)
    return llm


def create_chain():
    llm = load_llm()

    with open("data/knowledge.txt", "r") as f:
        knowledge = f.read()

    prompt_template = """
You are an agricultural expert. Based on the following knowledge, recommend the best fertilizer combination for the given soil and crop.

Knowledge:
{knowledge}

Soil: pH {ph}, Nitrogen {n}, Phosphorus {p}, Potassium {k}
Crop: {crop}

Provide recommendations including fertilizer types, quantities per acre, and application instructions. Be specific and safe (avoid salt injury, follow guidelines).
"""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["knowledge", "ph", "n", "p", "k", "crop"],
    )

    chain = prompt | llm
    return chain, knowledge
