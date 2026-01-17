I will implement a real-time log viewer in the frontend.

### Backend Implementation
1.  **Create `backend/routes/log_routes.py`**:
    *   Implement a `GET /api/logs/stream` endpoint.
    *   This endpoint will use Flask's `Response` with a generator function.
    *   The generator will continuously read new lines from `logs/backend.log` (tailing) and yield them as Server-Sent Events (SSE) data (e.g., `data: <log_line>\n\n`).
    *   It will handle the case where the file doesn't exist yet.
2.  **Register Route**:
    *   Update `backend/routes/__init__.py` to register the new `log_routes` blueprint.

### Frontend Implementation
1.  **Create `frontend/src/components/settings/LogViewer.vue`**:
    *   A component that displays logs in a scrollable terminal-like window (black background, monospace font).
    *   Use `EventSource` to connect to `/api/logs/stream`.
    *   Append new messages to a list and render them.
    *   Features: "Clear Logs" button, "Auto-scroll" toggle.
2.  **Update `frontend/src/views/SettingsView.vue`**:
    *   Add a new section "System Logs" below the existing configuration cards.
    *   Include the `LogViewer` component in this section.

### Verification
*   I will verify by writing a simple test script or manually triggering some actions (like reloading config) and checking if logs appear in the new viewer. (Since I cannot open a browser, I will rely on code correctness and successful file writes).

This approach provides a robust, real-time view of the backend logs directly in the Settings page.