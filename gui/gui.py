from PyInquirer import prompt


class GUI:
    questions = [
        {
            'type': 'input',
            'name': 'file',
            'message': 'Path to file with matches (csv or json):',
        },
        {
            'type': 'input',
            'name': 'player_a_index',
            'message': 'First Player Key: (assuming first column is 0, second 1, etc.)',
        },
        {
            'type': 'input',
            'name': 'player_b_index',
            'message': 'Second Player Key: (assuming first column is 0, second 1, etc.)',
        },
        {
            'type': 'input',
            'name': 'result_a_index',
            'message': 'Result for player A: (assuming first column is 0, second 1, etc.)',
        },
        {
            'type': 'list',
            'name': 'algorithm_name',
            'message': 'Algorithm you want to use to rate the matches:',
            'choices': ['elo', 'glicko-2'],
        },
        {
            'type': 'list',
            'name': 'output_format',
            'message': 'Output format:',
            'choices': ['csv', 'json'],
        },
        {
            'type': 'input',
            'name': 'result_win',
            'message': 'Result for a win:(how would a win is typed in the result column)',
        },
        {
            'type': 'input',
            'name': 'result_loss',
            'message': 'Result for a loss:(how would a loss is typed in the result column)',
        },
        {
            'type': 'input',
            'name': 'result_draw',
            'message': 'Result for a draw:(how would a win is typed in the result column)',
        },
    ]

    @staticmethod
    def display():
        return prompt(GUI.questions)
