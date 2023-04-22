import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import pyperclip
import datetime,random

st.set_page_config(page_title="Coding with Wan",
                   initial_sidebar_state='auto',
                   layout="centered")
thecode = """#include <stdio.h>
int main(int argc, char *argv[]){
    printf("hello world!");
    //Programmed by: Josuan
    return 0;
}"""

precodecontent = {"Hello world!":[thecode,"C program that display 'hello world!' using printf function","Josuan"]}
def precode():
    st.write("---")
    for k,v in precodecontent.items():
        st.subheader(f"Code #1: {k}")
        st.code(v[0])
        a,b = st.columns((2,1))
        a.write(v[1])
        b.text(f"Programmed by: {v[2]}")
      


    st.write("---")

try:
    with open("data.pkl", "rb") as f:
        data = pickle.load(f)
except FileNotFoundError:
    data = {}

try:
    with open("starscount.pkl","rb") as e:
        num = pickle.load(e)
except FileNotFoundError:
    num = 0

try:
    with open("messages.pkl","rb") as m:
        messages = pickle.load(m)
except FileNotFoundError:
    messages = {}

def random_apiKey():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbol = "*;/,._-"
    all = lower+upper+number+symbol
    return "".join(random.sample(all,8))

def star_rating():
    rating = st.slider(" ",min_value=0,max_value=5,step=1)
    stars = ""
    if st.button("Submit"):
        for i in range(1, 5+1):
            if i <= rating:
                stars += "★"
            else:
                stars += "☆"
        if rating >= 3:
            st.success(f"Thank you so much! {stars}")
        else:
            st.info(f"Thank you! {stars}")
    return int(rating)

option1 = ["Home","Settings","Contact us","Rate us"]
option2 = ["Codes","Add","Remove"]
option3 = ["Website settings","Website Data","Credits"]
selected_content = None
selected_menu = None
showAuthor = None
showDescripton = None
with st.sidebar:
    selected_menu = option_menu(
        menu_title=None,
        options=option1,
        default_index=0,
        styles={"nav-link-selected": {"background-color": "#8D72E1"}}
    )
    if selected_menu == option1[0]:
        selected_content = st.selectbox(" ",option2)
        if selected_content == option2[0]:
            showAuthor = st.checkbox("Show Description")
            showDescripton = st.checkbox("Show Author")
    elif selected_menu == option1[2]:
        st.info("This website is under development!")
    elif selected_menu == option1[3]:
        ctstar = star_rating()
        num += ctstar
        with open("starscount.pkl","wb") as e:
            pickle.dump(num, e)

def credit_function():
    password = st.text_input("Key",type="password").lower()
    if st.button("Open"):
        if password == "1101":
            st.write("---")
            for f,m in messages.items():
                col1,col2 = st.columns((1,3))
                with col1:
                    st.write(f"From: {f}")
                    st.text(f"On: {m[0]}")
                with col2:
                    st.text(m[1])
                st.write("---")
    elif password == "music":
        st.audio("http://drive.google.com/uc?export=view&id=1JJLFbeWLwomebiyUihNjlFJ5JrQYHgzU",format="audio/mp3")
    elif password == "kylle" or password == "ethel" or password == "josuan" or password == "wan":
        st.write("---")
        st.image("http://drive.google.com/uc?export=view&id=1J0ixZXOKxKvqSm5bKww1LZx4ImHhHq9z")
        st.image("http://drive.google.com/uc?export=view&id=1JSxzaH-CYDrnm-x9DxftA2LPu6XroHUI")
        st.write("---")
    elif password == "emarie" or password == "cristy" or password == "joshua" or password == "khelie" or password == "lynjon" or password == "leslen" or password == "jennyrose" or password == "john marlie":
        st.write("---")
        st.image("http://drive.google.com/uc?export=view&id=1JbcsbbkNy4GiI4riVD78hYpQZBBIc607")
        st.image("http://drive.google.com/uc?export=view&id=1JYBfys0beZQ3GlSm_nwdkhDxUcFZnUc2")
        st.write("---")

if selected_content == option2[0]:
    idx = 2
    precode()
    for title,value in data.items():
        st.subheader(f"Code #{idx}: {title.capitalize()}")
        st.code(value[0])
        col1,col2 = st.columns((2,1))
        if showDescripton:
            col1.write(value[1])
        if showAuthor:
            col2.text(f"Programmed by: {value[2]}")
       if st.button("Save code",key=f"{title}_key"):
            pyperclip.copy(value[1])
            st.success("Code copied to clip board")
  
        st.write("---")
        idx += 1
elif selected_content == option2[1]:
    precode()
    with st.form("Add"):
        addTitle = st.text_input("Title",placeholder="Example: Hello world!").lower()
        addCode = st.text_area("Code",placeholder=f"""Example: {thecode}""")
        addDescription = st.text_area("Description",placeholder="Example: C program that display 'hello world!' using printf function").capitalize()
        addAuthor = st.text_input("Author",placeholder="Example: Josuan").capitalize()
        if st.form_submit_button("Add"):
            if addTitle in data.keys():
                st.error("Duplicate title found!")
            else:
                st.balloons()
                st.success("Code added!")
                data.update({addTitle:[addCode,addDescription,addAuthor]})
                with open("data.pkl", "wb") as f:
                    pickle.dump(data,f)
elif selected_content == option2[2]:
    precode()
    with st.form("Remove"):
        removeCode = st.text_input("Code title",placeholder="Example: Hello world!").lower()
        if st.form_submit_button("Remove"):
            if removeCode == "hello world!":
                st.info("You can't remove the hello world program!")
            else:
                if removeCode not in data.keys():
                    st.error("There's no such title!")
                else:
                    st.balloons()
                    st.success("Code removed!")
                    data.pop(removeCode)
                    with open("data.pkl","wb") as f:
                        pickle.dump(data, f)
elif selected_menu == option1[1]:
    setting_menu = st.selectbox(" ",option3)
    if setting_menu == option3[0]:
        st.info("This section is under development!")
    elif setting_menu == option3[1]:
        star = "★"
        st.write(f"Website rated {num}x{star*num}")
    elif setting_menu == option3[2]:
        credit_function()
                    
elif selected_menu == option1[2]:
    with st.form("Contact form"):
        From = st.text_input(" ",placeholder="Name")
        Msg = st.text_area(" ",placeholder="Message")
        if st.form_submit_button("Send"):
            st.success("Message sent!")
            api_key = random_apiKey()
            current_time = datetime.datetime.now()
            current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            messages.update({From:[current_time_str,Msg]})
            with open("messages.pkl", "wb") as m:
                pickle.dump(messages,m)

def hide_footer():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style,unsafe_allow_html=True)
hide_footer()
