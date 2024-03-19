from django.db import models


## 'Gonggo.csv'
class Gonggo(models.Model):
    ## 공고명
    title = models.CharField(max_length=100, blank=True, null=True)

    ## 직무
    main_category = models.CharField(max_length=100, blank=True, null=True)

    ## 유사 직무
    sub_category = models.TextField(null=True)

    ## 업종
    industry = models.CharField(max_length=50, blank=True, null=True)

    ## 회사명
    company_names = models.CharField(max_length=50, blank=True, null=True)

    ## 주요업무
    main_tasks = models.TextField(null=True)

    ## 자격요건
    qualifications = models.TextField(null=True)

    ## 우대사항
    treatment = models.TextField(null=True)

    ## label_ratios
    label_ratios = models.TextField(null=True)

    class Meta:
        db_table = 'gonggos'
