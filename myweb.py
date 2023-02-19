import streamlit as st
import pandas as pd
tabel= pd.DataFrame({'column 1':[1,2,3,4,5],'column 2':[8,9,10,11,6]})
st.markdown("""
<style>
.css-9s5bis.edgvbvh3
{
    visibility:hidden;
}
.css-h5rgaw.egzxvld1
{
    visibility:hidden;
}
</style>


""",unsafe_allow_html=True)
st.subheader("HI I am your subheader")
st.header("i am header")
st.text("Hi, I am text funciton and programmer")
st.markdown("[Google](https://www.google.com)")
st.markdown("___")
st.caption("difference between .text and .write")  
st.text('st.text:Hello, *Worlld!* :sunglasses:')
st.write('st.write:   Hello, *Worlld!* :sunglasses:')
st.markdown("___")
st.text('metric')
st.metric(label='wind speed',value='120ms',delta='-1.4ms\^-1')
st.markdown("___")
st.text('Dataframe')
st.text('display the tabel:st.table(tabel)')
st.table(tabel)
st.text('operation on the tabel:st.dataframe(tabel)')
st.dataframe(tabel)
st.markdown("___")
st.text('embed image')
st.image('sky.jpg',caption="sunset sky",width=500)
st.markdown("___")
st.text('embed audio')
st.audio('record.mp3')
st.markdown("___")
st.text('embed video')
st.video('pcr_test.mp4')
def change():
    print("changed")
state = st.checkbox('Checkbox',value=True,on_change=change)
