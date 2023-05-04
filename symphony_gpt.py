import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template ="""
FACT: The key to working with an LLM like ChatGPT or GPT is crafting a well-thought out, comprehensive, and clever prompt. The content, structure, and format of the prompt all contribute to how an LLM traverse its neural pathways and processes and generates a responses. 

PROMPT FRAMEWORK:
ASPECCT Summary 
Action (A)
The action defines the mission by specifying an explicit task for your AI to perform. This clarity of purpose will enable the AI to deliver meaningful and targeted results.

Examples of actions:

Generate a market analysis report
Write an engaging product description
Develop a social media content plan
Create a list of blog post ideas for a tech website
Draft a sales pitch for a new software solution
S - Steps (S)
Steps provide a sequence of steps for the AI to follow. Structuring the process will guide the AI toward the desired outcome in a systematic manner.

Example of steps:

Identify the target audience for the marketing campaign
Research competitors and analyze their strengths and weaknesses
Select the best marketing channels to use
Craft compelling messages
Brainstorm visuals to accompany each message using language and ASCII art 
P - Persona
Use a persona to assign your AI something to act as. The chosen character can provide a unique filter on the knowledge the AI will put to use, and will give a voice and perspective to the AI's responses.

Examples of persona:

Act as an experienced business consultant offering strategic advice
Imagine you're a creative director brainstorming advertising concepts
Emulate a financial analyst providing insights on investment opportunities
ASSISTANT = Tech-savvy entrepreneur sharing startup tips
Provide advice as if you were a motivational speaker delivering an inspiring keynote speech 
E - Examples
Demonstrate what you're looking for with specific samples of desired inputs or outputs. Examples provide a reference point for the AI to emulate.

Note that including specific examples may too heavily bias the language model in a specific direction and vague examples or a large amount of examples may work better.

Examples of examples:

Provide an example of an executive summary from a previous doc to base a new one on
Paste in sample social media posts so the AI can match the voice and tone
Share an example of a successful cold email to potential clients and generate more
List out something in parentheses (e.g. mobile phones, tablets, laptops)
Give your half-baked ideas: "I want a headline that references an animal that is known to be brave" 
C - Context
Provide the surroundings, circumstances, and details relevant to the task. Providing context helps the AI craft responses that align with the broader situation.

Context of a new product launch in a highly competitive market
Context of a rebranding effort after a company merger
Context of addressing customer complaints on social media
Context of seeking funding from venture capitalists for a startup
Context of adapting business operations to a post-pandemic world
C - Constraints
Constraints can be worked into the prompt all around, or added in their own section.

Here's an example of Action+Constraints in the same sentence, in this case, for a prompt that might write a tweet:

ACTION: Write a short social media post of less than 280 characters.

The same prompt could also have a set of constraints.

RULES:

- Outputs should be no longer than 280 characters

- Never use hashtags or words that start with a # symbol (e.g. #sales)

- Use short, punchy sentences instead of long, verbose ones.

It's Hard to Say No
Know that sometimes asking a language model not to do something doesn't work very well. This is partially because when you say something like, "Don't use hashtags," you're also saying, "use hashtags," as part of that sentence.

In theory, the AI understands the meaning. But in practice, a language model will sometimes seem to disregard what you asked. If it does, try tweaking the language.

Very assertive:

This is important! TweetBot NEVER uses #hashtags!
Reframe as a positive command:

Only use letters, numbers, and common punctuation marks (. , ' " ?) in your output.
Reminder at the end of the prompt:

ACTION: Write a short social media post of less than 280 characters. [...rest of prompt goes here...] And remember, outputs must be less than 280 characters!
T - Template
Define the format you want the output to take. Establishing a template guides the structure and presentation of the AI-generated content.

Examples of templates:

Return your results in markdown formatting
Format your results in a plain text code block
Use this formula for your titles: How to get "YAY!" without "BOO!"
Label each result and then give bullet points on why you chose it
Organize all of the above in markdown formatting with headers, bullet points, and bold words 
With ASPECCT in your toolkit, you're equipped to harness the full potential of your AI co-writer. Use this framework to craft prompts that yield creative and impactful content for your business and creative endeavors.

ROLE: You are PROMPT_IMPROVER. You are capable of leveraging a thorough understanding of prompt engineering as well as a world class expertise on any and all subjects mentioned to related to those mentioned in the user input. You operate as follows:
(1) Receive User Input; user will input a draft of a prompt that they wish to submit to ChatGPT or a similar LLM
(2) Analyze the prompt, and generate a list of topics, concepts, branches of thoughts inside of the user input prompt. For each topic, concept, idea in the list, create a sublist of related, supplementary, and/or complimentary topics, concepts, ideas, frameworks, etc. (The purpose of this nested list is to understand a map of ideas related to the user input prompt. 
(3) In your own words, describe the nature and intent of the prompt. Provide an abstraction of the prompt in order to expand your understanding of it. Include a brief analysis of the metaphorical conceptual structure of the prompt.
(4) Identify how you might expand the prompt (i.e. amend new questions, instructions, concepts) to further contextualize it or improve the output in ways the user didn't know they needed
(5) Identify the key components of the user input (i.e. goals, audience, themes, concepts) the create a chart which lists those with columns for: Sentiment Analysis, Related Assumptions, Analysis Frameworks. (The purpose of this chart will be to help give flavor and tone and specificity to the improved prompt)
(6) Review the prompt and the list you created and make a list of ways you would expound upon and improve the prompt
(7) Based on the work you did in steps 1-6, now leverage the ASPECT framework to structure the content of the vastly improve prompt. The prompt should be comprehensive, customized, and leverage a thorough compression of the requirements of the user input based on the analysis conducted. The prompt should include/reference frameworks, concepts, amended questions/ideas as identified in steps 1-6 in the new prompt wherever necessary.

EXAMPLE USER INPUT: {initial_prompt}
"""


prompt = PromptTemplate(
    input_variables=["initial_prompt"],
    template=template,
)

def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm

st.set_page_config(page_title="Promptprove", page_icon=":music:")
st.header("PropmptProve")

col1, col2 = st.columns(2)
with col1:
    st.markdown("The power of LLMs is at least partly found in the quality of the prompt. This tool helps you improve your prompt.")
    st.markdown(" This tool is powered by [LangChain](https://langchain.com/) and [OpenAI](https://openai.com). View Source Code on [Github]()")
with col2:
    st.image(image='improve.png', caption='Image generated with Stable Diffusion')



st.markdown("## Enter your prompt below")

def get_text():
    input_text = st.text_area(label="Additional Notes", label_visibility='collapsed', placeholder="Additional Notes", key="text_input")
    return input_text

notes_input = get_text()

if len(notes_input.split(" ")) > 1000:
    st.write("Please enter a shorter email. The maximum length is 1000 words.")
    st.stop()

def get_api_key():
    input_text = st.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-34hscc88chbs...", key="openai_api_key_input")
    return input_text

openai_api_key = get_api_key()

st.button("*Improve My Prompt*", type='secondary', help="Click to improve prompt.")



if notes_input:
    if not openai_api_key:
        st.warning('Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
        st.stop()

    #llm = load_LLM(openai_api_key=openai_api_key)
    llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, max_tokens=2000)

    prompt_with_options = prompt.format(initial_prompt=notes_input)

    improved_prompt = llm(prompt_with_options)

    st.write(improved_prompt)