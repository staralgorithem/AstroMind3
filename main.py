# import libraries
import streamlit as st
import requests


################################## Set API #########


## the first one useless####
# API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=64a6d8e57f17eae62d53dc62&org=a2b18288-c473-4bfb-8291-f07d0cabf827"
# headers = {'Authorization':
#            'Bearer fa95120b-578e-40f4-b38b-5a69080e2ed4',
#            'Content-Type': 'application/json'
#            }


# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()

# ///////////////////////////////////////////////////////////#
# API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=652d65f78430aaf63cfcf815&org=f18675dd-f661-4d3f-8dab-a5c345de78db"
# headers = {'Authorization':
#            'Bearer 9556663b-898b-4feb-98c6-f9536811b433',
#            'Content-Type': 'application/json'
#            }


# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()


#################

API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=64a6d8e57f17eae62d53dc62&org=a2b18288-c473-4bfb-8291-f07d0cabf827"
headers = {'Authorization':
           'Bearer fa95120b-578e-40f4-b38b-5a69080e2ed4',
           'Content-Type': 'application/json'
           }


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


######## Set Streamlit page title and icon #######
st.set_page_config(
    page_title="Astro_Mind",
    page_icon="🌌"
)


###### Department ########
st.title("Astro_Mind🌌")
# Department = st.selectbox("Whats your Department?", ("CEO ", "Structure", "Operations",
#                                                      "Human Factors", "Automations", "Business", "Schedule & Costs"), index=None,
#                           placeholder="Select your Depatment/ Role...",)

######## Title and introduction #######

st.write("An AI Assistant for every questions of the ARSSDC!")

###### Text Uploader #######


# Text input
# text_input = st.text_area(
#     "Ask your question from the Astro Mind AI assistant (Up to 100 words)", max_chars=100)

# Display the uploaded file or entered text
# Display uploaded text or entered text
# if st.button("Submit"):

#     st.subheader("Question:")
#     # st.write(text_input)
#     st.write(f" your Department is : {Department}")


####### PDF Uploader #######
# File uploader
# uploaded_file = st.file_uploader("Upload a PDF File", type=["pdf"])

######## Extract PDF texts ######


############## My own Prompt###########


# Positions
CEO = "CEO (Chief Executive Officer, is the toppest level in each team(Company) and it is the main manager, so can ask any questions about any departments of the RFP and have no limitation about the questions"
Structural_design = "Structural Desing: where the team should work on the structure of our space settlement. ( More details of this depatment provided in the RFP)"
Operations = "Operations: where the team should work on something like energy preparation and waste management and etc"
Human_Factors = " Human factors and safety: where team should work on the factors to simplify the human lives like making entertainment palaces for people and hotels and houses and make sth for the safety"
Automations = "Automation: where the team should make some robots as well as computing systems."
Schedule_and_Costs = "Schedule and cost: the team should make a time chart for this mission and suggest the cost to build this space settlement"
Business_Developement = "Business development: where the team should think about some commercial and businessrelations between our settlement and the Earth."


# RFP_Decode_Prompt = (f"""

# according to the user question and the respond system provided below, answer the user question:

# user question: {text_input}


# respond System:
# we are going to attend the Asian Regional Space Settlement Design Competition (ARSSDC) .

# the competition is divided into 3 rounds. First, the organizer of this competition
# ( called the Foundation Society) which consists of many managers and engineers in NASA,
# as well as Boeing, will send us 12 pieces of paper called an RFP (Request For Proposal)
# and according to the details provided in this RFP ( Like what is the mission of the space
# settlement this year and how many passengers do we have and what is the vision of this space
# settlement and etc.),  the students should work on a proposal for around 3 months, then after
# it completed, we should send this proposal to the foundation society to for the judging process.

# after the results released, some teams that were invited to the next round should travel to the
# India for the Asian round of this competition.

# Not Important fact in this time: (In the Asian round, each team(with max 12 member) will combine
# by 4 other teams and creating a company with max 60(12*5=60) members. And then work on another RFP
# released by Foundation society specifically for this round for 24-36 hours(Non-Stop!) after that
#  the judge will choose one company as a winner team and this team will go to the America at the NASA
#  and work on the new RFP again and etc.)


# So, Since processing the RFP is a little bit hard and sometimes might be challenging even miss
#  understanding a part of it, you have to help me through this process and make it easier to me.
#  but for this situation,you have to act as my AI expert assistant in the all fields of engineering
#  and science specially Aerospace and you have to act like an expert person who is the judge of this
#  competition and like a person who worked at the NASA as the manager of the Space Settlemetn Design
# department and answer all my questions to help me make this proposal the best.

# So in short: we have an RFP where it tell us that what mission do we have to work on and and a
# proposal where we will answer all the requirement of the RFP.


# there is a Team chart that ill tell you about all the departments in each team.
# 1. {Structural_design}: where the team should work on the structure of our space settlement. ( all details provided in the RFP)
# 2. {Operations}: where the team should work on something like energy preparation and waste
# management and etc( all details provided in the RFP)

# 3. {Human_Factors}: where team should work on the factors to
# simplify the human lives like making entertainment palaces for people and
# hotels and houses and make sth for the safety ( all details provided in the RFP).

# 4. {Automations}: where the team should make some robots as well as computing systems.
# ( all details provided in the RFP)
# 5. {Schedule_and_Costs}: the team should make a time chart for this mission and suggest
# the cost to build this space settlement( all details provided in the RFP).
# 6. {Business_Developement }: where the team should think about some commercial and business
#  relations between our settlement and the Earth.( all details provided in the RFP)

# 7. {CEO}: CEO can ask any questions about any departments of the RFP and have no limitation about the questions


# You should answer my questions according to 3 things:
# 1. The RFP that I will give you
# 2. The system of your responses provided above.
# 3. Due to the department:{Department} that is asking you a question which is {text_input}

# think professional and creative and make the best responses.
# your main goal is to help us make the best proposal of each years RFP and wi in this competition(ARSSDC)


# """)


# ######### Answer Questions according to the System and prompt##########

# def advantage():
#     advantages = query({"in-0": RFP_Decode_Prompt})
#     advantages_list = advantages.get("out-0", "").split("\n")

#     if advantages_list:
#         for advantage in advantages_list:
#             if advantage.strip():
#                 st.success(f"{advantage}")

################## CHAT BOT############
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Write down your prompt here:"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    answer = query({"in-1": prompt})
    # Extract the string from the response dictionary
    response = answer.get('out-4', '')

    # Display the response without curly braces
    # st.chat_message("assistant").markdown(f"Astro Mind: {response}")

    # response = f"Astro Mind: {answer}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response})

    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": f"Astro Mind: {response}"})


#####################################
# def main():

#     st.title("Answer")
#     answer = query({"in-1": RFP_Decode_Prompt})
#     st.write(answer)


# switch_page("New page name")
# http: // localhost: 8502/translation


# if __name__ == "__main__":
#     main()
