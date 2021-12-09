import os
from google.cloud import texttospeech

"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""

# Set the appropriate environment variable
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text='Hello, World!')

# Build the voice request, select the language code ("en-US") and the ssml voice gender ("MALE")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", 
    name="en-US-Wavenet-A",
    ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open(r"C:\Users\Alex\Desktop\output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('The audio content has been written to a file.')
