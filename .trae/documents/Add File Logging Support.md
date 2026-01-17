I will implement a persistent file logging system to allow you to easily view runtime logs.

1.  **Modify `backend/app.py`**:
    *   Update the `setup_logging` function.
    *   Add a `RotatingFileHandler` to save logs to a file.
    *   Logs will be saved to the `logs/backend.log` file in the project root.
    *   Configure log rotation (max 10MB per file, keep 5 backup files) to manage disk space.
    *   Ensure the `logs` directory is automatically created if it doesn't exist.

After this change, you will be able to view the full runtime logs by opening `logs/backend.log`.