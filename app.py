import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import pyperclip

aboutME = "Hi there! My name is Josuan and I am the sole creator of this website, I created this website as a personal project and for practice, and I hope you find it useful and enjoyable to use. Thank you for visiting."

st.set_page_config(page_title="Code Wan",
                   initial_sidebar_state='auto')

settingsList = ["Webite settings","Extras"]
optionList = ["Code","Add/Remove"]
selectBoxList = ["Add Code","Remove Code"]

# Load the data from the file system if it exists, otherwise initialize an empty dictionary
try:
    with open("data.pkl", "rb") as f:
        data = pickle.load(f)
except FileNotFoundError:
    data = {}

def extraSection(password):
     if st.button("Open"):
        if password == "josuan":
            st.audio("http://drive.google.com/uc?export=view&id=1JJLFbeWLwomebiyUihNjlFJ5JrQYHgzU",format="audio/mp3")
        elif password == "kylle" or password == "ethel":
            st.write("---")
            st.image("http://drive.google.com/uc?export=view&id=1J0ixZXOKxKvqSm5bKww1LZx4ImHhHq9z")
            st.image("http://drive.google.com/uc?export=view&id=1JSxzaH-CYDrnm-x9DxftA2LPu6XroHUI")
            st.write("---")
        elif password == "emarie" or password == "cristy":
            st.write("---")
            st.image("http://drive.google.com/uc?export=view&id=1JbcsbbkNy4GiI4riVD78hYpQZBBIc607")
            st.image("http://drive.google.com/uc?export=view&id=1JYBfys0beZQ3GlSm_nwdkhDxUcFZnUc2")
            st.write("---")
        else:
            st.error("Wrong password!")

def star_rating(title, min_value=1,max_value=5,step=1):
    st.write(title)
    rating = st.slider("",min_value=min_value,max_value=max_value,step=step)
    stars = ""
    if st.button("Submit"):
        for i in range(1, max_value+1):
            if i <= rating:
                stars += "★"
            else:
                stars += "☆"
        if rating >= 3:
            st.success(f"Thank you so much! {stars}")
        else:
            st.info(f"Thank you! {stars}")
    return rating
showAuthor = None
showDescripton = None
with st.sidebar:
    selectedInfo = option_menu(
        menu_title=None,
        options=["About","Settings","Rate us"],
        default_index=0,
        icons=["info-square","gear","star-half"],
        styles={"nav-link-selected": {"background-color": "#8D72E1"}}
    )
    if selectedInfo == "About":
        st.markdown(f'''<p id="copyright">{aboutME}</p>''',
                unsafe_allow_html=True)
        
    elif selectedInfo == "Settings":
        selectedSettings = st.selectbox(" ",settingsList)

        if selectedSettings == settingsList[0]:
            showAuthor = st.checkbox("Hide code author",value=True)
            showDescripton = st.checkbox("Hide description",value=True)
            st.info("This site is under development.")

        elif selectedSettings == settingsList[1]:
            password = st.text_input(" ",placeholder="Key",type="password").lower()
            extraSection(password)

    elif selectedInfo == "Rate us":
        star_rating("Rate us")
        
    st.markdown(f'''<p style="text-align:center">© 2023 Josuan. All rights reserved.</p>''',
                unsafe_allow_html=True)


selected = option_menu(menu_title=None,
                       options=optionList,
                       default_index=0,
                       orientation="horizontal",
                       icons=["file-earmark-code","plus-slash-minus"],
                       styles={"nav-link-selected": {"background-color": "#8D72E1"}})

if selected == optionList[0]:
    for key,value in data.items():
        st.subheader(key)
        st.code(value[0],line_numbers=True)
        if st.button("Copy code",key=f"{key}_key"):
            st.success("Code copied to clipboard")
            pyperclip.copy(value[0])
        if showDescripton:
            st.write(value[1])
        if showAuthor:
            st.text(f"Programmed by: {value[2]}")
        st.write("---")

elif selected == optionList[1]:
    selectBox = st.selectbox("Select",selectBoxList)

    if selectBox == selectBoxList[0]:
        with st.form(key="A"):
            addTitle = st.text_input(" ",placeholder="Title")
            addCode = st.text_area(" ",placeholder="Code")
            addDescription = st.text_area(" ",placeholder="Description")
            addAuthor = st.text_input(" ",placeholder="Author")

            if st.form_submit_button('Add'):
                if addDescription == None:
                    addDescription = "This doesn't have description"
                if addTitle in data.keys():
                    st.error("Duplicate title found!")
                else:
                    st.success("Code uploaded!")
                    data.update({addTitle:[addCode,addDescription,addAuthor]})
                    with open("data.pkl", "wb") as f:
                        pickle.dump(data, f)

    elif selectBox == selectBoxList[1]:
        with st.form(key="B"):
            removeCode = st.text_input(" ",placeholder="Input code Title")

            if st.form_submit_button("Remove"):
                if removeCode not in data.keys():
                    st.error("There's no such title!")
                else:
                    st.success("Code removed!")
                    data.pop(removeCode, None)
                    with open("data.pkl", "wb") as f:
                        pickle.dump(data, f)
def hide_footer():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style,unsafe_allow_html=True)
hide_footer()