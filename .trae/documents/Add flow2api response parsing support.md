I will modify `backend/generators/image_api.py` to support the specific JSON response format from the flow2api program.

The changes will be made in the `_generate_via_images_api` method:
1.  Insert a new parsing logic block after getting the JSON response (`result = response.json()`).
2.  Check for the existence of the `media` key in the response.
3.  Traverse the nested structure: `media[0] -> image -> generatedImage -> fifeUrl`.
4.  Extract the `fifeUrl` value.
5.  Clean the URL by removing the surrounding backticks and whitespace (as seen in the user's example).
6.  Call the existing `_download_image` method to download and return the image data.

This modification will run alongside the existing OpenAI-compatible parsing logic (`data` -> `b64_json`), ensuring backward compatibility while adding support for the new format.