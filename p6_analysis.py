from p6_game import Simulator
import p6_tool

ANALYSIS = {}

def analyze(design):
    sim = Simulator(design)
    init = sim.get_initial_state()
    # next_state = sim.get_next_state(init, moves[0])
    # position, abilities = next_state # or None if character dies
    # i, j = position

    prev = {init: None}
    q = [init]
    while q:
        curr_state = q.pop(0)
        # print (str(curr_state[0]))

        moves = sim.get_moves()
        neighbors = []
        for move in moves:
            neighbor = sim.get_next_state(curr_state, move)
            if neighbor is not None:
                neighbors.append(neighbor)


        for next_state in neighbors:
            if next_state not in prev:
                prev[next_state] = curr_state
                q.append(next_state)

    ANALYSIS['prev'] = prev
    print('analysis complete')

def inspect((i, j), draw_line):
    # TODO: use ANALYSIS and (i,j) draw some lines
    pos = (i, j)
    prev = ANALYSIS['prev']

    # for state in points[pos]:
    #     prev_state = prev[state]
    #     curr_state = state
    #     while prev_state:
    #         draw_line(curr_state[0], prev_state[0])
    #         curr_state = prev_state
    #         prev_state = prev[prev_state]
    for state in prev:
        if state[0] == pos:
            prev_state = prev[state]
            curr_state = state
            offset = p6_tool.make_offset()
            color = p6_tool.make_color()
            while prev_state:
                draw_line(curr_state[0], prev_state[0], offset, color)
                curr_state = prev_state
                prev_state = prev[prev_state]
