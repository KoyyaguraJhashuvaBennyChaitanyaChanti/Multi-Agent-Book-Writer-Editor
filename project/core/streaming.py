def stream_markdown(text):
    for line in text.split("\n"):
        yield line + "\n"
