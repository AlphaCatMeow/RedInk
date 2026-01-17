import time
import os
import logging
from flask import Blueprint, Response, stream_with_context
from pathlib import Path

logger = logging.getLogger(__name__)

def create_log_blueprint():
    bp = Blueprint('logs', __name__)

    @bp.route('/logs/stream')
    def stream_logs():
        """
        Stream logs via Server-Sent Events (SSE)
        Reads from logs/backend.log
        """
        def generate():
            log_file = Path(__file__).parent.parent.parent / 'logs' / 'backend.log'
            
            # Ensure file exists
            if not log_file.exists():
                yield "data: Waiting for logs...\n\n"
                time.sleep(1)

            try:
                # Open file and read from the beginning
                with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                    # Start from the beginning of the file
                    # We do NOT seek to the end anymore
                    
                    while True:
                        line = f.readline()
                        if line:
                            # Send line as SSE data
                            yield f"data: {line.rstrip()}\n\n"
                        else:
                            # Wait for new data
                            time.sleep(0.5)
            except GeneratorExit:
                logger.info("Log stream client disconnected")
            except Exception as e:
                yield f"data: Error reading logs: {str(e)}\n\n"

        return Response(stream_with_context(generate()), mimetype='text/event-stream')

    return bp
