import sys


white_paper = []
blue_paper = []

paper_queue = []


def cutting_paper(paper, size):
    papers = (
        [line[0:size] for line in paper[0:size]],
        [line[size:] for line in paper[size:]],
        [line[size:] for line in paper[0:size]],
        [line[0:size] for line in paper[size:]]
    )

    return papers


def is_square(paper):
    color = paper[0][0]
    for line in paper:
        for x in line:
            if color != x:
                return False
    return True


def main():
    N = int(sys.stdin.readline().strip())

    paper = []
    for _ in range(N):
        line = [int(x) for x in sys.stdin.readline().strip().split()]
        paper.append(line)
    paper_queue.append(paper)

    while len(paper_queue) != 0:
        paper = paper_queue.pop()
        size = len(paper)
        if not is_square(paper) and size > 1:
            size = int(size / 2)
            papers = cutting_paper(paper, size)

            paper_queue.extend(papers)
            continue

        if paper[0][0] == 0:
            white_paper.append(paper)
        else:
            blue_paper.append(paper)

    print(len(white_paper))
    print(len(blue_paper))

main()
