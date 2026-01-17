I will implement support for streaming image generation requests, as required by the log message.

### Backend Implementation
1.  **Modify `backend/generators/image_api.py`**:
    *   Update `_generate_via_chat_api` method.
    *   Add a check for a `stream` configuration parameter.
    *   If `stream` is enabled, set `stream=True` in the API request payload.
    *   Implement handling for the streaming response to extract the full content. The current implementation expects a single JSON response, but streaming responses come in chunks (Server-Sent Events).
    *   I need to accumulate the chunks to form the complete response message, then parse it as before.

### Frontend Implementation
1.  **Modify `frontend/src/composables/useProviderForm.ts`**:
    *   Update `ImageProviderForm` interface to include a `stream` boolean field.
    *   Update `createEmptyImageForm` to initialize `stream: false`.
    *   Update `openEditImageModal` to load the `stream` value from the provider config.
    *   Update `saveImageProvider` to save the `stream` value.
2.  **Modify `frontend/src/components/settings/ImageProviderModal.vue`**:
    *   Add a toggle switch for "流式模式 (Stream Mode)" in the form.
    *   Add a help text explaining that some providers (like the one in the log) require this mode.

### Plan
1.  Update frontend composable (`useProviderForm.ts`) to manage the `stream` field.
2.  Update frontend component (`ImageProviderModal.vue`) to add the UI toggle.
3.  Update backend generator (`image_api.py`) to handle `stream=True` in requests and process streaming responses.