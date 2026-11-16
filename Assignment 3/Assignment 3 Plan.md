==🔴**This is output from OpenAI's GPT-6 Astra (Medium)**

**My recommendation: aim for about 11–12 hours total, build one revealing numerical experiment, and make the article about what that experiment taught you about trusting AI.** That gives you room for interesting maths without turning a two-page assignment into a much larger project.

The brief states **24 November at 14:00**, which differs from your four-day deadline. The plan below follows your tighter target; check Minerva for the submission date.

# What the assignment is actually asking

**The assessed output is a reflective article about responsible generative AI use, supported by your investigation of Gaussian elimination and NumPy.**
# You need to:
1. Understand and implement Gaussian elimination, then compare it with `np.linalg.solve`.
2. Try different ways of using AI and critically evaluate your own experience.
3. Develop practical recommendations for a final-year mathematics student preparing a report, presentation and viva.
4. Produce at most two pages, using the supplied formatting, with four main sections, engaging headings, an explained `minted` code snippet and your own labelled figure.
5. Include an accurate declaration of AI use.

The exercise sheets are supporting material, **not a checklist of everything you must complete**. You can skip the introductory Python exercises.

Your second submission provides a particularly good model: “Does fair mean equal?” introduces a conceptual problem, examines competing interpretations and then uses mathematics to justify your position. Here, the equivalent question could be **“What makes an answer trustworthy?”**
# Plan
### Day 1: Understand and implement
*4 hours*
1. 30 min: choose your question and start an experiment log.
2. 90 min: implement elimination and back substitution.
3. 60 min: compare with NumPy and test edge cases.
4. 60 min: investigate pivoting with AI assistance.
#### Aims
Working baseline, initial comparisons and notes on what AI contributed.
### Day 2: Investigate and draft
*4 hours*
1. 90 min: run the focused experiment below.
2. 45 min: produce one clear figure.
3. 30 min: check explanations against documentation.
4. 75 min: write the complete first draft.
#### Aims
A full article with actual results, figure and snippet.
### Day 3: Refine and finish:
*3 - 4 hours*
1. 60 min: strengthen reflection and counterarguments.
2. 45 min: explain the method aloud without AI.
3. 60 min: edit and compile the two-page article.
4. 15–45 min: final checks.
#### Aims
Final draft ready.

4. Buffer only
	Brief proofread and submission checks.
	Submit without adding new experiments.

# Report Template
### What would convince us?
*90-110 words*
Motivate the question and introduce your investigation.
### Putting the answer to the test
*200-240 words*
Describe your experiment and actual AI interactions.
### An answer is not an explanation
*240-290 words*
Evaluate benefits, limitations and competing viewpoints.
### What I would take into a viva
*90-120 words*
State your position and actionable recommendations.

# Coding:
## Implement basic Gaussian elimination
construct an augmented matrix, eliminate entries below the diagonal, then back-substitute. Work with floating-point copies so your function does not alter the original inputs.
## Validate it
use a small hand-checkable system, the supplied \(5\times5\) example and systems constructed from a known solution.
## Compare with NumPy
use identical inputs and measure the residual and solution error.
## Add partial pivoting
choose the largest absolute entry remaining in the pivot column and swap the corresponding rows.
## Run one controlled experiment and plot it
A small timing comparison is optional; extensive scaling experiments are not necessary for your chosen argument.

## NumPy Toolkit

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

# Strongest Approaches
## When does a correct method give a wrong answer
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
### Figure
relative solution error against $\varepsilon$, with three solver curves. Treat zero errors explicitly when using logarithmic axes.
### Reflective question
did AI merely supply the fix, or help you understand why the fix works? Record what it actually does—an accurate explanation is evidence too; you do not need to manufacture an AI failure.

## A. What does ‘correct’ mean?
A small residual does not necessarily mean a small solution error:
$$
\mathbf{r}=A\mathbf{x_{*}}-\mathbf{b},\qquad
\mathbf{e}=\mathbf{\hat{x}}-\mathbf{x_{*}},\qquad
\mathbf{e}=A^{-1}\mathbf{r}
$$
An ill-conditioned matrix can amplify a small residual into a substantial error. For example, with $A=\operatorname{diag}(1,\delta)$, $x_*=(1,1)^T$ and a deliberately chosen approximation $\hat{x}=(1,0)^T$, the residual has norm $\delta$, while the solution error has norm $1$.

This is a counterexample to **“small residual proves accuracy”**, not evidence that NumPy necessarily returns that approximation.

The philosophical connection is strong: **the quality of your verification depends on what you choose to measure**. Keep algorithmic stability and problem conditioning distinct.

## B. Why trust NumPy but distrust AI?
Both can appear to be black boxes. A useful distinction is the evidence supporting trust: documented assumptions, established algorithms, reproducible tests and known limitations.

The counterargument matters: mathematicians cannot rebuild every tool they use. Responsible understanding might mean knowing **the method’s assumptions, failure modes and appropriate checks**, rather than understanding every implementation detail.

## C. Can I recognise an explanation without understanding it?
Compare three AI roles: generating code, explaining a specific difficulty and questioning your reasoning. Afterwards, close the conversation and try to:

- Explain why row operations preserve solutions.
- Explain why a zero pivot does not necessarily mean singularity.
- Modify the implementation and predict the effect.

This gives your viva recommendations a concrete foundation.

## D. A counterexample is worth a thousand successful runs
Random tests can all pass while missing a predictable failure. A deliberately chosen small-pivot system probes an assumption directly.

The useful distinction is between **testing as evidence** and **proof as justification**. AI can help propose counterexamples, but you still need to establish what they demonstrate.

For your two pages, I would combine **A as the experiment, C as the main discussion, and D as the basis for your recommendations**. Add B only if you can explain it clearly without crowding out reflection.