# Raw Benchmark Outputs — TinyLlama 1.1B K-Quants

> Seed: 42 | Max tokens: 150 | Runner: llama.cpp
> Formats: Q4_K_M and Q5_K_M

---

## Q4_K_M Results

### Prompt 1: Logic & Reasoning
```
To answer the question, we need to follow a step-by-step process:
1. Identify the number of sisters Jane has.
2. Identify the number of sisters each of Jane's brothers has.
3. Multiply the number of sisters Jane has by the number of sisters each of her brothers has.
4. Divide the product by 2 to get the number of sisters Jane has.
In this case,
[Truncated — never gave final answer]
```
`Prompt: 100.2 t/s | Generation: 19.9 t/s`

### Prompt 2: JSON Formatting
```
Problem: The server's database queries were unoptimized, holding connections open for too long...
Solution: To fix this issue, we will implement a connection pool.
JSON Object:
{
  "problem": "...",
  "solution":
[Truncated — JSON incomplete]
```
`Prompt: 111.6 t/s | Generation: 23.1 t/s`

### Prompt 3: Constraint Adherence
```
Subject: Unfortunate Meeting Invite
Dear [Recipient],
I am sorry to inform you that I am unable to attend the meeting...
Unfortunately, I have a prior commitment that requires my immediate attention.
However, I understand that this is a mutual decision...
```
*('Unfortunately' in middle of email — constraint not followed at sentence start)*
`Prompt: 102.7 t/s | Generation: 24.9 t/s`

### Prompt 4: Reading Comprehension
```
Summary: The James Webb Space Telescope, a NASA-led mission, is an infrared space observatory
that launched on December 25, 2021, from Kourou, French Guiana, and arrived at the
Sun-Earth L2 Lagrange point in January 2022.
```
*(~40 words — ignored 15-word limit)*
`Prompt: 105.0 t/s | Generation: 24.4 t/s`

### Prompt 5: Creativity & Tone
```
Sure, a smartphone is a portable electronic device that is designed to perform various functions,
including making and receiving phone calls, sending and receiving text messages, accessing the
internet, and storing and playing music, videos, and other media files.
```
*(1 run-on sentence, no sailor persona)*
`Prompt: 79.7 t/s | Generation: 24.3 t/s`

---

## Q5_K_M Results

### Prompt 1: Logic & Reasoning
```
To answer this question, we need to perform the following steps:
1. Jane has 3 brothers.
2. Each of Jane's brothers has 2 sisters.
3. How many sisters does Jane have?
[Looped — repeated steps without concluding]
```
`Prompt: 66.7 t/s | Generation: 20.8 t/s`

### Prompt 2: JSON Formatting
```
The text contains the following problem and solution:
Problem: Our server costs increased by 40%...
Solution: To fix this, we will implement a connection pool.
Solution as JSON object:
{
  "problem": "...",
[Truncated — JSON incomplete]
```
`Prompt: 71.9 t/s | Generation: 20.2 t/s`

### Prompt 3: Constraint Adherence
```
Subject: Unfortunate Meeting Invitation
Dear [Recipient],
I am sorry to inform you that I am unable to attend the meeting...
Unfortunately, I have a prior commitment that requires my immediate attention.
However, I understand that this is a mutual decision...
```
*('Unfortunately' buried in body — same pattern as Q4_K_M)*
`Prompt: 65.4 t/s | Generation: 20.2 t/s`

### Prompt 4: Reading Comprehension
```
Summary: The James Webb Space Telescope, launched on December 25, 2021, from Kourou,
French Guiana, arrived at the Sun-Earth L2 Lagrange point in January 2022.
```
*(~30 words — closest to 15 words across all formats, but still over)*
`Prompt: 65.9 t/s | Generation: 20.0 t/s`

### Prompt 5: Creativity & Tone
```
Sure, here are three sentences that explain what a smartphone is:
1. A smartphone is a small, portable device that can perform a wide range of tasks...
2. Smartphones are designed to be easy to use and intuitive...
[Formatted as numbered list — no sailor persona]
```
`Prompt: 60.3 t/s | Generation: 21.0 t/s`
