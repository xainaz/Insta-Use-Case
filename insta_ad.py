from aixplain.factories import AgentFactory
from aixplain.modules.agent import ModelTool
from aixplain.enums import Function, Supplier
from IPython.display import display

user_prompt_product= "Please describe the product you would like to promote on Instagram. Include key details such as the product name, features, and what makes it unique.What is the primary goal of this Instagram campaign? Are you looking to increase brand awareness, drive sales, generate engagement, or something else?"

example_input= "Duet Portable monitor, my goal is for more user interaction on instagram page."


agent_list = AgentFactory.list()["results"]
for agent in agent_list:
    print(agent.__dict__)


product_agent= AgentFactory.get("66cf238077b232a2d698bae1")
#Same for all other agents..

product_agent_response = product_agent.run(
    f"""Take the following input {example_input} and extract the key 
    details about the product and the campaign's goals. Provide a 
    structured output containing: Product Name: The name of the product.
    Campaign Goal: The primary objective of the Instagram campaign 
    (e.g., brand awareness, driving sales, increasing engagement)."""
)


competitors_agent_response = competitors_analysis_agent.run(
    f"Based on the product '{product_agent_response}', perform a sentiment analysis of similar products. Provide insights into competitors' products and the general sentiment towards them."
)

marketing_strategy_response = marketing_strategy_agent.run(
    f"Using the following details: '{product_agent_response}' and competitors' insights '{competitors_agent_response}', formulate a marketing strategy for the Instagram campaign."
)

creative_content_response = image_and_text_creative_agent.run(
    f"Generate an Instagram post based on the product details '{product_agent_response}', competitors' analysis '{competitors_agent_response}', and marketing strategy '{marketing_strategy_response}'. Provide a caption and a generated image."
)

print("Product Details:", product_agent_response)
print("Competitors Analysis:", competitors_agent_response)
print("Marketing Strategy:", marketing_strategy_response)
print("Creative Content:", creative_content_response)


