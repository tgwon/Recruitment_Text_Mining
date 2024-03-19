import csv
import os, sys
import django


## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stat_wanted.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

def csv_to_db(django_model):
	# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stat_wanted.settings")
	# django.setup() 
	csv_path = './recruit/data/Gonggo.csv'
	with open(csv_path, newline='') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
			## 공고명,직무,유사 직무,업종,회사명,주요업무,자격요건,우대사항,label_ratios
			django_model.objects.create(
				title = row['공고명'],
                main_category = row['직무'],
                ## 유사 직무
                sub_category = row['유사 직무'],
                ## 업종
                industry = row['업종'],
                ## 회사명
                company_names = row['회사명'],
                ## 주요업무
                main_tasks = row['주요업무'],
                ## 자격요건
                qualifications = row['자격요건'],
                ## 우대사항
                treatment = row['우대사항'],
                ## label_ratios
                label_ratios = row['label_ratios'],
			)

from recruit.models import *
csv_to_db(Gonggo)