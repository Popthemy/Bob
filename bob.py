"""Bob's lackadaisical response"""


def response(hey_bob):
    """Bob only ever answers one of five things:

    "Sure." This is his response if you ask him a question, such as "How are you?"
    The convention used for questions is that it ends with a question mark.

    "Whoa, chill out!" This is his answer if you YELL AT HIM.
    The convention used for yelling is ALL CAPITAL LETTERS.

    "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.

    "Fine. Be that way!" This is how he responds to silence.
    The convention used for silence is nothing, or various combinations of whitespace characters.

    "Whatever." This is what he answers to anything else."""

    stripped, block = hey_bob.strip(), hey_bob.upper()

    # 4. "Fine. Be that way!" This is how he responds to silence.
    # The convention used for silence is nothing, or various combinations of whitespace characters.
    if len(stripped) == 0:
        return "Fine. Be that way!"

    # 3. "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
    if hey_bob.isupper() == True and stripped[(len(stripped)) - 1] == "?":
        return "Calm down, I know what I'm doing!"

    # 1. "Sure." This is his response if you ask him a question, such as "How are you?"
    #     The convention used for questions is that it ends with a question mark.
    if  stripped[(len(stripped)) - 1] == "?":
        return "Sure."



    # 2. "Whoa, chill out!" This is his answer if you YELL AT HIM.
    # The convention used for yelling is ALL CAPITAL LETTERS.
    if hey_bob.isupper() == True:
        return "Whoa, chill out!"

    # 5. "Whatever." This is what he answers to anything else.
    return "Whatever."


print(response("Okay if like my  spacebar  quite a bit?   ")) # sure

# correction

def response(hey_bob):
    hey_bob_stripped = hey_bob.strip()

    # 4. "Fine. Be that way!" This is how he responds to silence.
    if not hey_bob_stripped:
        return "Fine. Be that way!"

    # 3. "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
    if hey_bob.isupper() and hey_bob_stripped.endswith("?"):
        return "Calm down, I know what I'm doing."

    # 1. "Sure." This is his response if you ask him a question, such as "How are you?"
    if hey_bob_stripped.endswith("?"):
        return "Sure."

    # 2. "Whoa, chill out!" This is his answer if you YELL AT HIM.
    if hey_bob.isupper():
        return "Whoa, chill out!"

    # 5. "Whatever." This is what he answers to anything else.
    return "Whatever."

print(response("Okay if like my  spacebar  quite a bit?   "))  # Output: Sure.