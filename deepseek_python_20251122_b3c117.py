#!/usr/bin/env python3
"""
Arabic LLM Stress Test Suite - Main Evaluator
المقيّم الرئيسي لاختبار إجهاد النماذج اللغوية العربية
"""

import json
import asyncio
import argparse
from typing import Dict, List, Any
from pathlib import Path

from test_runner import TestRunner
from results_analyzer import ResultsAnalyzer
from utils.data_loader import DataLoader
from utils.report_generator import ReportGenerator

class StressTestEvaluator:
    def __init__(self, model_api=None):
        self.model_api = model_api
        self.test_runner = TestRunner(model_api)
        self.analyzer = ResultsAnalyzer()
        self.reporter = ReportGenerator()
        
    async def evaluate_model(self, model_name: str, test_categories: List[str] = None):
        """تقييم نموذج على فئات الاختبار المحددة"""
        
        if test_categories is None:
            test_categories = ['cognitive', 'linguistic', 'cultural', 'reasoning']
        
        print(f"🔍 بدء تقييم النموذج: {model_name}")
        print(f"📂 فئات الاختبار: {', '.join(test_categories)}")
        
        results = {}
        
        for category in test_categories:
            print(f"\n📁 جاري اختبار فئة: {category}")
            category_results = await self.test_runner.run_category_tests(category)
            results[category] = category_results
            
            # عرض النتائج الأولية
            self._print_category_summary(category, category_results)
        
        # تحليل النتائج
        analysis = self.analyzer.analyze_results(results)
        
        # إنشاء التقرير
        report = self.reporter.generate_report(model_name, results, analysis)
        
        return report
    
    def _print_category_summary(self, category: str, results: Dict):
        """عرض ملخص لفئة الاختبار"""
        total_tests = len(results)
        passed_tests = sum(1 for r in results.values() if r.get('passed', False))
        
        print(f"   ✅ نجح: {passed_tests}/{total_tests}")
        print(f"   📊 نسبة النجاح: {(passed_tests/total_tests)*100:.1f}%")

async def main():
    parser = argparse.ArgumentParser(description='Arabic LLM Stress Test Suite')
    parser.add_argument('--model', type=str, required=True, help='اسم النموذج المراد تقييمه')
    parser.add_argument('--categories', nargs='+', help='فئات الاختبار')
    parser.add_argument('--output', type=str, default='results', help='مجلد حفظ النتائج')
    
    args = parser.parse_args()
    
    # إنشاء المقيّم
    evaluator = StressTestEvaluator()
    
    # بدء التقييم
    report = await evaluator.evaluate_model(args.model, args.categories)
    
    # حفظ النتائج
    output_file = Path(args.output) / f"{args.model}_report.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n🎯 تم حفظ التقرير في: {output_file}")

if __name__ == "__main__":
    asyncio.run(main())