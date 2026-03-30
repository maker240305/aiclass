# GEMINI.md
## Environment
* **OS:** Win 11.
* **Shell:** CMD or PowerShell (Default).
## PowerShell Syntax (Strict)
* **Operator:** **DO NOT** use `&&` or `||`. Standard PowerShell (v5.1) does not support them. 
* **Alternative:** Use `;` for sequential execution (e.g., `cmd1; cmd2`) or separate lines.
## File System
* **Path:** Use backslash (`\`).
* **Spaces:** **ALWAYS** quote paths/filenames with spaces.

## Encoding (Strict)
* **Console Setup (REQUIRED):**
1. Run `chcp 65001` to set UTF-8.
2. In PowerShell: Add `$OutputEncoding = [System.Text.Encoding]::UTF8`.
3. For Python: Set `$env:PYTHONIOENCODING='utf-8'` or use `python -X utf8`.
* **COM Objects (xlwings/pywin32):**
- **Prefer English names** for Excel sheets/ranges (e.g., 'Scan' not '[스캔]').
- Avoid brackets `[]` with Korean text in COM object names.
- Korean text is safe in cell contents/headers, not in object identifiers.
* **File Saving Logic:**
1. **IF** file is `.reg`, `.bat`, `.cmd`, `.csv`:
→ **MUST use `encoding='cp949'`**.
2. **ELSE** (All other files):
→ Use `encoding='utf-8'`.
## Error Handling
* **Retry:** If task fails, attempt to fix and retry at least 2-3 times before giving up. 
* **Self-Correction:** Analyze errors, adjust approach, and re-execute automatically.
## Task Completion
* **Interruption:** If work is interrupted mid-task, briefly inform user before stopping. 
* **Notification:** Keep user informed of task status and any breaks in workflow.
## Language & Thinking
* **Output:** Korean (한국어). * **Code/Logs:** English.