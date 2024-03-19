import json
from django.shortcuts import render, redirect
from .predict import *
from recruit.models import Gonggo


def index(request):
    if request.method == 'POST':
        sentences = []
        for key, value in request.POST.items():
            if key.startswith('sentence'):
                sentences.append(value)

        new_data_clusters = predict_clusters(sentences)  # 예측된 클러스터를 가져오는 함수 호출

        clusters = {} 
        for i in new_data_clusters:
            clusters[i] = []

        result = []
        for i in range(len(sentences)):
            sentence = sentences[i]
            predicted_cluster = new_data_clusters[i]  # 해당 문장의 예측 클러스터
            result.append({'sentence': sentence, 'predicted_cluster': predicted_cluster})
            clusters[predicted_cluster].append(sentence)

        # clusters = json.dumps(clusters)
        # 각 클러스터에 대한 설명 작성
        cluster_descriptions = {
            0: "통계 및 연구와 관련된 클러스터입니다.",
            1: "데이터베이스와 관련된 클러스터입니다.",
            2: "백엔드 프로그래밍과 관련된 클러스터입니다.",
            3: "프로젝트 문제 해결과 관련된 클러스터입니다."
        }
        
        cluster_info = []
        for i in range(4):
            try:
                cluster_info.append({'cluster': i, 'description': cluster_descriptions[i], 'sentences': clusters[i]})
            except:
                pass


        cluster_data_dict, selected_job = get_cluster_job_ratios(new_data_clusters)  # 클러스터별 직무 비율 데이터 가져오기

        print(result)
        # cluster_data와 overall_ratios를 JSON 형태로 변환합니다.
        cluster_data = json.dumps(cluster_data_dict['cluster_data'])
        overall_ratios = json.dumps(cluster_data_dict['overall_ratios'])

        new_data_clusters = cluster_data_dict['cluster_data']
        output = get_cluster_keywords(sentences, selected_job, new_data_clusters)

        return render(request, 'my_page/result.html', {'cluster_info': cluster_info, 'result': result, 'clusters':clusters, 'output': output, 'cluster_data': cluster_data, 'overall_ratios': overall_ratios})

    return render(request, 'my_page/input_sentence.html')


def go_to_most_similar_job(request):
    predicted_clusters = request.GET.getlist('predictedClusters')

    similar_index = my_gonggo(predicted_clusters)
    similar_jobs = Gonggo.objects.filter(id__in=similar_index)

    return render(request, 'my_page/my_gonggo.html', {'similar_jobs': similar_jobs}) 
