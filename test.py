import assemblyai as aai
import os

# API key is set in system environment variables
aai.settings.api_key = os.environ["ASSEMBLYAI_API_KEY"]

transcriber = aai.Transcriber()

# You can use a local filepath:
# audio_file = "./example.mp3"

# Or use a publicly-accessible URL:
audio_file = "https://assembly.ai/sports_injuries.mp3"

config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.slam_1)

transcript = transcriber.transcribe(audio_file, config)

if transcript.status == aai.TranscriptStatus.error:
    print(f"Transcription failed: {transcript.error}")
    exit(1)

print(f" \nFull Transcript: \n\n{transcript.text}")
     