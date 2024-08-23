# End-to-End AI Voice Assistance with RAG Pipeline | Ollama | Mistral LLM 

This repository contains code for a voice assistant that interacts with an AI model for natural language understanding (NLU). The assistant is designed to record audio input from users, transcribe it, and then interact with the AI model to provide relevant responses.

## Features

- Record audio input from users in chunks.
- Transcribe the recorded audio using a pre-trained AI model.
- Interact with the AI model to generate responses based on user input.
- Utilizes a knowledge base for context-aware responses.

## Prerequisites

Before running the code, ensure you have the following dependencies installed:

- Python above 3.8
- `pyaudio`
- `numpy`
- `faster_whisper` (Installable via pip)
- `qdrant_client` (Installable via pip)
- Other dependencies specified in `requirements.txt`

## Usage

1. Clone this repository to your local machine.

   ```bash
   git clone git@github.com:ayaansh-roy/voice_assistant_llm.git

2. Install the dependencies using pip.

   ```bash
   pip install -r requirements.txt

3. Run the main script app.py.

   ```bash
   python app.py

4. Follow the prompts to interact with the voice assistant. Speak into the microphone when prompted.


## Notes
- Ensure that your system's microphone is correctly configured and accessible by the script.
- Make sure to handle exceptions and errors gracefully, especially during audio recording and transcription processes.
