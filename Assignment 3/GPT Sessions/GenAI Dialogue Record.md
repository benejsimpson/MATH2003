# Session 01 - Planning and report structure

## Me - Setup
Can you see the .md file in the project folder?
### AI response
**Model:** GPT-6 Astra (Medium)
Yes — I can see **Assignment 3.md** in the project folder and can read or edit it.
### Me
nice, read through this file - it was extracted from my assignment 3 for MATH2003. I want you to give me:

- a concise overview of the objectives of this assignment
- a plan for how to allocate time to this - it is due in 4 days but I want to have the final draft ready in 3 days
- a template for my submission - this will be written in latex and must be 2 pages. I have also included the zipped .tex template in the project folder given by the module leaders
- extract the coding tasks - I am much more familiar with python than most people on the course so no need to include ALL of the examples. I am less confident with numpy but have used it a few times - giving me a concise list of the key functions that this would require is most useful
- a list of your best ideas on approaches to take with the report - some more abstract and philosophical ideas would be interesting to see

ask me any questions that will help you complete this task for me before setting off to do it.
## AI response - Questions before starting
**Model:** GPT-6 Astra (Medium)

Two questions before I start:

1. **How much time can you spend on this each of the next three days?** Any commitments or days with less availability?
2. **What are you aiming for:** a strong, efficient submission, or a more ambitious report with deeper mathematical discussion and original analysis?

I’ll read the assignment and the supplied template to establish the requirements, then build the plan and a usable two-page LaTeX scaffold around them. I’ll separate ideas that directly meet the marking criteria from more exploratory or philosophical angles.

## Me - Answering questions
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
use a small hand-checkable system, the supplied \(5\times5\) example and systems constructed from a known solution.
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

## AI Response - Logging interactions
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

