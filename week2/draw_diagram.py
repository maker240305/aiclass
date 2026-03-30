import matplotlib.pyplot as plt
import networkx as nx
import matplotlib as mpl
import os

# 폰트 설정
mpl.rc('font', family='Malgun Gothic')
mpl.rcParams['axes.unicode_minus'] = False

def create_diagram(output_path):
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_facecolor('#f8f9fa')

    G = nx.DiGraph()

    center = "🌟 컨셉 🌟\n\n몰입하는\n크리에이티브 아키텍트"
    node1 = "🎯 목적 1\n\n기술적 자립\n(AI/엔진 마스터)\n\n[실행]\n매일 1시간 학습"
    node2 = "🎯 목적 2\n\n포트폴리오 구축\n(인디 게임 런칭)\n\n[실행]\n학기당 1개 제작"
    node3 = "🎯 목적 3\n\n글로벌 네트워킹\n(전문가 소통)\n\n[실행]\n오픈소스/커뮤니티 활동"

    # 화살표 방향: 목적 -> 컨셉 (목적이 모여드는 느낌)
    G.add_edge(node1, center)
    G.add_edge(node2, center)
    G.add_edge(node3, center)

    # 배치
    # 컨셉이 중앙에 있고 1, 2, 3 이 삼각형 모양으로 둘러싸게 배치
    pos = {
        center: (0, 0),
        node1: (-1, 0.8),
        node2: (1, 0.8),
        node3: (0, -1)
    }

    # 화살표 그리기 (nodes는 그리지 않고 화살표만 그림)
    nx.draw_networkx_edges(
        G, pos, 
        ax=ax, 
        arrowstyle='->', 
        arrowsize=30, 
        edge_color='#6c757d', 
        width=3, 
        node_size=6000, 
        alpha=0.8,
        connectionstyle='arc3,rad=0.1'
    )

    # 스타일 설정
    bbox_center = dict(boxstyle="round4,pad=2.0", fc="#007bff", ec="#0056b3", lw=3, alpha=0.95)
    bbox_goal = dict(boxstyle="round,pad=1.5", fc="#ffffff", ec="#ced4da", lw=2, alpha=0.95)

    # 텍스트 노드 직접 그리기
    for node, (x, y) in pos.items():
        if node == center:
            ax.text(x, y, node, fontsize=16, fontweight='bold', color='white', 
                    ha='center', va='center', bbox=bbox_center, linespacing=1.6)
        else:
            ax.text(x, y, node, fontsize=13, fontweight='bold', color='#495057', 
                    ha='center', va='center', bbox=bbox_goal, linespacing=1.5)

    plt.title('대학생활 성공 로드맵 도식화', fontsize=20, fontweight='bold', pad=20, color='#343a40')
    plt.axis('off')
    plt.tight_layout()
    
    # 저장
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return output_path

if __name__ == "__main__":
    out_path = os.path.join(os.path.dirname(__file__), 'concept_diagram.png')
    create_diagram(out_path)
    print(f"Diagram created at: {out_path}")
