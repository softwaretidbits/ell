import os
import random

import ell
import openai
from PIL import Image
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

# Using openai, but can change this as needed to another provider key
key = os.getenv('OPENAI_API_KEY')
assert (key is not None)
openai_client = openai.Client(api_key=key)


class Person(BaseModel):
    name: str
    age: int
    favorite_image: str


# Review model
class TidbitReview(BaseModel):
    title: str = Field(description="Title of the tidbit")
    rating: int = Field(description="Rating of the tidbit (1 to 10)")
    summary: str = Field(description="Summary of the tidbit")


# Tidbit for ell container model
class EllTidbit(BaseModel):
    ell.init(store='./logdir', autocommit=True)

    def hearing(self, name):
        print(f"=== What are you hearing {name}?")
        action = self.listen(name)
        print(action)

    def review(self):
        print("=== Providing a tidbit review.")
        review_message = self.create_tidbit_review("Visualize with ell-studio")
        review = review_message.parsed
        print(f"Tidbit: {review.title}, Rating: {review.rating}/10")
        print(f"Summary: {review.summary}")

    def greeting(self, name):
        print("=== Just say hello.")
        saying_hello = self.hello(name)
        print(saying_hello)

    def inspection(self, image_path):
        print("=== Perform an inspection.")
        image = Image.open(image_path)
        description = self.inspect_image(image)
        print(description)

    def generate_information(self):
        print("*** Generate foundations.")
        person = Person(name="Mr. Tidbit", age=43, favorite_image="images/cat-image.jpg")
        self.hearing(person.name)
        self.review()
        self.greeting(person.name)
        self.inspection(person.favorite_image)

    @ell.simple(model="gpt-4o-mini", client=openai_client)
    def listen(self, name: str):
        """You are a helpful assistant."""
        sound = self.get_random_noise()
        return f"{name} is now hearing a {sound}.  What would generate such a sound?"

    @ell.complex(model="gpt-4o-mini", client=openai_client, response_format=TidbitReview)
    def create_tidbit_review(self, tidbit: str):
        """You are a tidbit review generator.
        Given the name of a tidbit, you need to return a structured review."""
        return f"Generate a review for the tidbit {tidbit}"

    @ell.simple(model="gpt-4o-mini", client=openai_client)
    def hello(self, name: str):
        return [
            ell.system("You are my favorite assistant Babu Frik."),
            ell.user(f"Say hello to {name}!"),
            ell.assistant(f"I'd be happy to say hello to {name}"),
            ell.user("Perfect, I would like to change the greeting to Texan please.")
        ]

    @ell.simple(model="gpt-4o-mini", client=openai_client)
    def inspect_image(self, image: Image.Image):
        return [
            ell.system("You are my favorite assistant Babu Frik."),
            ell.user(["What is contained in this image provided?", image])
        ]

    def get_random_noise(self):
        noises = ["gulp", "plink", "whistle", "boom"]
        return random.choice(noises)


if __name__ == '__main__':
    print('')
    print(
        'Welcome to a SoftwareTidbits session (ell-2) about using ell-studio as part of your prompt engineering w/ Python and ell')
    print(
        'If you missed the first session, take a look at the project (ell-1) - https://medium.com/software-tidbits/prompt-engineering-using-ell-language-model-programming-lib-3658287c96e5')
    print('')
    print(
        "Execute the four use cases derived from the 'ell introduction' session to build up some persisted LMP information.")
    print('1. Run the ell-studio tool using your command line')
    print('Example: ell-studio --storage ./logdir')
    print('2. Open the link upon startup. By default this is: http://127.0.0.1:8080.')
    print('3. Explore!')
    print('---')

    # Construct our tidbit
    ell_tidbit = EllTidbit()

    # Run examples to generate information to use for visualization w/ ell-studio
    ell_tidbit.generate_information()
