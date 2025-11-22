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
---

## 📚 Usage Guide | دليل الاستخدام

### 1️⃣ إعداد البيئة

1. تأكد من تثبيت المتطلبات:

```bash
pip install -r requirements.txt
تأكد من وجود ملفات الاختبار في المجلد:
tests/
  ├─ multistep_reasoning.jsonl
  ├─ arabic_dialect_understanding.jsonl
  ├─ logic_and_math.jsonl
  └─ cultural_sensitivity.jsonl
2️⃣ منهجية التقييم (Evaluation Methodology)

يعتمد نظام التقييم في ALSTS على النقاط التالية:

كل عنصر اختبار يحتوي على:

prompt: السؤال أو المهمة المعطاة للنموذج

ideal_answer: إجابة مرجعية مثالية (Ground Truth)

آلية التقييم الأساسية:

يتم إرسال prompt إلى النموذج (GPT / Llama / Grok / Gemini…)

يُقارن مخرج النموذج بالنص المرجعي في ideal_answer

يتم إعطاء:

score = 1 إذا كان المخرج يحتوي على جوهر الإجابة المرجعية

score = 0 إذا كان بعيداً عنها أو خاطئاً

✅ في النسخة الحالية تم استخدام مقياس مبسط (string match / pattern match)،
ويمكن مستقبلاً استبداله بمقياس أكثر دقة (مثلاً: semantic similarity / grading LLM).

حساب النتائج:

يتم حساب متوسط الدرجات لكل فئة:

Multi-step reasoning

Dialects

Logic & Math

Cultural

ثم يُحسب متوسط عام (Overall ALSTS Score) بين 0 و 1، ويمكن تحويله إلى نسبة مئوية (%).
| Category   | Mean Score |
| ---------- | ---------: |
| multistep  |       0.75 |
| dialects   |       0.60 |
| logic_math |       0.55 |
| cultural   |       0.90 |

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
3️⃣ مثال على مخرجات التقييم (Sample Output)

عند تشغيل سكربت التقييم، قد تحصل على مخرجات مثل:
Loaded 4 test suites.
Running evaluation using: GPT-4o-mini (via API)
---------------------------------------------
Category: multistep        | Mean score: 0.78
Category: dialects         | Mean score: 0.65
Category: logic_math       | Mean score: 0.59
Category: cultural         | Mean score: 0.88
---------------------------------------------
Overall ALSTS Score: 0.72 (72%)
Results saved to: results/results_2025-11-22_16-40.csv
يمكنك بعد ذلك استخدام سكربت عرض النتائج (Dashboard) لرؤية النتائج بشكل رسومي.

---

## ثانياً: سكربت أتمتة التقييم  
📄 ملف جديد: `scripts/run_evaluation.py`

1. في GitHub اضغط: **Add file → Create new file**  
2. اسم الملف:

```text
scripts/run_evaluation.py
import json
import os
from datetime import datetime

import pandas as pd

# --------- الإعدادات الأساسية ---------

TEST_DIR = "tests"
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

# هنا تقدر تغيّر اسم النموذج المستخدمة فعلياً
MODEL_NAME = "MockModel"  # مثال: "GPT-4o-mini" أو "Llama-3-8B"


# --------- تحميل ملفات الاختبار ---------

def load_jsonl(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line.strip()))
    return data


def load_all_tests():
    tests = {}
    for filename in os.listdir(TEST_DIR):
        if filename.endswith(".jsonl"):
            key = filename.replace(".jsonl", "")
            tests[key] = load_jsonl(os.path.join(TEST_DIR, filename))
    return tests


# --------- دالة النموذج (استبدلها بالـ API الحقيقي) ---------

def mock_model(prompt: str) -> str:
    """
    دالة نموذج وهمي للاختبار.
    هنا تستبدلها لاحقاً بنداء فعلي إلى API مثل:
    - OpenAI GPT
    - Grok
    - Gemini
    - Llama
    """
    return "Mocked answer – replace this with real model output."


model = mock_model


# --------- دالة التقييم ---------

def score_answer(model_output: str, ideal_answer: str) -> float:
    """
    مقياس بسيط جداً:
    - إذا احتوى مخرج النموذج على أول 15 حرفاً من الإجابة المرجعية => 1
    - غير ذلك => 0
    يمكن تطوير هذا لاحقاً ليصبح أكثر ذكاءً.
    """
    model_output = (model_output or "").lower()
    ideal_answer = (ideal_answer or "").lower()
    if ideal_answer[:15] and ideal_answer[:15] in model_output:
        return 1.0
    return 0.0


def run_evaluation():
    print(f"Loading tests from: {TEST_DIR}")
    tests = load_all_tests()
    print(f"Loaded {len(tests)} test suites: {list(tests.keys())}")

    results = []

    for category, items in tests.items():
        print(f"\nRunning category: {category} ({len(items)} items)")
        for item in items:
            prompt = item.get("prompt", "")
            ideal = item.get("ideal_answer", "")
            output = model(prompt)
            s = score_answer(output, ideal)
            results.append(
                {
                    "model": MODEL_NAME,
                    "category": category,
                    "prompt": prompt,
                    "ideal_answer": ideal,
                    "output": output,
                    "score": s,
                }
            )

    df = pd.DataFrame(results)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    out_path = os.path.join(RESULTS_DIR, f"results_{MODEL_NAME}_{timestamp}.csv")
    df.to_csv(out_path, index=False, encoding="utf-8-sig")

    print("\n---------------------------------------------")
    print(f"Saved raw results to: {out_path}")

    summary = df.groupby("category")["score"].mean().reset_index()
    overall = df["score"].mean() if len(df) else 0.0

    print("\nCategory scores:")
    for _, row in summary.iterrows():
        print(f"  {row['category']:<25} => {row['score']:.2f}")

    print("\nOverall ALSTS Score:", f"{overall:.2f} ({overall*100:.0f}%)")

    return df, summary, overall


if __name__ == "__main__":
    run_evaluation()
بعدين من التيرمنال :
python scripts/run_evaluation.py

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
---

## 🛣 Roadmap | التوسع المستقبلي

### 1️⃣ توسيع مجالات الضغط (Stress Domains)
- إضافة اختبارات **السياق الطويل** (Long Context) لنصوص تتجاوز 4K–32K tokens.
- توسيع مجموعة اختبارات **الرياضيات المتقدمة** (Calculus, Probability, Discrete Math).
- إضافة سيناريوهات **Coding + Arabic Explanation** لاختبار الجمع بين الكود والشرح العربي.

### 2️⃣ دعم النماذج متعددة اللغات (Multilingual Models)
- إضافة ملفات اختبار موازية بالعربية + الإنجليزية لقياس الاتساق عبر اللغات.
- اختبار أداء نماذج مثل: Gemini, GPT, Llama في سيناريوهات ترجمة/مزج لغوي (Code-Switching).

### 3️⃣ معيار قياسي موحّد للنتائج (Standardized Benchmark)
- تعريف **ALSTS Score** كمعيار قياسي (0–100) يمكن مقارنته بين النماذج.
- إضافة ملفات `benchmark_config.json` لتوحيد إعدادات الاختبار.
- نشر نتائج دورية (Leaderboard) لنماذج مختلفة على GitHub.
