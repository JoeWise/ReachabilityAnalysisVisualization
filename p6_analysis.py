from p6_game import Simulator

ANALYSIS = {}

def analyze(design):
    sim = Simulator(design)
    init = sim.get_initial_state()
    moves = sim.get_moves()
    # next_state = sim.get_next_state(init, moves[0])
    # position, abilities = next_state # or None if character dies
    # i, j = position

    ANALYSIS[init] = None
    q = [init]
    while q:
        node = q.pop()

        neighbors = [sim.get_next_state(node, move) for move in moves]
        for next_node in neighbors:
            if next_node not in ANALYSIS:
                ANALYSIS[next_node] = node
                q.append(next_node)

def inspect((i,j), draw_line):
    # TODO: use ANALYSIS and (i,j) draw some lines
    raise NotImplementedError