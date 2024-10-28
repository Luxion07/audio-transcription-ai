
# Project for Automatic Audio File Transcription with Whisper

This project uses Whisper to transcribe audio files. All required commands can be run through `make`.

## Installation and Setup

1. Clone the project and navigate to its directory.
2. Ensure you have Python and `pip` installed. To set up the virtual environment and dependencies, run:

   ```bash
   python3 -m venv whisper_env
   source whisper_env/bin/activate
   pip install git+https://github.com/openai/whisper.git
   ```

3. Ensure that `ffmpeg` is installed:

   ```bash
   brew install ffmpeg
   ```

## Running the Transcription

To transcribe an audio file, run:

```bash
make transcription
```

This command activates the virtual environment and runs the `transcribe.py` script for transcription.

### Changing the Audio File Path

To transcribe a different audio file, change the file path in `transcribe.py`:

```python
result = model.transcribe("path_to_your_new_file.m4a", language="de")
```

## Deactivating the Virtual Environment

After completing the transcription, you can deactivate the virtual environment with:

```bash
deactivate
```
