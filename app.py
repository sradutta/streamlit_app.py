import streamlit as st

st.title("Dr.Dutta's Statistics Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "ai", "text": "Hi! I'm Dr. Dutta's AI Statistics Assistant. Ask me anything."}
    ]

def get_ttest_explanation():
    return """
### Two-Sample t-Test (Step-by-Step)

**Step 1: Goal**
Compare two groups to see if their means are truly different.

**Step 2: Hypotheses**
- H0: μ1 = μ2
- H1: μ1 ≠ μ2

**Step 3: Key Idea**
Signal vs Noise:
- Signal = difference in means
- Noise = variability

**Step 4: Formula**
t = (x̄1 - x̄2) / sqrt(s1²/n1 + s2²/n2)

**Step 5: Example**
Mean1 = 701.3, s1 = 10, n1 = 30  
Mean2 = 703.1, s2 = 12, n2 = 30  

Difference = -1.8  
Standard Error ≈ 2.85  

t ≈ -0.63

**Step 6: Interpretation**
Small t → not significant

**Step 7: Decision**
If p ≤ 0.05 → Reject H0  
If p > 0.05 → Do not reject H0

**Final Insight**
Difference must be large relative to variability.
"""

user_input = st.text_input("Ask something:")

if st.button("Send"):
    if user_input:
        st.session_state.messages.append({"role": "user", "text": user_input})

        lower = user_input.lower()

        if "t-test" in lower or "t test" in lower:
            response = get_ttest_explanation()
        elif "answer" in lower:
            response = "I can’t give direct answers, but I can guide you step by step."
        else:
            response = "Ask me about t-tests and I’ll explain step by step."

        st.session_state.messages.append({"role": "ai", "text": response})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"**You:** {msg['text']}")
    else:
        st.write(f"**AI:** {msg['text']}")