import sys
from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple


def search(edges: List[Tuple[str, str]]):
    # preprocess edges. result is a dict where each node has a list of next nodes reachable from it.
    connections: Dict[str, List[str]] = defaultdict(list)
    for node_a, node_b in edges:
        connections[node_a].append(node_b)
        connections[node_b].append(node_a)

    # maps nodes to boolean - are they big or small
    is_big = {}
    for node in connections:
        is_big[node] = node.upper() == node

    # List of nodes to visit. Each is  (node, seen, small_visited_twice, path)
    # seen is set of nodes
    # path is list of nodes in order of visit
    q = deque()
    q.append(("start", {"start"}, False, ["start"]))

    full_paths: Set[Tuple] = set()
    while q:
        node, seen, small_visited_twice, path = q.popleft()
        # print("  process:  ", node, seen, path)
        next_nodes = connections[node]

        for next_node in next_nodes:
            next_small_visited_twice = small_visited_twice
            if next_node == "end":
                # print("  path:  ", path, next_node)
                full_paths.add(tuple([*path, next_node]))
                continue
            if not is_big[next_node] and next_node in seen:
                if small_visited_twice or next_node == "start":
                    continue
                else:
                    next_small_visited_twice = True

            q.append((next_node, seen | {next_node}, next_small_visited_twice, [*path, next_node]))

    return full_paths


def main():
    edges: List[Tuple[str, str]] = []
    for line in sys.stdin.readlines():
        edge = tuple(line.strip().split("-"))
        assert len(edge) == 2
        edges.append(edge)

    paths = search(edges)

    print("-" * 50)
    for path in sorted(paths):
        print(path)

    print("-" * 50)
    print(len(paths))


if __name__ == "__main__":
    main()
