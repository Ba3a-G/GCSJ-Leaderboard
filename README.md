# Automating Google Cloud Study Jams
A bunch of scripts to automate Study Jams.

## How to use?
#### Create an API key
1. To create an API key, from the Navigation menu go to **APIs & Services** > **Credentials** in the Cloud Console.
2. Click **Create Credentials** and select **API key**.
3. Copy the API key, we are gonna need it in the next step

#### Run the corresponsing script from [/scripts](/scripts/)
```bash
curl https://raw.githubusercontent.com/Ba3a-G/automate-gcsj/main/genai/challenge_lab.sh | sh -s <API_KEY>
```
> [!IMPORTANT]  
> Replace <API_KEY> with your own!

## Contributing
1. Feel free to create a PR!
2. Docs improvements are accepted too.
3. And no, this repo is _not_ Hacktoberfest accepted.
