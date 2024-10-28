import whisper

model = whisper.load_model("large")
result = model.transcribe("./1.m4a", language="de")
print(result["text"])