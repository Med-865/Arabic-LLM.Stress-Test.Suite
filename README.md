# Arabic-LLM.Stress-Test.Suite
Comprehensive Stress-Test Suite for Arabic Large Language Models (LLMs)
# Arabic LLM Stress-Test Suite (ALSTS)  
A comprehensive evaluation suite designed to benchmark the performance, reasoning depth, cultural understanding, and linguistic accuracy of Large Language Models (LLMs) in Arabic.

This project provides a curated collection of multi-step prompts, computational reasoning challenges, culturally sensitive scenarios, and linguistic evaluation tasks.  
It is intended to test and benchmark models such as Gemini, Grok, and GPT across key dimensions of Arabic NLP.

---

## 🌍 Why This Project?  
Current LLMs show significant weaknesses in Arabic:  
- Shallow reasoning with multi-step prompts  
- Poor handling of technical and algorithmic terminology  
- Incorrect cultural context interpretation  
- Weak logical consistency in Arabic responses  
- Difficulty with diacritics, morphology, and sentence structure  

ALSTS provides stress-test prompts to expose these weaknesses and guide future fine-tuning efforts.

---

## 📂 Repository Structure  

# Arabic LLM Stress-Test Suite (ALSTS)  
A comprehensive evaluation suite designed to benchmark the performance, reasoning depth, cultural understanding, and linguistic accuracy of Large Language Models (LLMs) in Arabic.

This project provides a curated collection of multi-step prompts, computational reasoning challenges, culturally sensitive scenarios, and linguistic evaluation tasks.  
It is intended to test and benchmark models such as Gemini, Grok, and GPT across key dimensions of Arabic NLP.

---

## 🌍 Why This Project?  
Current LLMs show significant weaknesses in Arabic:  
- Shallow reasoning with multi-step prompts  
- Poor handling of technical and algorithmic terminology  
- Incorrect cultural context interpretation  
- Weak logical consistency in Arabic responses  
- Difficulty with diacritics, morphology, and sentence structure  

ALSTS provides stress-test prompts to expose these weaknesses and guide future fine-tuning efforts.

---

---

## 🧠 Included Prompt Categories  

### 1. Multi-Step Reasoning (سلاسل التفكير)  
Prompts requiring 3–5 explicit reasoning steps.

Example:  
```json
{  
  "prompt": "اشرح العلاقة بين الكفاءة واستخدام الذاكرة، ثم حلّل Merge Sort، ثم قدّم سيناريو هندسي حقيقي...",  
  "type": "multi_step"  
}
2. Computational Arabic (علوم الحاسوب بالعربية)

Questions designed to test algorithmic understanding in academic Arabic.

Example:{  
  "prompt": "اشرح بالتفصيل عمل خوارزمية BFS، ثم قارنها بـ DFS من حيث الذاكرة، ثم قدّم مثالاً عملياً.",  
  "type": "cs_arabic"  
}
3. Cultural Sensitivity (السياق الثقافي)

Prompts designed to test cultural awareness.

Example:{  
  "prompt": "هل عبارة 'يعطيك العافية' تُعدّ مجاملة أم نقداً في الثقافة الخليجية؟ فسّر بالتفصيل.",  
  "type": "culture"  
}
4. Logic & Math (المنطق والرياضيات)

Stress tests that expose logical hallucinations.

Example:{  
  "prompt": "إذا كان زمن تنفيذ الخوارزمية O(n log n)، فاشرح ما يعنيه ذلك لمدخلات حجمها 10 ملايين.",  
  "type": "logic_math"  
}
📊 Evaluation Methodology

We evaluate models across:

Accuracy

Reasoning Depth

Cultural Fidelity

Linguistic Precision

Technical Correctness

✨ About the Author

Created by Milad Aroumani, M.Sc. Artificial Intelligence
Specialized in:

Arabic NLP

Multi-step Prompt Engineering

Dataset Design for LLM Training

AI Safety & Evaluation
## 📂 Repository Structure  

