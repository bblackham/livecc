livecc
======

Quick hack of a web server for viewing compiler output for code fragments.

To install dependencies:

    pip install -r REQUIREMENTS.txt

To run:

    ./server.py

Then point your browser at http://127.0.0.1:8080/

Note: this is very insecure. Don't use this on public machines without more
thought. You probably want to run gcc and objdump in a sandbox. It was intended
for demonstration purposes only.
