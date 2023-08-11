import numpy as np
import pandas as pd
import streamlit as st

#st.markdown("<h1 style='text-align: center; font-size: 45px;'>Full Project video </h1>", unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center; font-size: 45px;'> Editied by Ahmed Salah</h1>", unsafe_allow_html=True)

#Video
#st.video('ask.mp4')
#st.markdown('----')
#st.markdown('----')
#st.markdown('----')
#st.markdown('----')
#st.markdown('----')
#st.markdown('----')

#Display the Page Title
Page_Title= st.markdown("<h1 style='text-align: center; font-size: 45px;'>Climate Change - Global Warming</h1>", unsafe_allow_html=True)


#Display the Page Subtitle
st.markdown("<h1 style='text-align: center; font-size: 25px;'> By (Ahmed Salah Khalil)</h1>", unsafe_allow_html=True)
st.markdown('----')




# Load the image
image = st.image("Screenshot_1.png")
st.markdown('----')

#Display Introduction
st.markdown("<h1 style='text-align: center; font-size: 30px;'>Content</h1>", unsafe_allow_html=True)

st.write("1- introdution")
st.write("2- data set")
st.write("3- data wrangling")
st.write("4- Exploratory data analysis")                 
st.write("5- conclusion")
st.write("6- what will future climate be like")

#introdution part
st.markdown("<h1 style='text-align: center; font-size: 30px;'>01- INTRODUCTION</h1>", unsafe_allow_html=True)



#Disply Introduction Data
st.write("Because of noticing the large change in the state of the climate during the past recent years, I decided to study the temperatures over the years to know the factors affecting this great change.")



#Video Formating
#st.markdown("<h1 style='text-align: Left; font-size: 25px;'>Global wormaing video</h1>", #unsafe_allow_html=True)
#st.video('ask.mp4')

st.markdown("-----")

st.markdown("<h1 style='text-align: Left; font-size: 25px;'>what is climate change?</h1>", unsafe_allow_html=True)
st.write("It is a change in temperature in a certain period from its normal range ")
st.markdown("-----")

st.markdown("<h1 style='text-align: Left; font-size: 25px;'>what does climate change effects?</h1>", unsafe_allow_html=True)
st.write("- wild fires")
st.write("- Heat Waves ")
st.write("- sea level rise (because of massive ice mass loss)")
st.write("- extreme weather events")

st.markdown("-----")

st.markdown("<h1 style='text-align: Left; font-size: 25px;'>objectives</h1>", unsafe_allow_html=True)
image = st.image("Screenshot_3.png")

st.write("1 -TO COLLECT AND CLEAN THE HUGE WEATHER DATA FROM (1749-2013)")
st.write(" 2 - TO EXPLORE AND ANALYZE THE DATA ")
st.write("3  - TO PREDICT FUTURE CLIMATE PATTERN")

st.markdown("------")

st.markdown("<h1 style='text-align: CENTER; font-size: 30px;'>02 -DATASET</h1>",unsafe_allow_html=True)
image = st.image("Screenshot_2.png")
st.write("-          7 CSV Files")
st.write("-         (8,599,212) ROWS")
st.write("-      32 FEATURES")
st.write("- Date: starts in 1750 for average land temperature and 1850 for max and min land temperatures and global ocean and land temperatures")
st.write("- LandAverageTemperature: global average land temperature in Celsius LandAverageTemperatureUncertainty: the 95% confidence interval around the average")
st.write("- LandMaxTemperature: global average maximum land temperature in Celsius")
st.write("- LandMaxTemperatureUncertainty: the 95% confidence interval around the maximum land temperature")

st.markdown("------")

st.markdown("<h1 style='text-align: CENTER; font-size: 30px;'>03 DATA WRANGLING</h1>",unsafe_allow_html=True)
st.write(" - Load and explore ")
image = st.image("Screenshot_4.png")
st.write(" - clean ")
image = st.image("Screenshot_5.png")
st.write(" - Feature extract and transform")
image = st.image("Screenshot_4.png")

st.markdown("-----")

