import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from langchain.schema import OutputParserException

# ------------------------------
# 1️⃣ LLM Setup
# ------------------------------
from dotenv import load_dotenv
import os
# --- Load API key ---
load_dotenv()  # reads .env file
api_key_gemini = os.getenv("GEMINI_KEY")
api_key_gorq = os.getenv("GORQ_KEY")

llm2 = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=api_key_gorq,
    temperature=0.6,
    max_tokens=150,
)

prompt = PromptTemplate(
    input_variables=["cuisine"],
    template=(
        "Generate a creative restaurant concept for '{cuisine}' cuisine. "
        "Return output as: RestaurantName, Slogan, MenuItem1, MenuItem2, MenuItem3.(coma separated values only). "
    ),
)

chain = LLMChain(llm=llm2, prompt=prompt)

# ------------------------------
# 2️⃣ Page Setup
# ------------------------------
st.set_page_config(page_title="AI Restaurant Creator", page_icon="🍜", layout="centered")
st.title("🍜 AI Restaurant Consltant")

# ------------------------------
# 3️⃣ Input Field
# ------------------------------
cuisine = st.text_input(
    "Enter cuisine style:",
    placeholder="e.g., Indian, Japanese, Italian"
)

# ------------------------------
# 4️⃣ Centered Button
# ------------------------------
st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
generate = st.button("Generate 🍽️")
st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------
# 5️⃣ Generate Concept
# ------------------------------
if generate:
    if not cuisine.strip():
        st.error("⚠️ Please enter a cuisine style first!")
    else:
        with st.spinner("Cooking ideas... 🍳"):
            try:
                response = chain.run(cuisine=cuisine)
                if not response or len(response.strip()) < 3:
                    raise OutputParserException("Empty or invalid response from model.")
            except Exception as e:
                st.error(f"❌ Error generating restaurant idea: {e}")
                st.stop()

        # Parse response
        try:
            parts = [x.strip() for x in response.split(",")]
            if len(parts) < 5:
                raise ValueError("Expected at least 5 comma-separated values.")

            name, slogan = parts[0], parts[1]
            menu_items = parts[2:]
        except Exception as e:
            st.warning(f"⚠️ Could not parse properly: {e}")
            st.text(response)
        else:
            st.divider()
            st.subheader("🍽️ Restaurant Concept")
            st.markdown(f"**Name:** {name}")
            st.markdown(f"**Slogan:** {slogan}")
            st.markdown("**Menu:**")
            for m in menu_items:
                st.markdown(f"- {m}")
            st.success("✅ Restaurant idea generated successfully!")
