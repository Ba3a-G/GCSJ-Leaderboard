# GCSJ
A monorepo for Google Cloud Study Jams.

## Web
[Backend](/api/) is made using AWS Lambda (serverless function), DynamoDB, and API Gateway. [Frontend](/frontend/) is built with React.

Into CTFs? I have hidden three flags in the [live website](https://gcsj.gdsclpu.dev/).

PS: Please don't judge me. The APIs were initially for my own use, it became an internal tool for GDSC LPU after a while, but eventually I was asked to make it public.

*I will probably rewrite the entire thing before next year's event*.

## Scripts
### How to use?
#### Create an API key
1. To create an API key, from the Navigation menu go to **APIs & Services** > **Credentials** in the Cloud Console.
2. Click **Create Credentials** and select **API key**.
3. Copy the API key, we are gonna need it in the next step

#### Run the corresponsing script from [/scripts](/scripts/)
```bash
curl https://raw.githubusercontent.com/Ba3a-G/automate-gcsj/main/scripts/genai/challenge_lab.sh | sh -s <API_KEY>
```
> [!IMPORTANT]  
> Replace <API_KEY> with your own!

## Contributing
1. Feel free to create a PR!
2. Docs improvements are accepted too.
3. And no, this repo is _not_ Hacktoberfest accepted.
