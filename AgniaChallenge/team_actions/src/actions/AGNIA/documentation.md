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

## ask_agnia

Description: 
Calls to AGNIA for text generation

Parameters:
- prompt(str): A user-written prompt for AGNIA neural network. 

Returns:
A LLMResponse object
