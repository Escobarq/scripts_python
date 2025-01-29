from pydub import AudioSegment
import speech_recognition as sr

# Cargar el archivo MP3 y convertirlo a WAV
audio = AudioSegment.from_mp3("ruta/al/archivo.mp3")
audio.export("audio.wav", format="wav")

# Cargar el archivo de audio
recognizer = sr.Recognizer()
audio_file = "audio.wav"  # Usa el MP3 directamente si funciona

with sr.AudioFile(audio_file) as source:
    recognizer.adjust_for_ambient_noise(source)  # Reducir ruido
    audio_data = recognizer.record(source)  # Leer todo el audio

# Intentar transcribir en español
try:
    transcription = recognizer.recognize_google(audio_data, language="es-ES")
    print("Transcripción:", transcription)
except sr.UnknownValueError:
    print("No se pudo entender el audio.")
except sr.RequestError:
    print("Error en la conexión con el servicio de reconocimiento.")
