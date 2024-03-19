import numpy as np
import networkx as nx
import operator
from openai import OpenAI
from glob import glob

# OpenAI API 키 설정 (자신의 API 키로 대체해야 함)
# apikey = "나의 키 등록하기"
# client = OpenAI(api_key=apikey)

#직무별 기술스택 그래프 불러오기
for g in glob('data/text_network/*.gml'):
    globals()[g.split('/')[-1].replace('_gpt.gml','')] = nx.read_gml(g)

def get_neighbors(target, graph):
  try:
    connected_nodes = list(graph.neighbors(target))
  except:
    connected_nodes = []

  # 연결된 노드 중에서 가중치가 높은 상위 4개 노드 출력
  if connected_nodes:
      weights = [(node, graph[target][node]['weight']) for node in connected_nodes]
      sorted_weights = sorted(weights, key=operator.itemgetter(1), reverse=True)
      return sorted_weights[:4]

  else:
      print(f"No nodes connected to '{target}'.")
      return -1

#만약 사용자 input이 graph내에 하나도 없을 경우 weight가 높은 순으로 node를 반환
def get_sorted_nodes(graph):

  edge_weights = nx.get_edge_attributes(graph, 'weight')

  # 가중치가 높은 순으로 노드 정렬
  sorted_nodes = sorted(edge_weights, key=edge_weights.get, reverse=True)

  return sorted_nodes[:10]

# # GPT-3 API 호출 함수
# def generate_text(skill):
#     response = client.chat.completions.create(model="gpt-3.5-turbo",
#     messages= [
#         {"role": "system", "content": "당신은 입력된 단어를 이용해서, 사용자에게 관련된 역량을 길러보라고 알려주는 machine입니다."},
#         {"role": "system", "content": "단어에 대한 설명은 생략하고, 짧은 문장으로만 답변을 제시하세요."},
#         {"role": "system", "content": "만약 React와 같이 기술스택과 관련한 단어를 입력받았다면, 당신의 답변은 'React 프레임워크 기술을 쌓아보세요.'와 같은 문장이어야 합니다."},
#         {"role": "system", "content": "학위와 관련된 단어를 입력받았다면, 당신의 답변은 '전문적인 지식이 요구되는 분야이니, 석사 이상의 학위 취득을 추천드립니다.'와 같은 문장이어야 합니다. "},
#         {"role": "system", "content": "경험 혹은 역량과 관련된 단어라면, 관련된 경험을 쌓아보라는 문장을 제시해야 합니다."},
#         {"role": "system", "content": "한글로 답변하세요."},
#         {"role": "user", "content" : skill}
#     ],
#     temperature=0.5)
#     return response.choices[0].message.content
