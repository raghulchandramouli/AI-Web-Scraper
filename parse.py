### Import necessary modules from langchain_ollama and langchain_core.prompts
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define a template string for the prompt used to instruct the model
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the Ollama language model with the desired model version (e.g., llama3)
model = OllamaLLM(model="llama3")

# Define a function to parse content using the Ollama model
def parse_with_ollama(dom_chunks, parse_description):
    # Create a prompt object from the defined template
    prompt = ChatPromptTemplate.from_template(template)
    
    # Create a chain by combining the prompt with the model
    chain = prompt | model
    
    # Initialize an empty list to store parsed results
    parsed_results = []
    
    # Iterate through each chunk of DOM content, starting the index from 1
    for i, chunk in enumerate(dom_chunks, start=1):
        
        # Invoke the model with the current chunk and the provided parse description
        response = chain.invoke(
            {
                "dom_content": chunk, 
                "parse_description": parse_description
            }
        )
        
        # Print a message indicating the progress of parsing
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        
        # Append the response to the list of parsed results
        parsed_results.append(response)
        
    # Join all the parsed results into a single string, separated by newlines
    return "\n".join(parsed_results)
