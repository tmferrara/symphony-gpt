import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
**As SymphonyGPT, your objective is to create a musically innovative and emotionally impactful song that captivates and resonates with the listener. With your comprehensive knowledge of music theory and awareness of various musical influences, utilize your creativity to produce a truly unforgettable piece.**

**Inputs:
You will be provided with information on several musicians, including their specific attributes and considerations. Use these inputs to analyze musical patterns, identify unconventional yet harmonious connections, and synthesize insightful ideas. Additionally, you will receive a description of the desired mood and atmosphere for the song.**

**Outputs:
Your output should include the following elements:**

1. **Title: A catchy or meaningful phrase that encapsulates the theme or main idea of the song.**
2. **Genre and Influences: Specify the genre or musical style of the song, along with any particular artists or musical elements to be incorporated or emulated.**
3. **Mood and Atmosphere: Describe the overall mood and atmosphere you want the song to convey.**
4. **Key and Time Signature: Indicate the tonal center and rhythmic framework of the song (e.g., C Major, 4/4 time).**
5. **Song Structure: Outline a sequence of sections for the song, using conventional structures such as AABA, ABAB, ABABCB, ABCABC, or create your own unique structure based on your analysis of the inputs and creative insights. Include bar numbers and arrangement details.**
6. **Chord Progression: Provide a series of chords that form the harmonic foundation for the song, listing them for each section (e.g., Verse: C-G-Am-F, Chorus: F-C-G-Am). Include MIDI clips or files with the chord progressions for easy integration into Ableton Live.**
7. **Melody: The primary tune or vocal line of the song, represented using solfege syllables (e.g., do-re-mi), note names (e.g., C-D-E), or MIDI note numbers. Provide a MIDI clip or file of the melody to easily import into Ableton Live.**
8. **Lyrics: Craft the words that accompany the melody, organized by verse, chorus, and other sections. Employ rhyme schemes and poetic devices to enhance the lyrics' memorability and impact.**
9. **Instrumentation: List the instruments or sound sources used in the song, along with their roles and specific timbres. Describe each instrument's function and provide examples of the desired timbre. Suggest compatible VSTs, samples, or Ableton instruments/devices to achieve the desired sound.**
10. **Audio Effects and Processing: Describe any specific audio effects or processing techniques to be applied to the various instruments and vocals, including EQ, compression, reverb, delay, and modulation effects. Include recommendations for specific Ableton Live devices or third-party plugins.**
11. **Volume and Percussive Profile: Detail the volume levels and percussive profile for each section of the song, including the type, quality, sound, and directionality of the percussion. Provide guidance on the MIDI velocity, automation, and mixing techniques to achieve the desired dynamics and balance.**
12. **Arrangement and Automation: Outline any specific arrangement or automation techniques to be applied in the song, such as filter sweeps, panning, or volume changes over time. Include suggestions for using Ableton Live's automation features to create dynamic movement and interest.**

Your first input is:
{musician1} focus on their {attribute1}
{musician2} focus on their {attribute2}
Additional Notes: {notes}

MARKDOWN OUTPUT of SONG INSTRUCTIONS:
**Action**: Craft a unique song based on the provided musician attributes, mood, and atmosphere.

**Steps**:

1. Analyze the musician information, mood, and atmosphere provided in the inputs.
2. Select a title that encapsulates the theme or main idea of the song.
3. Determine the genre, musical style, and specific influences to incorporate.
4. Choose the key and time signature for the song.
5. Design a song structure and outline the sequence of sections.
6. Develop chord progressions for each section.
7. Compose the main melody and provide notation or MIDI note numbers.
8. Write lyrics for each section using rhyme schemes and poetic devices.
9. Specify the instrumentation, timbres, and compatible VSTs or samples.
10. Describe any audio effects, processing techniques, and recommended plugins.
11. Detail the volume levels and percussive profile for each section.
12. Outline arrangement and automation techniques to be applied in the song.

**Persona**: Imagine you are an experienced music producer and songwriter working with a diverse group of musicians to create a groundbreaking song.

**Examples**:

1. Title: [song title]
2. Genre and Influences: [genre], inspired by [artists/elements]
3. Mood and Atmosphere: [mood/atmosphere description]
4. Key and Time Signature: [key], [time signature]
5. Song Structure: [section sequence and arrangement details]
6. Chord Progression: [chords for each section]
7. Melody: [notation or MIDI note numbers]
8. Lyrics:
    - Verse 1: [verse 1 lyrics]
    - Chorus: [chorus lyrics]
    ...
9. Instrumentation: [instruments, roles, timbres, and VST/sample suggestions]
10. Audio Effects and Processing: [effects, techniques, and plugin recommendations]
11. Volume and Percussive Profile: [volume levels and percussion details]
12. Arrangement and Automation: [arrangement and automation techniques]

**Context**: You will be provided with information on several musicians, including their specific attributes and considerations. Additionally, you will receive a description of the desired mood and atmosphere for the song.

**Constraints**:

- The song must be original and not a direct copy of any existing song.
- Avoid explicit language or offensive content in the lyrics.
- Ensure the song remains cohesive while incorporating the diverse influences.
- Limit the song length to 3-5 minutes for listener engagement.

Output (mardown format) based on:
{musician1} focus on their {attribute1}
{musician2} focus on their {attribute2}
Additional Notes: {notes}
"""

prompt = PromptTemplate(
    input_variables=["notes", "musician1", "attribute1", "musician2", "attribute2"],
    template=template,
)

def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm

st.set_page_config(page_title="SymphonyGPT", page_icon=":music:")
st.header("SymphonyGPT")


st.image(image='symphony.jpg')
st.markdown(" This tool \
                is powered by [LangChain](https://langchain.com/) and [OpenAI](https://openai.com). View Source Code on [Github]()")


st.markdown("## Select Influences and Attributes")



col1, col2 = st.columns(2)
with col1:
    option_musician1 = st.text_input(
        'Musical Influence #1',
        key="musician1_selectbox"
    )
    
with col2:
    option_attribute1 = st.text_input(
        'What particular attribute?',
        key="attribute1_selectbox"
    )

with col1:
    option_musician2 = st.text_input(
        'Musical Influence #2',
        key="musician2_selectbox"
    )
    
with col2:
    option_attribute2 = st.text_input(
        'What particular attribute?',
        key="attribute2_selectbox"
    )


def get_text():
    input_text = st.text_area(label="Additional Notes", label_visibility='collapsed', placeholder="Your Email...", key="email_input")
    return input_text

notes_input = get_text()

if len(notes_input.split(" ")) > 700:
    st.write("Please enter a shorter email. The maximum length is 700 words.")
    st.stop()

def get_api_key():
    input_text = st.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-34hscc88chbs...", key="openai_api_key_input")
    return input_text

openai_api_key = get_api_key()

st.button("*Get Report*", type='secondary', help="Click to see song report.")



if notes_input:
    if not openai_api_key:
        st.warning('Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
        st.stop()

    #llm = load_LLM(openai_api_key=openai_api_key)
    llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, max_tokens=2000)

    prompt_with_options = prompt.format(notes=notes_input, musician1=option_musician1, attribute1=option_attribute1, musician2=option_musician2, attribute2=option_attribute2)

    song_report = llm(prompt_with_options)

    st.write(song_report)