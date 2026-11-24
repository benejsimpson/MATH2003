# Session 01 - Planning and report structure

## Me - Setup
Can you see the .md file in the project folder?
### AI response
**Model:** GPT-6 Astra (Medium)
Yes — I can see **Assignment 3.md** in the project folder and can read or edit it.
## Me
nice, read through this file - it was extracted from my assignment 3 for MATH2003. I want you to give me:

- a concise overview of the objectives of this assignment
- a plan for how to allocate time to this - it is due in 4 days but I want to have the final draft ready in 3 days
- a template for my submission - this will be written in latex and must be 2 pages. I have also included the zipped .tex template in the project folder given by the module leaders
- extract the coding tasks - I am much more familiar with python than most people on the course so no need to include ALL of the examples. I am less confident with numpy but have used it a few times - giving me a concise list of the key functions that this would require is most useful
- a list of your best ideas on approaches to take with the report - some more abstract and philosophical ideas would be interesting to see

ask me any questions that will help you complete this task for me before setting off to do it.
### AI response - Questions before starting
**Model:** GPT-6 Astra (Medium)

Two questions before I start:

1. **How much time can you spend on this each of the next three days?** Any commitments or days with less availability?
2. **What are you aiming for:** a strong, efficient submission, or a more ambitious report with deeper mathematical discussion and original analysis?

I’ll read the assignment and the supplied template to establish the requirements, then build the plan and a usable two-page LaTeX scaffold around them. I’ll separate ideas that directly meet the marking criteria from more exploratory or philosophical angles.

### Me - Answering questions
1. this project is worth 10% of the module grade which is worth 10/120 of my total module points across all modules. I am willing to commit 3-5 hours per day to it
2. I would like it to be strong and efficient but also include some more abstract ideas - I have been disappointed with the lack of interesting maths that has been covered in this module so far and would like to explore some with this project

I have also included my previous 2 assignment submissions for this module in the project source folder so you can see how I like to structure my reports and my style of writing.
## AI response - [[Planning]]
**Model:** GPT-6 Astra (Medium)

**My recommendation: aim for about 11–12 hours total, build one revealing numerical experiment, and make the article about what that experiment taught you about trusting AI.** That gives you room for interesting maths without turning a two-page assignment into a much larger project.

The brief states **24 November at 14:00**, which differs from your four-day deadline. The plan below follows your tighter target; check Minerva for the submission date.

### What the assignment is actually asking

**The assessed output is a reflective article about responsible generative AI use, supported by your investigation of Gaussian elimination and NumPy.**
### You need to:
1. Understand and implement Gaussian elimination, then compare it with `np.linalg.solve`.
2. Try different ways of using AI and critically evaluate your own experience.
3. Develop practical recommendations for a final-year mathematics student preparing a report, presentation and viva.
4. Produce at most two pages, using the supplied formatting, with four main sections, engaging headings, an explained `minted` code snippet and your own labelled figure.
5. Include an accurate declaration of AI use.

The exercise sheets are supporting material, **not a checklist of everything you must complete**. You can skip the introductory Python exercises.

Your second submission provides a particularly good model: “Does fair mean equal?” introduces a conceptual problem, examines competing interpretations and then uses mathematics to justify your position. Here, the equivalent question could be **“What makes an answer trustworthy?”**
### Plan
#### Day 1: Understand and implement
*4 hours*
1. 30 min: choose your question and start an experiment log.
2. 90 min: implement elimination and back substitution.
3. 60 min: compare with NumPy and test edge cases.
4. 60 min: investigate pivoting with AI assistance.
##### Aims
Working baseline, initial comparisons and notes on what AI contributed.
#### Day 2: Investigate and draft
*4 hours*
1. 90 min: run the focused experiment below.
2. 45 min: produce one clear figure.
3. 30 min: check explanations against documentation.
4. 75 min: write the complete first draft.
##### Aims
A full article with actual results, figure and snippet.
#### Day 3: Refine and finish:
*3 - 4 hours*
1. 60 min: strengthen reflection and counterarguments.
2. 45 min: explain the method aloud without AI.
3. 60 min: edit and compile the two-page article.
4. 15–45 min: final checks.
##### Aims
Final draft ready.

4. Buffer only
	Brief proofread and submission checks.
	Submit without adding new experiments.

### Report Template
#### What would convince us?
*90-110 words*
Motivate the question and introduce your investigation.
#### Putting the answer to the test
*200-240 words*
Describe your experiment and actual AI interactions.
#### An answer is not an explanation
*240-290 words*
Evaluate benefits, limitations and competing viewpoints.
#### What I would take into a viva
*90-120 words*
State your position and actionable recommendations.

### Coding:
#### Implement basic Gaussian elimination
construct an augmented matrix, eliminate entries below the diagonal, then back-substitute. Work with floating-point copies so your function does not alter the original inputs.
#### Validate it
use a small hand-checkable system, the supplied $5\times5$ example and systems constructed from a known solution.
#### Compare with NumPy
use identical inputs and measure the residual and solution error.
#### Add partial pivoting
choose the largest absolute entry remaining in the pivot column and swap the corresponding rows.
#### Run one controlled experiment and plot it
A small timing comparison is optional; extensive scaling experiments are not necessary for your chosen argument.

### NumPy Toolkit

