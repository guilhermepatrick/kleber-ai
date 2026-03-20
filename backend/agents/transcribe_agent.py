import os
import whisper

os.environ["PATH"] = r"C:\ffmpeg\bin" + os.pathsep + os.environ.get("PATH", "")

# Carrega o modelo uma vez
model = whisper.load_model("medium")

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "transcriptions")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def transcribe(file_path: str, original_filename: str = "") -> tuple[str, str]:
    """Recebe o caminho de um arquivo de audio/video e retorna a transcricao e o caminho do txt."""
    print(f"[Whisper] Iniciando transcrição: {file_path}")

    result = model.transcribe(file_path, language="pt", verbose=True)
    text = result["text"]

    base_name = os.path.splitext(os.path.basename(original_filename or file_path))[0]
    output_path = os.path.join(OUTPUT_DIR, f"{base_name}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"[Whisper] Transcrição salva em: {output_path}")
    return text, output_path
