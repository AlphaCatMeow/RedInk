I will fix the issues related to the failed image generation and truncated logs.

### Analysis
The log shows two main issues:
1.  **Image Generation Failure**: Even with `stream=False` (which was the state in the log), the API returned a message asking to enable streaming mode. The user claims to have enabled it, but the log explicitly says `stream=False`. This suggests the configuration update might not have been applied or reloaded correctly by the service instance.
2.  **Truncated Logs**: The user complains about truncated response logs. The log output shows `{'id': ... 'conte` ending abruptly. This is likely due to `str(result)[:500]` in the error logging code in `backend/generators/image_api.py`.

### Plan
1.  **Fix Configuration Reloading**:
    *   Verify how `ImageApiGenerator` gets its config. It seems it's initialized once.
    *   I need to ensure that when `backend/services/image.py` creates the generator, it fetches the *latest* config from the file/database, or that the service is reset when config changes.
    *   Looking at `backend/routes/config_routes.py`, `_clear_config_cache` calls `reset_image_service`. I need to verify `backend/services/image.py` handles this reset correctly and that the generator is re-instantiated with the new config (including `stream` parameter).

2.  **Fix Log Truncation**:
    *   Modify `backend/generators/image_api.py`.
    *   Find the error logging lines where `str(result)[:500]` is used.
    *   Increase the limit (e.g., to 5000) or remove it entirely for error logs to ensure full details are captured for debugging.

3.  **Verification of Stream Mode**:
    *   I will double-check `backend/services/image.py` to ensure it passes the `stream` flag from the config to the generator.
    *   The log shows `stream=False`, which strongly implies the `ImageApiGenerator` instance was holding onto old config.

### Implementation Steps
1.  Modify `backend/generators/image_api.py` to increase log truncation limit.
2.  Check and possibly modify `backend/services/image.py` to ensure `stream` config is correctly read and passed during generator initialization.
3.  Ensure `reset_image_service` in `backend/services/image.py` properly clears the instance so the next request creates a new one with fresh config.