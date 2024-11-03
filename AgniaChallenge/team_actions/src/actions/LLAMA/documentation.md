# TypeHints Definition

# Models definition

class LLMRequest(BaseModel):
    team_id: str
    prompt: str
    max_tokens: Optional[int] = 20
    temperature: Optional[float] = 0.73
    length_penalty: Optional[int] = -45

class LLMResponse(BaseModel):
    output: str


# API Calls Documentation

## ask_lama

Description: 
Answer generation by given prompt with LLAMA

Parameters:
- prompt(str): A user-written prompt for LLAMA. 
- temperature(Optional[float]): A temperature for text generation
- max_tokens(Optional[int]): Max tokens 
- length_penalty(Optional[int]): Penalty for longer sequences

Returns:
A LLMResponse object