|Function or syntax|What you need it for|
|---|---|
|`np.array(data, dtype=float)`; `.copy()`|Floating-point inputs and protecting originals.|
|`.shape`; `A[i, j]`; `A[i, k:]`|Dimensions, individual entries and row slices.|
|`np.column_stack((A, b))`|Constructing the augmented matrix.|
|`np.zeros(n)`; `np.ones(n)`|Solution storage and a known test solution.|
|`A @ x`; `row @ vector`|Matrix multiplication and back-substitution sums.|
|`np.argmax(np.abs(M[k:, k]))`|Selecting a partial-pivot row; add `k` to the returned index.|
|`M[[k, p]] = M[[p, k]]`|Swapping complete augmented rows.|
|`np.linalg.solve(A, b)`|Library comparison.|
|`np.linalg.norm(...)`; `np.linalg.cond(A)`|Residuals, errors and sensitivity.|
|`np.random.default_rng(99)`; `rng.standard_normal(...)`|Reproducible random tests.|
|`np.logspace(...)`|Varying a small parameter across orders of magnitude.|
For timing, use `time.perf_counter()` and repeated measurements; generate inputs outside the timed section. For plotting, `plt.subplots()`, `ax.loglog()` and `fig.savefig()` are sufficient.

Two traps to avoid: `*` multiplies elementwise, whereas `@` performs matrix multiplication; mixing vectors of shape `(n,)` and `(n,1)` can silently produce unintended broadcasting.

### Strongest Approaches
#### When does a correct method give a wrong answer
Consider
$$
A_{\epsilon}=
\begin{pmatrix}
\epsilon & 1 \\
1  & 1
\end{pmatrix},\qquad
\mathbf{x_{*}}=
\begin{pmatrix}
1 \\
1
\end{pmatrix},\qquad
\mathbf{b}=A_{\epsilon}\mathbf{x_{*}}.
$$
Vary $\varepsilon$, for example from $10^{-1}$ to $10^{-16}$, and compare basic elimination, pivoted elimination and NumPy.

Without pivoting, elimination divides by a tiny number and creates large intermediate values. Swapping the rows avoids that small initial pivot. Crucially, the matrix remains reasonably well-conditioned as $\varepsilon\to0$: this isolates **a weakness in the algorithm**, rather than an inherently sensitive problem.
##### Figure
relative solution error against $\varepsilon$, with three solver curves. Treat zero errors explicitly when using logarithmic axes.
##### Reflective question
did AI merely supply the fix, or help you understand why the fix works? Record what it actually does—an accurate explanation is evidence too; you do not need to manufacture an AI failure.

#### A. What does ‘correct’ mean?
A small residual does not necessarily mean a small solution error:
$$
\mathbf{r}=A\mathbf{x_{*}}-\mathbf{b},\qquad
\mathbf{e}=\mathbf{\hat{x}}-\mathbf{x_{*}},\qquad
\mathbf{e}=A^{-1}\mathbf{r}
$$
An ill-conditioned matrix can amplify a small residual into a substantial error. For example, with $A=\operatorname{diag}(1,\delta)$, $x_*=(1,1)^T$ and a deliberately chosen approximation $\hat{x}=(1,0)^T$, the residual has norm $\delta$, while the solution error has norm $1$.

This is a counterexample to **“small residual proves accuracy”**, not evidence that NumPy necessarily returns that approximation.

The philosophical connection is strong: **the quality of your verification depends on what you choose to measure**. Keep algorithmic stability and problem conditioning distinct.

#### B. Why trust NumPy but distrust AI?
Both can appear to be black boxes. A useful distinction is the evidence supporting trust: documented assumptions, established algorithms, reproducible tests and known limitations.

The counterargument matters: mathematicians cannot rebuild every tool they use. Responsible understanding might mean knowing **the method’s assumptions, failure modes and appropriate checks**, rather than understanding every implementation detail.

#### C. Can I recognise an explanation without understanding it?
Compare three AI roles: generating code, explaining a specific difficulty and questioning your reasoning. Afterwards, close the conversation and try to:

- Explain why row operations preserve solutions.
- Explain why a zero pivot does not necessarily mean singularity.
- Modify the implementation and predict the effect.

This gives your viva recommendations a concrete foundation.

#### D. A counterexample is worth a thousand successful runs
Random tests can all pass while missing a predictable failure. A deliberately chosen small-pivot system probes an assumption directly.

The useful distinction is between **testing as evidence** and **proof as justification**. AI can help propose counterexamples, but you still need to establish what they demonstrate.

#### Recommendation
For your two pages, I would combine **A as the experiment, C as the main discussion, and D as the basis for your recommendations**. Add B only if you can explain it clearly without crowding out reflection.

## Me - How to log AI interactions
I want to keep a detailed log of all interactions I have with you throughout making this project. I will store the interactions on my GitHub. The github repo for this project has folders:

- GPT Sessions
    - this is where I want to store the dialogue we have throughout the entirety of the project
- Latex code
    - this is where I will store my latex code for the project. When big updates are made to my latex, I will put the .tex file in here
- Python code
    - this is where I will store my python code. I have already started on this.

