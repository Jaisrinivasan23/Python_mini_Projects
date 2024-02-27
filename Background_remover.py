import streamlit as st
from rembg import remove
from PIL import Image

def removebg(img):
    input = Image.open(img)
    return remove(input)


def home():
    st.title("Background remover")
    file_upload =st.file_uploader("Choose the photo",type=["jpeg","png","jpg"])

    if file_upload is not None:
       st.image(file_upload)
       result = removebg(file_upload)
       st.image(result)
       st.download_button(
           label="Bg",
           data=result,
           file_name="Bg.png"
       )




if __name__ == "__main__":
    home()