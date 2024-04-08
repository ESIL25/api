import streamlit as st

# 세션 상태 관리를 위한 함수
def init_state():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'

# 홈 페이지
def render_home():
    st.title('AI 소요기획과정')
    if st.button('메인 이미지'):
        st.session_state['page'] = 'menu'

# 메뉴 페이지
def render_menu():
    st.header('메뉴 선택')
    if st.button('머신러닝'):
        st.session_state['page'] = 'ml'
    elif st.button('딥러닝'):
        st.session_state['page'] = 'dl'
    elif st.button('실습'):
        st.session_state['page'] = 'practice'
    elif st.button('홈으로'):
        st.session_state['page'] = 'home'

# 머신러닝 페이지
def render_ml():
    st.subheader('머신러닝')
    if st.button('결정트리'):
        st.write('결정트리 관련 내용 표시')
    elif st.button('SVM'):
        st.write('SVM 관련 내용 표시')
    elif st.button('이전 단계로'):
        st.session_state['page'] = 'menu'
    elif st.button('홈으로'):
        st.session_state['page'] = 'home'

# 딥러닝 페이지
def render_dl():
    st.subheader('딥러닝')
    if st.button('CNN'):
        st.write('CNN 관련 내용 표시')
    elif st.button('RNN'):
        st.write('RNN 관련 내용 표시')
    elif st.button('이전 단계로'):
        st.session_state['page'] = 'menu'
    elif st.button('홈으로'):
        st.session_state['page'] = 'home'

# 실습 페이지
def render_practice():
    st.subheader('실습')
    if st.button('이전 단계로'):
        st.session_state['page'] = 'menu'
    elif st.button('홈으로'):
        st.session_state['page'] = 'home'

# 앱의 메인 흐름 관리
init_state()

if st.session_state['page'] == 'home':
    render_home()
elif st.session_state['page'] == 'menu':
    render_menu()
elif st.session_state['page'] == 'ml':
    render_ml()
elif st.session_state['page'] == 'dl':
    render_dl()
elif st.session_state['page'] == 'practice':
    render_practice()
