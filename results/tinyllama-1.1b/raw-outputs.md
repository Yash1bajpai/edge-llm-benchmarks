# Raw Benchmark Outputs — TinyLlama 1.1B

> Seed: 42 | Max tokens: 150 | Runner: llama.cpp

---

## Prompt 1: Logic & Reasoning

**Prompt:** `Jane has 3 brothers. Each of her brothers has 2 sisters. How many sisters does Jane have? Think step-by-step.`

### FP16
```
To answer your question, Jane has 3 brothers, each of whom has 2 sisters. So,
Jane has 2 sisters, and each sister has 2 sisters. Hence, Jane has 2 sisters.
```
`Prompt: 60.5 t/s | Generation: 9.5 t/s | RAM: 2212 MiB`

### INT8
```
To answer your question, Jane has 3 brothers. Each of her brothers has 2 sisters.
So, Jane has a total of 5 sisters.
```
`Prompt: 65.0 t/s | Generation: 16.4 t/s | RAM: 1229 MiB`

### INT4
```
To answer the question, we need to follow a specific order in answering the given problem:
1. Identify the problem: Jane has three brothers, each of whom has 2 sisters.
2. Break down the problem into simpler steps: Jane has 3 brothers, each of whom has 2 sisters.
3. Determine the answer to the original problem: How many sisters does Jane have?
4. Recap the steps involved...
[Never concluded — looped on problem restatement]
```
`Prompt: 109.3 t/s | Generation: 26.4 t/s | RAM: 744 MiB`

---

## Prompt 2: JSON Formatting

**Prompt:** `Extract the core problem and the proposed solution from this text: 'Our server costs increased by 40% due to unoptimized database queries holding connections open. To fix this, we will implement a connection pool.' Output the result strictly as a valid JSON object with keys 'problem' and 'solution'. Do not add any other text.`

### FP16
```json
{
  "problem": "Our server costs increased by 40% due to unoptimized database queries holding connections open.",
  "solution": "To fix this issue, we will add a connection pool to our database server. When a new connection is needed, we will retrieve a connection from the pool instead of creating a new one."
}
```
*(Wrapped in markdown code block — not strictly valid per instruction)*
`Prompt: 62.1 t/s | Generation: 9.4 t/s | RAM: 2212 MiB`

### INT8
```
{"problem": "Our server costs increased by 40% due to unoptimized database queries holding connections open.", "solution": "To fix this, we will implement a connection pool that will maintain a pool of database connections for each of our application's database connections."}
```
*(Raw JSON, no markdown wrapper — best adherence)*
`Prompt: 66.0 t/s | Generation: 16.9 t/s | RAM: 1229 MiB`

### INT4
```
The core problem mentioned in this text is that the server's database queries are unoptimized...
[prose preamble added]
{
    "problem": "Unoptimized database queries are holding on to database connections...",
    "solution": {
        "implementation": "We will create... [truncated at token limit]
    }
}
```
*(Added prose preamble + malformed nested solution object)*
`Prompt: 123.5 t/s | Generation: 27.1 t/s | RAM: 744 MiB`

---

## Prompt 3: Constraint Adherence

**Prompt:** `Write a polite 2-sentence email declining a meeting invite. You must start the first sentence with the word 'Unfortunately' and the second sentence with the word 'However'.`

### FP16
```
Unfortunately, I am unable to make it to the meeting on [date] due to a prior appointment.
However, I understand that [reason] and I hope you can find a time that works for everyone.
If you have any questions or concerns, please do not hesitate to reach out to me.

Best regards,
[Your Name]
```
*(Keyword constraints followed, but wrote 3+ sentences)*
`Prompt: 66.8 t/s | Generation: 9.5 t/s | RAM: 2212 MiB`

