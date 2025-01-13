## About
This is a local backend that predicting a word from the sentence based on a sentence context

## Run
- Navigate to the root folder and run `python app.py`
- The server will be run locally in your local machine at port 5000. (Feel free to change port number)

## Testing
- We can test with PostmanAPI
- Select `POST` method
- Navigate to `body` section
- A sample `json` could be
``` json
{
	"text": "During my internship, I collaborated with a team to develop a scalable"
}
```
- The result that we receive will be a list of 10 (we can adjust this number) words that place by its probability of how likely it would occur

## Personal Statement
- Have fun coding everyone :D