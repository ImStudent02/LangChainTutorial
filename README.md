# LangChain Tutorial with Gemini and Groq Models

This tutorial demonstrates how to use LangChain with different LLM providers (Google's Gemini and Groq) to create powerful AI applications. The examples show various LangChain features from basic to advanced usage.

## Setup

1. **Install Required Packages**
   ```bash
   pip install langchain langchain-google-genai google-generativeai python-dotenv langchain-groq
   ```

2. **Environment Setup**
   Create a `.env` file in the root directory with your API keys:
   ```
   GEMINI_KEY=your_gemini_api_key_here
   GORQ_KEY=your_groq_api_key_here
   ```

## Tutorial Contents

### 1. Basic LLM Usage
- Loading API keys securely using `python-dotenv`
- Initializing Gemini and Groq models
- Simple prompt invocations
- Temperature settings for creativity control

### 2. PromptTemplates
- Creating structured prompts with variables
- Formatting prompts with different inputs
- Best practices for template design

### 3. LLMChains
- Basic LLMChain usage
- Combining prompts with models
- Processing inputs and outputs

### 4. Sequential Chains
- SimpleSequentialChain for linear workflows
- Example: Restaurant name → Menu items → Slogan
- Multi-step processing with shared context

### 5. Model Configuration
Gemini Model:
```python
llm = GoogleGenerativeAI(                  
    model="gemini-2.0-flash",  # or "gemini-1.5-pro" for free tier
    temperature=0.6  # 0 (focused) to 1 (creative)
)
```

Groq Model:
```python
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.6,
    max_tokens=50
)
```

## Example Use Cases

1. **Restaurant Business Generator**
   - Generates restaurant names based on cuisine
   - Creates menu suggestions
   - Develops catchy slogans
   ```python
   result = overall_chain.invoke({"cuisine": "Japanese"})
   ```

2. **Company Name Generator**
   - Creates business names based on products
   - One-word focused responses
   ```python
   response = chain.run("Displays for various devices")
   ```

## Best Practices

1. **API Key Security**
   - Never commit API keys to version control
   - Use `.env` files for local development
   - Consider using secret managers for production

2. **Model Selection**
   - Gemini-2.0-flash: Latest, paid version
   - Gemini-1.5-pro: Free tier
   - Groq models: Alternative provider with different capabilities

3. **Temperature Settings**
   - 0.0: Focused, consistent responses
   - 0.6: Balanced creativity
   - 1.0: Maximum creativity (may be less accurate)

4. **Chain Design**
   - Keep prompts clear and specific
   - Use appropriate chain types for your use case
   - Consider using verbose=True for debugging

## Chain Types Overview

1. **Simple LLMChain**
   - Single step processing
   - Direct input → output flow
   - Best for simple transformations

2. **SimpleSequentialChain**
   - Linear process flow
   - Output of one chain becomes input of next
   - Single input → single output

3. **SequentialChain**
   - Multiple inputs and outputs
   - Maintains named variables throughout chain
   - More complex but more flexible

## Error Handling Tips

1. Always validate API keys are loaded correctly
2. Use try-except blocks around model calls
3. Set appropriate timeout values
4. Consider implementing retry logic

## Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction.html)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Groq Documentation](https://console.groq.com/docs/introduction)

## Project Structure
```
LangChainTutorial/
│
├── .env                 # API keys (not in version control)
├── .env.example        # Template for .env
├── .gitignore         # Git ignore file
├── test1.ipynb        # Main tutorial notebook
└── README.md          # This documentation
```

## Contributing

Feel free to:
1. Fork this repository
2. Create a new branch for your features
3. Submit pull requests with improvements
4. Report issues or suggestions

## License

This tutorial is available under the MIT License. Feel free to use it for your projects."# LangChainTutorial" 
