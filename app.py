import streamlit as st
from sommelier import search_wine, recommend_wine, describe_flavor
st.title("sommelier AI")


col1, col2 = st.column([3,1])

with col1:
uploaded_image = st.file_uploader("요리 이미지를 업로드하세요.",)
user_prompt = st.text_input("프롬프트를 입력하세요.", "이 요리에 어울리는 와인을 추천해주세요.")

with col2:
    if uploaded_image:
       st.image(uploadeded_iage, caption="업로드된 요리 이미지 ", use_container_width=true)


with col1:
   if st.button("추천하기"):
       if not uploaded_image:
          st.warning("이미지를 업로드해주세요.")
       else:
         with st.spinner("1단계: 요리의 맛과 향을 분석하는 중 ...")
              dish_flaver = describe_dish_flavor(uploaded_image.read(),"이 요리의 이름과 맛과 향과 같은 특징을 한 문장으로 설명해줘.")
              st.markdown(f"### 요리의 맘ㅅ과 향 분석 결과과")
              st.info(dish_flavor)

         with st.spinner("2단계: 요리에 어울리는 와인 리뷰를 검색하는 중중 ...")
              wine_search_result = search_wine()
         with st.spinner("3단계: AI 소믈리에가 와인 페어링에 대한 추전글을 생성하는 중중 ...")
              pass

         st.success("추천이 완료되었습니다!")

