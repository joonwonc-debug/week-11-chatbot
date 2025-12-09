import streamlit as st
from openai import OpenAI

# 페이지 기본 설정
st.set_page_config(
    page_title="Role-based Creative Chatbot",
    page_icon="Fs",
    layout="wide"
)

# --- 사이드바 설정 (API & Role Settings) ---
[cite_start]st.sidebar.title("API & Role Settings") [cite: 3]

# 1. OpenAI API 키 입력
[cite_start]api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password", help="sk-...") [cite: 4]

# 2. 역할 선택 (순서 중요: 먼저 정의해야 합니다!)
# 원본의 'Video Director' 외에 소설가, 화가 등 프리셋 추가
role_presets = {
    [cite_start]"Video Director": """You are a professional film director. Always analyze ideas in terms of visual storytelling - use camera movement, lighting, framing, and emotional tone to explain your thoughts. Describe concepts as if you are planning a film scene.""",  [cite: 7, 8, 9]
    "Novelist": """You are a best-selling novelist. Analyze ideas based on narrative structure, character development, and sensory details. Describe concepts using metaphors and evocative prose.""",
    "Abstract Painter": """You are an abstract painter. Interpret ideas through colors, textures, brushstrokes, and composition. Focus on the feelings and abstract concepts rather than realistic depiction."""
}

# 정의된 role_presets 변수를 사용하여 선택창 생성
[cite_start]selected_role = st.sidebar.selectbox("Choose a role:", list(role_presets.keys())) [cite: 6]

# 3. 역할 프롬프트 편집 (사용자가 수정 가능)
system_prompt = st.sidebar.text_area(
    "Edit Role Description:", 
    value=role_presets[selected_role],
    height=150
)

# --- 메인 화면 설정 ---
[cite_start]st.title("🎭 Role-based Creative Chatbot") [cite: 10]
[cite_start]st.markdown("### Select a creative role and ask your question!") [cite: 11]

# 구분선
st.divider()

# 사용자 입력창
[cite_start]user_input = st.text_area("Enter your question or idea:", placeholder="e.g., How can I express sadness in movement?") [cite: 12, 13]

# 응답 생성 버튼
[cite_start]if st.button("Generate Response", type="primary"): [cite: 14]
    if not api_key:
        st.error("⚠️ Please enter your OpenAI API Key in the sidebar first.")
    elif not user_input:
        st.warning("⚠️ Please enter a question or idea.")
    else:
        try:
            # OpenAI 클라이언트 초기화
            client = OpenAI(api_key=api_key)
            
            with st.spinner(f"Asking the {selected_role}..."):
                # 채팅 완료 요청
                response = client.chat.completions.create(
                    model="gpt-4o",  # gpt-3.5-turbo 등 사용 가능
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_input}
                    ]
                )
                
                result = response.choices[0].message.content
                
            # 결과 출력
            st.subheader("💡 Director's Insight")
            st.success(result)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

# --- 푸터 (Footer) ---
st.markdown("---")
[cite_start]st.caption("Built for 'Art & Advanced Big Data' Prof. Jahwan Koo (SKKU)") [cite: 15]
