custom_css = """
    /* ============================================
       MAIN CONTAINER
       ============================================ */
    .progress-text { 
        display: none !important;
    }
    
    .gradio-container { 
        max-width: 1000px !important;
        width: 100% !important;
        margin: 0 auto !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
        background: #0f0f0f !important;
        color: #ffffff !important;
    }
    
    /* ============================================
       TABS
       ============================================ */
    button[role="tab"] {
        color: #a3a3a3 !important;
        border-bottom: 2px solid transparent !important;
        border-radius: 0 !important;
        transition: all 0.2s ease !important;
        background: transparent !important;
    }
    
    button[role="tab"]:hover {
        color: #e5e5e5 !important;
    }
    
    button[role="tab"][aria-selected="true"] {
        color: #ffffff !important;
        border-bottom: 2px solid #ffffff !important;
        border-radius: 0 !important;
        background: transparent !important;
    }
    
    .tabs {
        border-bottom: none !important;
        border-radius: 0 !important;
    }
    
    .tab-nav {
        border-bottom: 1px solid #3f3f3f !important;
        border-radius: 0 !important;
    }
    
    button[role="tab"]::before,
    button[role="tab"]::after,
    .tabs::before,
    .tabs::after,
    .tab-nav::before,
    .tab-nav::after {
        display: none !important;
        content: none !important;
        border-radius: 0 !important;
    }
    
    #doc-management-tab {
        max-width: 500px !important;
        margin: 0 auto !important;
    }
    
    /* ============================================
       BUTTONS
       ============================================ */
    button {
        border-radius: 8px !important;
        border: none !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
    }
    
    .primary {
        background: #3b82f6 !important;
        color: white !important;
    }
    
    .primary:hover {
        background: #2563eb !important;
        transform: translateY(-1px) !important;
    }
    
    .stop {
        background: #ef4444 !important;
        color: white !important;
    }
    
    .stop:hover {
        background: #dc2626 !important;
        transform: translateY(-1px) !important;
    }
    
    /* ============================================
       CHAT INPUT BOX - FIXED TEXT COLOR
       ============================================ */
    /* Chat input textarea - white text for high contrast */
    textarea[placeholder*="message"],
    textarea[placeholder*="Message"],
    textarea[data-testid*="textbox"]:not(#file-list-box textarea) {
        background: #1a1a1a !important;
        border: 1px solid #3f3f3f !important;
        border-radius: 10px !important;
        color: #ffffff !important;
        box-shadow: none !important;
        padding: 12px !important;
    }
    
    textarea[placeholder*="message"]:focus,
    textarea[placeholder*="Message"]:focus,
    textarea[data-testid*="textbox"]:focus:not(#file-list-box textarea) {
        background: #1f1f1f !important;
        border-color: #3b82f6 !important;
        color: #ffffff !important;
        outline: none !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
    }
    
    /* Input placeholder text color */
    textarea[placeholder*="message"]::placeholder,
    textarea[placeholder*="Message"]::placeholder {
        color: #9ca3af !important;
        opacity: 1 !important;
    }
    
    /* Chat input container wrapper */
    .gr-text-input:has(textarea[placeholder*="message"]),
    .gr-text-input:has(textarea[placeholder*="Message"]),
    [class*="chatbot"] + * [data-testid="textbox"],
    form:has(textarea[placeholder*="message"]) > div,
    form:has(textarea[placeholder*="Message"]) > div {
        background: transparent !important;
        border: none !important;
        gap: 12px !important;
    }
    
    /* Submit button styling */
    form:has(textarea[placeholder*="message"]) button,
    form:has(textarea[placeholder*="Message"]) button,
    [class*="chatbot"] ~ * button[type="submit"] {
        background: #3b82f6 !important;
        border: none !important;
        padding: 8px 16px !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }
    
    form:has(textarea[placeholder*="message"]) button:hover,
    form:has(textarea[placeholder*="Message"]) button:hover {
        background: #2563eb !important;
    }
    
    form:has(textarea[placeholder*="message"]) {
        gap: 12px !important;
        display: flex !important;
    }
    
    /* ============================================
       MARKDOWN TEXT - BRIGHT COLORS
       ============================================ */
    /* Markdown text color - improved contrast */
    .markdown,
    .markdown *,
    [class*="markdown"] *,
    .prose,
    .prose * {
        color: #e5e5e5 !important;
    }
    
    /* Markdown headings */
    .markdown h1,
    .markdown h2,
    .markdown h3,
    .markdown h4,
    .markdown h5,
    .markdown h6,
    [class*="markdown"] h1,
    [class*="markdown"] h2,
    [class*="markdown"] h3 {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    /* Markdown paragraphs and lists */
    .markdown p,
    .markdown li,
    .markdown ul,
    .markdown ol {
        color: #e5e5e5 !important;
    }
    
    /* Markdown emphasized text */
    .markdown strong,
    .markdown b {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    /* ============================================
       FILE UPLOAD
       ============================================ */
    .file-preview, 
    [data-testid="file-upload"] {
        background: #1a1a1a !important;
        border: 1px solid #3f3f3f !important;
        border-radius: 5px !important;
        color: #ffffff !important;
        min-height: 200px !important;
    }
    
    .file-preview:hover, 
    [data-testid="file-upload"]:hover {
        border-color: #3b82f6 !important;
        background: #1f1f1f !important;
    }
    
    .file-preview *,
    [data-testid="file-upload"] * {
        color: #ffffff !important;
    }
    
    .file-preview .label,
    [data-testid="file-upload"] .label {
        display: none !important;
    }
    
    /* ============================================
       INPUTS & TEXTAREAS
       ============================================ */
    input, 
    textarea {
        background: #1a1a1a !important;
        border: 1px solid #3f3f3f !important;
        border-radius: 10px !important;
        color: #ffffff !important;
        transition: border-color 0.2s ease !important;
    }
    
    input:focus, 
    textarea:focus {
        border-color: #3b82f6 !important;
        outline: none !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
        color: #ffffff !important;
    }
    
    /* Input placeholder text */
    input::placeholder,
    textarea::placeholder {
        color: #9ca3af !important;
        opacity: 1 !important;
    }
    
    textarea[readonly] {
        background: #1a1a1a !important;
        color: #e5e5e5 !important;
    }
    
    /* ============================================
       FILE LIST BOX
       ============================================ */
    #file-list-box {
        background: #1a1a1a !important;
        border: 1px solid #3f3f3f !important;
        border-radius: 5px !important;
        padding: 10px !important;
    }
    
    #file-list-box textarea {
        background: transparent !important;
        border: none !important;
        color: #e5e5e5 !important;
        padding: 0 !important;
    }
    
    /* ============================================
       CHATBOT
       ============================================ */
    .chatbot {
        border-radius: 5px !important;
        background: #1a1a1a !important;
        border: none !important;
    }
    
    .message {
        border-radius: 10px !important;
        width: fit-content !important;
    }
    
    .message.user {
        background: #3b82f6 !important;
        color: white !important;
    }
    
    .message.bot {
        background: #1f1f1f !important;
        color: #e5e5e5 !important;
        border: 1px solid #3f3f3f !important;
    }
    
    /* ============================================
       PROGRESS BAR
       ============================================ */
    .progress-bar-wrap {
        border-radius: 10px !important;
        overflow: hidden !important;
        background: #1a1a1a !important;
    }

    .progress-bar {
        border-radius: 10px !important;
        background: #3b82f6 !important;
    }
    
    /* ============================================
       TYPOGRAPHY - GLOBAL TEXT COLOR
       ============================================ */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    p, span, div, label {
        color: #e5e5e5 !important;
    }
    
    /* Ensure all text has sufficient contrast */
    body, .gradio-container {
        color: #e5e5e5 !important;
    }
    
    /* ============================================
       GLOBAL OVERRIDES
       ============================================ */
    * {
        box-shadow: none !important;
    }
    
    footer {
        visibility: hidden;
    }
"""