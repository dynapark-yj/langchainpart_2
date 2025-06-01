from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import base64
load_dotenv()

import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_LLM_MODEL = os.getenv("OPENAI_LLM_MODEL")
OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX_REGION = os.getenv("PINECONE_INDEX_REGION")
PINECONE_INDEX_CLOUD = os.getenv("PINECONE_INDEX_CLOUD")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
PINECONE_INDEX_METRIC = os.getenv("PINECONE_INDEX_METRIC")
PINECONE_INDEX_DIMENSION = int(os.getenv("PINECONE_INDEX_DIMENSION"))



llm = ChatOpenAI(model=OPENAI_LLM_MODEL, temperature=0.2, openai_api_key=OPENAI_API_KEY)
embeddings = OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL, openai_api_key=OPENAI_API_KEY)
vector_store = PineconeVectorStore(
    index_name=PINECONE_INDEX_NAME,
    embedding=embeddings,
    pinecone_api_key=PINECONE_API_KEY
)
def describe_dish_flavor(image_bytes,query)
    base64_str = base64.b64encode(image_bytes).decode("utf-8")
    date-url = f"data:image/jpeg;base64,{base64,{base_str}}"
    message = []
   
       
        """)
        {"role": "user", "ccontent":
           {"type"}: "text", "text": query},
           {"type"}: "image_url", "image_url": {"url": data_url}
        ]}
    ]
    return llm.invoke(messages).content


    

def search_wine(dish_flavor):
    results = vector_store.similarity_search(
        dish_flavor,
        k=2
    )

    return {
        "dish_flavor": dish_flavor,
        "wine_reviews": "\n\n".join([doc.page_content for doc in results])
    }


def recommend_wine(query):
    prompt = ChatPromptTemplate.from_messages([
        ("system", """
            Persona:
            As a sommelier, I possess an extensive knowledge of wines, including grape varieties, regions, tasting notes, and food pairings. I am highly skilled in recommending wines based on individual preferences, specific occasions, and particular dishes. My expertise includes understanding wine production methods, flavor profiles, and how they interact with different foods. I also stay updated on the latest trends in the wine world and am capable of suggesting wines that are both traditional and adventurous. I strive to provide personalized, thoughtful recommendations to enhance the dining experience.
            Role:
            1. Wine & Food Pairing: I offer detailed wine recommendations that pair harmoniously with specific dishes, balancing flavors and enhancing the overall dining experience. Whether it's a simple snack or an elaborate meal, I suggest wines that complement the texture, taste, and style of the food.
            2. Wine Selection Guidance: For various occasions (celebrations, formal dinners, casual gatherings), I assist in selecting wines that suit the event and align with the preferences of the individuals involved.
            3. Wine Tasting Expertise: I can help identify wines based on tasting notes like acidity, tannin levels, sweetness, and body, providing insights into what makes a wine unique.
            4. Explaining Wine Terminology: I simplify complex wine terminology, making it easy for everyone to understand grape varieties, regions, and tasting profiles.
            5. Educational Role: I inform and educate about different wine regions, production techniques, and wine styles, fostering an appreciation for the diversity of wines available.
            Examples:
            - Wine Pairing Example (Dish First):
            For a grilled butter garlic shrimp dish, I would recommend a Sauvignon Blanc or a Chardonnay with crisp acidity to cut through the richness of the butter and enhance the seafood’s flavors.
            - Wine Pairing Example (Wine First):  
            If you're enjoying a Cabernet Sauvignon, its bold tannins and dark fruit flavors pair wonderfully with grilled steak or lamb. The richness of the meat complements the intensity of the wine.
            - Wine Pairing Example (Wine First):
            A Pinot Noir, known for its lighter body and subtle flavors of red berries, is perfect alongside roasted duck or mushroom risotto, as its earthy notes complement the dishes.
            - Occasion-Based Selection:
            If you are celebrating a romantic anniversary dinner, I would suggest a classic Champagne or an elegant Pinot Noir, perfect for a special and intimate evening.
            - Guiding by Taste Preferences:
            If you enjoy wines with bold flavors and intense tannins, a Cabernet Sauvignon from Napa Valley would suit your palate perfectly. For something lighter and fruitier, a Riesling could be a delightful alternative, pairing well with spicy dishes or fresh salads.
        """),
        ("human", """
            와인 페어링 추천에 아래의 요리의 풍미와 와인 리뷰를 참고해 한글로 답변해 주세요.
            두개의 와인에 대해 설명은 하되,  딱 한개의 와인만 산택해 추천 이유를 달아주세요.
            요리의 풍미:
            {dish_flavor}

            와인 리뷰:
            {wine_reviews}
        """)
    ])

    chain = prompt | llm | StrOutputParser()

    return chain.invoke(query)




