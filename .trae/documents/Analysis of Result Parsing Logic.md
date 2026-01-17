I will provide a detailed line-by-line explanation of the return result parsing logic in `backend/services/content.py` and `backend/services/outline.py`.

### 1. Content Parsing Logic (`backend/services/content.py`)
I will analyze the `_parse_json_response` function, which employs a three-stage strategy to robustly extract JSON data from AI responses:
- **Direct Parsing**: Attempting to parse the entire string as JSON.
- **Regex Extraction**: Looking for JSON inside Markdown code blocks (```json ... ```).
- **Brute-force Extraction**: Locating the first `{` and last `}`.

I will also explain how `generate_content` uses this parser and performs data validation (ensuring `titles` and `tags` are lists).

### 2. Outline Parsing Logic (`backend/services/outline.py`)
I will analyze the `_parse_outline` function, which processes the text-based outline format:
- **Splitting**: Using `<page>` (or the legacy `---`) to separate pages.
- **Type Extraction**: Using regex `\[(\S+)\]` to identify page types (e.g., [封面], [内容]) and mapping them to internal keys (`cover`, `content`, `summary`).
- **Structure Building**: Constructing a list of page dictionaries.

### 3. Summary
I will summarize how these two parsing strategies work together to handle the variability of AI model outputs.