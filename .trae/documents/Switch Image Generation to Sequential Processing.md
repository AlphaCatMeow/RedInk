I will modify `backend/services/image.py` to change the image generation from parallel (using `ThreadPoolExecutor`) to sequential processing. This will be applied to both the initial batch generation and the retry logic.

### 1. Modify `generate_images` method
*   Remove the `ThreadPoolExecutor` block.
*   Keep the logic that iterates through `other_pages`.
*   Call `_generate_single_image` sequentially for each page.
*   Update the logic to handle results and yield events one by one.
*   The high concurrency check (`if high_concurrency:`) will be effectively bypassed or modified to always run sequentially, as requested by the user to avoid service failure. I will remove the concurrency branch entirely.

### 2. Modify `retry_failed_images` method
*   Remove the `ThreadPoolExecutor` block.
*   Iterate through `pages` sequentially.
*   Call `_generate_single_image` for each page.
*   Yield events for each completion or failure.

This change ensures that requests are sent one after another, preventing overload on the backend service or external API limits.