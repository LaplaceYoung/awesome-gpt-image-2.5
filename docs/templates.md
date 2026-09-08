# Prompt templates

Slot convention: {subject}, {change}, {lock}, {style}, {copy}, {format}.

Keep locks and changes in separate sentences.

## TPL-01 Local tidy

Use the attached photo as the only source of truth for architecture, camera angle, and materials.
Change only this: {change}.
Do not change: {lock}.

## TPL-02 Identity-preserving restyle

The attached portrait is the identity lock. Keep face structure, age, and expression recognizable.
Restyle the frame as {style}.
Do not beautify, age-shift, or replace the subject.

## TPL-03 Multi-turn comment edit

This is an edit of the previous image, not a new generation.
Apply only the pinned note: {change}.
Leave every other region intact: {lock}.

## TPL-04 Poster set

{format}: a set of mid-century modern travel posters, printed look, visible paper grain.
Headline copy exactly: {copy}.
No misspelled lettering.

## TPL-05 Stamp sheet

A perforated vintage national-park stamp sheet.
Copy to render exactly: {copy}.

## TPL-06 Invitation

A formal wedding invitation, letterpress on thick cotton stock.
Render this copy exactly: {copy}

## TPL-07 Deck visual

A single presentation slide, 16:9, dark editorial background.
Title: {copy}.

## TPL-08 Pack shot

Studio pack shot of {subject}. Label text must match {copy} exactly.

## TPL-09 Sticker sheet

Die-cut sticker sheet. Motifs: {subject}.

## TPL-10 Impressionist cityscape

An impressionist cityscape of {subject}. Broken color, visible strokes.

## TPL-11 Cyberpunk street

Night street in a dense cyberpunk city. Subject: {subject}. Signage: {copy}.

## TPL-12 Retrofuturism

Retrofuturist illustration. Subject: {subject}. Print-poster finish.

## TPL-13 Sci-fi surrealism

Quiet surreal science-fiction tableau. Subject: {subject}.

## TPL-14 1980s yearbook headshot

Transform the attached person into a late-1980s studio yearbook headshot. Keep identity.

## TPL-15 Sketch to image

Treat the attached sketch as composition law. Finish it as {style}.

## TPL-16 Format template

Use the {format} template. Do not switch aspect ratio after the first frame.

## TPL-17 Shareable prompt wrapper

Reusable look recipe. Style: {style}. Must keep: {lock}.
