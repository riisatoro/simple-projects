"""
Mad Libs Generator

This is a Mad Libs generator. It will prompt the user for input and return a simple story based on the input provided.
"""


def get_prompt(word_type):
    """Get the prompt for the specified word type."""
    user_input = input(f"Enter a(n) {word_type}: ")
    return user_input


def make_story(noun1, adjective1, verb1, noun2, verb2):
    """Generate the story based on the prompts."""

    return f"""
    Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} all day.
    
    One day, {noun2} walked into the room and caught the {noun1} in the act.
    
    {noun2}: "What are you doing?!"
    {noun1}: "I'm just {verb2}. What's the big deal?"
    {noun2}: "Well, it's not every day that you see a {noun1} {verb1}ing in the middle of the day."
    {noun1}: "I suppose you're right. Maybe I should take a break."
    {noun2}: "That's a great idea. Why don't we go {verb2} instead?"
    {noun1}: "That sounds like fun!"
    """


def collect_prompts():
    """Collect the prompts for the story."""
    noun1 = get_prompt("noun 1")
    adjective1 = get_prompt("adjective 1")
    verb1 = get_prompt("verb 1")
    noun2 = get_prompt("noun 2")
    verb2 = get_prompt("verb 2")
    return noun1, adjective1, verb1, noun2, verb2


def main():
    """Run the main program."""
    noun1, adjective1, verb1, noun2, verb2 = collect_prompts()
    story = make_story(noun1, adjective1, verb1, noun2, verb2)
    print(story)


if __name__ == "__main__":
    main()
