# Judge statistics on the last Programing Fundamentals exam were not working correctly,
# so you have the task of taking all the submissions and analyzing them properly. You should collect all the submissions
# and print the final results and statistics about each language in which the participants submitted their solutions.
# You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive
# "exam finished". You should store each username and their submissions and points.
# If a student has two or more submissions for the same language, save only his maximum points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned".
# In that case, you should remove the user from the contest but preserve his submissions in the total count of
# submissions for each language.
# After receiving "exam finished", print each of the participants in the following format:
# "Results:
# {username1} | {points}
# {username2} | {points}
# …
# {usernameN} | {points}"
# After that, print each language used in the exam in the following format:
# "Submissions:
# {language1} - {submissions_count}
# {language2} - {submissions_count}
# …
# {language3} - {submissions_count}"

scores = {}
languages = {}

command = input()
while command != 'exam finished':
    if command.split('-')[1] == 'banned':
        name = command.split('-')[0]
        del scores[name]
        command = input()
        continue
    name, language, score = command.split('-')
    if name not in scores:
        scores[name] = 0
    if int(score) > scores[name]:
        scores[name] = int(score)
    if language not in languages:
        languages[language] = 0
    languages[language] += 1

    command = input()

print("Results:")
for name, score in scores.items():
    print(f'{name} | {score}')
print("Submissions:")
for lang, count in languages.items():
    print(f'{lang} - {count}')
