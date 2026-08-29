import pyttsx3
import PyPDF2

# Open the PDF file
file = open("Week 7 Word Embeddings.pdf", mode="rb")
pdf_reader = PyPDF2.PdfReader(file)
pages = len(pdf_reader.pages)
print(f"Total pages: {pages}")

# Initialize TTS engine
melo = pyttsx3.init()

# Create or open a text file to write the content
with open("spoken_text.txt", "w", encoding="utf-8") as output_file:
    for i in range(pages):
        page = pdf_reader.pages[i]
        text = page.extract_text()

        if text:  # Only if there's text on the page
            print(f"\n--- Speaking & Writing Page {i + 1} ---\n")
            melo.say(text)
            melo.runAndWait()
            output_file.write(f"\n--- Page {i + 1} ---\n")
            output_file.write(text + "\n")
        else:
            print(f"Page {i + 1} is empty or has no extractable text.")
            output_file.write(f"\n--- Page {i + 1}: No extractable text ---\n")