What is the best way to keep a log of our conversation history? I would Ideally like to have it in .md format. Each session should be a new .md file. The session .md file will have ## headers 'Me - brief summary (2-5 words)' and 'AI response - brief summary (2-5 words)'. Under each 'AI response' header will be the model used - generally GPT-6 Astra (Medium). Your response is then given under this header, nicely formatted for .md files - I am very familiar with obsidian and .md file formatting.

### AI Response - Logging interactions
**Model:** GPT-6 Astra (Medium)

The best approach is **one Markdown transcript per chat session**, saved in `GPT Sessions`, with a short instruction at the start of each new chat establishing the format.

Use filenames such as:

`GPT Sessions/2026-11-16_01_Planning-and-report-structure.md`

The date keeps them ordered, and the session number accommodates multiple chats on the same day.

Your format works well. I would add a small amount of metadata:

```
---
date: 2026-11-16
session: 01
topic: Planning and report structure
model: GPT-6 Astra (Medium)
---

# Session 01 — Planning and report structure

## Me - Assignment planning request

[Your message, preserved verbatim.]

## AI response - Proposed investigation plan

**Model:** GPT-6 Astra (Medium)

[My complete response, preserving paragraphs, lists, tables,
equations and fenced code blocks.]

## Me - Clarifying the experiment

[Your next message.]

## AI response - Explaining partial pivoting

**Model:** GPT-6 Astra (Medium)

[My next complete response.]
```

**Keep the dialogue verbatim; use summaries only in the headers.** This makes the record useful evidence of how your thinking developed, including mistakes, corrections and suggestions you chose not to follow.

For a reliable workflow:

1. **Start each chat with the logging instruction below.** Treat one chat thread as one session unless you explicitly split it.
2. **At useful checkpoints, ask me to update the session transcript.** This is safer than waiting until the end of a very long conversation, when earlier messages may no longer be available verbatim.
3. **Save and commit the updated file to GitHub.** Continue updating the same file throughout that session; Git records its successive versions.
4. **End with a final transcript update.** Optionally add your own short reflection about what you accepted, rejected, verified or learned—clearly separated from the dialogue.

You can use this instruction:
```
Maintain a Markdown transcript for this project session.

Use one file in "GPT Sessions", named:
YYYY-MM-DD_NN_Short-topic.md

Record my messages and your user-facing responses verbatim and
chronologically. Do not replace the dialogue with summaries.

Use these level-two headings:
## Me - [2–5-word summary]
## AI response - [2–5-word summary]

Immediately below every AI response heading, include:
**Model:** [model and reasoning setting I confirm]

Preserve Markdown formatting, equations and fenced code blocks.
Include substantive progress messages, labelled as progress updates.
Exclude raw tool output unless needed to understand a result; clearly
label any tool-result notes you add.

Never reconstruct unavailable messages or invent model metadata.
Flag any gaps explicitly.

Update the same transcript at checkpoints and at the end of the session.
Do not push to GitHub unless I explicitly ask you to.
```

Two practical details:

- **Confirm the model label from your interface.** I cannot reliably identify the exact displayed model and reasoning setting myself. Once you confirm it for a session, I can consistently use that label.
- **Keep artifact paths portable.** Preserve original links in the transcript, but add clearly labelled repository-relative links to relevant Python or LaTeX files where useful. Temporary download links may not remain usable.

For this assignment, a faithful transcript plus your own occasional reflection will be more valuable than a polished retrospective account: it shows what AI contributed and what intellectual work remained yours.


# Session 02 - Report Template
## Me
I am still a little confused as to what this report is actually achieving and what the final result should look like. Create your best version of this report. Make it interesting and engaging. Don't use too much jargon or overcomplicate things. This should be informative and fun, slightly philosophical and avant-garde. Take as much time as you need, plan and research the task carefully. The report must follow the latex template and must be within 2 pages.
Ask me any questions you need.

### AI Response - Create report version
**Model:** GPT-6 Astra (Medium)

*I’ll inspect the assignment brief, your current report and the LaTeX template first, then shape the report around a clear purpose and a concrete final result. I’ll keep it within two pages and flag only questions that the brief or files can’t resolve.*

*Ran a command, searched the web*

*The brief confirms this is a reflective article about how AI supports a maths project, with a small solver experiment as evidence. Your current draft is a scaffold rather than a finished report, and it has no record of your own solver results or AI interactions. I’m building a small, reproducible comparison for the article and will keep the reflection tied to that work, so the report won’t invent timing results or claim that an unrecorded experiment was yours.*

*Ran commands*

*The comparison now has a clear, teachable result: the small-pivot system stays well-conditioned, but plain elimination loses accuracy; pivoting and NumPy stay near floating-point precision. I’ve made that the report’s central idea, so the figure supports a critical point rather than just decorating the page. The draft is about 700 words, with a short code snippet, source notes and the required four sections.*

*Ran a command*

The report’s main point is that AI can help produce code and suggest an experiment, but evidence and understanding are what make the result trustworthy. The small pivot experiment gives it a concrete argument: plain elimination loses accuracy even though the system itself stays well-conditioned; pivoting and NumPy remain near floating-point precision. NumPy’s documentation and LAPACK’s routine description support the explanation of how the built-in solver works.

It’s about 700 words and follows the four-section structure. I couldn’t compile it here because a LaTeX compiler isn’t available, so check the final pagination in Overleaf. Before submitting, make sure the first-person reflections and AI-use declaration match what you personally did and learned.

