import shap
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the HuggingFace language model and tokenizer
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define a baseline for the DeepExplainer
baseline = tokenizer.encode("This is a baseline text.", return_tensors="pt")

# Create the DeepExplainer
explainer = shap.DeepExplainer(model, baseline)

# Define the input text to explain
input_text = "This is an example text to analyze."
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Calculate SHAP values
shap_values = explainer.shap_values(input_ids)

# Convert SHAP values to a DataFrame for visualization
shap_df = shap.force_plot(
    shap_values.base_values, shap_values.data,
    link="logit", tokenized_input=tokenizer.convert_ids_to_tokens(input_ids[0]),
    text_disambiguating=" "
)

# Visualize the SHAP values
shap_df.force_plot(
    shap_force_plot=True,
    figsize=(10, 6),
    matplotlib=True,
    show=True,
)