st.markdown("<h1 style='text-align: CENTER; font-size: 30px;'>04 - EXPLORATORY DATA ANALYSIS </h1>",unsafe_allow_html=True)
st.markdown("<h1 style='text-align: Left; font-size: 25px;'>Questions should be answered after running this analysis</h1>",unsafe_allow_html=True)
st.write(" - Did the world increase in temperature?")
st.write(" - what are the hottest countries? ")
st.write(" - comparing important countries ")
st.write(" - are the hottest countries increased in temp more than the coler ones ?")
st.write(" - by how much is that increase ?")
st.write(" - When did the Global Warming Start ?")
st.write(" - Why 1975 exactly?")
st.write(" - lets study 1975 much more ")
st.write(" - what is the AverageTemperature in egypt ? ")
st.write(" - what is the hotest mounth in egypt ? ")
st.write(" - what is the future climate will be like ? ")







# Define the questions and their corresponding chart types
questions = {
    "Did the world increase in temperature?": "1.png",
    "what are the hottest countries?": "2",
    "comparing important countries": "Chart_3",
    "are the hottest countries increased in temp more than the coler ones ?": "Chart_4",
    "by how much is that increase ?": "Chart_5",
    "When did the Global Warming Start ?": "Chart_6",
    "Why 1975 exactly?": "Chart_7",
    "lets study 1975 much more": "Chart_8",
    "what is the AverageTemperature in egypt ?": "Chart_9",
    "what is the hotest mounth in egypt ?": "Chart_10",
    "what is the future climate will be like ?": "Chart_11"
}

st.markdown("-----")



# Display the dropdown list
st.write("<h3 style='font-weight: bold;'>Select Yor Question:</h2>", unsafe_allow_html=True)
question = st.selectbox("", list(questions.keys()))






# Display the chart based on the selected question
if question == "Did the world increase in temperature?":
    st.image("1.png")
    
    
    
    
elif question == "what are the hottest countries?":
    st.image("2.png")
    st.image("22.png")

    
    
    
    
    
    
elif question == "comparing important countries":
    st.image("3.png")
    
    
    
    
    
elif question == "are the hottest countries increased in temp more than the coler ones ?":
    st.image("4.png")

    
    
    
    
    
    
elif question == "by how much is that increase ?":
    st.image("5.png")
    st.write("- Brazil and Argentina - BIG deforestation issues (their wildfires have     increased big time and the decrease in agriculture is the main factor)")
    st.write("- Kazakhstan - a place for testing biological and nuclear weapons by the Soviets. Also, here are located the most polluting industries. Most of their water is infected by industrial and agricultural runoff and it is in some places radioactivity")
    
    
    
    
    
elif question == "When did the Global Warming Start ?":
    st.image("6.png")
    
    
    
    
    
    
    
elif question == "Why 1975 exactly?":
    st.image("7.png")

    st.write("- No doubt the Industrial Revolution but especially when the human discover Freon and that had an effect between 1900 and 1975.")
    st.write("- combining with the population increase that started somewhere in 1975 (from ~2.5 bil in 1950 to 5 bil in 2000)created an enormous overall global warming state.")

    
    
    
    
    
    
    
    
    
elif question == "lets study 1975 much more":
    st.image("8.png")
    st.write("- I feel like 1975 was a (no turning back) point, so I chose this moment to compare temperatures before and after.")
    st.write("- Land Average Temperature - an increase from 8.37 degrees to 9.20; almost 1 full grade")
    st.write("- Land Maximum Temperature - an increase from 14.18 degrees to 14.89; 0.71 grades increase")
    st.write("- Land Minimum Temperatures - an increase from 2.45 degrees to 3.64; 1.19 grades increase")
    st.write("-  Why is the (Cold Weather) getting hotter more rapidly than the (Hot Weather) ?")
    






elif question == "what is the AverageTemperature in egypt ?":
    st.image("9.png")
    st.image("99.png")


    
    
    
    
    
    
elif question == "what is the hotest mounth in egypt ?":
    st.image("10.png")

     
     
     
     
     

elif question == "what is the future climate will be like ?":
    st.image("11.png")
    st.write("- a warmer atmosphere, a warmer and more acidic ocean, higher sea levels, and larger changes in precipitation patterns")
    
    
    
    
st.markdown("-----")

#Conclusion Data

st.markdown("<h1 style='text-align: center ; font-size: 30px;'>05 - Conclusion</h1>", unsafe_allow_html=True)    
st.write("- i find that there has been a global increase trend in temperature, particularly over the last 50 years. This is due to the violent activities of humankind. ")

st.write("- In more developed countries the temperature began to register higher much earlier")    

st.write("- Governments should be more aware of the upcoming danger, as it is an upcoming danger for everyone") 

st.write("- Nuclear reaction experiments must be stopped, and freon production must be stopped in a larger way") 