## Me - Clarifying coding task
what exactly is the coding task for this?

### AI Response
The coding task is to **write your own Gaussian elimination solver in Python, then compare it with `numpy.linalg.solve` on the same equations**.

1. **Write `gaussian_elimination(A, b)`.** Here, `A` contains the coefficients and `b` contains the right-hand sides. Use row operations to eliminate the entries below the diagonal, then work backwards to find the solution vector `x`. You can use NumPy arrays for the arithmetic while implementing the elimination yourself.
2. **Check that it works.** Pick a matrix `A` and a solution you already know, such as `x_true = [1, 1]`. Compute `b = A @ x_true`, then give only `A` and `b` to each solver. Compare what they return with `x_true`.
3. **Find a case where the methods behave differently.** The draft uses $A=\begin{pmatrix}\varepsilon&1\\1&1\end{pmatrix}$. As $\varepsilon$ gets smaller, plain elimination divides by a tiny number and rounding errors grow. Add **partial pivoting** to your solver so it swaps the two rows first, then compare all three methods: plain elimination, pivoted elimination and NumPy. Plot their solution errors against $\varepsilon$.

**The final coding result** is a working solver and a plot showing when swapping rows makes a difference. The brief requires a short code snippet and a figure in the article. Pivoting is the extension chosen for this draft, and timing benchmarks are optional.

The report then uses that experiment to explain **what AI helped you do, how you checked its suggestions, and what you could explain yourself in a viva**.

# Session 03 - Implement Gaussian Elimination
## Me
Design your own gaussian elimination algorithm in python, making it as efficient as possible. It can use numpy for arithmetic but all matrix operations should be written from scratch. It should take inputs: A,b; and return x such that Ax=b.
do you have any questions before starting?

