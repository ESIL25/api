import streamlit as st

# 앱의 제목 설정
st.title('AI 소요기획과정')

# 메인 이미지 및 버튼 클릭 이벤트 처리
if st.button('메인 이미지'):
    st.header('메뉴 선택')
    # 메뉴 버튼 생성
    if st.button('머신러닝'):
        st.subheader('머신러닝')
        if st.button('결정트리'):
            st.write('결정트리 관련 내용 표시')
        if st.button('SVM'):
            st.write('SVM 관련 내용 표시')
        
    if st.button('딥러닝'):
        st.subheader('딥러닝')
        if st.button('CNN'):
            st.write('CNN 관련 내용 표시')
        if st.button('RNN'):
            st.write('RNN 관련 내용 표시')
        
    if st.button('실습'):
        st.subheader('실습 관련 내용 표시')

# 이 부분에 달리를 통해 생성된 이미지를 삽입할 수 있습니다.
# 예를 들어, st.image('path/to/image.png') 함수를 사용하면 됩니다.
