import streamlit as st
import textwrap

st.set_page_config(page_title="Smartband Notes Splitter", layout="centered")

st.title("📚 Smartband Notes Splitter")
st.markdown("""
## 📤 Send Notes to Smartband

This tool helps you send cleaned-up notes to someone wearing a smartband 📲.  
No mobile interaction needed — just push, and it's delivered.

---

### 👤 **Instructions for the Sender**
- Paste the answers here.
- Enter a short label for the task (e.g., `Q1`, `A1`).
- The app splits the text into 130-character chunks.
- Each chunk appears in a copyable code box with auto-numbering like `[t1/1]`, `[t1/2]`, etc.
- Send these chunks to your friend in the exam hall — they’ll get push notifications directly.
- Refresh the page to start over.
            
✅ **Smartband-friendly** | ⚡ **Quick delivery** | 🔕 **Silent, no tapping needed**

---

### 📝 **Message Formatting Guide**
- `#` → for headings
- `##` → for subheadings
- `###` → for sub-subheadings
- `*` → for bullet points
- `[s1/1]` → for section ID  
- `<br>` → for line break  
- `<hr>` → for horizontal rule  
- `^` → for powers (e.g., 3^2 = 9)  
- `/` → for division (e.g., 6/3 = 2)

---

### 🔢 **Chunk Order Tips**
Use a format like `[1/10]`, `[2/10]` at the start of each chunk to keep the order clear.
""")


abbr = st.text_input("Enter task abbreviation (e.g., Q1, A1):")
text_input = st.text_area("Paste your cleaned text here:", height=300)

if st.button("Split Text"):
    if not abbr.strip():
        st.warning("Please enter a task abbreviation.")
    elif text_input.strip() == "":
        st.warning("Please paste some text first.")
    else:
        chunks = textwrap.wrap(text_input, width=130)
        st.success(f"Split into {len(chunks)} chunk(s):")
        for i, chunk in enumerate(chunks, 1):
            st.code(f"[{abbr}/{i}] {chunk}", language='text')