### INT8
```
Unfortunately, I am unable to attend the meeting scheduled for [Date] at [Time] due to an urgent work commitment.
However, I would be available for a phone call instead. If possible, please let me know the preferred time and date.

Thank you for your understanding and cooperation.
```
*(Same pattern — keywords followed, extra sentences added)*
`Prompt: 81.6 t/s | Generation: 17.6 t/s | RAM: 1229 MiB`

### INT4
```
Dear [Recipient],
I am sorry to inform you that I am unable to attend the meeting that you requested on [date and time].
I understand that we have a mutual project that requires our collaboration, but unfortunately, I have a prior commitment...
```
*(Ignored both keyword constraints completely — 'Unfortunately' buried in middle, 'However' missing)*
`Prompt: 115.2 t/s | Generation: 26.2 t/s | RAM: 744 MiB`

---

## Prompt 4: Reading Comprehension (15-word limit)

**Prompt:** `Summarize the following in exactly 15 words: 'The James Webb Space Telescope is an infrared space observatory that launched on December 25, 2021, from Kourou, French Guiana, and arrived at the Sun-Earth L2 Lagrange point in January 2022.'`

### FP16
```
The James Webb Space Telescope (JWST) is an infrared space observatory that was launched on December 25, 2021,
from Kourou, French Guiana, and arrived at the Sun-Earth L2 Lagrange point on January 22, 2022.
```
*(~40 words — completely ignored the 15-word constraint)*
`Prompt: 69.5 t/s | Generation: 9.5 t/s | RAM: 2212 MiB`

### INT8
```
The James Webb Space Telescope is a telescope launched on December 25, 2021, from Kourou, French Guiana,
and arrived at the Sun-Earth L2 Lagrange point in January 2022.
The telescope uses infrared technology to observe the universe and study cosmic phenomena.
```
*(~55 words — added extra sentence)*
`Prompt: 85.0 t/s | Generation: 17.6 t/s | RAM: 1229 MiB`

### INT4
```
The James Webb Space Telescope is a large, infrared space observatory that was launched on December 25, 2021,
from Kourou, French Guiana, and arrived at L2 Lagrange point on January 11, 2022.
```
*(~40 words — ignored limit)*
`Prompt: 117.2 t/s | Generation: 27.9 t/s | RAM: 744 MiB`

---

## Prompt 5: Creativity & Tone

**Prompt:** `You are a highly sarcastic, grumpy old sailor. Explain what a smartphone is in exactly 3 sentences.`

### FP16
```
A smartphone is a handheld device that is equipped with a large touchscreen and a computer-like processor,
allowing users to access internet, make calls, send and receive emails, and run various apps.
The term "smartphone" was coined by Ericsson in 1996, and it refers to the first smartphones,
which were designed to be versatile, multi-functional devices capable of handling multiple tasks.
```
*(2 sentences, no sailor persona, tone is purely factual)*
`Prompt: 68.1 t/s | Generation: 9.5 t/s | RAM: 2212 MiB`

### INT8
```
A smartphone is a handheld device that is equipped with a large touchscreen and a suite of software applications,
including a camera, GPS navigation, messaging, social media, email, and numerous other features.
The term "smartphone" was coined by Ericsson in 1996, and it refers to the ability of a phone to perform
advanced functions without requiring users to physically touch and manipulate the device.
```
*(2 sentences, no persona, similar to FP16)*
`Prompt: 82.2 t/s | Generation: 17.7 t/s | RAM: 1229 MiB`

### INT4
```
A smartphone is a device that uses advanced technology to connect to the internet, making it incredibly useful
for communication, entertainment, and navigation. It can be used to access online services such as social media,
email, and search engines, as well as to make and receive calls, send text messages, and play games.
A smartphone's operating system, applications, and hardware can be customized and upgraded to meet individual
users' preferences and needs. Smartphones are often referred to as "phablets" due to their large screen sizes...
```
*(4+ sentences, no sailor persona at all)*
`Prompt: 112.6 t/s | Generation: 25.4 t/s | RAM: 744 MiB`
