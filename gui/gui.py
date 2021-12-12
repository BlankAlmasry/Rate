from PyInquirer import prompt


class GUI:

    @staticmethod
    def questions(supported_readers, supported_writers, supported_algorithms):
        questions = [
            {
                'type': 'input',
                'name': 'file',
                'message': f'Path to file with matches ({", ".join(supported_readers)}):',
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
                'choices': supported_algorithms
            },
            {
                'type': 'list',
                'name': 'output_format',
                'message': 'Output format:',
                'choices': supported_writers,
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
        return questions

    @staticmethod
    def display(supported_readers, supported_writers, supported_algorithms):
        return prompt(GUI.questions(supported_readers, supported_writers, supported_algorithms))
