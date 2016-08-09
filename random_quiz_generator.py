#!/usr/bin/python
# random_quiz_generator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random
from quiz_data import capitals

# Generate 35 quiz files.
for quiz_num in xrange(1,36):
	with open('capital_quiz_{}.txt'.format(quiz_num), 'w') as qf:
		qf.write('Name:\nDate:\nPeriod:\n\n')
		qf.write('{} {} (Form {})\n\n'.format(' ' * 20, 'State Capitals Quiz', quiz_num))

		# Shuffle the order of the states.
		states = list(capitals.keys())
		random.shuffle(states)

		answers = []
		for question_num in xrange(50):
			correct_answer = capitals[states[question_num]]
			wrong_answers = list(capitals.values())
			del wrong_answers[wrong_answers.index(correct_answer)]
			wrong_answers = random.sample(wrong_answers, 3)
			answer_options = wrong_answers + [correct_answer]

			random.shuffle(answer_options)

			qf.write('{}. What is capital of {}?\n' \
				.format(question_num+1, states[question_num]))

			letters = 'ABCD'
			for i in xrange(4):
				qf.write('{:>4}. {}\n'.format(letters[i], answer_options[i]))
			qf.write('\n')

			# Saving answers to all quiz-question as a list
			answer_letter = letters[answer_options.index(correct_answer)]
			answers += ['{:>2}. {}: {} - {}' \
					.format(
						question_num+1,
						answer_letter,
						states[question_num],
						correct_answer
					)]
	
	# Writes answers to file
	with open('capital_quiz_answers_{}.txt'.format(quiz_num), 'w') as af:
		af.write('{} {} (Form {})\n\n' \
			.format(' ' * 20, '[Answers] State Capitals Quiz', quiz_num))
		for answer in answers:
			af.write('{}\n'.format(answer))