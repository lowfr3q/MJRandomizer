import random
import os
import openai

env_openai_key = os.getenv("OPENAI_API_KEY")
openai.api_key = env_openai_key

character_list = ["Marilyn Monroe", "Abraham Lincoln", "Nelson Mandela", "John F. Kennedy", "Martin Luther King",
                  "Queen Elizabeth II", "Winston Churchill", "Donald Trump", "Bill Gates", "Muhammad Ali",
                  "Mahatma Gandhi", "Mother Teresa", "Christopher Columbus", "Charles Darwin ", "Elvis Presley",
                  "Albert Einstein", "Paul McCartney", "Queen Victoria", "Pope Francis", "Jawaharlal Nehru",
                  "Leonardo da Vinci", "Vincent Van Gogh", "Franklin D. Roosevelt", "Pope John Paul II",
                  "Thomas Edison", "Rosa Parks", "Lyndon Johnson", "Ludwig Beethoven", "Oprah Winfrey", "Indira Gandhi",
                  "Eva Peron", "Benazir Bhutto", "George Orwell", "Vladimir Putin", "Dalai Lama", "Walt Disney",
                  "Neil Armstrong", "Peter Sellers", "Barack Obama", "Malcolm X", "J.K.Rowling", "Richard Branson",
                  "Pele", "Angelina Jolie", "Jesse Owens", "John Lennon", "Henry Ford", "Haile Selassie",
                  "Joseph Stalin", "Lord Baden Powell", "Michael Jordon", "Vladimir Lenin", "Ingrid Bergman",
                  "Fidel Castro", "Leo Tolstoy", "Greta Thunberg", "Pablo Picasso", "Oscar Wilde", "Coco Chanel",
                  "Charles de Gaulle", "Amelia Earhart", "John M Keynes", "Louis Pasteur", "Mikhail Gorbachev", "Plato",
                  "Adolf Hitler", "Sting", "Elon Musk", "Mary Magdalene", "Alfred Hitchcock", "Michael Jackson",
                  "Madonna", "Mata Hari", "Cleopatra", "Grace Kelly", "Malala Yousafzai", "Steve Jobs", "Ronald Reagan",
                  "Lionel Messi", "Babe Ruth", "Bob Geldof", "Roger Federer", "Sigmund Freud", "Woodrow Wilson",
                  "Mao Zedong", "Katherine Hepburn", "Audrey Hepburn", "David Beckham", "Tiger Woods", "Usain Bolt",
                  "Carl Lewis", "Prince Charles", "Jacqueline Kennedy Onassis", "Joe Biden", "Kim Kardashian",
                  "C.S. Lewis", "Billie Holiday", "J.R.R. Tolkien", "Billie Jean King", "Margaret Thatcher",
                  "Anne Frank", "Simon Bolivar", "Marie Antoinette", "Cristiano Ronaldo", "Emmeline Pankhurst",
                  "Emile Zatopek", "Desmond Tutu", "Lech Walesa", "Julie Andrews", "Florence Nightingale",
                  "Marie Curie", "Stephen Hawking", "Tim Berners Lee", "Aung San Suu Kyi", "Lance Armstrong",
                  "Shakira", "Jon Stewart", "Wright Brothers", "Ernest Hemingwa", "Roman Abramovich", "Tom Cruise",
                  "Rupert Murdoch", "Al Gore", "Sacha Baron Cohen", "George Clooney", "Paul Krugman", "Jimmy Wales",
                  "Brad Pitt", "Kylie Minogue", "Stephen King"]
food_list = ["soup", "fish", "steak", "crab", "lobster", "ice cream", "hamburgers", "candy", "fries", "fast food",
             "indian food", "trash", "crackers", "yogurt", "bananas", "apples", "fruit", "pizza", "cookies", "rice",
             "bugs", "salad", "mexican food", "tacos", "a burrito", "beans", "eggs", "cereal", "fried chicken",
             "chicken tenders", "a bloomin' onion", "cheesecake", "cake", "jell-o", "mashed potatoes"]
drink_list = ["soda", "Coke", "Pepsi", "CapriSun", "Water", "milk", "tea", "iced tea", "lemonade", "juice", "rum",
              "vodka", "martinis", "orange juice", "drain-o", "sparkling water", "grog", "wine", "coffee", "beer",
              "a milkshake", "hot chocolate"]
action_list = ["arriving", "jumping", "writing a letter", "running", "laughing", "choking", "climbing", "crawling",
               "crying", "dancing", "rolling", "painting", "dreaming", "sleeping", "exercising", "reading",
               "playing kazoo", "laying down", "walking a dog", "buying a sandwich", "yelling", "creeping", "floating",
               "practising magic", "coughing", "sneezing", "filling up gas", "calling their Mom", "seeing a movie",
               "fighting a moose", "fighting a squid", "fighting a giraffe", "baking a cake", "rowing", "getting angry",
               "playing house", "shivering", "drinking " + random.choice(drink_list),
               "eating " + random.choice(food_list), "talking to " + random.choice(character_list)]
places_list = ["on a mountain", "on a plane", "on a bike", "on a cruise", "on an adventure", "on the moon",
               "on a spaceship", "on Hollywood Blvd", "on a TV show", "on a surfboard", "on a skateboard",
               "on a bike", "on a mission", "on a vacation", "on a bad day", "on Wall St.", "on the streets",
            "in Los Angeles", "in Hawaii", "in Dubai", "in Las Vegas", "in Dublin", "in England", "in China",
               "in India", "in Tokyo", "in Japan", "in the ocean", "in midair", "in a casino", "in a mall",
               "in a crisis", "in a water park", "in Disneyland", "in a Starbucks", "in McDonald's", "in IKEA",
               "in Burger King", "in a movie theater", "in the heat of the moment"]
prompt_list = ["Donald Trump on a bike", "Keanu Reeves writing a letter", "Sunflowers in the rain", "Huge soccer match"]


def compose_prompt():
    prompt_string = random.choice(character_list) + " " + random.choice(action_list) + " " + random.choice(places_list)
    return prompt_string


def compose_prompt_ai():
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Create a paragraph from this prompt: A highly detailed description of" + random.choice(character_list) +
               " in a place doing something",
        temperature=0.8,
        max_tokens=45,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    split_list = str(response.choices[0]["text"]).strip().split(".")[:-1]
    return str('. '.join(split_list))


def get_prompt(number=1):
    prompt_string = ""
    while number > 0:
        if env_openai_key is not None:
            prompt_string = prompt_string + "\"" + compose_prompt_ai() + "\", "
        else:
            prompt_string = prompt_string + "\"" + compose_prompt() + "\", "
        number -= 1
    return prompt_string
