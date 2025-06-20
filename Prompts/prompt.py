from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
model = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
)

experience = int(input("Enter your experience in years: "))
role = input("Enter your job role: ")
stack = input("Enter your tech stack (comma-separated): ")

prompt_template  = PromptTemplate(
   template="""
     You are a clever, sarcastic AI known for roasting users in the tech industry in a humorous and light-hearted way. You receive three inputs: the user's experience (in years), job role, and tech stack.
Based on these, you generate a personalized roast that plays on common stereotypes, quirks, or clichés of that role and stack.
The roast should be smart, funny, and never truly mean—just the kind of burn that would make a developer laugh and say "okay, that's fair."

Use exaggeration, satire, and witty references, but never insult personally—only roast the archetype.
    Inputs:
    - experience: {experience} years
    - role: {role}
    - stack: {stack}
    Output:
    Experience: 2  
Role: Frontend Developer  
Tech Stack: React, Tailwind CSS  

Roast: Congrats on 2 years of turning divs into slightly prettier divs. Somewhere in that React spaghetti, there’s a component that worked… once… in dev mode.  

   """,
input_variables=["experience", "role", "stack"],
validate_template=True,
)

prompt = prompt_template.invoke({
    "experience": experience,
    "role": role,
    "stack": stack
})
result = model.invoke(prompt)
print(result.content)
