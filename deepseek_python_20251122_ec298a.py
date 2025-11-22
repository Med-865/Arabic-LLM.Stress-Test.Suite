"""
Test Runner - منفذ اختبارات الإجهاد
"""

import asyncio
import json
from typing import Dict, List, Any
from pathlib import Path

class TestRunner:
    def __init__(self, model_api=None):
        self.model_api = model_api
        self.base_path = Path("tests")
    
    async def run_category_tests(self, category: str) -> Dict[str, Any]:
        """تشغيل جميع اختبارات فئة محددة"""
        
        category_path = self.base_path / category
        if not category_path.exists():
            return {"error": f"فئة غير موجودة: {category}"}
        
        results = {}
        
        # العثور على جميع ملفات الاختبار في الفئة
        test_files = list(category_path.glob("*.json"))
        
        for test_file in test_files:
            test_name = test_file.stem
            test_data = self._load_test_file(test_file)
            
            if test_data:
                test_result = await self._execute_test(test_data)
                results[test_name] = test_result
        
        return results
    
    def _load_test_file(self, file_path: Path) -> Dict:
        """تحميل ملف الاختبار"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ خطأ في تحميل ملف {file_path}: {e}")
            return None
    
    async def _execute_test(self, test_data: Dict) -> Dict[str, Any]:
        """تنفيذ اختبار فردي"""
        
        test_type = test_data.get('type', 'qa')
        questions = test_data.get('questions', [])
        
        test_results = {
            'test_type': test_type,
            'total_questions': len(questions),
            'passed_questions': 0,
            'details': []
        }
        
        for i, qa in enumerate(questions):
            question = qa.get('question', '')
            expected = qa.get('expected', '')
            difficulty = qa.get('difficulty', 'medium')
            
            # محاكاة استدعاء النموذج (ستحتاج لتعديل هذا الجزء)
            model_response = await self._call_model(question)
            
            # تقييم الإجابة
            is_correct = self._evaluate_response(model_response, expected, test_type)
            
            result_detail = {
                'question': question,
                'expected': expected,
                'actual': model_response,
                'is_correct': is_correct,
                'difficulty': difficulty
            }
            
            if is_correct:
                test_results['passed_questions'] += 1
            
            test_results['details'].append(result_detail)
        
        test_results['score'] = (test_results['passed_questions'] / test_results['total_questions']) * 100
        
        return test_results
    
    async def _call_model(self, question: str) -> str:
        """استدعاء النموذج (محاكاة حالياً)"""
        # TODO: استبدل هذا بالاستدعاء الفعلي للنموذج
        await asyncio.sleep(0.1)  # محاكاة الانتظار
        
        # محاكاة إجابات عشوائية للاختبار
        responses = [
            "أعتذر، لا أملك معلومات كافية للإجابة على هذا السؤال.",
            "هذا سؤال مثير للاهتمام. بناءً على معرفتي...",
            "الإجابة الصحيحة هي...",
            "لا يمكنني تقديم إجابة دقيقة على هذا السؤال.",
            "هذا يتطلب تحليلاً更深...",
            question[::-1]  # إجابة خاطئة عشوائية
        ]
        
        import random
        return random.choice(responses)
    
    def _evaluate_response(self, actual: str, expected: str, test_type: str) -> bool:
        """تقييم استجابة النموذج"""
        # محاكاة التقييم - ستطور هذا لاحقاً
        return len(actual) > 10  # معيار بسيط للاختبار