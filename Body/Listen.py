import subprocess
import sys
import os
import json
import pyaudio
from datetime import datetime, timedelta
from vosk import Model, KaldiRecognizer

SAMPLE_RATE = 16000
CHUNK_SIZE = 4000


class Transcriber():
    def __init__(self, model_path):
        self.model = Model(model_path)

    def fmt(self, data):
        data = json.loads(data)

        start = min(r["start"] for r in data.get("result", [{"start": 0}]))
        end = max(r["end"] for r in data.get("result", [{"end": 0}]))

        return {
            "start": str(timedelta(seconds=start)),
            "end": str(timedelta(seconds=end)),
            "text": data["text"]
        }

    def transcribe(self, duration=10):
        rec = KaldiRecognizer(self.model, SAMPLE_RATE)
        rec.SetWords(True)

        transcription = []

        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=SAMPLE_RATE,
                            input=True,
                            frames_per_buffer=CHUNK_SIZE)

        print("Recording...")

        start_time = datetime.now()
        while (datetime.now() - start_time).total_seconds() < duration:
            data = stream.read(CHUNK_SIZE)
            if rec.AcceptWaveform(data):
                transcription.append(self.fmt(rec.Result()))

        stream.stop_stream()
        stream.close()
        audio.terminate()

        end_time = datetime.now()
        time_elapsed = end_time - start_time
        print(f"Time elapsed: {time_elapsed}")

        return {
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "elapsed_time": time_elapsed,
            "transcription": transcription,
        }
    
    def transcribe_from_file(self, filename):
        rec = KaldiRecognizer(self.model, SAMPLE_RATE)
        rec.SetWords(True)

        if not os.path.exists(filename):
            raise FileNotFoundError(filename)

        transcription = []

        with open(filename, "rb") as f:
            while True:
                data = f.read(CHUNK_SIZE)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    transcription.append(self.fmt(rec.Result()))

        transcription.append(self.fmt(rec.FinalResult()))

        return {
            "transcription": transcription,
        }



if __name__ == "__main__":
    model_path = "./Brain/vosk-model-small-hi-0.22"
    transcriber = Transcriber(model_path)
    duration = 10  # Set the duration of recording in seconds
    result = transcriber.transcribe(duration)
    print(result)
