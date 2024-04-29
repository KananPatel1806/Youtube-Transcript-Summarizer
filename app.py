from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from IPython.display import YouTubeVideo

app = Flask(__name__)

@app.get('/summary')
def summary_api():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    YouTubeVideo(video_id)
    YouTubeTranscriptApi.get_transcript(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    result = ""
    for i in transcript:
        result += ' ' + i['text']
    summarizer = pipeline('summarization')
    num_iters = int(len(result)/1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        print("input text \n" + result[start:end])
        out = summarizer(result[start:end])
        out = out[0]
        out = out['summary_text']
        print("Summarized text\n"+out)
        summarized_text.append(out)
    return summarized_text, 200

#     summary = get_summary(get_transcript(video_id))
#     return summary, 200

# def get_transcript(video_id):
#     transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
#     transcript = ' '.join([d['text'] for d in transcript_list])
#     return transcript

# def get_summary(transcript):
#     summariser = pipeline('summarization')
#     summary = ''
#     for i in range(0, (len(transcript)//1000)+1):
#         summary_text = summariser(transcript[i*1000:(i+1)*1000])[0]['summary_text']
#         summary = summary + summary_text + ' '
#     return summary
@app.get('/translate')
def translate():
    url = request.args.get('url', '')
    video_id1 = url.split('=')[1]
    YouTubeVideo(video_id1)
    YouTubeTranscriptApi.get_transcript(video_id1)
    transcript = YouTubeTranscriptApi.get_transcript(video_id1)
    result = ""
    for i in transcript:
        result += ' ' + i['text']
    summarizer = pipeline('summarization')
    num_iters = int(len(result)/1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        print("input text \n" + result[start:end])
        out = summarizer(result[start:end])
        out = out[0]
        out = out['summary_text']
        print("Summarized text\n"+out)
        summarized_text.append(out)
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt") 
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")
    model_inputs = tokenizer(summarized_text, return_tensors="pt")
    generated_tokens = model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"])
    translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return translation

#gujarati
# @app.get('/translate1')
# def translate1():
#     url = request.args.get('url', '')
#     video_id1 = url.split('=')[1]
#     YouTubeVideo(video_id1)
#     YouTubeTranscriptApi.get_transcript(video_id1)
#     transcript = YouTubeTranscriptApi.get_transcript(video_id1)
#     result = ""
#     for i in transcript:
#         result += ' ' + i['text']
#     summarizer = pipeline('summarization')
#     num_iters = int(len(result)/1000)
#     summarized_text = []
#     for i in range(0, num_iters + 1):
#         start = 0
#         start = i * 1000
#         end = (i + 1) * 1000
#         print("input text \n" + result[start:end])
#         out = summarizer(result[start:end])
#         out = out[0]
#         out = out['summary_text']
#         print("Summarized text\n"+out)
#         summarized_text.append(out)
#     model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt") 
#     tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")
#     model_inputs = tokenizer(summarized_text, return_tensors="pt")
#     generated_tokens = model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["gu_IN"])
#     translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
#     ls=[]
#     for i in translation:
#         ls.append(i)
#         return i

#tamil
@app.get('/translate2')
def translate2():
    url = request.args.get('url', '')
    video_id1 = url.split('=')[1]
    YouTubeVideo(video_id1)
    YouTubeTranscriptApi.get_transcript(video_id1)
    transcript = YouTubeTranscriptApi.get_transcript(video_id1)
    result = ""
    for i in transcript:
        result += ' ' + i['text']
    summarizer = pipeline('summarization')
    num_iters = int(len(result)/1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        print("input text \n" + result[start:end])
        out = summarizer(result[start:end])
        out = out[0]
        out = out['summary_text']
        print("Summarized text\n"+out)
        summarized_text.append(out)
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt") 
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")
    model_inputs = tokenizer(summarized_text, return_tensors="pt")
    generated_tokens = model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["ta_IN"])
    translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    ls=[]
    for i in translation:
        ls.append(i)
        return i

#for telgu
@app.get('/translate3')
def translate3():
    url = request.args.get('url', '')
    video_id1 = url.split('=')[1]
    YouTubeVideo(video_id1)
    YouTubeTranscriptApi.get_transcript(video_id1)
    transcript = YouTubeTranscriptApi.get_transcript(video_id1)
    result = ""
    for i in transcript:
        result += ' ' + i['text']
    summarizer = pipeline('summarization')
    num_iters = int(len(result)/1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        print("input text \n" + result[start:end])
        out = summarizer(result[start:end])
        out = out[0]
        out = out['summary_text']
        print("Summarized text\n"+out)
        summarized_text.append(out)
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt") 
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")
    model_inputs = tokenizer(summarized_text, return_tensors="pt")
    generated_tokens = model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["te_IN"])
    translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    ls=[]
    for i in translation:
        ls.append(i)
        return i

#french
@app.get('/translate4')
def translate4():
    url = request.args.get('url', '')
    video_id1 = url.split('=')[1]
    YouTubeVideo(video_id1)
    YouTubeTranscriptApi.get_transcript(video_id1)
    transcript = YouTubeTranscriptApi.get_transcript(video_id1)
    result = ""
    for i in transcript:
        result += ' ' + i['text']
    summarizer = pipeline('summarization')
    num_iters = int(len(result)/1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = 0
        start = i * 1000
        end = (i + 1) * 1000
        print("input text \n" + result[start:end])
        out = summarizer(result[start:end])
        out = out[0]
        out = out['summary_text']
        print("Summarized text\n"+out)
        summarized_text.append(out)
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt") 
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")
    model_inputs = tokenizer(summarized_text, return_tensors="pt")
    generated_tokens = model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["fr_XX"])
    translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    ls=[]
    for i in translation:
        ls.append(i)
        return i



if __name__ == '__main__':
    app.run()