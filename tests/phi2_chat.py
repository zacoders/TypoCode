from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# model_id = "microsoft/phi-2"
# model_id = "ai-forever/rugpt3medium_based_on_gpt2"

# model_id = "sberbank-ai/rugpt3large_based_on_gpt2"
model_id = "t-tech/T-lite-it-1.0"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    load_in_8bit=True,          # 8-бит квантование — влезает в VRAM
    device_map="auto"           # автоматически использует GPU
)


def chat(words: list[str], letters: list[str], combos: list[str]):
    prompt = f"""
        Напиши текст из 10 предложений, включай эти слова: '{', '.join(words)}', и слова в которых есть эти буквы '{', '.join(letters)}', и эти сочетания букв '{', '.join(combos)}'.
        Пиши так чтобы было ИНТЕРЕСНО, можно использовать факты, названия, новости, исторические события, и многое другое.

        Вот текст сразу соответствующий всем требованиям, с добавлением деталей и фактов:\n
    """
    # prompt = "Напиши текст на тему Танки, 10 предложений. Хорошо вот текст с учетом всех условий: "
    print('\n\n\n')
    print(prompt)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=500,
        do_sample=True,
        temperature=0.99,   # ниже = более детерминированно
        top_k=30,          # ограничивает выбор 30 наиболее вероятных токенов
        top_p=0.95         # или используйте nucleus sampling (альтернатива top_k)
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("\n💬 Сгенерировано предложение:\n", response[len(prompt):].strip())


# words = ["кошка", "прыгать", "окно", "солнце", "пейзаж", "смотреть"]
# words = ["танк", "дуло", "гусеница", "броня", "калибр", "выстрел", "пробитие"]
# words = ["программа", "код", "переменная", "класс", "цикл", "условие", "производительность"]

words = [
    "танк",
    "дуло",
    "гусеница",
    "броня",
    "калибр",
    "выстрел",
    "пробитие",
    "кошка",
    "прыгать",
    "окно",
    "солнце",
    "пейзаж",
    "смотреть",
    "программа",
    "код",
    "переменная",
    "класс",
    "цикл",
    "условие",
    "производительность"]
    
letters = ["к", "ш", 'м', 'н']
combos = ["ко", "шк", 'ст', 'нн', 'уя']

while True:
    chat(words, letters, combos)
