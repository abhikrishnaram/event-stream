from flask import Flask, Response
import time

app = Flask(__name__)

input_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
chunk_length = 50

def split_string():
    words = input_string.split()  # Split the input string into words
    result = []
    current_chunk = ""

    for word in words:
        if len(current_chunk) + len(word) + 1 <= chunk_length:
            # If adding the current word to the current chunk doesn't exceed the desired length
            if current_chunk:
                current_chunk += " "  # Add a space if the chunk is not empty
            current_chunk += word  # Add the word to the current chunk
        else:
            # If adding the current word would exceed the desired length, start a new chunk
            result.append(current_chunk)
            current_chunk = word

    if current_chunk:
        result.append(current_chunk)  # Add the last chunk if it's not empty

    result.append("end")  # Add an empty chunk to signal the end of the stream

    return result


def event_stream():
    for d in split_string():
        time.sleep(1)  # Simulate some processing time
        yield f"data: {d}\n\n"

@app.route('/api/events')
def sse():
    return Response(event_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
