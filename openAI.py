
import json
import base64
import openai


class OpenAI:

    def __init__(self):

        # self.get_api_key(api_key_file_path)
        openai.api_key = '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'

        self.model = openai.Model.retrieve("text-davinci-003")

        self.prompt_raw = """your task is to parse an input string and turn it into a JSON object with the following information , if the input string does not create the required information then put null in the JSON. The JSON should consist of the following information:
- Age specified in query (field name: age, field type: string, possible values: [kid, teen, teen adult, adult])
- Season specified in the query (field name: season, field type: string, possible values: [summer, winter, summer winter])
- Types of outfit specified is form of list of strings (field name: type, field type: list, possible values: [ethnic, casual, formal, business casual, military, corset, floral, party-wear])
- Gender specified in query (field name: gender, field type: string, possible values: [male, female])
- Colours of outfit specified in query in form of a list of strings (field name: colour, field type: list)

In general, if certain information is not stated, set the respective field to null

This is the query:

%s

The structured JSON representation is:
```json
{"age":"""


    # def get_api_key(self, file_path):
    #     try:
    #         with open(file_path, 'r') as api_key:
    #             openai.api_key = api_key.readline()
    #     except FileNotFoundError:
    #         raise Exception(f"OpenAI API key file doesnt exist at {file_path}")


    def request(self, query):
        full_prompt = self.prompt_raw % query

        num_prompt_tokens = int(len(full_prompt) / 3) # estimate the length of the prompt
        max_tokens = 4000 - num_prompt_tokens # calculate the max available tokens for the response

        # call the OpenAI API
        response = openai.Completion.create(
            model='text-davinci-003', # the best GPT-3 model
            prompt=full_prompt,
            temperature=0,
            max_tokens=max_tokens,
            top_p=0.1,
            stop=['```'],
            echo=True # returns the whole prompt including the completion
        )

        result_raw = response.choices[0].text
        json_str = result_raw.split('```json')[1].strip() # since we used echo=True, we can split on the json marker

        return json.loads(json_str)