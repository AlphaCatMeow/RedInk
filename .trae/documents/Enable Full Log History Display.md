I will modify the log streaming logic to show the complete log history instead of truncating it.

### Backend Modification
1.  **Update `backend/routes/log_routes.py`**:
    *   Change the file reading logic to start from the beginning of the file (`start_pos = 0`).
    *   Remove the logic that calculates `file_size - 5000`.
    *   Keep the streaming behavior for new lines (`while True: ... yield ...`).
    *   This ensures that when the user connects, they receive the entire content of `backend.log` and then continue to receive new updates.

### Frontend Modification
*   No changes required in `LogViewer.vue` as it simply appends whatever data it receives. However, I should note that receiving a very large log file might impact browser performance, but since the user explicitly requested "complete display, do not truncate", I will proceed with full loading. (The frontend already has a safety limit `logs.value.slice(-2000)` which might need to be increased or removed if the user truly wants *everything*, but typically backend truncation is the main issue. I'll check if the frontend limit needs adjustment too).

**Refinement**: The user said "do not truncate", implying they want to see all logs.
*   Backend: Read from byte 0.
*   Frontend: The `LogViewer.vue` has `if (logs.value.length > 2000) { logs.value = logs.value.slice(-2000) }`. I should remove or significantly increase this limit to honor the user's request.

### Plan
1.  Modify `backend/routes/log_routes.py` to read from the beginning of the file.
2.  Modify `frontend/src/components/settings/LogViewer.vue` to increase the line limit (e.g., to 10,000 or remove it) to avoid frontend truncation.