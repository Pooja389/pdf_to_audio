import PyPDF2
from gtts import gTTS

def pdf_to_audio(pdf_path,audio_path):
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_path,"rb"))

    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()

    if text == "":
        print("no text found")
        return

    tts = gTTS(text=text,lang="en")
    tts.save(audio_path)
    print(f"audiobook saved as {audio_path}")