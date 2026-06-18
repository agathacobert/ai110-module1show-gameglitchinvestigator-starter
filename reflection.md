# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first run it, I realized the GO LOWER and GO HIGHER were not correct. If the number was 80, and I typed 85, it would say: "GO HIGHER." If I typed a 70, it would say "GO LOWER." SO I changed that in the correct section.

Additionally, I had to convert the data types to ensure accurate numerical comparisons. The original code was incorrectly attempting to compare an integer (the user's guess) with a string (the secret number).


- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input              | Expected Behavior      | Actual Behavior       | Console Output / Error |
|-------|-------------------|-----------------|-----------------------|
| Guess higher number| Prompt says "Go LOWER" |  It says "Go HIGHER"  | None
| Guess lower number | Prompt says "Go HIGHER"| It says "Go LOWER"    | None
| Entering a guess   | Compare as numbers.    | Compare as strings    | TypeError

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- First I played the game multiple times to understand what was wrong. When I caught the LOWER and HIGHER was backwards, I looked for that section and fixed it. Then I tried running again, and realized was one of the labels was still backwards. Then I asked claude to show me what was wrong. For the part where it was referencing a string instead of int, I asked Claude becuase I did not catcht that on my own.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- I just saved it, and played again just like the beginning, by opening in the browser. Then I saw it worked without the bugs I have encountered before. 

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- I’d tell a friend that every time you click a button, Streamlit wipes the screen and runs the whole script over from the top to keep everything fresh. Since that would normally make the app forget everything, we use session state as a memory bank. It keeps important data, like score or the secret number, active and saved while the rest of the code resets, which allows the game to track your progress until you win or run out of turns.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? 
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit is to try the application/game first, then try to fix it, and THEN ask AI. This way I can use my brain to understand it rather thant just read what AI is telling me and copy, which is something I've done a lot.