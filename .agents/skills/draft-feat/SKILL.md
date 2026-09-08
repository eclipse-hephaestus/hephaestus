---
name: draft-feat
description: Draft use cases (user-facing capabilities) from a raw idea or a whole list of them, each a single need with no parent to trace to.
---

# Draft a use case (user story)

The produced need is a **use case**: a single user-facing capability, stated
in stakeholder vocabulary, with no parent to trace to — `user_story` is the
ROOT of the V for this project, so there is no upstream stage to link into.

Pass `-p <project path>` on every `ubc agent` command. `<project path>` is the
directory that holds the target `ubproject.toml` (the project the need you are
authoring belongs to). A repository can contain several `ubproject.toml`
files, so without `-p` the command runs against the current directory and can
target the wrong project. Resolve `<project path>` once from the briefing you
were handed and reuse it on every call.

When these instructions say `ubc`, run the exact `ubc` binary whose path the
harness gave you in the task (it is version-matched to the editor). Do not
run a bare `ubc` from your PATH, and do not download or install your own
`ubc`. If no explicit path was given, use the `ubc` already on your PATH.

## Use the briefing and the tools — do NOT spelunk the filesystem

The briefing in your prompt ALREADY contains the resolved route and id prefix
for this stage. Do NOT re-discover the project: no `find`, `grep`, `cat`, or
reading `.rst` files to rebuild context. When you genuinely need one specific
need's full detail (for example, checking whether a similar use case already
exists), run `ubc agent audit --id <ID> -p <project path>`; for a need's
context briefing run `ubc agent context --id <ID> -p <project path>`. These
give structured, reliable data: prefer them over reading files. Author once at
the reported route; do NOT run `ubc build` repeatedly to poke at state — the
engine rebuilds and reports after you finish.

Author at the route and with the id prefix the engine reports for this stage.

## Input: one idea, or a whole list

Unlike the decomposition stages below this one, there is no parent need to
read for context — the raw material comes directly from whoever is talking to
you: a single sentence, a short paragraph, or a list of several unrelated
bullets pasted in one message.

Treat each logically distinct idea in the input as a candidate for its own
need. Do not fold unrelated bullets into one need, do not merge them into a
vaguer umbrella capability, and do not invent extra use cases the input didn't
ask for.

## Propose before you author

Do NOT write any RST yet. First present a short, scannable outline of what you
plan to author and ask the user to approve or adjust it. The outline lists,
for each use case:

- the id (with the reported prefix) and capability-oriented title,
- a one-line summary of the user-observable capability,
- if you split one input item into more than one need (because it bundled two
  independently-shippable capabilities), say so and why.

Keep it a scannable list, not the full RST. Wait for the user to approve or
adjust, and do not author until they confirm. On approval, author exactly what
you agreed, then leave the independent review to the separate review step.

## Output shape (one directive per use case)

```rst
.. <type>:: <capability-oriented title>
   :id: <ID with the reported prefix>
   :status: draft

   <1-3 sentence description of the ONE user-observable capability, in
   stakeholder vocabulary, describing the outcome/effect rather than the
   internal mechanism.>
```

`<type>` is the type named in your briefing for this stage. There is no
trace-link option here — `user_story` is the root of the V for this project.

## Rules

- **If you cannot decide or lack the context to author this faithfully, do NOT
  guess or fabricate.** Write `[NEEDS CLARIFICATION: <exactly what you need to
  know>]` in the body and stop. A human resolves it before the gate goes green —
  the gate fails closed on any need whose body still carries the marker.
- Exactly ONE user-facing capability per directive. If an input item actually
  bundles two capabilities that could ship independently, split it into two
  needs and say so in your outline.
- The capability must be something a user or stakeholder directly observes,
  not an internal mechanism.
- The body names no implementation constructs — no class, function, module,
  internal endpoint, or database table. A named tool or technology in the
  TITLE is fine when adopting that tool IS the stakeholder-facing decision
  (e.g. "Bazel as the harmonized build system") — but keep the BODY about what
  changes for the people using it, not how the tool works internally.
- Title and body use vocabulary a non-implementer stakeholder could confirm.
  Be lenient with domain-specific terms and abbreviations — assume they are
  defined elsewhere (e.g. a glossary) rather than spelling every one out.
- The `:id:` carries the reported prefix and matches the project's `id_regex`.
- Do NOT write a verdict here. Drafting authors the NEED; the verdict is
  authored later by the stage's review skill.

## Confirm

After authoring, run `ubc build needs`. Because each use case is the root of
its own stream (no parent to scope from), confirm each with
`ubc agent gaps --scope <NEW_ID> -p <project path>` using the new need's own
id, then run `ubc agent status -p <project path>` to see which downstream
stages it unblocks.
