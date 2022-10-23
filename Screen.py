def draw_border():
    line_y = consts.NUM_OF_LINES_LOSE * consts.BUBBLE_RADIUS * 2 - (
            consts.NUM_OF_LINES_LOSE - 1) * consts.ROWS_OVERLAP
    pygame.draw.line(screen, consts.BORDER_COLOR, start_pos=(0, line_y),
                     end_pos=(consts.WINDOW_WIDTH, line_y))