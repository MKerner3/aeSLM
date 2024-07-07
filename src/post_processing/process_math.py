from transformers import AutoTokenizer, AutoModelForCausalLM
import re

def is_math_expression(text):
    # Simple regex to detect basic math expressions
    return bool(re.search(r'\d', text) and re.search(r'[+\-*/]', text))

def evaluate_expression(expression):
    try:
        # Using eval safely with a limited scope
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception as e:
        return str(e)

def process_response(response):
    # Find all potential math expressions in the response
    math_expressions = re.findall(r'\b\d+\s*[\+\-*/]\s*\d+\b', response)
    for expr in math_expressions:
        result = evaluate_expression(expr)
        response = response.replace(expr, str(result))
    return response

# Load the language model from local GGUF file
model_id = "."  # Path to the current directory
filename = "model-unsloth.Q4_K_M.gguf"  # Your GGUF file name

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_id, gguf_file=filename)
print("Tokenizer loaded.")

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(model_id, gguf_file=filename)
print("Model loaded.")

# Get user input
user_input = input("Please enter your question or command: ")

# Generate response from the language model
inputs = tokenizer(user_input, return_tensors='pt')
outputs = model.generate(**inputs)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Store the response in a string
response_string = response

# Process the response to evaluate math expressions
final_response = process_response(response_string)

# Print the final corrected response
print(final_response)