import streamlit as st

#검색창 만들기
#입력창에서 데이터를 받아서
#st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")
photo_name = st.text_input('텍스트를 입력하세요')

if(photo_name == 'ningning01'):
    st.image("./data/ningning01.jpeg")
    st.download_button('링크 다운로드', "./data/ningning01.jpeg")
elif(photo_name == 'ningning02'):
    st.image("./data/ningning02.jpeg")
    st.download_button('링크 다운로드', "./data/ningning02.jpeg")
elif(photo_name == 'ningning03'):
    st.image("./data/ningning03.jpeg")
    st.download_button('링크 다운로드', "./data/ningning03.jpeg")


#해당 문자열이 일치하는 이미지를 화면에 출력해보세요
#st.link_button(label, url, *, help=None, type="secondary", disabled=False, use_container_width=False)