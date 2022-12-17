import argparse
import openai
import yaml

class ChatGPT:
    def __init__(self):
        self.api_key = openai.api_key
    
    def generate_response(self, prompt):
        """
        Generates a response to the given prompt using the GPT-3 API.
        """
        response = openai.Completion.create(
            #engine="text-davinci-002",
            engine="code-davinci-002",
            prompt=prompt,
            temperature=0.2,
            max_tokens=1024,
        )
        print(response)
        return response.choices[0].text

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", required=True, help="API key for the GPT-3 API")
    parser.add_argument("--project-file", required=True, help="YAML project file")
    parser.add_argument("--training-data", required=True, help="Markdown training data file")
    args = parser.parse_args()
    
    # Set the API key for the GPT-3 API
    openai.api_key = args.api_key
    
    # Create an instance of the ChatGPT class
    chat_gpt = ChatGPT()
    
    # Read the project file
    with open(args.project_file, "r") as f:
        project = yaml.safe_load(f)

    # Read the training data file
    with open(args.training_data, "r") as f:
        training_data = f.read()

    # Create the prompts
    prompts = []
    for file in project["files"]:
        prompts.append(f"{training_data}\nFile: {file['name']}\nDescription: {file['description']}\nContents:\n")

    # Call the GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompts,
        temperature=0.5,
        max_tokens=1024,
    )

    # Parse the response
    for i, file in enumerate(project["files"]):
        filename = file["name"]
        contents = response["choices"][i]["text"]
        print(f"Writing {filename}")
        print("---")
        print(contents)
        print("---")
        #with open(os.path.join(args.output_dir, filename), "w") as f:
        #    f.write(contents)


if __name__ == "__main__":
    main()
