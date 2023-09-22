# Event Stream
This guide will explain what an event stream is and provide step-by-step instructions on how to run a Flask backend application in the `./backend` directory and a Next.js frontend application in the `./frontend` directory.

## What is an Event Stream?

An event stream, often referred to as a data stream or event-driven architecture, is a mechanism for transmitting a continuous flow of data from a server to a client in real-time. This is commonly used in web applications to enable features such as real-time updates, notifications, and chat applications.

## Setting up the Flask Backend

1. Ensure you have Python installed on your system.

2. Navigate to the `./backend` directory in your terminal.

3. Create a virtual environment (optional but recommended):
   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
4. Install Flask and any other necessary dependencies:
   ```shell
   pip install flask
   ```
5. Run python file
   ```shell
   python main.py
   ```

Your Flask backend should now be running on http://localhost:8000.

## Setting up the Next.js Frontend

Ensure you have Node.js and npm (Node Package Manager) installed on your system.

1. Navigate to the `./frontend` directory in your terminal.

2. Start the development server:
   ```shell
   npm run dev
   ```

Your Next.js frontend should now be running on http://localhost:3000.

## Connecting the Frontend to the Backend

To connect your Next.js frontend to the Flask backend and utilize an event stream, we are using Server-Sent Events (SSE) technology.

*Remember to handle CORS (Cross-Origin Resource Sharing)*

That's it! You now have a Flask backend and a Next.js frontend running concurrently, implementing a basic SSE.



https://github.com/abhikrishnaram/event-stream/assets/66553902/9376b7f3-0d7e-4f49-85fd-76054892b98f

