from django.shortcuts import render
from django.http import HttpResponse
from .utils import *
import numpy as np
import networkx as nx
import operator
from openai import OpenAI
from glob import glob
# from .apikey import apikey

# OpenAI API 키 설정 (자신의 API 키로 대체해야 함)
# apikey = "나의 키 등록하기"
# client = OpenAI(api_key=apikey)

def index(request):
    if request.method == 'POST':
        selected_jobs = request.POST.getlist('selected_job')
        skill_set = request.POST.get('skill_set')

        #직무별 기술스택 그래프 불러오기
        for g in glob('data/text_network/*.gml'):
            print(g)
            globals()[g.split('/')[-1].replace('_gpt.gml','')] = nx.read_gml(g)
            print(g.split('/')[-1].replace('_gpt.gml',''))

        #전역변수
        graph_list = []
        for selected_job in selected_jobs:
            if selected_job == 'DBA':
                graph_list.append(DBA_graph)
            elif selected_job == '머신러닝 엔지니어':
                graph_list.append(ML_graph)
            elif selected_job == '데이터 사이언티스트':
                graph_list.append(DSC_graph)
            elif selected_job == 'BI 엔지니어':
                graph_list.append(BI_graph)
            elif selected_job == '데이터 엔지니어':
                graph_list.append(DE_graph)
            else:
                graph_list.append(BD_graph)

        output = []
        for GRAPH in graph_list:
            #주변 노드가 담길 list
            neighbor_list = []
            extracted_nodes = []

            #input의 주변 노드를 구함
            for skill in skill_set.split(','):
                tmp = get_neighbors(skill.strip().lower(), GRAPH)
            if tmp != -1:
                neighbor_list.append(tmp)

            #주변 노드를 담는 리스트가 비어있지 않으면
            if neighbor_list:
                # gpt 모델에 전달할 기술스택 리스트를 뽑는 과정
                for i in range(len(neighbor_list)):
                    for j in range(4):
                        extracted_nodes.append(neighbor_list[i][j][0])

            #사용자의 스킬이 그래프 내에 존재하지 않아서 주변 노드 리스트가 비어있는 경우
            else:
                rank = get_sorted_nodes(GRAPH)
                for i in range(len(rank)):
                    extracted_nodes.append(rank[i][0])
                    extracted_nodes.append(rank[i][1])

            # extracted_nodes에서 사용자에게 인풋으로 받은 기술스택은 추천하지 않도록 제거
            skill_set_list = [value.strip() for value in skill_set.split(',')]
            extracted_nodes = [value for value in extracted_nodes if value not in skill_set_list]
            outputs = list(set(extracted_nodes))
            
            import json

            # JSON 파일을 딕셔너리로 불러오기
            with open('advice.json', 'r', encoding='utf-8') as f:
                advice_dict = json.load(f)

            result = []
            # result.append(','.join(outputs))
            for output in outputs:
                try:
                    t =advice_dict[output]
                    result.append(t)
                except:
                    print(f'No {output}')
                    pass
            
            output = result
            # gpt_input = ",".join(list(set(extracted_nodes)))
            # #gpt 답변
            # generated_sentence = generate_text(gpt_input)
            # # 문장을 점(.)으로 나누기
            # sentences = [sentence.strip() for sentence in generated_sentence.split('.') if sentence]
            # 공백을 제거하고 문장을 다시 조립
            # output.extend(sentences)

        # output은 이제 모든 선택된 직무에 대한 결과를 담고 있습니다.
        return render(request, 'my_skill/index.html', {'output': output})

    else:
        return render(request, 'my_skill/index.html')


def show_total_graph(request):
    return render(request, 'my_skill/graph.html')