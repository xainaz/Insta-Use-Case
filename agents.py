from aixplain.factories import AgentFactory, ModelFactory
from aixplain.modules.agent import ModelTool
from aixplain.enums import Function, Supplier

text_generation_model =ModelFactory.get("6622cf096eb563537126b1a1")
summarization_model = ModelFactory.get("6622cf096eb563537126b1a1")
text_to_image_model= ModelFactory.get("64aee5824d34b1221e70ac07") #This is stable diffusion

ner_tool = ModelTool(
    function=Function.NAMED_ENTITY_RECOGNITION,
    supplier=Supplier.MICROSOFT
)

sentiment_analysis_tool = ModelTool(
    function=Function.SENTIMENT_ANALYSIS,
    supplier=Supplier.GOOGLE)

text_generation_tool = ModelTool(
    Model= text_generation_model
)

summarization_tool = ModelTool(
    Model= summarization_model
)

image_generation_tool= ModelTool(
    Model= text_to_image_model
)

product_identification_agent= AgentFactory.create(
    name= "Product and Goal Identification Agent",
    tools=[ner_tool],
    description="An agent that analyses text and extracts model name and goal.",
    llm_id="6646261c6eb563165658bbb1"
)

competitors_analysis_agent= AgentFactory.create(
    name= "Product and Goal Identification Agent",
    tools=[sentiment_analysis_tool],# Add web scraping tool here
    description="Information about the product and possibly competitors' websites or data sources.",
    llm_id="6646261c6eb563165658bbb1"
)

marketing_strategy_agent= AgentFactory.create(
    name= "Marketing Strategy Agent", 
    tools= [text_generation_tool, summarization_tool],
    description= "Formulate marketing strategies based on product and competitor insights.",
    llm_id="6646261c6eb563165658bbb1"
)

image_and_text_creative_agent= AgentFactory.create(
    name= "Image and text creation Agent", 
    tools= [text_generation_tool, image_generation_tool],
    description= "Generate creative content for Instagram posts: captions and images.",
    llm_id="6646261c6eb563165658bbb1"
)

#Instagram Scraping Library: instaloader