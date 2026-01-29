from openai import OpenAI
import pathlib

# cliente OpenAI (usa la API key del sistema)
client = OpenAI()

# ruta del audio
audio_path = pathlib.Path("audio.wma")

# abrir el archivo
with open(audio_path, "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-1",
        language="es"
    )

# guardar resultado en TXT
with open("transcripcion.txt", "w", encoding="utf-8") as f:
    f.write(transcription.text)

print("✅ Transcripción lista: transcripcion.txt")
