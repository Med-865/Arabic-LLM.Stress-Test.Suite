# Arabic LLM Stress-Test Suite (ALSTS)
**Comprehensive Benchmarking for Arabic NLP Performance in Large Language Models (LLMs)**  
**منظومة شاملة لاختبار وإجهاد نماذج الذكاء الاصطناعي في اللغة العربية**

---

## 🌍 Overview | نظرة عامة

تواجه النماذج اللغوية الكبرى (LLMs) صعوبات حقيقية عند التعامل مع اللغة العربية، خاصةً في:
- تعدد اللهجات  
- اختلاف السياقات الثقافية  
- المصطلحات التقنية  
- الاستدلال متعدد الخطوات  
- المنطق والرياضيات  
- النصوص الطويلة  

ولذلك، تم إنشاء **ALSTS** كأول مشروع مفتوح المصدر يقدّم اختبارات لأداء النماذج باللغة العربية عبر عدة محاور.

---

# 📦 Features | المزايا

## 1. Multi-Step Reasoning  
اختبارات عقلانية تتطلب 3–5 خطوات.

## 2. Computational Arabic  
اختبارات علوم الحاسوب بالعربية الأكاديمية.

## 3. Cultural Sensitivity  
اختبارات الحساسية للسياق العربي (خليجي – مصري – شامي…).

## 4. Logic & Math  
أسئلة منطق ورياضيات لكشف الهلوسة الحسابية.

## 5. Long-Text Handling  
اختبارات معالجة النصوص الطويلة.

---

# 📝 Example Tests | أمثلة اختبارات

### 1. فهم اللهجة المصرية
**Prompt:**  
"ما معنى جملة (إنت هتفضل تعمللي فيها من بنها؟) واشرح السياق."

### 2. النصوص الطويلة
"اقرأ النص (800 كلمة)، ثم لخصه، ثم استخرج الأفكار، ثم اقترح 3 أسئلة تحليلية."

### 3. الخوارزميات
"اشرح BFS بالعربية الأكاديمية، ثم قارن بـ DFS من حيث الذاكرة."

### 4. الحساسية الثقافية الخليجية
"هل عبارة (الله يقطعك) مزحة أم إساءة في الثقافة الكويتية؟ متى تُستخدم؟"

---

# 📂 Repository Structure | هيكلة المشروع

Arabic-LLM-Stress-Test-Suite/
│
├── prompts/
│ ├── multi_step_reasoning.jsonl
│ ├── computational_arabic.jsonl
│ ├── cultural_sensitivity.jsonl
│ └── logic_and_math.jsonl
│
├── evaluations/
│ ├── gemini_results.md
│ ├── grok_results.md
│ └── chatgpt_results.md
│
├── notebooks/
│ └── evaluation_pipeline.ipynb
│
└── requirements.txt


---

# ▶️ How to Run | التشغيل

## 1. Install Requirements
pip install -r requirements.txt

## 2. Run the Evaluation Notebook
افتح:
notebooks/evaluation_pipeline.ipynb

يقوم بـ:
- تحميل JSONL  
- تشغيل النموذج  
- استخراج النتائج  
- تخزين التقييم  

---

# 📊 Initial Results | النتائج الأولية

| Model | Accuracy | Reasoning | Culture | Math |
|-------|----------|-----------|--------|-------|
| GPT-4o-mini | 82% | جيد | ممتاز | جيد |
| Gemini 1.5 Flash | 77% | متوسط | ممتاز | متوسط |
| Grok 2 | 63% | ضعيف | ضعيف | ضعيف |
| Llama 3 8B | 55% | ضعيف | متوسط | ضعيف |

---

# ✨ Author | المؤلف  
**Milad Aroumani – M.Sc. Artificial Intelligence**  
Specialized in:  
- Arabic NLP  
- Prompt Engineering  
- AI Evaluation  
- LLM Training  

📧 Email: mr.uefa@gmail.com  
🔗 GitHub: https://github.com/Med-865
transformers
datasets
pandas
numpy
jupyter
accelerate
torch
multi_step_reasoning.jsonl
computational_arabic.jsonl
{"prompt": "اشرح مفهوم Big O، ثم طبّقه على البحث الثنائي، ثم أعط مثالاً.", "difficulty": "hard"}
{"prompt": "حلّل Merge Sort، ثم وضّح لماذا تحتاج مساحة إضافية.", "difficulty": "hard"}
{"prompt": "اشرح العلاقة بين الكفاءة والذاكرة، ثم طبّقها على DFS وBFS.", "difficulty": "hard"}
{"prompt": "اشرح خوارزمية BFS بالعربية الأكاديمية.", "category": "cs"}
{"prompt": "قارن بين Stack وQueue بمثال برمجي.", "category": "cs"}
{"prompt": "حلل التعقيد الزمني لـ QuickSort.", "category": "cs"}
{"prompt": "هل كلمة (ثقل دم) مجاملة أم إهانة في الثقافة المصرية؟", "category": "culture"}
{"prompt": "ما معنى (عسى ما شر) في الثقافة الكويتية؟", "category": "culture"}
{"prompt": "هل عبارة (شو بدك؟) عدوانية في الشام؟", "category": "culture"}
gemini_results.md
# Gemini Evaluation Results
Gemini 1.5 Flash tested on 20 prompts.

- Multi-step reasoning: متوسط  
- Culture: ممتاز  
- Math: متوسط  
- Logic: جيد  
grok_results.md
# Grok Evaluation Results
Grok 2 tested on 20 prompts.

- Reasoning: ضعيف  
- Culture: ضعيف  
- Math: ضعيف جداً  
chatgpt_results.md
# ChatGPT Evaluation Results
GPT-4o-mini tested on 20 prompts.

- Reasoning: جيد  
- Culture: ممتاز  
- Math: جيد  


import json
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "meta-llama/Llama-3-8B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)

def run_prompt(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

with open("../prompts/multi_step_reasoning.jsonl", "r", encoding="utf-8") as f:
    lines = f.readlines()

for l in lines:
    data = json.loads(l)
    print("PROMPT:", data["prompt"])
    print("RESPONSE:", run_prompt(data["prompt"]))
    print("-----")
