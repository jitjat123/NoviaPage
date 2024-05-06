import streamlit as st

st.set_page_config (
  page_title = 'Te amo',
  initial_sidebar_state = 'expanded',
  page_icon="💞"  
)


st.title("Hola mi novia 💖")

st.write("""Quiero decirte que te amo profundamente, y no sabes cuanto extraño estar contigo
            que eres la unicar persona a la que amo y la unica que quiero en mi vida,
            no sabes lo feliz que me haces y lo agradecido que estoy de que seas mi novia,
            que no hay dia que no piense en ti, y se que el momento de nuestro reencuentro va
            a ser uno de los momentos mas hermosos de mi vida.""")

st.title("Un recuerdo hermoso 💏")
video_file = open('novialinda.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

st.title("¿Quieres ser mi novia?")
col1, col2 = st.columns(2)
# Establecer el ancho del botón para centrarlo

with col1:
  st.markdown(
      """
      <style>
      .stButton > button {
          display: block;
          width: 50%;
          margin: auto;
          font-size: 16px;
          background-color: #4CAF50; 
          color: white;
          padding: 12px 20px;
          text-align: center;
          border: none;
          border-radius: 4px;
          cursor: pointer;
      }
      </style>
      """,
      unsafe_allow_html=True,
  )
  if st.button("Acepto",type="secondary"):
      st.success("¡Sabía que dirías que sí! 💘 (Envíame un pantallazo de este mensaje 💌)")



with col2:
  st.markdown(
    """
    <style>
    .stButton > button {
        key="primary"
        display: block;
        width: 50%;
        margin: auto;
        font-size: 16px;
        background-color: #4CAF50;
        color: white;
        padding: 12px 20px;
        text-align: center;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
  )
  if st.button("No Acepto",type="primary"):
      st.error("Intenta de nuevo 💢")
