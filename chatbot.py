import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a personal assistant"}]

def CustomGPT(user_input):
    messages.append({"role": "user", "content":user_input})
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content":ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomGPT, inputs = "text", outputs = "text", title = "Personal assistant")

demo.launch(share=True)