### AI Response
[gaussian_elimination.py](https://chatgpt.com/library?file_id=libfile_4b67444038d48191822d769bcc4b59f1&account_id=personal) contains `gaussian_elimination(A, b)`. It uses partial pivoting, forward elimination and back substitution, all implemented from scratch. NumPy handles elementwise arithmetic, pivot selection and summation.

```
from gaussian_elimination import gaussian_elimination
A = [[0, 2],
	[1, 3]]
b = [4, 7]

x = gaussian_elimination(A, b)
print(x)
# [1. 2.]
```

The zero in the top-left corner makes this a useful test. The solver swaps the two equations before dividing by the first pivot.

For efficiency, it updates up to 32 rows at once and reuses the same temporary array at every pivot. This keeps the arithmetic in NumPy while limiting temporary storage to $O(n)$ beyond the working matrix. The overall running time is $O(n^3)$ for a dense $n\times n$ system.

I tested real and complex systems up to $100\times100$, including sizes just below and above the 32-row block boundary. I also checked that the solver preserves its inputs and raises `ValueError` on a singular example.

# Session 04 - Fix Listings Error
## Me
I'm trying to use latex listings package but getting erorrs:

==🟡Pasted Latex code==

## AI Response
**Model:** GPT-6 Astra (Medium)
The error is caused by a **typo on line 2** of your LaTeX document.

You currently have:

```
\usepackage{lisitings}
```

Change it to:

```
\usepackage{listings}
```

The package is called `listings`, not `lisitings`.

### **Corrected preamble**

```
\documentclass[11pt,a4paper]{article}

\usepackage{listings}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage[left=2.5cm,right=2cm,top=1.5cm,bottom=2cm]{geometry}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{minted}
\usepackage{url}
```

### **Optional: Improve the Python code formatting**

Since you're including Python code in your report, you can configure `listings` to provide syntax highlighting and line numbers.

Add this after `\usepackage{listings}`:

```
\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    commentstyle=\color{gray},
    stringstyle=\color{red},
    numbers=left,
    numberstyle=\tiny,
    breaklines=true,
    frame=single,
    showstringspaces=false
}
```

You'll also need:

```
\usepackage{xcolor}
```

Then your existing code will work without changing it:

```
\begin{lstlisting}
known = np.sum(rows[k, k + 1:n] * x[k + 1:])
\end{lstlisting}
```

**One other thing:** You're currently loading both `minted` and `listings`. You only need one for your report. Since you're using `lstlisting`, I'd recommend keeping `listings` and removing `\usepackage{minted}`.

# Session 05 - Writing Gen AI Article
## Me - Requesting feedback on report
I've decided to go down a slightly different route with this assignment. I read some of the articles that were given as examples - from [https://chalkdustmagazine.com/](https://chalkdustmagazine.com/). I am thinking of writing it more informally, with some witty comments throughout, taking the route of: written to a student who is scrambling to get their assessment in on time. they could choose to use gen ai to create it for them but these are the drawbacks: ...  
also using the task of gaussian elimination and computer matrix operations to link to how gen-ai and LLMs do NLP. Here is what I have so far, what are your thoughts:

==🟡Pasted Latex code==
## AI Response
**Model:** GPT-6 Astra (Medium)
I’d go with this angle. The student scrambling before a deadline gives you someone to write _to_, and “The tricky thing is noticing when it doesn’t” gives the article a question worth answering. **I’d bring Gaussian elimination into the opening paragraph.** As it stands, the student disappears just as things get interesting. Give them a piece of AI-generated code and a decision to make: _would you submit it?_

I’d keep “something, anything” and the aside about the markers. Both sound like you. The sentence I’d cut is “Fortunately, we live in the modern world and have access to a wide range of technologies…” It sounds more formal than everything around it, and the reader already knows why someone with an unfinished assessment might open ChatGPT.

Here’s how I’d shape the opening while keeping your voice:

> You’ve found yourself, yet again, scrambling the night before your assessment is due, trying to piece together something, _anything_, that will score you some marks. We’ve all been there, probably including whoever’s going to mark it. Tonight’s task is to write a Python program that solves a system of equations by Gaussian elimination. You open ChatGPT.
> 
> A few seconds later, you’ve got a function. It’s even commented. You try it on the example from the lecture notes and it gives the right answer. How many more examples would you try before you’d put your name on it?

That last question gives you a route through the two pages. It also lets the humour come from the situation. “It’s even commented” tells us quite a lot about our student’s usual submissions.

**For the link to language models, I’d lean into the coincidence that you’ve just asked a machine doing matrix arithmetic to write a program that does matrix arithmetic.** That’s a lovely way into the maths. You could follow the opening with something like:

> There’s a nice bit of irony here. Before you’ve done a single row operation, the language model has already been busy multiplying matrices. It splits your prompt into chunks of text called _tokens_ and represents each one as a list of numbers. Matrix multiplications help it work out how the tokens relate to one another in context. From there, it assigns probabilities to possible next tokens, picks one, and repeats. Eventually, you’ve got a Python function. Whether it works is a question we can test. [OpenAI API](https://platform.openai.com/tokenizer?vwaf=228&utm_source=chatgpt.com)

That fixes two technical points in your draft. “The most likely response” suggests the model chooses a whole answer in one go. The token-by-token account is both more accurate and easier to picture. I’d also drop “trillions of pages” and the Bel paragraph. The article describes the parameter count as _reported_, and even a confirmed count wouldn’t establish that nobody understands how the model works. For your reader, the more interesting uncertainty is sitting right there on their screen. [OpenAI API](https://platform.openai.com/tokenizer?vwaf=228&utm_source=chatgpt.com)

**Then give the reader a system they can solve faster than they can run the code:**

$$ \begin{aligned} 0x+y&=1,\\ x+y&=2. \end{aligned} $$

You can see immediately that $y=1$ and $x=1$. A naïve elimination routine starts with the top-left entry as its pivot and tries to divide by zero. A row swap fixes it. Run this through the code you actually received and report what happened. If it handled the swap correctly, that’s a good result for the article too. You can show the reader the line that saved it and explain why it mattered.

That’s where I’d take the slightly philosophical angle. The student opened ChatGPT because they didn’t know how to write the solver. Now they’ve got one, and they need enough mathematics to decide whether to trust it. **“The tricky thing is noticing when it doesn’t”** would land much harder just before that little system of equations. I’d keep it word for word.

## Me - Slight changes

this is what I have now:

==🟡Pasted Latex code==

## AI Response

I’d keep the three-option structure. The third option works because the first two set up a choice most students recognise, and the viva gives the choice a consequence. The strongest bit is the joke about `known`. It’s specific to _your_ experience, it gets a laugh, and it gives you a way to answer the question in your title.

**The main change I’d make is to let the reader find out what `known` does.** At the moment, you raise two questions in _Your assignment_ — how do we write the script, and how do we know it works? Most of the article answers the first. You could answer the second in four lines, using the code already on the page.

### 1. Bring `known` back in Option 3

I’d keep “Unlike computers, we don’t have to make binary decisions.” Then I’d replace the more abstract sentences about striking a balance with something the student actually _does_. For example:

> You go back to the line that bothered you. This time, you ask ChatGPT to explain `known`, then try its explanation on paper. Suppose one row reads $2x+3y=7$, and you’ve already worked out that $y=1$. The contribution you already know is $3y=3$. Subtract it from 7, divide by 2, and you get $x=2$. So that’s what `known` is doing. A slightly generous choice of variable name at the time.
> 
> Tomorrow, if the examiner asks what that line does, you’ve got a better answer than “well, it passed the examples.”

That works because the NumPy line really does multiply the coefficients **to the right of the pivot** by the corresponding values you’ve already found, then add those products. It’s the familiar step in back-substitution hiding inside unfamiliar syntax. If you actually try this as part of your investigation, you can also report how well the AI explained it.

### 2. Fix the pseudocode before polishing the prose

This is the one part I’d definitely change for mathematical reasons. Sorting rows by leading zeros at the start doesn’t guarantee a usable pivot later. Also, `Subtract RiCj*R1Cj from the rows beneath` describes a product of two entries, whereas elimination subtracts a multiple of the **whole pivot row**, including its right-hand side. The listing currently stops at echelon form, just before the step where `known` appears.

For a square system with a unique solution, you could make the listing shorter _and_ more accurate:

```
For each column, working from left to right:
    Choose the remaining row with the largest absolute entry in this column.
    If that entry is zero, the system has no unique solution.
    Swap the chosen row into the pivot position.
    For each row below it:
        factor = entry below pivot / pivot
        Subtract factor times the whole pivot row from this row.
Work upwards, solving each equation using the values already found.
```

That last line sets up the return to `known`. It also gives you a more revealing test than running another lecture example: **swap the order of two equations and see whether your solver still finds the same solution.** The reader can predict what ought to happen before you tell them what your code did.

### 3. Give Option 2 the same voice as Option 1

Option 1 sounds like you talking to another student. Halfway through Option 2, phrases like “iterating the method of” and “the aforementioned pseudo-code abstraction paradigm” sound like the student has remembered this is being marked. I’d cut the class-structure discussion and “hundreds of lines of code”. Neither is necessary to make your point. The idea underneath is much more approachable:

> Do one example by hand and write down the instructions you wish someone else would follow. “Swap these rows.” “Make this entry zero.” “Do that again for the next row.” You’ve just found two functions and a loop.

I’d also reconsider **“It doesn’t have to be perfect or even efficient, it just needs to be yours.”** It has a nice rhythm, but your third option makes a more interesting argument: you can understand a line somebody else wrote, and you can write a line yourself that turns out to be wrong. **“Could you explain why it works?”** is the better standard for the viva, whichever route the student took.

Two small finishing edits: change “unknown to **me**” to “unknown to **you**” to stay with the reader, and give Option 3 the same LaTeX heading level as Options 1 and 2. Before submission, replace the bracketed footnote reminder with an accurate account of how you used AI, including any generated code or wording you retained.

With two pages, I’d spend the space on **one line of code the reader comes to understand and one test whose outcome they can predict**. That gives the article an ending you’ve earned: the student still has the same function they had five minutes ago, but now they have a reason to trust part of it.

## Me - Explain `known` better
the more confusing thing about the 'known' line was what `rows[k, k + 1:n] * x[k + 1:]` actually represents.

## AI Response
`rows[k, k + 1:n] * x[k + 1:]` pairs **each coefficient to the right of the pivot** with **the value of its corresponding unknown**. The `*` multiplies those pairs element by element. The surrounding `np.sum(...)` then adds the products.

Suppose the current row represents $2x+3y-4z=7$, and back-substitution has already given you $y=1$ and $z=2$. Here’s how to read the line:

|Python|What it selects or calculates|Example|
|---|---|---|
|`rows[k, k + 1:n]`|In row `k`, take the coefficients after the pivot. The slice stops before column `n`, which holds the right-hand side.|`[3, -4]`|
|`x[k + 1:]`|Take the entries of the solution vector after position `k`. These are the values already found.|`[1, 2]`|
|`rows[k, k + 1:n] * x[k + 1:]`|Multiply matching entries.|`[3, -8]`|
|`np.sum(...)`|Add those products to get the value of $3y-4z$.|`-5`|

The detail that makes it click is **both slices start at `k + 1`**. That lines up the $y$-coefficient with $y$, the $z$-coefficient with $z$, and so on. The equation now reads $2x-5=7$, so $x=6$.

For your article, I’d keep the `known` joke and bring it back in Option 3 with something like this:

> Back to `known`. What threw you were the two sets of square brackets. Take $2x+3y-4z=7$. By the time you reach this row, you already know $y$ and $z$. The first slice picks out $3$ and $-4$, the second picks out $y$ and $z$, and NumPy multiplies them in pairs. Add the results and you’ve got $3y-4z$. You’ve been doing this bit by hand for years. It was the colons that got you.

# Session 06 - LLM Token Representation
## Me
are tokens treated as multidimensional vectors in llms?

## AI Response
Yes. In Large Language Models (LLMs), **tokens are represented as multidimensional vectors**, called _embeddings_.

However, a token itself is not a vector. It is initially an integer ID, which is then mapped to a vector.

## **1. From tokens to vectors**

Suppose the input is:

> "The cat sat"

A tokenizer might convert this into:

$$ [1023,\ 5472,\ 8921] $$

Each integer is then mapped to a vector in $\mathbb{R}^d$, where $d$ is the model's embedding dimension.

For example, if $d=4$:

$$ \text{cat}\longrightarrow \begin{bmatrix} 0.21\\ -0.73\\ 0.45\\ 0.12 \end{bmatrix} $$

In practice, embedding dimensions are commonly in the hundreds or thousands.

## **2. What do the dimensions represent?**

The interesting part is that **individual dimensions generally don't correspond to clearly defined properties**.

For example, we cannot reliably say:

- Dimension 1 = how positive a word is
    
- Dimension 2 = whether it's an animal
    
- Dimension 3 = how formal it is
    

Instead, semantic and syntactic information is distributed across many dimensions.

Tokens with related meanings often have related vector representations.

Illustrative 2D projection of token embeddings
![[download.svg|700]]
Conceptual illustration, not actual measured embeddings. Real token representations exist in much higher-dimensional spaces.

## **3. The vectors change as the model processes the sentence**

This is an important distinction.

The initial embedding represents a token without knowing its surrounding context.

As the embedding passes through the transformer layers, it develops into a **contextual representation**.

Consider:

- "I deposited money in the **bank**."
    
- "I sat beside the river **bank**."
    

The token "bank" may initially have the same embedding in both sentences, but its representation changes as the model processes the surrounding tokens through attention and other operations.

Mathematically, a simplified transformer layer performs:

$$ H^{(l+1)}=f_l(H^{(l)}) $$

where $H^{(l)}\in\mathbb{R}^{n\times d}$ represents the contextual vectors for all $n$ tokens at layer $l$.

## **4. Why this matters**

By representing tokens as vectors, the model can use linear algebra to:

- Measure relationships between representations using dot products.
    
- Calculate attention weights to determine which tokens contribute to each other's representations.
    
- Transform information through learned matrices.
    
- Produce probability distributions over possible next tokens.
    

**The key idea:** An LLM is not manipulating words directly. It is performing mathematical operations on high-dimensional numerical representations of tokens.

One particularly interesting consequence is that concepts and relationships can sometimes be represented as _directions_ in vector space, rather than as individual coordinates. This is part of why linear algebra is so fundamental to modern language models.

# Session 07 - Python float alias equivalent
## Me
is there a py equivalent to c++ using f128 = np.float128

## AI Response
**Model:** GPT-6 Astra (Medium)
Yes. In Python, you can create a type alias by assigning the type to a variable:

```
import numpy as npf128 = np.float128x = f128(3.14159)
```

This is equivalent to C++:

```
using f128 = __float128;
```

**Important:** `np.float128` is not available on all platforms, particularly Windows. Even where available, it does not necessarily provide true 128-bit floating-point precision.

For a more portable alternative:

```
f128 = np.longdouble
```

However, `np.longdouble` typically provides only 64-bit floating-point precision on Windows.

## Me - Precise float representation
whats the most precise float representation to use?

## AI Response
For **maximum floating-point precision in Python**, I recommend `mpmath`. It supports arbitrary precision, meaning you can specify 50, 100, 1,000 or more significant decimal digits.

## **1. Best for maximum precision:** `mpmath`

Install with:

```
pip install mpmath
```

Then:

```
from mpmath import mpmp.dps = 100  # 100 decimal digits of precisionf128 = mp.mpfx = f128("1.234567890123456789")y = f128("3.141592653589793238")print(x * y)
```

You can increase `mp.dps` as needed.

mpmath.org+1

## **2. Precision comparison**

|Type|Decimal precision|Performance|
|---|---|---|
|`float` / `np.float64`|~16 digits|Very fast|
|`np.longdouble` (Windows)|~16 digits|Fast|
|IEEE `float128` (binary128)|~34 digits|Slower|
|`mpmath.mpf`|Arbitrary|Slower|

NumPy's `np.longdouble` generally offers no additional precision over `float64` on Windows.

NumPy v2.5 Manual+1

## **3. Alternative: Python's built-in** `decimal`

If you don't want another dependency:

```
from decimal import Decimal, getcontextgetcontext().prec = 100f128 = Decimalx = f128("1.234567890123456789")
```

`Decimal` also provides arbitrary configurable decimal precision.

Python 3.15.2 documentation

**My recommendation:** For numerical algorithms such as Gaussian elimination, use ordinary `float64` unless you specifically need greater precision. If you do, use `mpmath.mpf`, but be aware that it is substantially slower than hardware floating-point arithmetic.

Also, increasing precision does not automatically make an algorithm numerically stable.

# Session 08 - Row swapping design
## Me
I did a rewrite to simplify. I am having trouble with the row swapping. Give advice on how to restructure / change a function so this works:

==🟡Pasted Python code==
## AI Response

The main issue is that you're treating `row_index` as the position of a row, rather than using its **actual position in** `self.rows`.

I'd recommend simplifying your design so that `Matrix` is responsible for row ordering, while `Row` is responsible only for operations on its entries.

## **1. Fix** `Matrix.swap_rows()`

Currently:

```
def swap_rows(self, row1: int, row2: int):    self.rows[row1].update_row_index(row2)    self.rows[row2].update_row_index(row1)
```

This changes the `row_index` attributes, but **doesn't actually swap the rows**.

Instead:

```
def swap_rows(self, row1: int, row2: int):    self.rows[row1], self.rows[row2] = self.rows[row2], self.rows[row1]
```

Python's tuple assignment swaps the two `Row` objects directly within the list.

You can now remove `row_index` entirely from your `Row` class, including `update_row_index()`.

## **2. Simplify** `GaussianElimination.__str__()`

Your current implementation sorts the rows by their `row_index` attributes.

Since the rows are now stored in their actual order, you don't need to sort anything.

```
def __str__(self):    s = ""    for row in self.matrix.rows:        s += f"{row}\n"    return s
```

This also means that `Matrix.__str__()` and `GaussianElimination.__str__()` are doing essentially the same thing. You could simply use:

```
def __str__(self):    return str(self.matrix)
```

## **3. Rethink** `GaussianElimination.order_rows()`

This is the most important algorithmic change.

Your current implementation sorts _all_ rows based on the magnitude of their first non-zero entry.

However, Gaussian elimination requires you to select the best pivot **for the current column, among rows that haven't already been processed**.

For example, suppose your matrix contains:

$$ A= \begin{pmatrix} 2&3&1\\ 5&1&4\\ 1&6&2 \end{pmatrix} $$

For column 0, the best pivot is 5, so we swap rows 0 and 1:

$$ \begin{pmatrix} 5&1&4\\ 2&3&1\\ 1&6&2 \end{pmatrix} $$

But for column 1, we must choose between rows 1 and 2, without moving row 0.

### **Recommended replacement**

Instead of `order_rows()`, create:

```
def select_pivot_row(self, col: int):    pivot_ind = max(        range(col, self.num_rows),        key=lambda i: abs(self.matrix.rows[i].entries[col].value)    )    self.matrix.swap_rows(col, pivot_ind)
```

This implements **partial pivoting**:

- `range(col, self.num_rows)` considers only remaining rows.
    
- `abs(...)` selects the largest pivot magnitude.
    
- `swap_rows(col, pivot_ind)` moves that row into the correct position.
    

Call this at the beginning of each elimination step.

## **4. Update** `make_pivot_column()`

With those changes, your function becomes:

```
def make_pivot_column(self, col: int):    self.select_pivot_row(col)    pivot_row = self.matrix.rows[col]    pivot_value = pivot_row.entries[col].value    if pivot_value == 0:        raise ValueError("Matrix is singular")    pivot_row.scalar_multiply_row(1 / pivot_value)    for row in self.matrix.rows[col+1:]:        scalar = row.entries[col].value        row.subtract_multiple_of_row(pivot_row, scalar)
```

Notice that I've changed `first_non_zero_value` to `entries[col].value`.

This is because **the pivot must be selected from the current column**, not necessarily from the first non-zero entry of the row.

## **5. One other important bug:** `Row.subtract_multiple_of_row()`

Your current implementation is:

```
def subtract_multiple_of_row(self, row_to_subtract: Row, scalar: flong):    for i,val in enumerate(row_to_subtract.entries):        if val == 0:            pass        val.subtract_multiple_of_entry(self.entries[i], scalar)
```

This modifies `row_to_subtract`, rather than `self`.

For Gaussian elimination, you want:

$$ R_i \leftarrow R_i-\lambda R_{\text{pivot}} $$

So the function should be:

```
def subtract_multiple_of_row(self, row_to_subtract: 'Row', scalar: flong):    for i, val in enumerate(self.entries):        val.subtract_multiple_of_entry(row_to_subtract.entries[i], scalar)
```

This correctly updates the row on which the method was called, leaving the pivot row unchanged.

Also, `if val == 0` compares an `Entry` object with zero, rather than its numerical value. The check isn't necessary here.

## **Recommended final structure**

Keep your three main classes, with the following division of responsibilities:

|Class|Responsibility|
|---|---|
|`Entry`|Scalar arithmetic|
|`Row`|Row arithmetic, accessing entries|
|`Matrix`|Storing rows, swapping rows, augmentation|
|`GaussianElimination`|Pivot selection, elimination, back substitution|

The elimination algorithm then has a simple structure:

```
for col in range(self.num_rows):    self.make_pivot_column(col)
```

Each iteration:

1. Selects the best pivot row from the remaining rows.
    
2. Swaps it into position.
    
3. Normalises the pivot row.
    
4. Eliminates the entries below the pivot.
    

**One further recommendation:** you can remove `first_non_zero_index` and `first_non_zero_value` from the pivoting logic entirely. Since you know which column you're processing, direct indexing is simpler and avoids repeatedly searching each row.

Your overall object-oriented approach can work without a major rewrite. The key improvement is to establish **one source of truth for row order:** `Matrix.rows`.

# Session 09 - Comparing float precision
## Me
produce a python script that compares pythons built-in floating point representation with NumPy's float64. This should be done by either multiplying or dividing a set of numbers with each float representation and producing a pyplot of the resulting errors.

## AI Response - 
**Model:** GPT-6 Astra (Medium)
**Produced Python script:** compare_float_precision.py

The script alternately multiplies by $17/16$ and $15/16$. Both factors are exactly representable in binary, so any error comes from rounding the products. It uses Python’s `Fraction` to calculate the exact product at each step and plots the absolute error for each type.

**Python `float` and NumPy `float64` produced identical results in all 200 multiplications.** The plot uses a line for Python and hollow circles every fifth step for NumPy so you can see where they overlap.

Run it with `python compare_float_precision.py` to display the plot.

## Me
I was hoping to see a difference in their accuracy? I thought NumPy's float64 was supposed to be better than pythons built-in float?

## AI Response
Python’s built-in `float` already uses **64-bit double precision** on your PC, just like NumPy’s `float64`. Both have 53 bits of precision, or roughly 16 decimal digits. If you multiply the same numbers in the same order, both round the same way. **The overlapping curves are the expected result.**

NumPy’s advantage here is that it can process whole arrays efficiently and lets you choose the precision. For example, `np.float32` has fewer bits available, so it starts rounding sooner. You can see the difference with a single multiplication:

```
>>> 4097.0 * 4097.016785409.0>>> float(np.float64(4097) * np.float64(4097))16785409.0>>> float(np.float32(4097) * np.float32(4097))16785408.0
```

The exact answer is $16{,}785{,}409$. At that size, consecutive `float32` values are **two units apart**, so the odd integer falls between two representable values. Python’s `float` and NumPy’s `float64` can still represent it exactly.

For your assignment plot, I’d **add `np.float32` as a third series**. That gives you a visible accuracy difference while keeping the original comparison.





---
*Module:* [[_Investigations in Mathematics (MATH2003) Home]]
*Assignment: [[MATH2003 - Assignment 3]]*

